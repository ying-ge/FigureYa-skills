#!/usr/bin/env python3
"""
R 代码分析器 - 智能分析 R 脚本并提取关键信息
R Code Analyzer - Intelligently analyze R scripts and extract key information

功能 | Features:
- 识别使用的 R 包
- 识别数据输入格式
- 识别图表类型
- 识别关键参数
- 自动生成文档初稿
"""

import re
import yaml
from typing import Dict, List, Any, Tuple
from pathlib import Path


class RCodeAnalyzer:
    """R 代码分析器类 | R Code Analyzer class"""

    def __init__(self, chart_config_path: str = None):
        """
        初始化分析器
        Initialize analyzer

        参数 | Parameters:
            chart_config_path: 图表类型配置文件路径 | Chart type config file path
        """
        self.chart_config = self._load_config(chart_config_path)
        self.r_package_keywords = self._build_r_package_keywords()

    def _load_config(self, config_path: str = None) -> Dict:
        """加载配置文件"""
        if config_path is None:
            base_dir = Path(__file__).parent.parent
            config_path = base_dir / "chart_type_mapping.yaml"

        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def _build_r_package_keywords(self) -> Dict[str, List[str]]:
        """构建 R 包关键词映射"""
        return {
            # 可视化包 | Visualization packages
            "ggplot2": ["scatter plot", "bar plot", "box plot", "line plot", "violin plot"],
            "survminer": ["kaplan-meier", "survival curve", "survival plot"],
            "pheatmap": ["heatmap", "heat map"],
            "ComplexHeatmap": ["heatmap", "complex heatmap", "oncoprint"],
            "EnhancedVolcano": ["volcano plot", "volcano"],
            "maftools": ["oncoprint", "oncoplot", "mutation plot"],
            "forestplot": ["forest plot", "forest plot"],
            "circlize": ["circos", "chord diagram", "circular plot"],

            # 分析包 | Analysis packages
            "survival": ["kaplan-meier", "survival analysis", "cox regression"],
            "limma": ["volcano plot", "ma plot", "differential expression"],
            "DESeq2": ["volcano plot", "ma plot", "differential expression"],
            "edgeR": ["volcano plot", "ma plot", "differential expression"],
            "stats": ["correlation", "t-test", "anova"],
            "corrplot": ["correlation plot", "correlation matrix"],
        }

    def analyze_script(self, r_code: str) -> Dict[str, Any]:
        """
        分析 R 脚本
        Analyze R script

        参数 | Parameters:
            r_code: R 代码字符串 | R code string

        返回 | Returns:
            分析结果字典 | Analysis result dictionary
        """
        print("分析 R 代码... | Analyzing R code...")

        result = {
            "r_packages": self._identify_r_packages(r_code),
            "data_inputs": self._identify_data_inputs(r_code),
            "chart_type": self._infer_chart_type(r_code),
            "parameters": self._extract_parameters(r_code),
            "functions": self._identify_functions(r_code),
        }

        # 生成文档建议
        # Generate documentation suggestions
        result["suggestions"] = self._generate_documentation_suggestions(result)

        print(f"  ✓ 识别到 {len(result['r_packages'])} 个 R 包")
        print(f"  ✓ 识别到 {len(result['data_inputs'])} 个数据输入")
        print(f"  ✓ 推断图表类型: {result['chart_type']}")
        print(f"  ✓ 识别到 {len(result['parameters'])} 个参数")

        return result

    def _identify_r_packages(self, r_code: str) -> List[str]:
        """
        识别 R 包
        Identify R packages

        参数 | Parameters:
            r_code: R 代码字符串 | R code string

        返回 | Returns:
            R 包列表 | R package list
        """
        packages = []

        # 匹配 library() 或 require() 调用
        # Match library() or require() calls
        patterns = [
            r'(?:library|require)\s*\(\s*["\']?([\w.]+)["\']?\s*\)',
            r'(?:library|require)\s*\(\s*([\w.]+)\s*\)',
        ]

        for pattern in patterns:
            matches = re.findall(pattern, r_code)
            packages.extend(matches)

        # 去重并排序
        # Deduplicate and sort
        return sorted(set(packages))

    def _identify_data_inputs(self, r_code: str) -> List[Dict[str, str]]:
        """
        识别数据输入
        Identify data inputs

        参数 | Parameters:
            r_code: R 代码字符串 | R code string

        返回 | Returns:
            数据输入列表 | Data input list
        """
        inputs = []

        # 匹配读取数据的函数
        # Match data reading functions
        patterns = [
            r'read\.csv\s*\(\s*["\']([^"\']+)["\']',
            r'read\.table\s*\(\s*["\']([^"\']+)["\']',
            r'read\.delim\s*\(\s*["\']([^"\']+)["\']',
            r'fread\s*\(\s*["\']([^"\']+)["\']',
        ]

        for pattern in patterns:
            matches = re.findall(pattern, r_code)
            for filename in matches:
                inputs.append({
                    "filename": filename,
                    "type": self._infer_file_type(filename),
                })

        # 如果没有找到明确的文件名，尝试推断
        # If no explicit filename found, try to infer
        if not inputs:
            # 查找变量赋值
            # Look for variable assignments
            pattern = r'(\w+)\s*<-\s*read\.(csv|table|delim|fread)\s*\('
            matches = re.findall(pattern, r_code)
            for var_name in matches:
                inputs.append({
                    "variable": var_name,
                    "type": "data_frame",
                    "note": "文件名未在代码中明确指定"
                })

        return inputs

    def _infer_file_type(self, filename: str) -> str:
        """推断文件类型"""
        if filename.endswith('.csv'):
            return 'CSV'
        elif filename.endswith('.txt'):
            return 'TXT'
        elif filename.endswith('.tsv'):
            return 'TSV'
        else:
            return 'Unknown'

    def _infer_chart_type(self, r_code: str) -> str:
        """
        推断图表类型
        Infer chart type

        参数 | Parameters:
            r_code: R 代码字符串 | R code string

        返回 | Returns:
            推断的图表类型 | Inferred chart type
        """
        r_code_lower = r_code.lower()

        # 获取 R 包
        packages = self._identify_r_packages(r_code)
        package_str = ' '.join(packages).lower()

        # 获取函数名
        functions = self._identify_functions(r_code)
        function_str = ' '.join(functions).lower()

        # 基于包和函数推断
        # Infer based on packages and functions

        # 生存分析 | Survival analysis
        if any(pkg in package_str for pkg in ['survival', 'survminer']):
            if 'survfit' in function_str or 'ggsurvplot' in function_str:
                return "kaplan_meier_survival_curve"

        # 火山图 | Volcano plot
        if any(pkg in package_str for pkg in ['enhancedvolcano', 'limma', 'deseq2', 'edger']):
            if 'volcano' in function_str or 'enhancevolcano' in function_str:
                return "volcano_plot"

        # 热图 | Heatmap
        if any(pkg in package_str for pkg in ['pheatmap', 'complexheatmap', 'circlize']):
            if any(func in function_str for func in ['pheatmap', 'heatmap', 'heatmap']):
                return "heatmap"

        # 箱线图 | Box plot
        if 'geom_boxplot' in r_code_lower or 'boxplot' in function_str:
            return "box_plot"

        # 散点图 | Scatter plot
        if 'geom_point' in r_code_lower or 'geom_jitter' in r_code_lower:
            if 'geom_line' not in r_code_lower:  # 排除线图
                return "scatter_plot"

        # 柱状图 | Bar plot
        if 'geom_bar' in r_code_lower or 'geom_col' in r_code_lower:
            return "bar_plot"

        # 小提琴图 | Violin plot
        if 'geom_violin' in r_code_lower:
            return "violin_plot"

        # PCA 图 | PCA plot
        if 'prcomp' in function_str or 'pca' in r_code_lower:
            return "pca_plot"

        # MA plot
        if 'plotma' in function_str or 'ma plot' in r_code_lower:
            return "ma_plot"

        # Oncoprint
        if any(pkg in package_str for pkg in ['maftools']):
            if 'oncoprint' in function_str or 'oncoplot' in function_str:
                return "oncoprint"

        # Forest plot
        if 'forestplot' in function_str:
            return "forest_plot"

        # 默认
        # Default
        return "unknown_chart"

    def _extract_parameters(self, r_code: str) -> Dict[str, Dict[str, str]]:
        """
        提取参数
        Extract parameters

        参数 | Parameters:
            r_code: R 代码字符串 | R code string

        返回 | Returns:
            参数字典 | Parameter dictionary
        """
        parameters = {}

        # 查找赋值语句
        # Find assignment statements
        # 匹配 variable <- value 或 variable = value
        pattern = r'(\w+)\s*(?:<-=|=)\s*([^,\n]+)(?:\s*[,#])'

        matches = re.findall(pattern, r_code)

        for var_name, var_value in matches:
            # 清理值
            # Clean value
            var_value = var_value.strip()

            # 过滤掉明显的函数调用和过长语句
            # Filter out obvious function calls and long statements
            if any(keyword in var_value for keyword in ['function', 'read.csv', 'library', 'require']):
                continue

            if len(var_value) > 100:  # 过长
                continue

            parameters[var_name] = {
                "value": var_value,
                "type": self._infer_parameter_type(var_value),
                "description": self._generate_parameter_description(var_name, var_value)
            }

        return parameters

    def _infer_parameter_type(self, value: str) -> str:
        """推断参数类型"""
        value = value.strip().lower()

        if value in ['true', 'false']:
            return 'logical'
        elif value.replace('.', '').isdigit():
            return 'numeric'
        elif value.startswith('"') or value.startswith("'"):
            return 'string'
        elif 'c(' in value or 'list(' in value:
            return 'vector'
        else:
            return 'unknown'

    def _generate_parameter_description(self, name: str, value: str) -> str:
        """生成参数描述"""
        descriptions = {
            'pval': '是否显示 P 值 | Show p-value',
            'conf.int': '是否显示置信区间 | Show confidence interval',
            'conf.level': '置信水平 | Confidence level',
            'palette': '配色方案 | Color palette',
            'width': '图表宽度 | Chart width',
            'height': '图表高度 | Chart height',
            'logfc': 'log2 fold change 阈值 | log2 fold change threshold',
            'pvalue': 'P value 阈值 | P value threshold',
            'main': '图表标题 | Chart title',
            'xlab': 'X 轴标签 | X axis label',
            'ylab': 'Y 轴标签 | Y axis label',
        }

        name_lower = name.lower()
        for key, desc in descriptions.items():
            if key in name_lower:
                return desc

        return "参数 | Parameter"

    def _identify_functions(self, r_code: str) -> List[str]:
        """
        识别函数调用
        Identify function calls

        参数 | Parameters:
            r_code: R 代码字符串 | R code string

        返回 | Returns:
            函数列表 | Function list
        """
        # 匹配函数调用
        # Match function calls
        pattern = r'(\w+)\s*\('
        matches = re.findall(pattern, r_code)

        # 过滤掉常见的控制结构
        # Filter out common control structures
        control_structures = {'if', 'else', 'for', 'while', 'function', 'return'}
        functions = [m for m in matches if m not in control_structures]

        # 去重并排序
        # Deduplicate and sort
        return sorted(set(functions))

    def _generate_documentation_suggestions(self, analysis: Dict[str, Any]) -> Dict[str, str]:
        """
        生成文档建议
        Generate documentation suggestions

        参数 | Parameters:
            analysis: 分析结果 | Analysis result

        返回 | Returns:
            文档建议 | Documentation suggestions
        """
        chart_type = analysis.get("chart_type", "unknown")
        r_packages = analysis.get("r_packages", [])

        # 生成需求描述建议
        # Generate requirement description suggestions
        req_desc = self._generate_requirement_description_suggestion(chart_type, r_packages)

        # 生成应用场景建议
        # Generate application scenario suggestions
        app_scenario = self._generate_application_scenario_suggestion(chart_type)

        # 生成数据要求建议
        # Generate data requirement suggestions
        data_req = self._generate_data_requirement_suggestion(analysis)

        return {
            "requirement_description": req_desc,
            "application_scenario": app_scenario,
            "data_requirements": data_req,
        }

    def _generate_requirement_description_suggestion(self, chart_type: str, r_packages: List[str]) -> str:
        """生成需求描述建议"""

        chart_names = {
            "volcano_plot": "火山图",
            "heatmap": "热图",
            "kaplan_meier_survival_curve": "生存曲线",
            "box_plot": "箱线图",
            "scatter_plot": "散点图",
            "bar_plot": "柱状图",
            "violin_plot": "小提琴图",
            "pca_plot": "PCA 图",
            "ma_plot": "MA 图",
            "oncoprint": "突变谱图",
            "forest_plot": "森林图",
        }

        chart_name = chart_names.get(chart_type, chart_type.replace('_', ' '))

        desc = f"""绘制 {chart_name}，展示数据的可视化效果。
Draw {chart_name.replace('_', ' ')} to display data visualization.

**自动识别信息 | Auto-identified information:**
- 图表类型 | Chart type: {chart_type}
- 使用的 R 包 | R packages used: {', '.join(r_packages) if r_packages else 'None'}

**需要补充 | Need to supplement:**
- 具体的应用场景描述
- 数据来源说明
- 期望的视觉效果
- 相关文献引用（如果有）
"""

        return desc

    def _generate_application_scenario_suggestion(self, chart_type: str) -> str:
        """生成应用场景建议"""

        scenarios = {
            "volcano_plot": """
### 方法原理和特点
火山图，用于展示差异表达分析结果。散点表示基因，X 轴为 log2 fold change，
Y 轴为 -log10(p-value)。显著差异基因分布在图的两侧。

Volcano plot to display differential expression results. Points represent genes,
X axis is log2 fold change, Y axis is -log10(p-value). Significantly differentially
expressed genes are distributed on both sides.

### 具体使用场景
适用于：
- 转录组学差异分析
- 蛋白质组学定量分析
- 代谢组学差异分析

Applicable to:
- Transcriptomics differential analysis
- Proteomics quantitative analysis
- Metabolomics differential analysis
""",
            "kaplan_meier_survival_curve": """
### 方法原理和特点
Kaplan-Meier 估计量，用于估计生存函数。是非参数统计方法，
不依赖生存时间的分布假设。可以比较不同组别的生存差异。

Kaplan-Meier estimator to estimate survival function. Non-parametric statistical
method without assuming survival distribution. Can compare survival differences
between groups.

### 具体使用场景
适用于：
- 临床研究的生存分析
- 两组或多组生存时间比较
- 估计中位生存时间

Applicable to:
- Survival analysis in clinical studies
- Compare survival time between two or more groups
- Estimate median survival time
""",
            "heatmap": """
### 方法原理和特点
热图，用颜色展示数据矩阵中数值的大小。常用于展示基因表达模式、
样本聚类结果等。

Heatmap to display data matrix values using colors. Commonly used to show gene
expression patterns, sample clustering results.

### 具体使用场景
适用于：
- 高通量数据的可视化
- 聚类分析结果展示
- 模式识别和探索

Applicable to:
- High-throughput data visualization
- Clustering result display
- Pattern recognition and exploration
""",
            "box_plot": """
### 方法原理和特点
箱线图，通过统计量展示数据分布。显示中位数、四分位数、
极值等。常用于比较不同组别的分布差异。

Box plot to display data distribution through statistics. Shows median, quartiles,
extremes. Commonly used to compare distribution differences between groups.

### 具体使用场景
适用于：
- 连续变量分布比较
- 异常值检测
- 多组数据对比

Applicable to:
- Continuous variable distribution comparison
- Outlier detection
- Multi-group data comparison
""",
        }

        return scenarios.get(chart_type, """
### 方法原理和特点
[待补充具体方法的原理和特点]

### 具体使用场景
适用于：
- [应用场景 1]
- [应用场景 2]

Applicable to:
- [Use case 1]
- [Use case 2]
""")

    def _generate_data_requirement_suggestion(self, analysis: Dict[str, Any]) -> str:
        """生成数据要求建议"""

        data_inputs = analysis.get("data_inputs", [])
        chart_type = analysis.get("chart_type", "unknown")
        r_packages = analysis.get("r_packages", [])

        req = f"### 数据格式 | Data format\n\n"

        if data_inputs:
            req += "根据代码分析，需要以下数据：\n"
            req += "Based on code analysis, the following data is required:\n\n"

            for inp in data_inputs:
                if "filename" in inp:
                    req += f"- **{inp['filename']}** ({inp['type']})\n"
                elif "variable" in inp:
                    req += f"- **{inp['variable']}** (数据框 | data frame)\n"
                if "note" in inp:
                    req += f"  - {inp['note']}\n"
        else:
            req += "未在代码中找到明确的数据输入说明。\n"
            req += "No explicit data input specification found in code.\n\n"
            req += "通常需要的数据格式：\n"
            req += "Typically required data format:\n\n"

            # 根据图表类型推断数据要求
            if "survival" in chart_type.lower():
                req += "- time: 生存时间 | survival time\n"
                req += "- status: 事件状态 (0=删失, 1=事件) | event status (0=censored, 1=event)\n"
                req += "- group: 分组变量 | grouping variable\n"
            elif "volcano" in chart_type.lower():
                req += "- 基因名 | gene name\n"
                req += "- logFC: log2 fold change\n"
                req += "- P.Value: P 值\n"
            elif "heatmap" in chart_type.lower():
                req += "- 表达矩阵：行为基因，列为样本 | Expression matrix (genes as rows, samples as columns)\n"

        req += f"\n### 识别到的 R 包 | Identified R packages\n\n"
        req += f"{', '.join(r_packages) if r_packages else 'None'}\n"

        return req


def main():
    """主函数 | Main function"""
    import argparse

    parser = argparse.ArgumentParser(
        description="分析 R 代码 | Analyze R code"
    )
    parser.add_argument(
        "input_file",
        help="R 脚本文件路径 | R script file path"
    )

    args = parser.parse_args()

    # 检查文件是否存在
    # Check if file exists
    if not Path(args.input_file).exists():
        print(f"Error: File not found: {args.input_file}")
        return 1

    # 读取 R 代码
    # Read R code
    with open(args.input_file, "r", encoding="utf-8") as f:
        r_code = f.read()

    # 分析代码
    # Analyze code
    analyzer = RCodeAnalyzer()
    result = analyzer.analyze_script(r_code)

    # 输出结果
    # Output result
    print("\n" + "="*60)
    print("分析结果 | Analysis result:")
    print("="*60)

    print(f"\n识别到的 R 包 | Identified R packages:")
    for pkg in result['r_packages']:
        print(f"  - {pkg}")

    print(f"\n图表类型推断 | Chart type inference:")
    print(f"  {result['chart_type']}")

    print(f"\n识别到的参数 | Identified parameters:")
    for param_name, param_info in result['parameters'].items():
        print(f"  {param_name} = {param_info['value']}")
        print(f"    ({param_info['description']})")

    return 0


if __name__ == "__main__":
    exit(main())
