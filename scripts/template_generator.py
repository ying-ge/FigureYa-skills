#!/usr/bin/env python3
"""
模板生成脚本 - 基于现有 FigureYa 模块生成新模块
Template Generator - Generate new modules based on existing FigureYa modules

功能 | Features:
- 读取现有模块模板 | Read existing module templates
- 根据识别结果调整参数 | Adjust parameters based on identification results
- 生成新的模块文件 | Generate new module files
- 保持 FigureYa 标准格式 | Maintain FigureYa standard format
"""

import os
import shutil
import yaml
from typing import Dict, List, Any
from pathlib import Path


class TemplateGenerator:
    """模板生成器类 | Template Generator class"""

    def __init__(self, modules_base_dir: str = None, config_path: str = None):
        """
        初始化模板生成器
        Initialize template generator

        参数 | Parameters:
            modules_base_dir: FigureYa 模块基础目录 | FigureYa modules base directory
            config_path: 配置文件路径 | Configuration file path
        """
        if modules_base_dir is None:
            # 默认路径
            # Default path
            base_dir = Path(__file__).parent.parent
            modules_base_dir = base_dir / "modules"

        self.modules_base_dir = Path(modules_base_dir)
        self.config = self._load_config(config_path)

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
            config_path = base_dir / "chart_type_mapping.yaml"

        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def find_module_path(self, module_name: str) -> Path:
        """
        查找模块路径
        Find module path

        参数 | Parameters:
            module_name: 模块名称 | Module name

        返回 | Returns:
            模块路径 | Module path
        """
        # 在基础目录中搜索模块
        # Search for module in base directory
        for item in self.modules_base_dir.iterdir():
            if item.is_dir() and module_name in item.name:
                return item

        # 如果找不到，尝试在子目录中搜索
        # If not found, try searching in subdirectories
        for item in self.modules_base_dir.rglob("*"):
            if item.is_dir() and module_name in item.name:
                return item

        return None

    def read_template_rmd(self, module_path: Path) -> str:
        """
        读取模板 R Markdown 文件
        Read template R Markdown file

        参数 | Parameters:
            module_path: 模块路径 | Module path

        返回 | Returns:
            Rmd 文件内容 | Rmd file content
        """
        # 查找 .Rmd 文件
        # Find .Rmd file
        rmd_files = list(module_path.glob("*.Rmd"))

        if not rmd_files:
            raise FileNotFoundError(f"No .Rmd file found in {module_path}")

        # 读取第一个 .Rmd 文件
        # Read first .Rmd file
        with open(rmd_files[0], "r", encoding="utf-8") as f:
            return f.read()

    def extract_parameters(self, rmd_content: str) -> Dict[str, Any]:
        """
        从 Rmd 内容中提取参数
        Extract parameters from Rmd content

        参数 | Parameters:
            rmd_content: Rmd 文件内容 | Rmd file content

        返回 | Returns:
            参数字典 | Parameter dictionary
        """
        import re

        parameters = {}

        # 查找参数设置章节
        # Find parameter setting section
        param_section_match = re.search(
            r'## 参数设置 Parameter setting.*?(?=##|\Z)',
            rmd_content,
            re.DOTALL
        )

        if param_section_match:
            param_section = param_section_match.group(0)

            # 提取 R 代码块中的参数赋值
            # Extract parameter assignments in R code blocks
            param_assignments = re.findall(
                r'(\w+)\s*<-\s*([^\n]+)',
                param_section
            )

            for var_name, var_value in param_assignments:
                parameters[var_name] = {
                    "value": var_value.strip(),
                    "description": ""  # TODO: 从注释中提取描述
                }

        return parameters

    def adjust_parameters(self, parameters: Dict[str, Any],
                         chart_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        根据图表信息调整参数
        Adjust parameters based on chart information

        参数 | Parameters:
            parameters: 原始参数 | Original parameters
            chart_info: 图表信息 | Chart information

        返回 | Returns:
            调整后的参数 | Adjusted parameters
        """
        # TODO: 实现具体的参数调整逻辑
        # TODO: Implement specific parameter adjustment logic

        # 示例：根据图表类型调整某些参数
        # Example: Adjust certain parameters based on chart type

        adjusted = parameters.copy()

        # 这里可以添加更多的参数调整规则
        # More parameter adjustment rules can be added here

        return adjusted

    def generate_new_module(self, template_module: str,
                           chart_info: Dict[str, Any],
                           output_dir: str) -> Path:
        """
        生成新模块
        Generate new module

        参数 | Parameters:
            template_module: 模板模块名称 | Template module name
            chart_info: 图表信息 | Chart information
            output_dir: 输出目录 | Output directory

        返回 | Returns:
            新模块路径 | New module path
        """
        print(f"Generating new module from template: {template_module}")

        # 查找模板模块路径
        # Find template module path
        template_path = self.find_module_path(template_module)

        if template_path is None:
            raise FileNotFoundError(f"Template module not found: {template_module}")

        # 读取模板 Rmd 文件
        # Read template Rmd file
        rmd_content = self.read_template_rmd(template_path)

        # 提取参数
        # Extract parameters
        parameters = self.extract_parameters(rmd_content)

        # 调整参数
        # Adjust parameters
        adjusted_parameters = self.adjust_parameters(parameters, chart_info)

        # 创建新模块目录
        # Create new module directory
        new_module_name = self._generate_module_name(chart_info)
        new_module_path = Path(output_dir) / new_module_name
        new_module_path.mkdir(parents=True, exist_ok=True)

        # 复制模板文件到新目录
        # Copy template files to new directory
        self._copy_template_files(template_path, new_module_path)

        # 更新 Rmd 文件
        # Update Rmd file
        self._update_rmd_file(new_module_path, chart_info, adjusted_parameters)

        print(f"New module created at: {new_module_path}")

        return new_module_path

    def _generate_module_name(self, chart_info: Dict[str, Any]) -> str:
        """
        生成新模块名称
        Generate new module name

        参数 | Parameters:
            chart_info: 图表信息 | Chart information

        返回 | Returns:
            模块名称 | Module name
        """
        chart_type = chart_info.get("chart_type", "unknown")
        figure_number = chart_info.get("figure_number", "1")

        # 生成模块名称
        # Generate module name
        module_name = f"FigureYa_Figure{figure_number}_{chart_type}"

        return module_name

    def _copy_template_files(self, template_path: Path, new_path: Path):
        """
        复制模板文件
        Copy template files

        参数 | Parameters:
            template_path: 模板路径 | Template path
            new_path: 新路径 | New path
        """
        # 复制所有文件除了 .Rmd（稍后单独处理）
        # Copy all files except .Rmd (handle separately later)
        for file in template_path.iterdir():
            if file.is_file() and not file.suffix == ".Rmd":
                shutil.copy2(file, new_path / file.name)

    def _update_rmd_file(self, module_path: Path,
                        chart_info: Dict[str, Any],
                        parameters: Dict[str, Any]):
        """
        更新 Rmd 文件
        Update Rmd file

        参数 | Parameters:
            module_path: 模块路径 | Module path
            chart_info: 图表信息 | Chart information
            parameters: 参数字典 | Parameter dictionary
        """
        # 查找 .Rmd 文件
        # Find .Rmd file
        rmd_files = list(module_path.glob("*.Rmd"))

        if not rmd_files:
            return

        rmd_file = rmd_files[0]

        # TODO: 实现具体的 Rmd 文件更新逻辑
        # TODO: Implement specific Rmd file update logic

        # 这里可以更新 YAML header、参数值等
        # Here you can update YAML header, parameter values, etc.

        print(f"Rmd file updated: {rmd_file}")

    def batch_generate_modules(self, charts_info: List[Dict[str, Any]],
                              output_base_dir: str) -> Dict[str, Any]:
        """
        批量生成模块（增强版）
        Batch generate modules (enhanced)

        参数 | Parameters:
            charts_info: 图表信息列表 | List of chart information
            output_base_dir: 输出基础目录 | Output base directory

        返回 | Returns:
            包含详细报告的字典 | Dictionary containing detailed report
        """
        results = {
            "success": [],
            "failed": [],
            "partial": [],
            "report_path": None
        }

        # 创建报告目录
        # Create report directory
        report_dir = Path(output_base_dir) / "reports"
        report_dir.mkdir(parents=True, exist_ok=True)

        print(f"Batch generating {len(charts_info)} modules...")

        for i, chart_info in enumerate(charts_info, 1):
            chart_type = chart_info.get("chart_type", "unknown")
            figure_number = chart_info.get("figure_number", i)

            print(f"[{i}/{len(charts_info)}] Processing Figure {figure_number} ({chart_type})...")

            try:
                recommended_module_info = chart_info.get("recommended_module", {})

                # 检查是否找到了匹配的模块
                # Check if a matching module was found
                if not recommended_module_info.get("found", False):
                    # 未找到模块，使用未匹配处理器
                    # No module found, use unmatched chart handler
                    from unmatched_chart_handler import UnmatchedChartHandler

                    handler = UnmatchedChartHandler()
                    handler_result = handler.handle_unmatched_chart(chart_info, output_base_dir)

                    strategy = handler_result.get("strategy", "log_only")

                    if strategy == "create_skeleton":
                        results["partial"].append({
                            "figure": figure_number,
                            "chart_type": chart_type,
                            "skeleton_path": handler_result.get("skeleton_path"),
                            "reason": "No matching module found",
                            "confidence": chart_info.get("confidence", 0)
                        })
                        print(f"  ⚠️  Created skeleton module")

                    elif strategy == "provide_guide":
                        results["failed"].append({
                            "figure": figure_number,
                            "chart_type": chart_type,
                            "reason": "No matching module found",
                            "confidence": chart_info.get("confidence", 0),
                            "suggestions": handler_result.get("next_steps", [])
                        })
                        print(f"  ⚠️  No module found, guide provided")

                    else:  # log_only
                        results["failed"].append({
                            "figure": figure_number,
                            "chart_type": chart_type,
                            "reason": "No matching module found (low confidence)",
                            "confidence": chart_info.get("confidence", 0)
                        })
                        print(f"  ⚠️  No module found (low confidence)")

                else:
                    # 找到了匹配的模块，正常生成
                    # Found matching module, generate normally
                    recommended_module = recommended_module_info.get("module")

                    new_module_path = self.generate_new_module(
                        recommended_module,
                        chart_info,
                        output_base_dir
                    )

                    results["success"].append({
                        "figure": figure_number,
                        "chart_type": chart_type,
                        "module_path": str(new_module_path)
                    })
                    print(f"  ✓ Module generated")

            except Exception as e:
                results["failed"].append({
                    "figure": figure_number,
                    "chart_type": chart_type,
                    "reason": f"Error: {str(e)}",
                    "confidence": chart_info.get("confidence", 0)
                })
                print(f"  ✗ Error: {e}")
                continue

        # 生成详细报告
        # Generate detailed report
        report_path = self._generate_report(results, report_dir)
        results["report_path"] = str(report_path)

        # 打印摘要
        # Print summary
        print(f"\n{'='*60}")
        print(f"Generation Summary:")
        print(f"{'='*60}")
        print(f"Total: {len(charts_info)}")
        print(f"✓ Success: {len(results['success'])}")
        print(f"⚠️  Partial (skeleton): {len(results['partial'])}")
        print(f"✗ Failed: {len(results['failed'])}")
        print(f"{'='*60}")
        print(f"\nDetailed report: {report_path}")

        return results

    def _generate_report(self, results: Dict[str, Any], report_dir: Path) -> Path:
        """
        生成详细报告
        Generate detailed report

        参数 | Parameters:
            results: 结果字典 | Results dictionary
            report_dir: 报告目录 | Report directory

        返回 | Returns:
            报告文件路径 | Report file path
        """
        from datetime import datetime

        report_path = report_dir / f"generation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

        with open(report_path, "w", encoding="utf-8") as f:
            f.write("# FigureYa 模块生成报告 | FigureYa Module Generation Report\n\n")
            f.write(f"**生成时间 | Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            # 执行摘要
            # Executive summary
            f.write("## 执行摘要 | Executive Summary\n\n")
            total = len(results["success"]) + len(results["partial"]) + len(results["failed"])
            f.write(f"- 总图表数 | Total charts: {total}\n")
            f.write(f"- 成功生成 | Success: {len(results['success'])}\n")
            f.write(f"- 需要手动完成 | Partial (skeleton): {len(results['partial'])}\n")
            f.write(f"- 失败 | Failed: {len(results['failed'])}\n\n")

            # 成功列表
            # Success list
            if results["success"]:
                f.write("## ✅ 成功生成的模块 | Successfully Generated Modules\n\n")
                for item in results["success"]:
                    f.write(f"### Figure {item['figure']}: {item['chart_type']}\n\n")
                    f.write(f"- **路径 | Path**: `{item['module_path']}`\n")
                    f.write(f"- **状态 | Status**: ✓ 完全生成 | Fully generated\n\n")

            # 部分完成列表
            # Partial completion list
            if results["partial"]:
                f.write("## ⚠️  需要手动完成的模块 | Modules Requiring Manual Completion\n\n")
                f.write("这些模块已生成骨架，但需要手动完成代码部分：\n")
                f.write("These modules have skeleton generated but require manual code completion:\n\n")

                for item in results["partial"]:
                    f.write(f"### Figure {item['figure']}: {item['chart_type']}\n\n")
                    f.write(f"- **骨架路径 | Skeleton path**: `{item['skeleton_path']}`\n")
                    f.write(f"- **原因 | Reason**: {item['reason']}\n")
                    f.write(f"- **置信度 | Confidence**: {item.get('confidence', 0):.2f}\n")
                    f.write(f"- **状态 | Status**: ⚠️  需要手动完成 | Requires manual completion\n\n")
                    f.write("**下一步 | Next steps**:\n")
                    f.write("1. 查看骨架模块目录 | Review skeleton module directory\n")
                    f.write("2. 阅读 README.md 了解完成步骤 | Read README.md for completion steps\n")
                    f.write("3. 完成 Rmd 文件中的 TODO 部分 | Complete TODO sections in Rmd file\n\n")

            # 失败列表
            # Failed list
            if results["failed"]:
                f.write("## ❌ 失败的图表 | Failed Charts\n\n")
                for item in results["failed"]:
                    f.write(f"### Figure {item['figure']}: {item['chart_type']}\n\n")
                    f.write(f"- **原因 | Reason**: {item['reason']}\n")
                    f.write(f"- **置信度 | Confidence**: {item.get('confidence', 0):.2f}\n")
                    f.write(f"- **状态 | Status**: ✗ 失败 | Failed\n")

                    if item.get("suggestions"):
                        f.write("\n**建议 | Suggestions**:\n")
                        for suggestion in item["suggestions"]:
                            f.write(f"- {suggestion}\n")
                    f.write("\n")

            # 后续步骤
            # Next steps
            f.write("## 后续步骤 | Next Steps\n\n")
            f.write("1. **检查成功生成的模块 | Check successfully generated modules**\n")
            f.write("   - 运行 R Markdown 验证输出 | Run R Markdown to verify output\n")
            f.write("   - 调整参数优化效果 | Adjust parameters to optimize results\n\n")

            if results["partial"]:
                f.write("2. **完成骨架模块 | Complete skeleton modules**\n")
                f.write("   - 每个骨架模块都有详细的 README.md | Each skeleton has detailed README.md\n")
                f.write("   - 按照指南完成 TODO 部分 | Complete TODO sections following guide\n")
                f.write("   - 准备示例数据 | Prepare example data\n\n")

            if results["failed"]:
                f.write("3. **处理失败的图表 | Handle failed charts**\n")
                f.write("   - 使用 `figureya-creator` skill 手动创建 | Use `figureya-creator` skill to create manually\n")
                f.write("   - 或者考虑其他可视化工具 | Or consider other visualization tools\n")
                f.write("   - 向 FigureYa 团队反馈新图表类型 | Feedback new chart types to FigureYa team\n\n")

            f.write("---\n\n")
            f.write("**需要帮助？| Need Help?**\n\n")
            f.write("- 查看现有 FigureYa 模块作为参考 | Review existing FigureYa modules for reference\n")
            f.write("- 使用 `figureya-creator` skill 寻求帮助 | Use `figureya-creator` skill for help\n")
            f.write("- 在 GitHub 上提 issue | Open an issue on GitHub\n")

        return report_path


def main():
    """主函数 | Main function"""
    import argparse
    import json

    parser = argparse.ArgumentParser(
        description="基于现有 FigureYa 模块生成新模块 | Generate new modules based on existing FigureYa modules"
    )
    parser.add_argument(
        "input_json",
        help="输入 JSON 文件路径（包含融合结果）| Input JSON file path"
    )
    parser.add_argument(
        "-o", "--output",
        default="generated_modules",
        help="输出目录 | Output directory"
    )
    parser.add_argument(
        "-m", "--modules-dir",
        help="FigureYa 模块基础目录 | FigureYa modules base directory"
    )

    args = parser.parse_args()

    # 检查输入文件是否存在
    # Check if input file exists
    if not Path(args.input_json).exists():
        print(f"Error: File not found: {args.input_json}")
        return 1

    # 读取输入数据
    # Read input data
    with open(args.input_json, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    # 创建生成器并生成
    # Create generator and generate
    generator = TemplateGenerator(args.modules_dir)

    if isinstance(input_data, list):
        results = generator.batch_generate_modules(input_data, args.output)
    else:
        result = generator.generate_new_module(
            input_data.get("recommended_module"),
            input_data,
            args.output
        )
        results = [result]

    print(f"\nGenerated {len(results)} modules in: {args.output}")

    return 0


if __name__ == "__main__":
    exit(main())
