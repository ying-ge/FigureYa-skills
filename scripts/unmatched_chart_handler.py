#!/usr/bin/env python3
"""
未匹配图表处理器 - 处理没有找到匹配 FigureYa 模块的图表
Unmatched Chart Handler - Handle charts without matching FigureYa modules

功能 | Features:
- 根据置信度和信息丰富度选择处理策略
- 创建占位符模块
- 生成手动创建指南
- 记录失败信息
"""

import os
from typing import Dict, List, Any
from pathlib import Path
from datetime import datetime


class UnmatchedChartHandler:
    """未匹配图表处理器类 | Unmatched Chart Handler class"""

    def __init__(self):
        """
        初始化处理器
        Initialize handler
        """
        pass

    def handle_unmatched_chart(self, chart_info: Dict[str, Any],
                               output_dir: str = None) -> Dict[str, Any]:
        """
        处理未匹配的图表
        Handle unmatched chart

        参数 | Parameters:
            chart_info: 图表信息 | Chart information
            output_dir: 输出目录 | Output directory

        返回 | Returns:
            处理结果和策略 | Handling result and strategy
        """
        chart_type = chart_info.get("chart_type", "unknown")
        confidence = chart_info.get("confidence", 0)
        evidence = chart_info.get("evidence", {})

        # 根据置信度和信息丰富度选择策略
        # Select strategy based on confidence and information richness
        has_r_packages = len(evidence.get("text", {}).get("r_packages", [])) > 0
        has_methods = len(evidence.get("text", {}).get("methods", {})) > 0

        if confidence >= 0.7 and (has_r_packages or has_methods):
            # 高置信度且有工具信息：创建骨架
            # High confidence with tool info: create skeleton
            strategy = "create_skeleton"
        elif confidence >= 0.5:
            # 中等置信度：提供手动指南
            # Medium confidence: provide manual guide
            strategy = "provide_guide"
        else:
            # 低置信度：仅记录
            # Low confidence: log only
            strategy = "log_only"

        return self._execute_strategy(chart_info, strategy, output_dir)

    def _execute_strategy(self, chart_info: Dict[str, Any],
                          strategy: str, output_dir: str) -> Dict[str, Any]:
        """
        执行处理策略
        Execute handling strategy

        参数 | Parameters:
            chart_info: 图表信息 | Chart information
            strategy: 策略名称 | Strategy name
            output_dir: 输出目录 | Output directory

        返回 | Returns:
            处理结果 | Handling result
        """
        chart_type = chart_info.get("chart_type", "unknown")
        figure_number = chart_info.get("figure_number", "1")

        result = {
            "figure": figure_number,
            "chart_type": chart_type,
            "strategy": strategy,
            "confidence": chart_info.get("confidence", 0),
            "timestamp": datetime.now().isoformat()
        }

        if strategy == "create_skeleton":
            # 导入骨架生成器
            # Import skeleton generator
            from skeleton_generator import SkeletonGenerator

            skeleton_gen = SkeletonGenerator()

            if output_dir is None:
                output_dir = "output"

            skeleton_path = skeleton_gen.generate_skeleton(chart_info, output_dir)

            result["skeleton_path"] = str(skeleton_path)
            result["message"] = f"Created skeleton module at {skeleton_path}"
            result["next_steps"] = [
                f"Review skeleton at {skeleton_path}",
                "Complete the TODO sections in the Rmd file",
                "Prepare example data",
                "Test and validate the module"
            ]

        elif strategy == "provide_guide":
            # 生成手动创建指南
            # Generate manual creation guide
            guide = self._generate_manual_guide(chart_info)

            result["guide"] = guide
            result["message"] = "Manual creation guide provided"
            result["next_steps"] = [
                "Use figureya-creator skill with the reference image",
                "Follow the guide below to create the module manually",
                "Consider contributing the module back to FigureYa"
            ]

        else:  # log_only
            result["message"] = "Chart logged only (low confidence)"
            result["next_steps"] = [
                "Review the chart manually",
                "Consider if this chart type should be added to FigureYa"
            ]

        return result

    def _generate_manual_guide(self, chart_info: Dict[str, Any]) -> str:
        """
        生成手动创建指南
        Generate manual creation guide

        参数 | Parameters:
            chart_info: 图表信息 | Chart information

        返回 | Returns:
            指南文本 | Guide text
        """
        chart_type = chart_info.get("chart_type", "unknown")
        confidence = chart_info.get("confidence", 0)
        evidence = chart_info.get("evidence", {})
        figure_number = chart_info.get("figure_number", "1")

        # 识别到的信息
        # Identified information
        r_packages = evidence.get("text", {}).get("r_packages", [])
        methods = evidence.get("text", {}).get("methods", {})
        visual_type = evidence.get("visual", {}).get("identified_type", "Unknown")

        # 查找相似模块
        # Find similar modules
        similar_modules = self._find_similar_modules(chart_type)

        guide = f"""
# 手动创建 FigureYa 模块指南
# Manual FigureYa Module Creation Guide

## 图表信息 | Chart Information

- **图表类型 | Chart Type**: {chart_type}
- **视觉识别 | Visual Recognition**: {visual_type}
- **识别置信度 | Confidence**: {confidence:.2f}
- **来源 | Source**: Figure {figure_number}
- **图片路径 | Image Path**: {chart_info.get('image_path', 'N/A')}

## 识别到的工具 | Identified Tools

### R 包 | R Packages
{', '.join(r_packages) if r_packages else 'None detected'}

### 统计方法 | Statistical Methods
"""
        for category, method_list in methods.items():
            guide += f"- **{category}**: {', '.join(method_list)}\n"

        guide += "\n## 推荐参考模块 | Recommended Reference Modules\n\n"

        if similar_modules:
            for i, similar in enumerate(similar_modules, 1):
                guide += f"{i}. **{similar['name']}** (`{similar['module']}`)\n"
                guide += f"   - 相似原因 | Match reason: {similar['match_reason']}\n"
        else:
            guide += "未找到相似模块。请查看 FigureYa 模块库寻找类似的可视化。\n"
            guide += "No similar modules found. Please browse FigureYa module library for similar visualizations.\n"

        guide += f"""

## 创建步骤 | Creation Steps

### 步骤 1：收集信息 | Step 1: Gather Information

1. 查看原始图片，理解需要绘制的内容
   - Review the original image to understand what needs to be plotted
2. 识别关键特征（颜色、布局、标注等）
   - Identify key features (colors, layout, annotations, etc.)
3. 确定数据结构要求
   - Determine data structure requirements

### 步骤 2：准备数据 | Step 2: Prepare Data

**重要**：使用真实的示例数据，而不是 AI 生成的假数据。
**Important**: Use real example data, not AI-generated fake data.

- 数据文件格式（CSV/TXT）
- Data file format (CSV/TXT)
- 列名和含义
- Column names and meanings
- 示例数据量
- Example data size

### 步骤 3：使用 figureya-creator | Step 3: Use figureya-creator

在 Claude Code 中使用以下提示：

```
用户：我想要创建一个 FigureYa 模块来绘制 {chart_type}

参考图片：{chart_info.get('image_path', 'N/A')}

识别到的 R 包：{', '.join(r_packages) if r_packages else 'None'}

请帮我生成符合 FigureYa 标准的模块。
```

### 步骤 4：完善模块 | Step 4: Refine Module

1. 填写"需求描述"章节
   - Complete "Requirement description" section
2. 添加应用场景说明
   - Add application scenario description
3. 调整参数设置
   - Adjust parameter settings
4. 准备示例数据
   - Prepare example data

### 步骤 5：测试验证 | Step 5: Test and Validate

1. 运行 R Markdown 生成报告
   - Run R Markdown to generate report
2. 检查输出质量
   - Check output quality
3. 调整参数优化效果
   - Adjust parameters to optimize results
4. 验证可重复性
   - Verify reproducibility

## 提示和建议 | Tips and Suggestions

### 代码实现
1. 参考识别到的 R 包文档
   - Reference documentation of identified R packages
2. 查找类似图表的示例代码
   - Search for example code of similar charts
3. 使用 ggplot2 作为基础绘图系统
   - Use ggplot2 as base plotting system

### 参数设置
1. 从常见参数开始（颜色、尺寸、标签）
   - Start with common parameters (colors, dimensions, labels)
2. 逐步添加复杂功能
   - Gradually add complex features
3. 提供合理的默认值
   - Provide reasonable default values

### 文档质量
1. 双语文档（中英文）
   - Bilingual documentation (Chinese/English)
2. 清晰的示例
   - Clear examples
3. 可运行的代码
   - Executable code

## 完成后 | After Completion

创建完成后，你可以：

1. **使用这个模块进行数据分析**
   - Use this module for data analysis
2. **分享给其他人使用**
   - Share with others for use
3. **贡献回 FigureYa 项目**（如果觉得有价值）
   - Contribute back to FigureYa project (if valuable)

## 获取帮助 | Get Help

如果遇到问题：

1. 参考现有的 FigureYa 模块
   - Reference existing FigureYa modules
2. 使用 `figureya-creator` skill 寻求帮助
   - Use `figureya-creator` skill for help
3. 查看 FigureYa 文档和示例
   - Check FigureYa documentation and examples
4. 在 GitHub 上提 issue
   - Open an issue on GitHub

---

生成时间 | Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

        return guide

    def _find_similar_modules(self, chart_type: str) -> List[Dict[str, str]]:
        """
        查找相似的模块
        Find similar modules

        参数 | Parameters:
            chart_type: 图表类型 | Chart type

        返回 | Returns:
            相似模块列表 | List of similar modules
        """
        # 简单的关键词匹配
        # Simple keyword matching
        # 实际实现应该读取配置文件
        # Actual implementation should read config file

        similar = []

        # 这里可以添加更多匹配逻辑
        # More matching logic can be added here

        return similar


def main():
    """主函数 | Main function"""
    import argparse
    import json

    parser = argparse.ArgumentParser(
        description="处理未匹配的图表 | Handle unmatched charts"
    )
    parser.add_argument(
        "input_json",
        help="输入 JSON 文件（包含图表信息）| Input JSON file (containing chart info)"
    )
    parser.add_argument(
        "-o", "--output",
        default="output",
        help="输出目录 | Output directory"
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
        chart_info = json.load(f)

    # 创建处理器并处理
    # Create handler and process
    handler = UnmatchedChartHandler()
    result = handler.handle_unmatched_chart(chart_info, args.output)

    # 输出结果
    # Output result
    print(json.dumps(result, indent=2, ensure_ascii=False))

    return 0


if __name__ == "__main__":
    exit(main())
