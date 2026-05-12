# 安装 FigureYa Skills

[English](#english) | [中文](#chinese)

<a id="english"></a>
## English

## Available Skills

This repository currently contains 2 skills:

1. **figureya-creator** - Convert R code to standardized FigureYa modules
2. **figureya-learn-statistics** - Learn statistics through FigureYa modules

## Installation Methods

### Method 1: Install All Skills (Recommended)

```bash
# Clone the repository
git clone https://github.com/ying-ge/FigureYa-skills.git

# Copy all skills to Claude Code skills directory
cp FigureYa-skills/skills/*.md ~/.claude/skills/

# Verify installation
ls -la ~/.claude/skills/
```

### Method 2: Install Individual Skills

#### Install FigureYa Creator

```bash
curl -o ~/.claude/skills/figureya-creator.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-creator.md
```

#### Install FigureYa Learn Statistics

```bash
curl -o ~/.claude/skills/figureya-learn-statistics.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-learn-statistics.md
```

### Method 3: Manual Download from Browser

1. Visit the skill file on GitHub:
   - FigureYa Creator: [figureya-creator.md](https://github.com/ying-ge/FigureYa-skills/blob/main/skills/figureya-creator.md)
   - FigureYa Learn Statistics: [figureya-learn-statistics.md](https://github.com/ying-ge/FigureYa-skills/blob/main/skills/figureya-learn-statistics.md)

2. Click the "Raw" button

3. Right-click "Save As" and save to:
   - `~/.claude/skills/figureya-creator.md`
   - `~/.claude/skills/figureya-learn-statistics.md`

## Verification

After installation, verify the skills are available:

```bash
# List all installed skills
ls -la ~/.claude/skills/

# You should see:
# figureya-creator.md
# figureya-learn-statistics.md
```

## Usage

### Using FigureYa Creator

In Claude Code:

```
Use figureya-creator to convert my R code to FigureYa format
```

### Using FigureYa Learn Statistics

In Claude Code:

```
I want to learn statistics with FigureYa
```

```
What is Cox regression? Which FigureYa modules should I use?
```

See [QUICK_START.md](QUICK_START.md) for more usage examples.

## System Requirements

- Claude Code installed
- FigureYa project cloned (recommended: `/Users/pro/FigureYa/`)
- R and RStudio (for running FigureYa modules)

## Uninstallation

To remove individual skills:

```bash
# Remove FigureYa Creator
rm ~/.claude/skills/figureya-creator.md

# Remove FigureYa Learn Statistics
rm ~/.claude/skills/figureya-learn-statistics.md
```

To remove all FigureYa skills:

```bash
rm ~/.claude/skills/figureya-*.md
```

## Updates

To update to the latest version:

```bash
# Navigate to the repository
cd FigureYa-skills

# Pull latest changes
git pull origin main

# Re-copy skills to ~/.claude/skills/
cp skills/*.md ~/.claude/skills/
```

Or for individual skills:

```bash
# Backup old version (optional)
mv ~/.claude/skills/figureya-learn-statistics.md ~/.claude/skills/figureya-learn-statistics.md.backup

# Download latest version
curl -o ~/.claude/skills/figureya-learn-statistics.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-learn-statistics.md
```

## Troubleshooting

### Skill not found after installation

1. Verify the file exists:
   ```bash
   ls -la ~/.claude/skills/
   ```

2. Check file permissions:
   ```bash
   chmod 644 ~/.claude/skills/figureya-*.md
   ```

3. Restart Claude Code

### Claude Code can't find FigureYa modules

The skills assume FigureYa is installed at `/Users/pro/FigureYa/`. If your FigureYa is installed elsewhere, you may need to adjust the paths in the skill files.

## Documentation

- **README**: [README.md](README.md) - Project overview
- **Quick Start**: [QUICK_START.md](QUICK_START.md) - Usage examples
- **Statistics Skill Details**: [STATISTICS_LEARNING_SKILL.md](STATISTICS_LEARNING_SKILL.md)

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

1. **figureya-creator** - 将 R 代码转换为标准化的 FigureYa 模块
2. **figureya-learn-statistics** - 通过 FigureYa 模块学习统计学

## 安装方法

### 方法 1：安装所有 Skills（推荐）

```bash
# 克隆仓库
git clone https://github.com/ying-ge/FigureYa-skills.git

# 复制所有 skills 到 Claude Code skills 目录
cp FigureYa-skills/skills/*.md ~/.claude/skills/

# 验证安装
ls -la ~/.claude/skills/
```

### 方法 2：单独安装

#### 安装 FigureYa Creator

```bash
curl -o ~/.claude/skills/figureya-creator.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-creator.md
```

#### 安装 FigureYa Learn Statistics

```bash
curl -o ~/.claude/skills/figureya-learn-statistics.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-learn-statistics.md
```

### 方法 3：从浏览器手动下载

1. 访问 GitHub 上的 skill 文件：
   - FigureYa Creator: [figureya-creator.md](https://github.com/ying-ge/FigureYa-skills/blob/main/skills/figureya-creator.md)
   - FigureYa Learn Statistics: [figureya-learn-statistics.md](https://github.com/ying-ge/FigureYa-skills/blob/main/skills/figureya-learn-statistics.md)

2. 点击 "Raw" 按钮

3. 右键 "另存为" 保存到：
   - `~/.claude/skills/figureya-creator.md`
   - `~/.claude/skills/figureya-learn-statistics.md`

## 验证安装

安装后，验证 skills 是否可用：

```bash
# 列出所有已安装的 skills
ls -la ~/.claude/skills/

# 你应该看到：
# figureya-creator.md
# figureya-learn-statistics.md
```

## 使用方法

### 使用 FigureYa Creator

在 Claude Code 中：

```
用 figureya-creator 将我的 R 代码转换为 FigureYa 格式
```

### 使用 FigureYa Learn Statistics

在 Claude Code 中：

```
我要用 FigureYa 学习统计
```

```
什么是 Cox 回归？应该用哪些 FigureYa 模块？
```

更多使用示例请参阅 [QUICK_START.md](QUICK_START.md)。

## 系统要求

- 已安装 Claude Code
- 已克隆 FigureYa 项目（推荐路径：`/Users/pro/FigureYa/`）
- 已安装 R 和 RStudio（用于运行 FigureYa 模块）

## 卸载

删除单个 skill：

```bash
# 删除 FigureYa Creator
rm ~/.claude/skills/figureya-creator.md

# 删除 FigureYa Learn Statistics
rm ~/.claude/skills/figureya-learn-statistics.md
```

删除所有 FigureYa skills：

```bash
rm ~/.claude/skills/figureya-*.md
```

## 更新

更新到最新版本：

```bash
# 进入仓库目录
cd FigureYa-skills

# 拉取最新更改
git pull origin main

# 重新复制 skills 到 ~/.claude/skills/
cp skills/*.md ~/.claude/skills/
```

或者单独更新某个 skill：

```bash
# 备份旧版本（可选）
mv ~/.claude/skills/figureya-learn-statistics.md ~/.claude/skills/figureya-learn-statistics.md.backup

# 下载最新版本
curl -o ~/.claude/skills/figureya-learn-statistics.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-learn-statistics.md
```

## 故障排除

### 安装后找不到 skill

1. 验证文件存在：
   ```bash
   ls -la ~/.claude/skills/
   ```

2. 检查文件权限：
   ```bash
   chmod 644 ~/.claude/skills/figureya-*.md
   ```

3. 重启 Claude Code

### Claude Code 找不到 FigureYa 模块

这些 skills 假设 FigureYa 安装在 `/Users/pro/FigureYa/`。如果你的 FigureYa 安装在其他位置，可能需要在 skill 文件中调整路径。

## 文档

- **README**: [README.md](README.md) - 项目概述
- **快速开始**: [QUICK_START.md](QUICK_START.md) - 使用示例
- **统计学 Skill 详情**: [STATISTICS_LEARNING_SKILL.md](STATISTICS_LEARNING_SKILL.md)

## 反馈和贡献

如果你有问题或建议：
- 在 GitHub 上提 issue
- 提交 pull request
- 分享你的使用经验

## 许可证

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License
