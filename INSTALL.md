# 安装"用 FigureYa 学习统计学"Skill

## 方法 1：手动安装（推荐）

### 步骤：

1. **下载 skill 文件**
   ```bash
   # 从 GitHub 仓库下载
   curl -o ~/.claude/skills/figureya-learn-statistics.md \
     https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-learn-statistics.md
   ```

2. **或者克隆整个仓库**
   ```bash
   cd /tmp
   git clone https://github.com/ying-ge/FigureYa-skills.git
   cp FigureYa-skills/skills/figureya-learn-statistics.md ~/.claude/skills/
   ```

3. **验证安装**
   ```bash
   ls -la ~/.claude/skills/figureya-learn-statistics.md
   ```

## 方法 2：使用 FigureYa-skills 仓库

如果你已经克隆了 FigureYa-skills 仓库：

```bash
# 在仓库根目录执行
cp skills/figureya-learn-statistics.md ~/.claude/skills/
```

## 方法 3：从浏览器下载

1. 访问：https://github.com/ying-ge/FigureYa-skills/blob/main/skills/figureya-learn-statistics.md
2. 点击 "Raw" 按钮
3. 右键 "另存为" 保存到 `~/.claude/skills/figureya-learn-statistics.md`

## 安装后使用

在 Claude Code 中输入：

```
我要用 FigureYa 学习统计
```

或者：

```
我想学习 [某个统计方法]
```

## 相关文档

- **完整功能说明**: [STATISTICS_LEARNING_SKILL.md](https://github.com/ying-ge/FigureYa-skills/blob/main/STATISTICS_LEARNING_SKILL.md)
- **快速使用指南**: [QUICK_START.md](https://github.com/ying-ge/FigureYa-skills/blob/main/QUICK_START.md)
- **GitHub 仓库**: https://github.com/ying-ge/FigureYa-skills

## 系统要求

- Claude Code 已安装
- FigureYa 项目已克隆到本地（推荐路径：`/Users/pro/FigureYa/`）
- R 和 RStudio（用于运行 FigureYa 模块）

## 卸载

如果需要卸载这个 skill：

```bash
rm ~/.claude/skills/figureya-learn-statistics.md
```

## 更新

如果已有旧版本，可以先备份再更新：

```bash
# 备份旧版本
mv ~/.claude/skills/figureya-learn-statistics.md ~/.claude/skills/figureya-learn-statistics.md.backup

# 下载新版本
curl -o ~/.claude/skills/figureya-learn-statistics.md \
  https://raw.githubusercontent.com/ying-ge/FigureYa-skills/main/skills/figureya-learn-statistics.md
```

## 反馈和建议

如果你有改进建议，欢迎：
- 在 GitHub 上提 Issue
- 提交 Pull Request
- 分享你的学习心得

## 许可证

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License
