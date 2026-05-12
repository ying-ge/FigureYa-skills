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

### 1. FigureYa Creator (figureya-creator)

A specialized skill that helps researchers convert their R visualization code into standardized FigureYa modules.

**Features**:
- Convert R code to FigureYa-standard format
- Create complete module structure with all required files
- Generate bilingual documentation (Chinese/English)
- Ensure quality standards for publication

**Use when**: You want to create new FigureYa modules or convert existing R code to FigureYa format.

**Documentation**: See `skills/figureya-creator.md`

### 2. FigureYa Learn Statistics (figureya-learn-statistics)

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

### 3. FigureYa Inference Thinking (figureya-inference-thinking) 🆕

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

## Installation

### Quick Install

Install all skills at once:

```bash
# Clone the repository
git clone https://github.com/ying-ge/FigureYa-skills.git

# Copy all skills to Claude Code skills directory
cp FigureYa-skills/skills/*.md ~/.claude/skills/
```

### Individual Installation

Install specific skills:

```bash
# Install FigureYa Creator
curl -o ~/.claude/skills/figureya-creator.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-creator.md

# Install FigureYa Learn Statistics
curl -o ~/.claude/skills/figureya-learn-statistics.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-learn-statistics.md

# Install FigureYa Inference Thinking 🆕
curl -o ~/.claude/skills/figureya-inference-thinking.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-inference-thinking.md
```

See [INSTALL.md](INSTALL.md) for detailed installation instructions.

## Usage

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
│   ├── figureya-creator.md                 # FigureYa module creator skill
│   ├── figureya-learn-statistics.md        # Statistics learning skill
│   └── figureya-inference-thinking.md      # Statistical inference thinking skill 🆕
├── docs/                                   # Additional documentation
├── INSTALL.md                              # Installation guide
├── QUICK_START.md                          # Quick start guide
├── STATISTICS_LEARNING_SKILL.md           # Detailed skill documentation
├── INFERENCE_THINKING_SKILL.md            # Inference thinking skill documentation 🆕
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

### 1. FigureYa Creator (figureya-creator)

一个专用的 skill，帮助研究者将他们的 R 可视化代码转换为标准化的 FigureYa 模块。

**功能**：
- 将 R 代码转换为 FigureYa 标准格式
- 创建包含所有必需文件的完整模块结构
- 生成双语文档（中英文）
- 确保发表级别的质量标准

**使用场景**：当你想创建新的 FigureYa 模块或将现有 R 代码转换为 FigureYa 格式时使用。

**文档**：参见 `skills/figureya-creator.md`

### 2. FigureYa Learn Statistics (figureya-learn-statistics)

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

### 3. FigureYa Inference Thinking (figureya-inference-thinking) 🆕

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

## 安装

### 快速安装

一次性安装所有 skills：

```bash
# 克隆仓库
git clone https://github.com/ying-ge/FigureYa-skills.git

# 复制所有 skills 到 Claude Code skills 目录
cp FigureYa-skills/skills/*.md ~/.claude/skills/
```

### 单独安装

安装特定的 skill：

```bash
# 安装 FigureYa Creator
curl -o ~/.claude/skills/figureya-creator.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-creator.md

# 安装 FigureYa Learn Statistics
curl -o ~/.claude/skills/figureya-learn-statistics.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-learn-statistics.md

# 安装 FigureYa Inference Thinking 🆕
curl -o ~/.claude/skills/figureya-inference-thinking.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-inference-thinking.md
```

详细安装说明请参阅 [INSTALL.md](INSTALL.md)。

## 使用方法

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

## 安装

## 项目结构

```
FigureYa-skills/
├── skills/
│   ├── figureya-creator.md                 # FigureYa 模块创建工具
│   ├── figureya-learn-statistics.md        # 统计学学习 skill
│   └── figureya-inference-thinking.md      # 统计推断思维 skill 🆕
├── docs/                                   # 附加文档
├── INSTALL.md                              # 安装指南
├── QUICK_START.md                          # 快速使用指南
├── STATISTICS_LEARNING_SKILL.md           # 详细 skill 文档
├── INFERENCE_THINKING_SKILL.md            # 统计思维 skill 文档 🆕
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

## Version History

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
