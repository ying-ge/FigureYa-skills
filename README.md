# FigureYa Module Creator / FigureYa 模块创建工具

[English](#english) | [中文](#chinese)

<a id="english"></a>
## English

FigureYa Module Creator is a specialized skill for Claude Code that helps researchers convert their R visualization code into standardized FigureYa modules.

### What is FigureYa?

[FigureYa](https://github.com/ying-ge/FigureYa) is a standardized visualization framework containing 300+ biomedical data analysis and visualization modules. It provides:

- Standardized R Markdown templates
- Publication-ready visualizations
- Comprehensive documentation
- Easy-to-use analysis workflows

### Purpose of This Tool

This tool helps you:

1. **Convert your R code** into FigureYa-standard format
2. **Create complete module structure** with all required files
3. **Generate bilingual documentation** (Chinese/English)
4. **Ensure quality standards** for publication

### How to Use

Simply use the `figureya-creator` skill in Claude Code and provide your R visualization code. The skill will:

- Analyze your code structure
- Create the standard FigureYa directory structure
- Generate the R Markdown file with proper formatting
- Create `install_dependencies.R` script
- Prepare input data templates
- Generate documentation

### Example

```r
# Your original code
library(ggplot2)
data <- read.csv("result.csv")
ggplot(data, aes(x=logFC, y=-log10(pval))) +
  geom_point() +
  theme_minimal()
```

The tool converts this into a complete FigureYa module with:
- Proper YAML header
- Bilingual documentation
- Parameter explanations
- Usage examples
- Output formatting

### Output Structure

```
FigureYaXXX[ModuleName]/
├── FigureYaXXX[ModuleName].Rmd      # Main R Markdown file
├── install_dependencies.R           # Dependency installer
├── FigureYaXXX[ModuleName].html     # Generated report
├── easy_input_*.csv                 # Input data templates
├── example.png                      # Reference image
└── [output].pdf                     # Vector graphics output
```

### Citation

If you use FigureYa in your research, please cite:

> Xiaofan Lu, et al. (2025). FigureYa: A Standardized Visualization Framework for Enhancing Biomedical Data Interpretation and Research Efficiency. iMetaMed. https://doi.org/10.1002/imm3.70005

### Links

- FigureYa Repository: https://github.com/ying-ge/FigureYa
- FigureYa Documentation: https://ying-ge.github.io/FigureYa/
- FigureYa Wiki: https://github.com/ying-ge/FigureYa/wiki

---

<a id="chinese"></a>
## 中文

FigureYa 模块创建工具是 Claude Code 的一个专用 skill，帮助研究者将他们的 R 可视化代码转换为标准化的 FigureYa 模块。

### 什么是 FigureYa？

[FigureYa](https://github.com/ying-ge/FigureYa) 是一个包含 300+ 生物医学数据分析和可视化模块的标准化框架。它提供：

- 标准化的 R Markdown 模板
- 发表级的可视化质量
- 完整的文档说明
- 易用的分析流程

### 工具用途

这个工具帮助你：

1. **转换 R 代码**为 FigureYa 标准格式
2. **创建完整模块结构**包含所有必需文件
3. **生成双语文档**（中英文）
4. **确保质量标准**达到发表要求

### 使用方法

在 Claude Code 中使用 `figureya-creator` skill，提供你的 R 可视化代码。该工具会：

- 分析你的代码结构
- 创建标准的 FigureYa 目录结构
- 生成格式正确的 R Markdown 文件
- 创建 `install_dependencies.R` 脚本
- 准备输入数据模板
- 生成文档

### 示例

```r
# 你的原始代码
library(ggplot2)
data <- read.csv("result.csv")
ggplot(data, aes(x=logFC, y=-log10(pval))) +
  geom_point() +
  theme_minimal()
```

工具会将此转换为完整的 FigureYa 模块，包含：
- 正确的 YAML header
- 双语文档
- 参数说明
- 使用示例
- 输出格式化

### 输出结构

```
FigureYaXXX[模块名]/
├── FigureYaXXX[模块名].Rmd          # 主 R Markdown 文件
├── install_dependencies.R           # 依赖包安装脚本
├── FigureYaXXX[模块名].html         # 生成的报告
├── easy_input_*.csv                 # 输入数据模板
├── example.png                      # 参考图片
└── [输出].pdf                       # 矢量图输出
```

### 引用

如果你在研究中使用了 FigureYa，请引用：

> Xiaofan Lu, et al. (2025). FigureYa: A Standardized Visualization Framework for Enhancing Biomedical Data Interpretation and Research Efficiency. iMetaMed. https://doi.org/10.1002/imm3.70005

### 相关链接

- FigureYa 仓库：https://github.com/ying-ge/FigureYa
- FigureYa 文档：https://ying-ge.github.io/FigureYa/
- FigureYa Wiki：https://github.com/ying-ge/FigureYa/wiki

---

## License

This project follows the same license as FigureYa: [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/)
