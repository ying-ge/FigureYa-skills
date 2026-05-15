#!/usr/bin/env python3

# Copyright (c) 2025 FigureYa Community
# Licensed under the MIT License
#
"""
文本挖掘脚本 - 从 PDF 文本中提取方法和工具信息
Text Mining Script - Extract method and tool information from PDF text

功能 | Features:
- 提取 Materials and Methods 部分 | Extract Materials and Methods section
- 识别 R 包 | Identify R packages
- 识别统计方法 | Identify statistical methods
- 提取 Figure 提及 | Extract Figure mentions
- 匹配图表类型 | Match chart types
"""

import re
import json
import yaml
from typing import Dict, List, Set, Any
from pathlib import Path


class TextMiner:
    """文本挖掘器类 | Text Miner class"""

    def __init__(self, config_path: str = None):
        """
        初始化文本挖掘器
        Initialize text miner

        参数 | Parameters:
            config_path: 配置文件路径 | Configuration file path
        """
        self.config = self._load_config(config_path)
        self.r_packages = self._build_r_package_set()
        self.stat_methods = self._build_stat_method_dict()

    def _load_config(self, config_path: str = None) -> Dict:
        """
        加载配置文件
        Load configuration file

        参数 | Parameters:
            config_path: 配置文件路径 | Configuration file path

        返回 | Returns:
            配置字典 | Configuration dictionary
        """
        if config_path is None:
            # 默认路径
            # Default path
            base_dir = Path(__file__).parent.parent
            config_path = base_dir / "method_keywords.yaml"

        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def _build_r_package_set(self) -> Set[str]:
        """
        构建 R 包集合
        Build R package set

        返回 | Returns:
            R 包集合 | R package set
        """
        packages = set()
        for category in self.config.get("r_packages", {}).values():
            if isinstance(category, list):
                packages.update(category)
        return packages

    def _build_stat_method_dict(self) -> Dict[str, List[str]]:
        """
        构建统计方法字典
        Build statistical method dictionary

        返回 | Returns:
            统计方法字典 | Statistical method dictionary
        """
        return self.config.get("statistical_methods", {})

    def find_r_packages(self, text: str) -> List[str]:
        """
        识别文中提到的 R 包
        Identify R packages mentioned in text

        参数 | Parameters:
            text: 输入文本 | Input text

        返回 | Returns:
            找到的 R 包列表 | List of found R packages
        """
        found = []

        # 转换为小写以进行不区分大小写的匹配
        # Convert to lowercase for case-insensitive matching
        text_lower = text.lower()

        for package in self.r_packages:
            # 使用单词边界匹配
            # Use word boundary matching
            pattern = r'\b' + re.escape(package.lower()) + r'\b'
            if re.search(pattern, text_lower):
                found.append(package)

        return sorted(found)

    def find_statistical_methods(self, text: str) -> Dict[str, List[str]]:
        """
        识别文中提到的统计方法
        Identify statistical methods mentioned in text

        参数 | Parameters:
            text: 输入文本 | Input text

        返回 | Returns:
            找到的方法字典 | Dictionary of found methods
        """
        found = {}
        text_lower = text.lower()

        for category, keywords in self.stat_methods.items():
            matched = []
            for keyword in keywords:
                if keyword.lower() in text_lower:
                    matched.append(keyword)

            if matched:
                found[category] = matched

        return found

    def extract_methods_section(self, text: str) -> str:
        """
        提取 Methods 或 Materials and Methods 部分
        Extract Methods or Materials and Methods section

        参数 | Parameters:
            text: 全文 | Full text

        返回 | Returns:
            Methods 部分文本 | Methods section text
        """
        # 常见的章节标题模式
        # Common section title patterns
        patterns = [
            r'(?:Materials?\s+and\s+)?Methods\s*\n(.*?)(?:\n\s*[A-Z][a-z]+\s*\n)',
            r'Methods\s*\n(.*?)(?:\n\s*[A-Z][a-z]+\s*\n)',
            r'Methodology\s*\n(.*?)(?:\n\s*[A-Z][a-z]+\s*\n)',
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
            if match:
                return match.group(1).strip()

        return ""

    def extract_figure_mentions(self, text: str) -> Dict[str, List[str]]:
        """
        提取正文中对 Figure 的描述
        Extract figure descriptions from text

        参数 | Parameters:
            text: 输入文本 | Input text

        返回 | Returns:
            Figure 描述字典 | Figure description dictionary
        """
        mentions = {}

        # 匹配 "Figure 1 shows..." 或 "Fig. 1 displays..." 等模式
        # Match patterns like "Figure 1 shows..." or "Fig. 1 displays..."
        patterns = [
            r'(?:Figure|Fig\.)\s+(\d+[A-Z]?)\s+(?:shows?|displays?|represents?|illustrates?|depicts?)\s+(.+?)(?:\.|\n)',
            r'(?:Figure|Fig\.)\s+(\d+[A-Z]?)\s+(.+?)(?:\.|\n)',
        ]

        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for fig_num, description in matches:
                fig_key = f"Figure {fig_num}"
                if fig_key not in mentions:
                    mentions[fig_key] = []
                mentions[fig_key].append(description.strip())

        return mentions

    def extract_supplementary_methods(self, text: str) -> str:
        """
        提取 Supplementary 中的方法信息
        Extract method information from Supplementary

        参数 | Parameters:
            text: 全文 | Full text

        返回 | Returns:
            Supplementary 方法文本 | Supplementary method text
        """
        # 查找 Supplementary 相关部分
        # Find Supplementary related sections
        patterns = [
            r'Supplementary\s+(?:Materials?\s+)?(?:and\s+)?Methods\s*\n(.*?)(?:\n\s*[A-Z][a-z]+\s*\n)',
            r'Supplementary\s+(?:Information|Data)\s*\n(.*?)(?:\n\s*[A-Z][a-z]+\s*\n)',
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
            if match:
                return match.group(1).strip()

        return ""

    def match_chart_type_from_text(self, text: str) -> Dict[str, float]:
        """
        从文本推断图表类型
        Infer chart type from text

        参数 | Parameters:
            text: 输入文本 | Input text

        返回 | Returns:
            图表类型及其置信度 | Chart types and their confidence scores
        """
        scores = {}
        text_lower = text.lower()

        chart_descriptions = self.config.get("chart_descriptions", {})

        for chart_type, keywords in chart_descriptions.items():
            score = 0
            matched_keywords = []

            for keyword in keywords:
                if keyword.lower() in text_lower:
                    score += 1
                    matched_keywords.append(keyword)

            # 归一化分数 | Normalize score
            if score > 0:
                scores[chart_type] = {
                    "score": score,
                    "confidence": min(score / len(keywords), 1.0),
                    "matched_keywords": matched_keywords
                }

        return scores

    def mine_text(self, text_data: Dict[str, str]) -> Dict[str, Any]:
        """
        完整的文本挖掘
        Complete text mining

        参数 | Parameters:
            text_data: 文本数据字典 | Text data dictionary

        返回 | Returns:
            挖掘结果字典 | Mining result dictionary
        """
        full_text = text_data.get("full_text", "")

        print("Text mining in progress...")

        # 提取 Methods 部分
        # Extract Methods section
        methods_text = self.extract_methods_section(full_text)
        print(f"Extracted Methods section: {len(methods_text)} characters")

        # 提取 Supplementary 部分
        # Extract Supplementary section
        supplementary_text = self.extract_supplementary_methods(full_text)
        print(f"Extracted Supplementary section: {len(supplementary_text)} characters")

        # 识别 R 包
        # Identify R packages
        r_packages = self.find_r_packages(full_text)
        print(f"Found {len(r_packages)} R packages: {', '.join(r_packages[:5])}{'...' if len(r_packages) > 5 else ''}")

        # 识别统计方法
        # Identify statistical methods
        stat_methods = self.find_statistical_methods(full_text)
        print(f"Found {len(stat_methods)} method categories")

        # 提取 Figure 提及
        # Extract Figure mentions
        figure_mentions = self.extract_figure_mentions(full_text)
        print(f"Found {len(figure_mentions)} Figure mentions")

        # 从文本推断图表类型
        # Infer chart types from text
        chart_type_scores = self.match_chart_type_from_text(full_text)
        print(f"Matched {len(chart_type_scores)} chart types from text")

        return {
            "methods_section": methods_text,
            "supplementary_section": supplementary_text,
            "r_packages": r_packages,
            "statistical_methods": stat_methods,
            "figure_mentions": figure_mentions,
            "chart_type_scores": chart_type_scores
        }


def main():
    """主函数 | Main function"""
    import argparse

    parser = argparse.ArgumentParser(
        description="从 PDF 文本中提取方法和工具信息 | Extract method and tool information from PDF text"
    )
    parser.add_argument(
        "input_text",
        help="输入文本文件路径 | Input text file path"
    )
    parser.add_argument(
        "-c", "--config",
        help="配置文件路径 | Configuration file path"
    )
    parser.add_argument(
        "-o", "--output",
        default="text_mining_results.json",
        help="输出 JSON 文件路径 | Output JSON file path"
    )

    args = parser.parse_args()

    # 检查输入文件是否存在
    # Check if input file exists
    if not Path(args.input_text).exists():
        print(f"Error: File not found: {args.input_text}")
        return 1

    # 读取输入文本
    # Read input text
    with open(args.input_text, "r", encoding="utf-8") as f:
        full_text = f.read()

    # 创建文本挖掘器并挖掘
    # Create text miner and mine
    text_miner = TextMiner(args.config)
    results = text_miner.mine_text({"full_text": full_text})

    # 保存结果
    # Save results
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\nResults saved to: {args.output}")

    return 0


if __name__ == "__main__":
    exit(main())
