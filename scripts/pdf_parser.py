#!/usr/bin/env python3
"""
PDF 解析脚本 - 从 PDF 文件中提取图片和文本
PDF Parser - Extract images and text from PDF files

功能 | Features:
- 提取所有图片 | Extract all images
- 提取全文文本 | Extract full text
- 提取图片位置信息 | Extract image position information
- 保存图片到文件 | Save images to files
"""

import fitz  # PyMuPDF
import os
import json
from typing import List, Dict, Any
from pathlib import Path


class PDFParser:
    """PDF 解析器类 | PDF Parser class"""

    def __init__(self, pdf_path: str, output_dir: str = "output"):
        """
        初始化 PDF 解析器
        Initialize PDF parser

        参数 | Parameters:
            pdf_path: PDF 文件路径 | PDF file path
            output_dir: 输出目录 | Output directory
        """
        self.pdf_path = pdf_path
        self.output_dir = output_dir
        self.doc = fitz.open(pdf_path)

        # 创建输出目录 | Create output directory
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(os.path.join(output_dir, "figures"), exist_ok=True)

    def extract_figures(self) -> List[Dict[str, Any]]:
        """
        提取 PDF 中的所有图片
        Extract all images from PDF

        返回 | Returns:
            图片列表，每个图片包含路径、页码、索引等信息
            List of images, each containing path, page number, index, etc.
        """
        figures = []

        for page_num in range(len(self.doc)):
            page = self.doc[page_num]
            image_list = page.get_images(full=True)

            # 获取页面尺寸（用于文本匹配）
            # Get page dimensions (for text matching)
            page_rect = page.rect

            for img_index, img in enumerate(image_list):
                try:
                    # 提取图片
                    # Extract image
                    xref = img[0]
                    base_image = self.doc.extract_image(xref)

                    if not base_image:
                        continue

                    image_bytes = base_image["image"]
                    image_ext = base_image["ext"]

                    # 保存图片
                    # Save image
                    image_filename = f"figure_page{page_num+1}_{img_index+1}.{image_ext}"
                    image_path = os.path.join(self.output_dir, "figures", image_filename)

                    with open(image_path, "wb") as img_file:
                        img_file.write(image_bytes)

                    # 获取图片位置信息
                    # Get image position information
                    try:
                        img_rect = page.get_image_rects(xref)[0] if page.get_image_rects(xref) else None
                    except:
                        img_rect = None

                    figures.append({
                        "page": page_num + 1,
                        "index": img_index + 1,
                        "filename": image_filename,
                        "path": image_path,
                        "rect": {
                            "x0": img_rect.x0 if img_rect else 0,
                            "y0": img_rect.y0 if img_rect else 0,
                            "x1": img_rect.x1 if img_rect else 0,
                            "y1": img_rect.y1 if img_rect else 0,
                            "width": img_rect.width if img_rect else 0,
                            "height": img_rect.height if img_rect else 0,
                        } if img_rect else None,
                        "ext": image_ext
                    })

                except Exception as e:
                    print(f"Warning: Failed to extract image {img_index} from page {page_num+1}: {e}")
                    continue

        return figures

    def extract_text(self) -> Dict[str, str]:
        """
        提取 PDF 中的文本
        Extract text from PDF

        返回 | Returns:
            包含全文和各部分文本的字典
            Dictionary containing full text and section texts
        """
        full_text = ""
        pages_text = {}

        for page_num in range(len(self.doc)):
            page = self.doc[page_num]
            page_text = page.get_text()
            full_text += page_text + "\n"
            pages_text[page_num + 1] = page_text

        return {
            "full_text": full_text,
            "pages": pages_text
        }

    def extract_text_near_image(self, page_num: int, rect: Dict[str, float],
                               window: int = 100) -> str:
        """
        提取图片附近的文本
        Extract text near an image

        参数 | Parameters:
            page_num: 页码 | Page number
            rect: 图片位置信息 | Image position information
            window: 搜索窗口大小（像素）| Search window size (pixels)

        返回 | Returns:
            图片附近的文本 | Text near the image
        """
        if rect is None:
            return ""

        page = self.doc[page_num - 1]

        # 扩展搜索区域
        # Extend search area
        search_rect = fitz.Rect(
            max(0, rect["x0"] - window),
            max(0, rect["y0"] - window),
            min(page.rect.width, rect["x1"] + window),
            min(page.rect.height, rect["y1"] + window)
        )

        # 提取搜索区域内的文本
        # Extract text within search area
        text = page.get_text("text", clip=search_rect)

        return text.strip()

    def extract_sections(self, text: str) -> Dict[str, str]:
        """
        从文本中提取常见章节
        Extract common sections from text

        参数 | Parameters:
            text: 全文 | Full text

        返回 | Returns:
            各章节的文本 | Text of each section
        """
        sections = {}
        import re

        # Methods 部分的常见模式
        # Common patterns for Methods section
        methods_patterns = [
            r'(?:Materials?\s+and\s+)?Methods\s*\n(.*?)(?:\n\s*[A-Z][a-z]+\s*\n)',
            r'Methods\s*\n(.*?)(?:\n\s*[A-Z][a-z]+\s*\n)',
            r'Methodology\s*\n(.*?)(?:\n\s*[A-Z][a-z]+\s*\n)',
        ]

        for pattern in methods_patterns:
            match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
            if match:
                sections["methods"] = match.group(1).strip()
                break

        # Results 部分
        # Results section
        results_pattern = r'Results\s*\n(.*?)(?:\n\s*[A-Z][a-z]+\s*\n)'
        match = re.search(results_pattern, text, re.DOTALL | re.IGNORECASE)
        if match:
            sections["results"] = match.group(1).strip()

        # Discussion 部分
        # Discussion section
        discussion_pattern = r'Discussion\s*\n(.*?)(?:\n\s*[A-Z][a-z]+\s*\n|$)'
        match = re.search(discussion_pattern, text, re.DOTALL | re.IGNORECASE)
        if match:
            sections["discussion"] = match.group(1).strip()

        return sections

    def parse(self) -> Dict[str, Any]:
        """
        完整解析 PDF
        Fully parse PDF

        返回 | Returns:
            包含所有提取信息的字典
            Dictionary containing all extracted information
        """
        print(f"Parsing PDF: {self.pdf_path}")

        # 提取图片
        # Extract images
        print("Extracting figures...")
        figures = self.extract_figures()
        print(f"Found {len(figures)} figures")

        # 提取文本
        # Extract text
        print("Extracting text...")
        text_data = self.extract_text()

        # 提取章节
        # Extract sections
        print("Extracting sections...")
        sections = self.extract_sections(text_data["full_text"])

        # 为每个图片提取附近的文本
        # Extract text near each image
        print("Extracting text near figures...")
        for figure in figures:
            figure["nearby_text"] = self.extract_text_near_image(
                figure["page"],
                figure["rect"]
            )

        # 保存元数据
        # Save metadata
        metadata = {
            "pdf_path": self.pdf_path,
            "num_pages": len(self.doc),
            "num_figures": len(figures),
            "figures": figures,
            "sections": list(sections.keys()),
            "has_methods": "methods" in sections,
            "has_results": "results" in sections,
            "has_discussion": "discussion" in sections,
        }

        metadata_path = os.path.join(self.output_dir, "metadata.json")
        with open(metadata_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)

        # 保存文本
        # Save text
        text_path = os.path.join(self.output_dir, "full_text.txt")
        with open(text_path, "w", encoding="utf-8") as f:
            f.write(text_data["full_text"])

        # 保存章节文本
        # Save section texts
        for section_name, section_text in sections.items():
            section_path = os.path.join(self.output_dir, f"{section_name}_section.txt")
            with open(section_path, "w", encoding="utf-8") as f:
                f.write(section_text)

        print(f"\nParsing complete! Output saved to: {self.output_dir}")
        print(f"- Figures: {len(figures)}")
        print(f"- Full text: {text_path}")
        print(f"- Metadata: {metadata_path}")
        print(f"- Sections: {', '.join(sections.keys())}")

        return {
            "figures": figures,
            "text": text_data,
            "sections": sections,
            "metadata": metadata
        }

    def close(self):
        """关闭 PDF 文档 | Close PDF document"""
        if self.doc:
            self.doc.close()


def main():
    """主函数 | Main function"""
    import argparse

    parser = argparse.ArgumentParser(
        description="从 PDF 中提取图片和文本 | Extract images and text from PDF"
    )
    parser.add_argument(
        "input_pdf",
        help="输入 PDF 文件路径 | Input PDF file path"
    )
    parser.add_argument(
        "-o", "--output",
        default="output",
        help="输出目录 | Output directory (default: output)"
    )

    args = parser.parse_args()

    # 检查输入文件是否存在
    # Check if input file exists
    if not os.path.exists(args.input_pdf):
        print(f"Error: File not found: {args.input_pdf}")
        return 1

    # 创建解析器并解析
    # Create parser and parse
    pdf_parser = PDFParser(args.input_pdf, args.output)
    result = pdf_parser.parse()
    pdf_parser.close()

    return 0


if __name__ == "__main__":
    exit(main())
