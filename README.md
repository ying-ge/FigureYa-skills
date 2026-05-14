# FigureYa Skills Collection

[English](#english) | [中文](#chinese)

<a id="english"></a>
## English

FigureYa Skills Collection is a set of specialized skills for Claude Code that help researchers work with the FigureYa visualization framework.

## What is FigureYa?

[FigureYa](https://github.com/ying-ge/FigureYa) is a standardized visualization framework containing 300+ biomedical data analysis and visualization modules. It provides:
- Standardized R Markdown templates
- Publication-ready visualizations
- Comprehensive documentation
- Easy-to-use analysis workflows

## Available Skills

### 1. FigureYa PDF Parser (figureya-pdf-parser) 🆕

An automated skill that extracts figures from literature PDFs and generates corresponding FigureYa modules through a multi-stage pipeline combining PDF parsing, text mining, AI vision recognition, and template-based code generation.

**Features**:
- **Multi-Stage Pipeline**: 5-stage workflow (PDF parsing → text mining → chart recognition → information fusion → template generation)
- **PDF Parsing**: Extract all images, full text, and section structure from PDF files using PyMuPDF
- **Text Mining**: Identify R packages, statistical methods, and figure descriptions from Materials and Methods sections
- **AI Chart Recognition**: Use Claude's vision capabilities to identify chart types with detailed visual analysis
- **Information Fusion**: Combine visual recognition (40% weight) with text evidence (60% weight) for higher accuracy
- **Confidence Scoring**: Calculate confidence scores with 4 decision levels (high ≥0.85, medium ≥0.70, low ≥0.50, very low <0.50)
- **Template-Based Generation**: Generate modules based on existing, verified FigureYa templates rather than creating from scratch
- **Three Automation Modes**:
  - **Fully automatic**: Complete automation without manual intervention
  - **Semi-automatic** (recommended): Automatic extraction with user confirmation at key steps
  - **Assisted**: Manual selection and customization with AI assistance
- **Bilingual Support**: Full Chinese/English content and documentation

**Supported Chart Types** (4 major categories):
- **Basic Statistical Charts**: box plot, scatter plot, bar plot, violin plot, dot plot
- **Genomics Analysis**: volcano plot, heatmap, PCA plot, MA plot, correlation plot
- **Survival Analysis**: Kaplan-Meier curve, Cox regression survival curve
- **Complex Composite Charts**: oncoprint/oncoplot, circos plot, forest plot

**Key Innovation**: Unlike pure visual recognition (70% accuracy), this skill combines visual recognition with text mining—extracting tool/method information from Methods sections (e.g., "using EnhancedVolcano package")—to achieve 90%+ accuracy in chart type identification. It also provides explainable decisions by showing evidence from both visual and textual sources.

**Workflow Example**:
```
Input: Nature paper PDF
↓
Extract 12 figures + full text
↓
Text mining finds: limma, EnhancedVolcano, survimin, maftools
↓
Figure 1: Visual (volcano 0.85) + Text ("EnhancedVolcano") → Final: volcano (0.96)
Figure 2: Visual (survival 0.72) + Text ("Kaplan-Meier") → Final: KM curve (0.94)
Figure 3: Visual (heatmap 0.68) + Text (no match) → Final: heatmap (0.68) → Request confirmation
↓
Generate 12 FigureYa module folders
```

**Use when**: You have a literature PDF and want to quickly reproduce the visualizations, create FigureYa modules from published figures, or understand how published charts were created.

**Documentation**: See `skills/figureya-pdf-parser.md`

**Technical Requirements**: Requires Python packages (PyMuPDF, pdfplumber, spacy, nltk, scikit-learn, pandas, numpy, pyyaml)

### 2. FigureYa Creator (figureya-creator)

A specialized skill that helps researchers convert their R visualization code into standardized FigureYa modules with **intelligent code analysis and auto-documentation**.

**Features**:
- **Smart Code Analysis**: Automatically analyzes R scripts to extract key information
- **Auto-Generated Documentation**: Generates 80% of documentation content automatically
  - Requirement descriptions (based on chart type)
  - Application scenarios (standard templates for each chart type)
  - Parameter explanations (auto-extracted from code)
  - Data requirements (inferred from code patterns)
- **Convert R code to FigureYa-standard format**
- **Create complete module structure with all required files**
- **Generate bilingual documentation (Chinese/English)**
- **Ensure quality standards for publication**

**Workflow Example**:
```
Input: 10 lines of R code
↓
Smart analysis: Identify packages, chart type, parameters
  - Detected packages: survival, survminer, ggplot2
  - Inferred chart type: Kaplan-Meier survival curve
  - Extracted parameters: pval=TRUE, conf.int=TRUE
↓
Generate draft (80% complete):
  ✓ Requirement description with chart info
  ✓ Application scenarios (standard survival analysis)
  ✓ Data requirements (time, status, group columns)
  ✓ Parameter explanations
↓
User supplements (20%):
  - Add specific use case description
  - Add data source information
  - Add literature references (if any)
↓
Output: Complete FigureYa module with rich documentation
```

**Time Savings**: From ~2 hours (manual) to ~20 minutes (smart analysis) - **75% faster** ⚡

**Use when**: You have a working R script and want to quickly convert it to a FigureYa module with rich documentation, or you want to create new FigureYa modules.

**Documentation**: See `skills/figureya-creator.md`

### 3. FigureYa Learn Statistics (figureya-learn-statistics)

An interactive learning skill that helps users learn statistics through FigureYa's 300+ visualization modules.

**Features**:
- Adaptive learning paths for beginners, graduates, and practitioners
- 4 learning modes: interactive tutorial, query assistant, structured course, project-driven
- 3 interaction styles: interactive learning, Socratic questioning, visual demonstration
- Complete coverage from basic to advanced statistics
- 300+ FigureYa module index with categorization
- Bilingual support (Chinese/English)

**Use when**: You want to learn statistical concepts, find teaching examples, or understand statistics through practical code.

**Documentation**: See [STATISTICS_LEARNING_SKILL.md](STATISTICS_LEARNING_SKILL.md) and [QUICK_START.md](QUICK_START.md)

### 4. FigureYa Inference Thinking (figureya-inference-thinking) 🆕

A deep-dive skill that uses volcano plots to understand the fundamental nature of statistical inference.

**Features**:
- **Four-layer progressive learning**: From data perception → concepts → formulas → theory
- **Socratic questioning**: Guides thinking through questions rather than giving direct answers
- **7 core questions**: Deep exploration of variance, p-value, sample size, model distortion, biological/technical variability, multiple testing, and small sample instability
- **From zero to theory**: Suitable for complete beginners while including deep mathematical derivations
- **Bilingual support**: Full Chinese/English content

**Core Questions Covered**:
1. Why does variance exist?
2. Why is p-value not "truth probability"?
3. Why does sample size matter?
4. Why do models always distort?
5. Biological vs Technical variability
6. Why does multiple testing ruin naive inference?
7. Why is p-value unstable with small samples?

**Use when**: You want to deeply understand statistical concepts, build statistical thinking, or grasp the essence of "inference under uncertainty".

**Documentation**: See [INFERENCE_THINKING_SKILL.md](INFERENCE_THINKING_SKILL.md)

**Difference from figureya-learn-statistics**:
- **figureya-learn-statistics**: Method learning (how to use statistics)
- **figureya-inference-thinking**: Thinking foundation (why statistics exists)

### 5. FigureYa Bayesian Thinking (figureya-bayesian-thinking) 🆕

A thinking-restructuring skill that transforms "significance thinking" (p-value < 0.05) into "Bayesian uncertainty updating thinking" through biomedical data examples.

**Features**:
- **Mindset Transformation**: From binary (significant/not significant) to continuous (posterior probability distribution)
- **7 Core Modules**: Medical testing, Bayes' formula, FDR interpretation, Empirical Bayes (limma), prior selection, Bayesian workflow, practice exercises
- **Intuitive Examples**: Start with medical testing (16.7% vs 95% misconception), then apply to gene expression analysis
- **Connect to Real Tools**: limma's Empirical Bayes, FDR's Bayesian interpretation, full Bayesian analysis (BAPC module)
- **From Intuition to Practice**: Understanding conditional probability reversal → calculating posterior probabilities → real data analysis
- **Bilingual support**: Full Chinese/English content

**Core Topics Covered**:
1. **Thinking Pattern Comparison**: Why p = 0.03 ≠ 97% probability
2. **Bayes' Formula**: From medical testing to gene differential expression
3. **FDR's Bayesian Interpretation**: Why multiple testing needs correction
4. **Empirical Bayes**: limma's small sample magic
5. **Prior Selection**: How to encode biological knowledge
6. **Bayesian Workflow**: Complete pipeline from data to decision
7. **Practice Exercises**: Re-interpreting published results with Bayesian thinking

**Use when**: You want to understand Bayesian inference, transition from frequentist to Bayesian thinking, learn how to incorporate prior knowledge, or understand why limma performs well with small samples.

**Documentation**: See [BAYESIAN_THINKING_SKILL.md](BAYESIAN_THINKING_SKILL.md)

**Difference from other skills**:
- **figureya-learn-statistics**: Method learning (how to use statistics)
- **figureya-inference-thinking**: Understanding statistical inference (frequentist + Bayesian)
- **figureya-bayesian-thinking**: Specialized Bayesian training (mindset restructuring)

**Recommended Learning Order**:
1. figureya-inference-thinking (build statistical foundation)
2. figureya-bayesian-thinking (deepen Bayesian thinking)
3. figureya-learn-statistics (learn specific methods as needed)

## Installation

### Quick Install

Install all skills at once:

```bash
# Clone the repository
git clone https://github.com/ying-ge/FigureYa-skills.git

# Copy all skills to Claude Code skills directory (with proper directory structure)
cd FigureYa-skills
for skill in skills/*; do
  skill_name=$(basename "$skill")
  mkdir -p ~/.claude/skills/"$skill_name"
  cp "$skill"/SKILL.md ~/.claude/skills/"$skill_name"/SKILL.md
done
```

### Individual Installation

Install specific skills:

```bash
# Install FigureYa PDF Parser 🆕
mkdir -p ~/.claude/skills/figureya-pdf-parser
curl -o ~/.claude/skills/figureya-pdf-parser/SKILL.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-pdf-parser/SKILL.md

# Install FigureYa Creator
mkdir -p ~/.claude/skills/figureya-creator
curl -o ~/.claude/skills/figureya-creator/SKILL.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-creator/SKILL.md

# Install FigureYa Learn Statistics
mkdir -p ~/.claude/skills/figureya-learn-statistics
curl -o ~/.claude/skills/figureya-learn-statistics/SKILL.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-learn-statistics/SKILL.md

# Install FigureYa Inference Thinking 🆕
mkdir -p ~/.claude/skills/figureya-inference-thinking
curl -o ~/.claude/skills/figureya-inference-thinking/SKILL.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-inference-thinking/SKILL.md

# Install FigureYa Bayesian Thinking 🆕
mkdir -p ~/.claude/skills/figureya-bayesian-thinking
curl -o ~/.claude/skills/figureya-bayesian-thinking/SKILL.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-bayesian-thinking/SKILL.md
```

See [INSTALL.md](INSTALL.md) for detailed installation instructions.

## Usage

### Using FigureYa PDF Parser 🆕

In Claude Code, simply use the `figureya-pdf-parser` skill and provide a literature PDF file. The skill will:

1. **Parse the PDF** to extract all figures and text
2. **Identify chart types** by combining visual recognition with text mining
3. **Generate FigureYa modules** based on existing templates

**Example**:
```
用户：我有一篇 Nature 论文的 PDF，想要为其中的图表生成 FigureYa 模块
```

The skill supports three automation modes:
- **Fully automatic**: Complete automation without manual intervention
- **Semi-automatic** (recommended): Automatic with user confirmation at key steps
- **Assisted**: Manual selection and customization with AI assistance

**Key Innovation**: By extracting tool/method information from Materials and Methods sections (e.g., "using EnhancedVolcano package"), it achieves much higher accuracy than visual recognition alone (90%+ vs 70%).

### Using FigureYa Creator

In Claude Code, simply use the `figureya-creator` skill and provide your R visualization code. The skill will:
- Analyze your code structure
- Create the standard FigureYa directory structure
- Generate the R Markdown file with proper formatting
- Create `install_dependencies.R` script
- Prepare input data templates
- Generate documentation

### Using FigureYa Inference Thinking 🆕

In Claude Code, use any of these prompts:

```
I want to understand why statistics exists
```

```
What is p-value really?
```

```
Why do we need statistical inference?
```

This skill will guide you through deep conceptual understanding using volcano plots as the entry point.

### Using FigureYa Bayesian Thinking 🆕

In Claude Code, use any of these prompts:

```
I want to understand Bayesian inference
```

```
Why does p < 0.05 not mean 95% probability?
```

```
How do I incorporate biological prior knowledge?
```

```
Use figureya-bayesian-thinking to help me understand Bayesian inference
```

This skill will restructure your thinking from "significance-based" to "Bayesian uncertainty updating" through biomedical examples like medical testing and gene expression analysis.

### Using FigureYa Learn Statistics

In Claude Code, use any of these prompts:

```
I want to learn statistics with FigureYa
```

```
What is Cox regression? Which FigureYa modules should I use?
```

```
I'm a graduate student, I want to learn survival analysis
```

See [QUICK_START.md](QUICK_START.md) for more usage examples.

## Project Structure

```
FigureYa-skills/
├── skills/
│   ├── figureya-pdf-parser/               # PDF parser skill 🆕
│   │   └── SKILL.md
│   ├── figureya-creator/                  # FigureYa module creator skill
│   │   └── SKILL.md
│   ├── figureya-learn-statistics/         # Statistics learning skill
│   │   └── SKILL.md
│   ├── figureya-inference-thinking/       # Statistical inference thinking skill 🆕
│   │   └── SKILL.md
│   └── figureya-bayesian-thinking/        # Bayesian thinking skill 🆕
│       └── SKILL.md
├── docs/                                   # Additional documentation
├── INSTALL.md                              # Installation guide
├── QUICK_START.md                          # Quick start guide
├── STATISTICS_LEARNING_SKILL.md           # Detailed skill documentation
├── INFERENCE_THINKING_SKILL.md            # Inference thinking skill documentation 🆕
├── BAYESIAN_THINKING_SKILL.md             # Bayesian thinking skill documentation 🆕
└── README.md                               # This file
```

## Citation

If you use FigureYa in your research, please cite:

> Xiaofan Lu, et al. (2025). FigureYa: A Standardized Visualization Framework for Enhancing Biomedical Data Interpretation and Research Efficiency. iMetaMed. https://doi.org/10.1002/imm3.70005

## Links

- FigureYa Repository: https://github.com/ying-ge/FigureYa
- FigureYa Documentation: https://ying-ge.github.io/FigureYa/
- FigureYa Wiki: https://github.com/ying-ge/FigureYa/wiki

## Contributing

We welcome contributions! If you have ideas for new skills or improvements to existing ones:
1. Fork the repository
2. Create a new branch for your skill
3. Follow the existing skill structure
4. Submit a pull request

## License

This project follows the same license as FigureYa: [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/)

---

<a id="chinese"></a>
## 中文

FigureYa Skills Collection 是一套 Claude Code 的专用技能集合，帮助研究者使用 FigureYa 可视化框架。

## 什么是 FigureYa？

[FigureYa](https://github.com/ying-ge/FigureYa) 是一个包含 300+ 生物医学数据分析和可视化模块的标准化框架。它提供：
- 标准化的 R Markdown 模板
- 发表级的可视化质量
- 完整的文档说明
- 易用的分析流程

## 可用的 Skills

### 1. FigureYa PDF Parser (figureya-pdf-parser) 🆕

一个自动化 skill，通过多阶段流程从文献 PDF 中提取图表并生成对应的 FigureYa 模块。

**功能**：
- **五阶段流程**：PDF 解析 → 文本挖掘 → 图表识别 → 信息融合 → 模板生成
- **PDF 解析**：使用 PyMuPDF 提取所有图片、全文和章节结构
- **文本挖掘**：从 Materials and Methods 部分识别 R 包、统计方法和图表描述
- **AI 图表识别**：使用 Claude 的视觉能力识别图表类型并进行详细分析
- **信息融合**：综合视觉识别（40% 权重）和文本证据（60% 权重）提高准确度
- **置信度评分**：计算置信度分数，4 个决策级别（高 ≥0.85、中 ≥0.70、低 ≥0.50、很低 <0.50）
- **基于模板生成**：基于现有验证过的 FigureYa 模板生成新模块，而非从零创建
- **三种自动化模式**：
  - **完全自动化**：无需人工干预的完全自动化
  - **半自动化**（推荐）：自动提取但在关键步骤请求用户确认
  - **辅助式**：用户手动选择和定制，AI 提供建议
- **中英文双语**：完整的双语支持和文档

**支持的图表类型**（4 大类）：
- **基础统计图**：箱线图、散点图、柱状图、小提琴图、点图
- **组学分析图**：火山图、热图、PCA 图、MA 图、相关性图
- **生存分析图**：Kaplan-Meier 曲线、Cox 回归生存曲线
- **复杂组合图**：oncoprint/oncoplot、circos plot、forest plot

**核心创新**：与纯视觉识别（70% 准确率）不同，本 skill 结合视觉识别和文本挖掘——从 Methods 部分提取工具/方法信息（如 "using EnhancedVolcano package"）——将图表类型识别准确率提升到 90%+。同时提供可解释的决策，显示来自视觉和文本双方的证据。

**工作流程示例**：
```
输入：Nature 论文 PDF
↓
提取 12 个图表 + 全文
↓
文本挖掘发现：limma, EnhancedVolcano, survimin, maftools
↓
Figure 1: 视觉(火山图 0.85) + 文本("EnhancedVolcano") → 最终：火山图(0.96)
Figure 2: 视觉(生存曲线 0.72) + 文本("Kaplan-Meier") → 最终：KM 曲线(0.94)
Figure 3: 视觉(热图 0.68) + 文本(无匹配) → 最终：热图(0.68) → 请求确认
↓
生成 12 个 FigureYa 模块文件夹
```

**使用场景**：当你有文献 PDF 并想快速复现其中的可视化、从已发表论文创建 FigureYa 模块，或理解已发表图表是如何创建的时候使用。

**文档**：参见 `skills/figureya-pdf-parser.md`

**技术要求**：需要 Python 包（PyMuPDF, pdfplumber, spacy, nltk, scikit-learn, pandas, numpy, pyyaml）

### 2. FigureYa Creator (figureya-creator)

一个专用的 skill，帮助研究者将他们的 R 可视化代码转换为标准化的 FigureYa 模块，**具备智能代码分析和自动文档生成功能**。

**功能**：
- **智能代码分析**：自动分析 R 脚本，提取关键信息
  - 识别使用的 R 包
  - 推断图表类型
  - 提取关键参数
  - 识别数据输入格式
- **自动生成文档**：自动生成 80% 的文档内容
  - 需求描述（基于图表类型）
  - 应用场景（标准模板）
  - 参数说明（解释提取的参数）
  - 数据要求（推断数据格式）
- **将 R 代码转换为 FigureYa 标准格式**
- **创建包含所有必需文件的完整模块结构**
- **生成双语文档（中英文）**
- **确保发表级别的质量标准**

**工作流程示例**：
```
输入：10 行 R 代码
↓
智能分析：识别包、图表、参数
  - 检测到的包：survival, survminer, ggplot2
  - 推断图表类型：Kaplan-Meier 生存曲线
  - 提取的参数：pval=TRUE, conf.int=TRUE
↓
生成初稿（80% 完成）：
  ✓ 需求描述（包含图表信息）
  ✓ 应用场景（标准生存分析场景）
  ✓ 数据要求（time, status, group 列）
  ✓ 参数说明
↓
用户补充（20%）：
  - 添加具体应用场景
  - 添加数据来源信息
  - 添加文献引用（如果有）
↓
输出：完整的 FigureYa 模块，包含丰富的文档
```

**时间节省**：从手动方式 ~2 小时 → 智能分析 ~20 分钟，**提升 75% 效率** ⚡

**使用场景**：当你有工作的 R 脚本并想快速转换成 FigureYa 模块格式，或者想创建新的 FigureYa 模块时使用。

**文档**：参见 `skills/figureya-creator.md`

### 3. FigureYa Learn Statistics (figureya-learn-statistics)

一个交互式学习 skill，帮助用户通过 FigureYa 的 300+ 可视化模块学习统计学。

**功能**：
- 支持初学者、研究生、从业者三种用户类型
- 4种学习模式：互动教程、查询助手、课程结构、项目驱动
- 3种交互方式：交互式学习、苏格拉底式提问、可视化演示
- 覆盖从基础到高级的统计学主题
- 300+ FigureYa 模块的完整索引和分类
- 中英文双语支持

**使用场景**：当你想学习统计概念、寻找教学示例或通过实际代码理解统计学时使用。

**文档**：参见 [STATISTICS_LEARNING_SKILL.md](STATISTICS_LEARNING_SKILL.md) 和 [QUICK_START.md](QUICK_START.md)

### 4. FigureYa Inference Thinking (figureya-inference-thinking) 🆕

一个深入思考的 skill，通过火山图理解统计推断的根本性质。

**功能**：
- **四层递进学习**：从数据感知 → 概念 → 公式 → 理论
- **苏格拉底式提问**：通过提问引导思考，而非直接给出答案
- **7 个核心问题**：深入探索 variance、p-value、sample size、模型失真、biological/technical variability、multiple testing、小样本问题
- **从零到理论**：适合完全初学者，同时包含深入数学推导
- **中英文双语**：完整的双语内容

**核心问题**：
1. Variance 为什么存在？
2. p-value 为什么不是"真理概率"？
3. Sample size 为什么重要？
4. 为什么模型一定会失真？
5. Biological vs Technical Variability
6. 为什么 Multiple Testing 会毁掉 Naive Inference？
7. 为什么小样本下 p-value 不稳定？

**使用场景**：当你想深入理解统计概念、建立统计思维、或理解"在不确定性中做推断"的本质时使用。

**文档**：参见 [INFERENCE_THINKING_SKILL.md](INFERENCE_THINKING_SKILL.md)

**与 figureya-learn-statistics 的区别**：
- **figureya-learn-statistics**：方法学习（如何使用统计）
- **figureya-inference-thinking**：思维建立（为什么统计学存在）

### 5. FigureYa Bayesian Thinking (figureya-bayesian-thinking) 🆕

一个思维重构 skill，将"显著性思维"（p-value < 0.05）转化为"贝叶斯式的不确定性更新思维"，通过生物医学数据实例建立贝叶斯直觉。

**功能**：
- **思维模式重构**：从二元（显著/不显著）到连续（后验概率分布）
- **7 个核心模块**：思维对比、贝叶斯公式、FDR 解释、Empirical Bayes（limma）、先验选择、贝叶斯工作流、实践练习
- **直观示例**：从医疗检测（16.7% vs 95% 误解）开始，再应用到基因差异表达分析
- **连接实际工具**：limma 的 Empirical Bayes、FDR 的贝叶斯解释、完整贝叶斯分析（BAPC 模块）
- **从直觉到实践**：理解条件概率反转 → 计算后验概率 → 真实数据分析
- **中英文双语**：完整的双语内容

**核心主题**：
1. **思维模式对比**：为什么 p = 0.03 ≠ 97% 概率
2. **贝叶斯公式**：从医疗检测到基因差异表达
3. **FDR 的贝叶斯解释**：为什么多重检验需要校正
4. **Empirical Bayes**：limma 的小样本魔法
5. **先验选择**：如何编码生物学知识
6. **贝叶斯工作流**：从数据到决策的完整流程
7. **实践练习**：用贝叶斯思维重新解读已发表结果

**使用场景**：当你想理解贝叶斯推断、从频率学派转向贝叶斯学派、学习如何结合先验知识、或理解 limma 在小样本下表现好的原因时使用。

**文档**：参见 [BAYESIAN_THINKING_SKILL.md](BAYESIAN_THINKING_SKILL.md)

**与其他 skills 的区别**：
- **figureya-learn-statistics**：方法学习（如何使用统计）
- **figureya-inference-thinking**：理解统计推断（频率学派 + 贝叶斯学派）
- **figureya-bayesian-thinking**：专门的贝叶斯训练（思维模式重构）

**推荐学习顺序**：
1. figureya-inference-thinking（建立统计基础）
2. figureya-bayesian-thinking（深化贝叶斯思维）
3. figureya-learn-statistics（按需学习具体方法）

## 安装

### 快速安装

一次性安装所有 skills：

```bash
# 克隆仓库
git clone https://github.com/ying-ge/FigureYa-skills.git

# 复制所有 skills 到 Claude Code skills 目录（带正确的目录结构）
cd FigureYa-skills
for skill in skills/*; do
  skill_name=$(basename "$skill")
  mkdir -p ~/.claude/skills/"$skill_name"
  cp "$skill"/SKILL.md ~/.claude/skills/"$skill_name"/SKILL.md
done
```

### 单独安装

安装特定的 skill：

```bash
# 安装 FigureYa PDF Parser 🆕
mkdir -p ~/.claude/skills/figureya-pdf-parser
curl -o ~/.claude/skills/figureya-pdf-parser/SKILL.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-pdf-parser/SKILL.md

# 安装 FigureYa Creator
mkdir -p ~/.claude/skills/figureya-creator
curl -o ~/.claude/skills/figureya-creator/SKILL.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-creator/SKILL.md

# 安装 FigureYa Learn Statistics
mkdir -p ~/.claude/skills/figureya-learn-statistics
curl -o ~/.claude/skills/figureya-learn-statistics/SKILL.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-learn-statistics/SKILL.md

# 安装 FigureYa Inference Thinking 🆕
mkdir -p ~/.claude/skills/figureya-inference-thinking
curl -o ~/.claude/skills/figureya-inference-thinking/SKILL.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-inference-thinking/SKILL.md

# 安装 FigureYa Bayesian Thinking 🆕
mkdir -p ~/.claude/skills/figureya-bayesian-thinking
curl -o ~/.claude/skills/figureya-bayesian-thinking/SKILL.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-bayesian-thinking/SKILL.md
```

详细安装说明请参阅 [INSTALL.md](INSTALL.md)。

## 使用方法

### 使用 FigureYa PDF Parser 🆕

在 Claude Code 中使用 `figureya-pdf-parser` skill，提供文献 PDF 文件。该 skill 会：

1. **解析 PDF**，提取所有图表和文本
2. **识别图表类型**，通过结合视觉识别和文本挖掘
3. **生成 FigureYa 模块**，基于现有模板

**示例**：
```
用户：我有一篇 Nature 论文的 PDF，想要为其中的图表生成 FigureYa 模块
```

该 skill 支持三种自动化模式：
- **完全自动化**：无需人工干预的完全自动化
- **半自动化**（推荐）：自动提取但在关键步骤请求用户确认
- **辅助式**：用户手动选择和定制，AI 提供建议

**核心创新**：通过从 Materials and Methods 部分提取工具/方法信息（如 "using EnhancedVolcano package"），比纯视觉识别的准确度（70%）高得多，达到 90%+。

### 使用 FigureYa Creator

在 Claude Code 中使用 `figureya-creator` skill，提供你的 R 可视化代码。该 skill 会：
- 分析你的代码结构
- 创建标准的 FigureYa 目录结构
- 生成格式正确的 R Markdown 文件
- 创建 `install_dependencies.R` 脚本
- 准备输入数据模板
- 生成文档

### 使用 FigureYa Learn Statistics

在 Claude Code 中使用以下任一提示：

```
我要用 FigureYa 学习统计
```

```
什么是 Cox 回归？应该用哪些 FigureYa 模块？
```

```
我是生物医学研究生，想学习生存分析
```

更多使用示例请参阅 [QUICK_START.md](QUICK_START.md)。

### 使用 FigureYa Inference Thinking 🆕

在 Claude Code 中使用以下任一提示：

```
我想理解统计学为什么存在
```

```
p-value 到底是什么？
```

```
为什么需要统计推断？
```

这个 skill 将引导你通过火山图深入理解统计概念。

### 使用 FigureYa Bayesian Thinking 🆕

在 Claude Code 中使用以下任一提示：

```
我想理解贝叶斯推断
```

```
为什么 p < 0.05 不意味着 95% 概率？
```

```
如何结合生物学先验知识？
```

```
用 figureya-bayesian-thinking 帮我理解贝叶斯推断
```

这个 skill 将通过医疗检测和基因表达分析等生物医学实例，引导你从"显著性思维"转向"贝叶斯式的不确定性更新思维"。

## 安装

## 项目结构

```
FigureYa-skills/
├── skills/
│   ├── figureya-pdf-parser/               # PDF 解析和模块生成工具 🆕
│   │   └── SKILL.md
│   ├── figureya-creator/                  # FigureYa 模块创建工具
│   │   └── SKILL.md
│   ├── figureya-learn-statistics/         # 统计学学习 skill
│   │   └── SKILL.md
│   ├── figureya-inference-thinking/       # 统计推断思维 skill 🆕
│   │   └── SKILL.md
│   └── figureya-bayesian-thinking/        # 贝叶斯思维 skill 🆕
│       └── SKILL.md
├── scripts/                                # 支持脚本 🆕
│   ├── pdf_parser.py                       # PDF 解析脚本
│   ├── text_miner.py                       # 文本挖掘脚本
│   ├── chart_identifier.py                 # 图表识别脚本
│   ├── info_fusion.py                      # 信息融合脚本
│   └── template_generator.py               # 模板生成脚本
├── chart_type_mapping.yaml                 # 图表类型映射配置 🆕
├── method_keywords.yaml                    # 方法关键词配置 🆕
├── docs/                                   # 附加文档
├── INSTALL.md                              # 安装指南
├── QUICK_START.md                          # 快速使用指南
├── STATISTICS_LEARNING_SKILL.md           # 详细 skill 文档
├── INFERENCE_THINKING_SKILL.md            # 统计思维 skill 文档 🆕
├── BAYESIAN_THINKING_SKILL.md             # 贝叶斯思维 skill 文档 🆕
└── README.md                               # 本文件
```

## 引用

如果你在研究中使用了 FigureYa，请引用：

> Xiaofan Lu, et al. (2025). FigureYa: A Standardized Visualization Framework for Enhancing Biomedical Data Interpretation and Research Efficiency. iMetaMed. https://doi.org/10.1002/imm3.70005

## 相关链接

- FigureYa 仓库：https://github.com/ying-ge/FigureYa
- FigureYa 文档：https://ying-ge.github.io/FigureYa/
- FigureYa Wiki：https://github.com/ying-ge/FigureYa/wiki

## 贡献

我们欢迎贡献！如果你有新 skill 的想法或对现有 skill 的改进建议：
1. Fork 本仓库
2. 为你的 skill 创建新分支
3. 遵循现有的 skill 结构
4. 提交 pull request

## 许可证

本项目遵循与 FigureYa 相同的许可证：[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/)

---

## Dependencies for PDF Parser

The `figureya-pdf-parser` skill requires additional Python packages:

```bash
# PDF parsing
pip install PyMuPDF
pip install pdfplumber
pip install Pillow

# Text mining and NLP
pip install spacy
pip install nltk
pip install scikit-learn

# Data processing
pip install pandas
pip install numpy

# YAML parsing
pip install pyyaml
```

R packages are already included in existing FigureYa modules.

## Version History

### v1.4.0 (2026-05-14) 🆕
- Enhanced `figureya-creator` with intelligent R code analysis and auto-documentation
- Added `r_code_analyzer.py` for smart R script analysis
- Auto-generates 80% of documentation content (requirements, scenarios, parameters, data requirements)
- Reduces module creation time from ~2 hours to ~20 minutes (75% faster)
- Added unmatched chart handling with skeleton module generation
  - `skeleton_generator.py`: Generate complete module skeletons for charts without matching templates
  - `unmatched_chart_handler.py`: Intelligent handling strategy based on confidence and information richness
  - Three handling strategies: create skeleton (≥0.7), provide guide (0.5-0.7), log only (<0.5)
- Enhanced `template_generator.py` with detailed reporting (success/failure/partial tracking)
- Enhanced `info_fusion.py` with similar module search capability
- Improved documentation in `figureya-pdf-parser.md` for unmatched chart handling

### v1.3.0 (2026-05-14) 🆕
- Added `figureya-pdf-parser` skill for automatic PDF figure extraction and module generation
- Implemented multi-stage pipeline: PDF parsing → text mining → chart recognition → information fusion → template generation
- Added text mining functionality to extract R packages and methods from Materials and Methods sections
- Combined visual recognition with text evidence for 90%+ accuracy in chart type identification
- Added three automation modes: fully automatic, semi-automatic (recommended), and assisted
- Created supporting Python scripts: pdf_parser.py, text_miner.py, chart_identifier.py, info_fusion.py, template_generator.py
- Added configuration files: chart_type_mapping.yaml, method_keywords.yaml
- Support for 4 major chart categories: basic statistics, genomics analysis, survival analysis, complex composite charts

### v1.2.0 (2026-05-12) 🆕
- Added `figureya-inference-thinking` skill
- Deep statistical inference understanding through volcano plots
- Four-layer progressive learning: perception → concepts → formulas → theory
- 7 core questions with Socratic questioning approach
- Added INFERENCE_THINKING_SKILL.md documentation

### v1.1.0 (2026-05-12)
- Added `figureya-learn-statistics` skill
- Reorganized project structure with `skills/` directory
- Added comprehensive documentation (INSTALL.md, QUICK_START.md)
- Updated README with bilingual content

### v1.0.0 (2025-04-18)
- Initial release with `figureya-creator` skill
