# 安装 FigureYa Skills

[English](#english) | [中文](#chinese)

<a id="english"></a>
## English

## Available Skills

This repository currently contains 2 skills:

1. **figureya-pdf-parser** 🆕 - Extract figures from PDF and generate FigureYa modules
2. **figureya-creator** - Convert R code to standardized FigureYa modules

## Installation Methods

### Method 1: Install All Skills (Recommended)

```bash
# Clone the repository
git clone https://github.com/ying-ge/FigureYa-skills.git

# Copy all skills to Claude Code skills directory (with proper structure)
cd FigureYa-skills
for skill in skills/*; do
  skill_name=$(basename "$skill")
  mkdir -p ~/.claude/skills/"$skill_name"
  cp "$skill"/SKILL.md ~/.claude/skills/"$skill_name"/SKILL.md
done

# Verify installation
ls -la ~/.claude/skills/
```

### Method 2: Install Individual Skills

#### Install FigureYa PDF Parser 🆕

```bash
mkdir -p ~/.claude/skills/figureya-pdf-parser
curl -o ~/.claude/skills/figureya-pdf-parser/SKILL.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-pdf-parser/SKILL.md
```

#### Install FigureYa Creator

```bash
mkdir -p ~/.claude/skills/figureya-creator
curl -o ~/.claude/skills/figureya-creator/SKILL.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-creator/SKILL.md
```

### Method 3: Manual Download from Browser

1. Visit the skill file on GitHub:
   - FigureYa PDF Parser: [SKILL.md](https://github.com/ying-ge/FigureYa-skills/blob/main/skills/figureya-pdf-parser/SKILL.md)
   - FigureYa Creator: [SKILL.md](https://github.com/ying-ge/FigureYa-skills/blob/main/skills/figureya-creator/SKILL.md)

2. Click the "Raw" button

3. Right-click "Save As" and save to:
   - `~/.claude/skills/figureya-pdf-parser/SKILL.md`
   - `~/.claude/skills/figureya-creator/SKILL.md`

## Verification

After installation, verify the skills are available:

```bash
# List all installed skills
ls -la ~/.claude/skills/

# You should see directories:
# figureya-pdf-parser/
# figureya-creator/

# Each directory should contain SKILL.md
ls ~/.claude/skills/figureya-creator/
# Output: SKILL.md
```

## Usage

### Using FigureYa PDF Parser 🆕

In Claude Code:

```
Use figureya-pdf-parser to extract figures from my PDF
```

### Using FigureYa Creator

In Claude Code:

```
Use figureya-creator to convert my R code to FigureYa format
```

### Using FigureYa Inference Thinking 🆕

In Claude Code:

```
I want to understand why statistics exists
```

```
What is p-value really?
```

### Using FigureYa Bayesian Thinking 🆕

In Claude Code:

```
I want to understand Bayesian inference
```

```
Why does p < 0.05 not mean 95% probability?
```

See [QUICK_START.md](QUICK_START.md) for more usage examples.

## System Requirements

- Claude Code installed
- FigureYa project cloned (recommended: `/Users/pro/FigureYa/`)
- R and RStudio (for running FigureYa modules)
- Python packages for PDF parser (PyMuPDF, pdfplumber, spacy, nltk, scikit-learn, pandas, numpy, pyyaml)

## Uninstallation

To remove individual skills:

```bash
# Remove FigureYa PDF Parser
rm -rf ~/.claude/skills/figureya-pdf-parser

# Remove FigureYa Creator
rm -rf ~/.claude/skills/figureya-creator

# Remove other skills
```

To remove all FigureYa skills:

```bash
rm -rf ~/.claude/skills/figureya-*
```

## Updates

To update to the latest version:

```bash
# Navigate to the repository
cd FigureYa-skills

# Pull latest changes
git pull origin main

# Re-copy skills to ~/.claude/skills/
for skill in skills/*; do
  skill_name=$(basename "$skill")
  mkdir -p ~/.claude/skills/"$skill_name"
  cp "$skill"/SKILL.md ~/.claude/skills/"$skill_name"/SKILL.md
done
```

Or for individual skills:

```bash
# Backup old version (optional)
mv ~/.claude/skills/figureya-creator/SKILL.md ~/.claude/skills/figureya-creator/SKILL.md.backup

# Download latest version
curl -o ~/.claude/skills/figureya-creator/SKILL.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-creator/SKILL.md
```

## Troubleshooting

### Skill not found after installation

1. Verify the directory structure:
   ```bash
   ls -la ~/.claude/skills/
   ```

2. Check if SKILL.md exists:
   ```bash
   ls ~/.claude/skills/figureya-creator/
   ```

3. Check file permissions:
   ```bash
   chmod 644 ~/.claude/skills/*/SKILL.md
   ```

4. Restart Claude Code

### Claude Code can't find FigureYa modules

The skills assume FigureYa is installed at `/Users/pro/FigureYa/`. If your FigureYa is installed elsewhere, you may need to adjust the paths in the skill files.

## Documentation

- **README**: [README.md](README.md) - Project overview
- **Quick Start**: [QUICK_START.md](QUICK_START.md) - Usage examples
- **Statistics Skill Details**: [STATISTICS_LEARNING_SKILL.md](STATISTICS_LEARNING_SKILL.md)
- **Inference Thinking**: [INFERENCE_THINKING_SKILL.md](INFERENCE_THINKING_SKILL.md) 🆕
- **Bayesian Thinking**: [BAYESIAN_THINKING_SKILL.md](BAYESIAN_THINKING_SKILL.md) 🆕

## Feedback and Contributions

If you have issues or suggestions:
- Open an issue on GitHub
- Submit a pull request
- Share your experience

## License

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License

---

<a id="chinese"></a>
## 中文

## 可用的 Skills

本仓库目前包含 2 个 skills：

1. **figureya-pdf-parser** 🆕 - 从 PDF 提取图表并生成 FigureYa 模块
2. **figureya-creator** - 将 R 代码转换为标准化的 FigureYa 模块

## 安装方法

### 方法 1：安装所有 Skills（推荐）

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

# 验证安装
ls -la ~/.claude/skills/
```

### 方法 2：单独安装

#### 安装 FigureYa PDF Parser 🆕

```bash
mkdir -p ~/.claude/skills/figureya-pdf-parser
curl -o ~/.claude/skills/figureya-pdf-parser/SKILL.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-pdf-parser/SKILL.md
```

#### 安装 FigureYa Creator

```bash
mkdir -p ~/.claude/skills/figureya-creator
curl -o ~/.claude/skills/figureya-creator/SKILL.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-creator/SKILL.md
```

### 方法 3：从浏览器手动下载

1. 访问 GitHub 上的 skill 文件：
   - FigureYa PDF Parser: [SKILL.md](https://github.com/ying-ge/FigureYa-skills/blob/main/skills/figureya-pdf-parser/SKILL.md)
   - FigureYa Creator: [SKILL.md](https://github.com/ying-ge/FigureYa-skills/blob/main/skills/figureya-creator/SKILL.md)

2. 点击 "Raw" 按钮

3. 右键 "另存为" 保存到：
   - `~/.claude/skills/figureya-pdf-parser/SKILL.md`
   - `~/.claude/skills/figureya-creator/SKILL.md`

## 验证安装

安装后，验证 skills 是否可用：

```bash
# 列出所有已安装的 skills
ls -la ~/.claude/skills/

# 你应该看到目录：
# figureya-pdf-parser/
# figureya-creator/

# 每个目录应该包含 SKILL.md
ls ~/.claude/skills/figureya-creator/
# 输出：SKILL.md
```

## 使用方法

### 使用 FigureYa PDF Parser 🆕

在 Claude Code 中：

```
用 figureya-pdf-parser 从我的 PDF 中提取图表
```

### 使用 FigureYa Creator

在 Claude Code 中：

```
用 figureya-creator 将我的 R 代码转换为 FigureYa 格式
```

### 使用 FigureYa Inference Thinking 🆕

在 Claude Code 中：

```
我想理解统计学为什么存在
```

```
p-value 到底是什么？
```

### 使用 FigureYa Bayesian Thinking 🆕

在 Claude Code 中：

```

## 系统要求

- 已安装 Claude Code
- 已克隆 FigureYa 项目（推荐路径：`/Users/pro/FigureYa/`）
- 已安装 R 和 RStudio（用于运行 FigureYa 模块）
- PDF parser 所需的 Python 包（PyMuPDF, pdfplumber, spacy, nltk, scikit-learn, pandas, numpy, pyyaml）

## 卸载

删除单个 skill：

```bash
# 删除 FigureYa PDF Parser
rm -rf ~/.claude/skills/figureya-pdf-parser

# 删除 FigureYa Creator
rm -rf ~/.claude/skills/figureya-creator

# 删除其他 skills
```

删除所有 FigureYa skills：

```bash
rm -rf ~/.claude/skills/figureya-*
```

## 更新

更新到最新版本：

```bash
# 进入仓库目录
cd FigureYa-skills

# 拉取最新更改
git pull origin main

# 重新复制 skills 到 ~/.claude/skills/
for skill in skills/*; do
  skill_name=$(basename "$skill")
  mkdir -p ~/.claude/skills/"$skill_name"
  cp "$skill"/SKILL.md ~/.claude/skills/"$skill_name"/SKILL.md
done
```

或者单独更新某个 skill：

```bash
# 备份旧版本（可选）
mv ~/.claude/skills/figureya-creator/SKILL.md ~/.claude/skills/figureya-creator/SKILL.md.backup

# 下载最新版本
curl -o ~/.claude/skills/figureya-creator/SKILL.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-creator/SKILL.md
```

## 故障排除

### 安装后找不到 skill

1. 验证目录结构：
   ```bash
   ls -la ~/.claude/skills/
   ```

2. 检查 SKILL.md 是否存在：
   ```bash
   ls ~/.claude/skills/figureya-creator/
   ```

3. 检查文件权限：
   ```bash
   chmod 644 ~/.claude/skills/*/SKILL.md
   ```

4. 重启 Claude Code

### Claude Code 找不到 FigureYa 模块

这些 skills 假设 FigureYa 安装在 `/Users/pro/FigureYa/`。如果你的 FigureYa 安装在其他位置，可能需要在 skill 文件中调整路径。

## 文档

- **README**: [README.md](README.md) - 项目概述

## 反馈和贡献

如果你有问题或建议：
- 在 GitHub 上提 issue
- 提交 pull request
- 分享你的使用经验

## 许可证

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License
