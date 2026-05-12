# 用 FigureYa 学习统计学 Skill

## 简介

这是一个 Claude Code skill，帮助用户通过 FigureYa 的 300+ 生物医学数据可视化模块来学习统计学。

## 功能特点

### 1. 自适应学习路径
- 支持 3 种用户类型：初学者、研究生、从业者
- 根据用户背景推荐合适的学习路径
- 从基础统计到高级统计的完整覆盖

### 2. 多种学习模式
- **🎓 互动教程式**：引导式学习，每个概念配合实践
- **🔍 查询助手式**：回答统计概念问题，推荐相关模块
- **📚 课程结构式**：按主题组织的系统课程
- **🚀 项目驱动式**：通过实际项目学习

### 3. 三种交互方式
- **💬 交互式学习**：直接讲解和代码示例
- **🤔 苏格拉底式提问**：引导思考，不直接给答案
- **📊 可视化演示**：重点展示可视化解释

### 4. 完整的统计主题覆盖
- 基础统计：描述统计、假设检验、相关分析
- 中级统计：回归分析、方差分析、降维分析
- 高级统计：生存分析、机器学习、多元统计
- 生物统计专题：差异分析、富集分析、临床统计

## 使用方法

### 在 Claude Code 中使用

1. **直接使用 skill**：
   ```
   我要用 FigureYa 学习统计
   ```

2. **询问具体统计概念**：
   ```
   什么是 Cox 回归？FigureYa 里有哪些相关模块？
   ```

3. **请求学习路径**：
   ```
   我是生物医学研究生，想学习生存分析
   ```

4. **查询模块推荐**：
   ```
   我想做 RNA-seq 的 PCA 分析，应该用哪个模块？
   ```

### Skill 文件位置

```
~/.claude/skills/figureya-learn-statistics.md
```

## 学习路径示例

### 初学者路径（8-12周）
1. 描述统计基础（箱线图、热图）
2. 假设检验入门（t检验、ANOVA）
3. 相关性与简单回归
4. 生存分析基础

### 研究生路径（10-15周）
1. 快速回顾基础统计
2. 多元回归和logistic回归
3. 降维分析（PCA、t-SNE）
4. 生存分析深度学习
5. 差异分析和富集分析

### 从业者路径（12-18周）
1. 高级回归方法
2. 机器学习算法
3. 交互验证和模型评估
4. 高级可视化和报告

## 支持的统计方法

### 基础统计
- 箱线图: `FigureYa12box`
- 热图: `FigureYa9heatmap`
- 相关分析: `FigureYa37correlationV2_update`
- ANOVA: `FigureYa48Adonis`

### 降维分析
- PCA: `FigureYa101PCA`
- t-SNE: `FigureYa27tSNE_update`
- UMAP: `FigureYa93UMAP`

### 生存分析
- 生存曲线: `FigureYa1survivalCurve_update`
- Cox回归: `FigureYa66UnivariateCox`
- Nomogram: `FigureYa30nomogram_update`

### 机器学习
- SVM: `FigureYa65SVM`
- 随机森林: `FigureYa221tenFoldRF`
- 机器学习综合: `FigureYa293machineLearning`

### 差异分析
- DESeq2: `FigureYa118MulticlassDESeq2`
- edgeR: `FigureYa120MulticlassedgeR`
- limma: `FigureYa119Multiclasslimma`

### 富集分析
- GSEA: `FigureYa13GSEA_Java_update`
- GO富集: `FigureYa52GOplot`
- KEGG富集: `FigureYa214KEGG_hierarchyV2`

## 最佳实践

1. **循序渐进**：按推荐路径学习，不要跳过基础
2. **动手实践**：运行每个模块的代码，修改参数观察结果
3. **结合实际**：用自己的数据练习
4. **深入理解**：阅读模块的"应用场景"部分，理解方法原理
5. **记录总结**：记录学习心得和分析结果

## 相关资源

- **FigureYa GitHub**: https://github.com/ying-ge/FigureYa
- **FigureYa 文档**: https://ying-ge.github.io/FigureYa/
- **FigureYa 项目位置**: `/Users/pro/FigureYa/`

## 常见问题

**Q: 我没有 R 语言基础，可以学习吗？**
A: 可以！从简单模块开始，逐步熟悉 R 语法。

**Q: 如何获取模块中的示例数据？**
A: 每个模块目录都有 `easy_input_*.csv` 文件。

**Q: 可以用自己的数据吗？**
A: 可以！模块支持替换为你自己的数据。

**Q: 如何判断我是否掌握了某个方法？**
A: 如果你能解释原理、知道何时使用、能用自己数据完成分析并正确解释结果，就说明掌握了。

## 更新日志

### v1.0.0 (2026-05-12)
- 初始版本发布
- 支持 3 种用户类型
- 支持 4 种学习模式
- 支持 3 种交互方式
- 覆盖基础到高级统计主题
- 包含完整的 FigureYa 模块索引
- 提供个性化学习路径推荐

## 贡献

如果你有改进建议，欢迎：
- 提出新的学习路径
- 推荐更多 FigureYa 模块
- 分享学习心得
- 报告问题或 bug

## 许可证

本项目遵循与 FigureYa 相同的许可证：[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/)
