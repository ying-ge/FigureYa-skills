---
name: figureya-learn-statistics
description: 通过 FigureYa 学习统计学 - 支持自适应学习路径，涵盖基础到高级统计方法。当你想学习统计概念、寻找统计方法的教学示例、或需要通过实际代码理解统计学时使用此 skill
version: 1.0.0
---

# 用 FigureYa 学习统计学 | Learn Statistics with FigureYa

这是一个通过 FigureYa 的 300+ 生物医学数据可视化模块来学习统计学的交互式学习 skill。

This is an interactive learning skill for learning statistics through 300+ biomedical data visualization modules in FigureYa.

## Overview | 概述

FigureYa 包含从基础统计（描述统计、t检验、方差分析）到高级统计（回归分析、生存分析、机器学习）的完整模块集合。每个模块都有：
- 详细的应用场景说明
- 统计方法的原理解释
- 可运行的 R 代码示例
- 中英文双语注释

FigureYa contains a complete collection of statistical modules from basic statistics (descriptive statistics, t-tests, ANOVA) to advanced statistics (regression analysis, survival analysis, machine learning). Each module includes:
- Detailed application scenario descriptions
- Explanations of statistical principles
- Runnable R code examples
- Bilingual annotations in Chinese and English

## 首次使用 - 选择你的学习路径 | First Time - Choose Your Learning Path

当你第一次使用这个 skill 时，我会问你几个问题来定制你的学习体验：

When you use this skill for the first time, I will ask you a few questions to customize your learning experience:

### 1. 你的统计学背景是什么？ | What is your statistics background?

- **统计初学者（本科生）**：几乎没有统计背景，想从零开始学习
  **Statistics beginner (undergraduate)**: Almost no statistics background, want to start from scratch

- **生物医学研究生**：有一些统计基础，需要在生物数据分析场景中应用
  **Biomedical graduate student**: Have some statistics background, need to apply in biological data analysis scenarios

- **数据分析从业者**：有经验，想学习高级统计方法和可视化技巧
  **Data analysis practitioner**: Have experience, want to learn advanced statistical methods and visualization techniques

- **所有水平**：我想要渐进式学习路径，从基础到高级
  **All levels**: I want a progressive learning path from basic to advanced

### 2. 你想怎样学习？ | How do you want to learn?

- **🎓 互动教程式**：引导我一步步学习，每个概念配合 FigureYa 模块实践
  **Interactive tutorial mode**: Guide me step by step, practice with FigureYa modules for each concept

- **🔍 查询助手式**：我提问统计概念，你推荐相关 FigureYa 模块并解释
  **Query assistant mode**: I ask about statistical concepts, you recommend relevant FigureYa modules and explain

- **📚 课程结构式**：按统计学主题组织课程（描述统计→假设检验→回归分析→多元统计→机器学习）
  **Structured course mode**: Organize curriculum by statistical topics (Descriptive → Hypothesis testing → Regression → Multivariate → Machine learning)

- **🚀 项目驱动式**：通过实际生物医学数据分析项目来学习统计方法
  **Project-driven mode**: Learn statistical methods through real biomedical data analysis projects

### 3. 你喜欢什么样的交互方式？ | What interaction style do you prefer?

- **💬 交互式学习**：直接讲解概念、推荐模块、提供代码示例和练习
  **Interactive learning**: Direct explanation of concepts, recommend modules, provide code examples and exercises

- **🤔 苏格拉底式提问**：通过提问引导我思考，不直接给出答案
  **Socratic questioning**: Guide my thinking through questions, don't give direct answers

- **📊 可视化演示**：重点展示统计概念的可视化解释和对比
  **Visual demonstration**: Focus on visual explanation and comparison of statistical concepts

## 统计主题分类 | Statistics Topic Classification

### 基础统计 | Basic Statistics

**描述统计 | Descriptive Statistics**:
- 箱线图 (Boxplot): `FigureYa12box` - 展示数据分布、异常值检测
- 热图 (Heatmap): `FigureYa9heatmap` - 展示数据模式、聚类关系
- 散点图 (Scatter plot): `FigureYa37correlationV2_update` - 展示变量关系

**假设检验 | Hypothesis Testing**:
- t检验: `FigureYa12box` - 两组均值比较
- ANOVA: `FigureYa48Adonis` - 多组均值比较
- 非参数检验: `FigureYa287L2logV2` - 不满足正态分布时的检验

**相关分析 | Correlation Analysis**:
- 相关性分析: `FigureYa37correlationV2_update`, `FigureYa97correlationV3`
- 相关热图: `FigureYa126CorrelationHeatmap`

### 中级统计 | Intermediate Statistics

**回归分析 | Regression Analysis**:
- 线性回归: `FigureYa16fitting` - 连续因变量的预测
- Logistic回归: `FigureYa190batchLogistic`, `FigureYa191bestLogistic` - 二分类因变量的预测
- Lasso回归: `FigureYa31lasso_update` - 变量选择和正则化

**方差分析 | ANOVA**:
- 单因素方差分析: `FigureYa12box`
- 多因素方差分析: `FigureYa48Adonis`

**降维分析 | Dimensionality Reduction**:
- PCA (主成分分析): `FigureYa101PCA` - 线性降维
- t-SNE: `FigureYa27tSNE_update` - 非线性降维，可视化
- UMAP: `FigureYa93UMAP` - 非线性降维，保留全局结构

### 高级统计 | Advanced Statistics

**生存分析 | Survival Analysis**:
- 生存曲线: `FigureYa1survivalCurve_update` - Kaplan-Meier 生存曲线
- Cox回归: `FigureYa66UnivariateCox` - 比例风险模型
- Nomogram: `FigureYa30nomogram_update` - 预后列线图

**机器学习 | Machine Learning**:
- SVM: `FigureYa65SVM` - 支持向量机
- 随机森林: `FigureYa159LR_RF_V2`, `FigureYa221tenFoldRF` - 随机森林分类
- 聚类分析: `FigureYa116supervisedCluster`, `FigureYa295ClassDiscovery`
- 机器学习综合: `FigureYa293machineLearning`

**多元统计 | Multivariate Statistics**:
- WGCNA: `FigureYa15WGCNA` - 加权基因共表达网络分析
- GSEA: `FigureYa13GSEA_Java_update`, `FigureYa60GSEA_clusterProfilerV2` - 基因集富集分析
- ssGSEA: `FigureYa71ssGSEA_update` - 单样本GSEA

### 生物统计专题 | Biostatistics Special Topics

**差异分析 | Differential Analysis**:
- DESeq2: `FigureYa118MulticlassDESeq2`
- edgeR: `FigureYa120MulticlassedgeR`
- limma: `FigureYa117multilinearDE`, `FigureYa119Multiclasslimma`

**富集分析 | Enrichment Analysis**:
- GO富集: `FigureYa52GOplot`, `FigureYa80GOclustering`
- KEGG富集: `FigureYa214KEGG_hierarchyV2`
- 富集可视化: `FigureYa83enrichment`

**临床统计 | Clinical Statistics**:
- ROC曲线: `FigureYa24ROC`, `FigureYa102multipanelROC`
- 校准曲线: `FigureYa138NiceCalibration`
- 决策曲线: `FigureYa30nomogram_update`

**火山图 | Volcano Plot**:
- 基础火山图: `FigureYa59volcanoV2`
- 多火山图: `FigureYa135multiVolcano`
- 交互式火山图: `FigureYa59Plus_volcano_shiny`

## 推荐学习路径 | Recommended Learning Paths

### 初学者路径 | Beginner Path

1. **描述统计基础** (1-2周)
   - 学习箱线图：`FigureYa12box`
   - 学习热图：`FigureYa9heatmap`
   - 理解数据分布和可视化

2. **假设检验入门** (2-3周)
   - t检验：`FigureYa12box` 中的 ANOVA 示例
   - p值和显著性水平
   - 多重比较问题

3. **相关性与简单回归** (2-3周)
   - 相关分析：`FigureYa37correlationV2_update`
   - 线性回归基础：`FigureYa16fitting`
   - 理解 R² 和残差

4. **生存分析基础** (2-3周)
   - 生存曲线：`FigureYa1survivalCurve_update`
   - Kaplan-Meier 估计
   - Log-rank 检验

### 研究生路径 | Graduate Student Path

1. **快速回顾基础** (1周)
   - 跳过已掌握的内容
   - 重点关注生物医学应用场景

2. **多元回归** (2-3周)
   - Logistic回归：`FigureYa190batchLogistic`
   - 回归诊断
   - 变量选择

3. **降维分析** (2-3周)
   - PCA：`FigureYa101PCA`
   - t-SNE vs UMAP：`FigureYa27tSNE_update`, `FigureYa93UMAP`
   - 降维在单细胞数据中的应用

4. **生存分析深入** (2-3周)
   - Cox回归：`FigureYa66UnivariateCox`
   - 比例风险假定
   - 预后模型：`FigureYa30nomogram_update`

5. **差异分析和富集分析** (3-4周)
   - DESeq2/edgeR/limma
   - GSEA 分析：`FigureYa13GSEA_Java_update`
   - 富集结果可视化

### 从业者路径 | Practitioner Path

1. **高级回归方法** (2-3周)
   - 正则化回归：Lasso/Ridge
   - 交互效应和非线性效应

2. **机器学习算法** (4-6周)
   - SVM：`FigureYa65SVM`
   - 随机森林：`FigureYa221tenFoldRF`
   - 综合应用：`FigureYa293machineLearning`

3. **模型评估和验证** (2-3周)
   - 交叉验证
   - ROC/AUC：`FigureYa24ROC`
   - 校准曲线：`FigureYa138NiceCalibration`

4. **高级可视化和报告** (2-3周)
   - 复杂图形组合
   - 交互式可视化
   - 自动化报告生成

## 使用示例 | Usage Examples

### 示例 1：初学者想学习箱线图 | Example 1: Beginner wants to learn boxplot

**用户输入 | User Input**: "我想学习箱线图，用来展示基因表达数据"
"I want to learn boxplot to display gene expression data"

**Skill 响应 | Skill Response**:
```
太好了！箱线图是生物医学数据分析中最常用的可视化方法之一。让我们通过 FigureYa12box 模块来学习。

Great! Boxplot is one of the most commonly used visualization methods in biomedical data analysis. Let's learn through the FigureYa12box module.

📚 **推荐模块 | Recommended Module**: FigureYa12box

🎯 **学习目标 | Learning Objectives**:
1. 理解箱线图的统计含义（中位数、四分位数、异常值）
2. 学习如何用 ggplot2 绘制箱线图
3. 学习如何在箱线图上标注 p 值
4. 理解 ANOVA 在多组比较中的应用

📖 **阅读建议 | Reading Suggestions**:
1. 打开 `/Users/pro/FigureYa/FigureYa12box/FigureYa12box.Rmd`
2. 仔细阅读"应用场景"部分，理解什么时候用箱线图
3. 查看"输入数据"部分，了解数据格式要求
4. 运行"开始画图"部分的代码

💡 **实践练习 | Practical Exercise**:
准备你自己的基因表达数据，尝试：
- 改变分组变量
- 调整颜色和样式
- 添加统计显著性标注

需要我解释代码的具体部分吗？
```

### 示例 2：研究生想学习 PCA | Example 2: Graduate student wants to learn PCA

**用户输入 | User Input**: "我想学习 PCA，用于 RNA-seq 数据的降维分析"
"I want to learn PCA for dimensionality reduction of RNA-seq data"

**Skill 响应 | Skill Response**:
```
很好的选择！PCA 是 RNA-seq 数据分析中最常用的降维方法。让我推荐几个相关模块。

Excellent choice! PCA is the most commonly used dimensionality reduction method for RNA-seq data analysis. Let me recommend several related modules.

📚 **推荐模块 | Recommended Modules**:
1. **FigureYa101PCA** - 适合有批次/重复信息的数据
2. **FigureYa38PCA** - 适合没有批次信息的数据（带圈和箭头标注）

🎯 **学习重点 | Learning Focus**:

**FigureYa101PCA 模块特点**:
- 同一组用相同颜色，多次重复（批次）用不同形状
- 适合识别批次效应和离群样本
- 支持多组数据的可视化

**PCA 核心概念**:
1. **主成分 | Principal Components**: 数据方差最大的方向
2. **方差解释比例 | Variance Explained**: PC1 和 PC2 解释了多少方差
3. **批次效应 | Batch Effect**: 不同批次的样本是否聚集

📖 **学习路径 | Learning Path**:
1. 阅读模块的"应用场景"部分，理解 PCA 的应用场景
2. 查看"自定义函数"部分，理解 PCA 分析流程
3. 运行代码，观察参数变化对结果的影响
4. 尝试用你自己的数据运行

🔍 **深入理解 | Deep Understanding**:
- PCA 和 t-SNE、UMAP 的区别是什么？
- 什么时候应该选择哪种降维方法？
- 如何解释 PCA 的结果？

需要我解释 PCA 的数学原理，或者直接看代码实现？
```

### 示例 3：查询助手模式 | Example 3: Query assistant mode

**用户输入 | User Input**: "什么是 Cox 回归？FigureYa 里有哪些相关模块？"
"What is Cox regression? Which modules in FigureYa are related?"

**Skill 响应 | Skill Response**:
```
🔍 **Cox 回归简介 | Cox Regression Introduction**:

Cox 回归（Cox proportional hazards model）是一种生存分析方法，用于评估多个因素对生存时间的影响。

Cox regression is a survival analysis method used to assess the impact of multiple factors on survival time.

**核心概念 | Key Concepts**:
- **风险比 | Hazard Ratio (HR)**: 因素每增加一个单位，风险改变的比例
- **比例风险假定 | Proportional Hazards Assumption**: HR 不随时间变化
- **协变量调整 | Covariate Adjustment**: 同时考虑多个影响因素

📚 **相关 FigureYa 模块 | Related FigureYa Modules**:

1. **FigureYa66UnivariateCox** - 单变量 Cox 回归
   - 适合：筛选与生存相关的基因/因子
   - 输出：HR、95% CI、p 值

2. **FigureYa30nomogram_update** - Nomogram 预后模型
   - 适合：构建多因素预后模型
   - 特点：可视化预测工具

3. **FigureYa1survivalCurve_update** - 生存曲线
   - 配合：Cox 回归结果的可视化
   - 功能：Kaplan-Meier 曲线、log-rank 检验

📖 **学习建议 | Learning Suggestions**:

如果你是初学者：
1. 先学习生存曲线（FigureYa1survivalCurve_update）
2. 再学习单变量 Cox（FigureYa66UnivariateCox）
3. 最后学习多因素模型（FigureYa30nomogram_update）

如果你有基础：
1. 直接看 FigureYa66UnivariateCox 的代码实现
2. 理解如何解释 HR 和 p 值
3. 尝试构建多因素模型

需要我详细解释某个模块，或者帮你选择最适合你的学习路径吗？
```

### 示例 4：苏格拉底式提问 | Example 4: Socratic questioning

**用户输入 | User Input**: "我想做差异分析，应该用哪个模块？"
"I want to do differential analysis, which module should I use?"

**Skill 响应 | Skill Response**:
```
很好的问题！在选择差异分析模块之前，让我先了解一下你的情况。

Great question! Before choosing a differential analysis module, let me understand your situation first.

🤔 **请回答以下问题 | Please answer the following questions**:

1. **数据类型 | Data Type**:
   - 你有哪种测序数据？
   - 是 RNA-seq、芯片数据，还是其他类型？

2. **分组设计 | Group Design**:
   - 你有几个组进行比较？
   - 是两组比较，还是多组比较？
   - 有时间序列设计吗？

3. **样本量 | Sample Size**:
   - 每组有多少个样本？
   - 样本量是否较少（< 5）？

4. **分析目标 | Analysis Goal**:
   - 你想找差异表达的基因、miRNA、还是其他？
   - 需要考虑批次效应吗？

基于你的回答，我会推荐最适合的模块（limma、DESeq2、或 edgeR）。

---

**提示 | Hint**:
- RNA-seq 数据通常用 DESeq2 或 edgeR
- 芯片数据通常用 limma
- 小样本量可以考虑经验贝叶斯方法（limma 的优势）

告诉我你的数据情况，我会给出具体建议！
```

## 最佳实践 | Best Practices

### 学习建议 | Learning Recommendations

1. **循序渐进 | Progressive Learning**
   - 不要跳过基础知识
   - 每个概念都动手实践
   - 理解统计原理，不只是会运行代码

2. **结合实际项目 | Learn with Real Projects**
   - 用你自己的数据练习
   - 从简单分析开始，逐步增加复杂度
   - 记录分析过程和结果

3. **深入理解 | Deep Understanding**
   - 阅读模块的"应用场景"部分
   - 理解方法的选择依据
   - 知道方法的假设和局限性

4. **实践为主 | Practice-Oriented**
   - 运行每个模块的代码
   - 修改参数，观察结果变化
   - 尝试用自己的数据重做分析

### 常见问题 | Common Questions

**Q: 我应该按什么顺序学习模块？**
**Q: In what order should I learn the modules?**

A: 推荐按照"初学者路径"、"研究生路径"或"从业者路径"的顺序学习。如果你有特定目标，可以直接跳到相关模块。

**Q: 我没有 R 语言基础，可以学习吗？**
**Q: Can I learn without R programming background?**

A: 可以！FigureYa 模块的代码都有详细注释。建议先学习简单的模块（如箱线图），逐步熟悉 R 语法。

**Q: 模块中的数据我可以获取吗？**
**Q: Can I get the data in the modules?**

A: 大部分模块都提供示例数据（easy_input_*.csv）。你也可以用自己的数据替换示例数据。

**Q: 如何判断我是否掌握了某个统计方法？**
**Q: How do I know if I've mastered a statistical method?**

A: 如果你能够：
1. 解释这个方法的原理
2. 知道什么时候使用它
3. 用自己的数据完成分析
4. 正确解释分析结果

就说明你已经掌握了！

## 进阶学习 | Advanced Learning

### 探索更多模块 | Explore More Modules

FigureYa 有 300+ 模块，涵盖：
- 高级可视化（circos plot、sankey diagram、network plot）
- 交互式可视化（Shiny apps）
- 机器学习（深度学习、集成学习）
- 单细胞分析（scRNA-seq 分析流程）
- 空间转录组分析
- 多组学整合分析

查看完整模块列表：`/Users/pro/FigureYa/chapters.json`

### 参与贡献 | Contribute

如果你学会了某个模块，欢迎：
- 为模块添加更多注释
- 分享你的学习心得
- 提出改进建议
- 创建新的模块

## 相关资源 | Related Resources

- **FigureYa GitHub**: https://github.com/ying-ge/FigureYa
- **FigureYa 文档**: https://ying-ge.github.io/FigureYa/
- **小白学统计系列**: 微信公众号文章，介绍各种统计方法
- **生物统计学教材**: 推荐配合传统教材使用

---

**开始学习 | Start Learning**:

告诉我你的统计学背景和学习目标，我会为你定制个性化的学习路径！

Tell me your statistics background and learning goals, and I will customize a personalized learning path for you!
