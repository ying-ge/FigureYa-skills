# 用 FigureYa 理解数据推断 Skill

## 简介 | Introduction

这是一个通过火山图深入理解统计推断本质的 Claude Code skill。它不是教你"如何使用统计方法"，而是帮助你"理解统计学为什么存在"。

This is a Claude Code skill for deeply understanding the essence of statistical inference through volcano plots. It doesn't teach you "how to use statistical methods", but helps you "understand why statistics exists".

## 核心特点 | Key Features

### 🎯 四层递进教学 | Four-Layer Progressive Learning

1. **数据感知**（Layer 1）：不用术语，纯粹描述现象
2. **概念建立**（Layer 2）：引入术语和直觉理解
3. **数学推导**（Layer 3）：从直觉到公式
4. **理论深化**（Layer 4）：理解统计推断本质

### 🤔 苏格拉底式提问 | Socratic Questioning

不直接给出答案，而是通过提问引导思考：
- "你看到了什么？"
- "为什么会这样？"
- "如果...会怎样？"

### 📊 7 个核心问题 | 7 Core Questions

1. **Variance 为什么存在？**
   - 从火山图看到数据的离散性
   - 理解测量总是有波动
   - 推导标准差公式和性质

2. **p-value 为什么不是"真理概率"？**
   - 常见误解：p = 0.03 = 97% 概率真的有差异
   - 正确理解：p = 0.03 = 如果无差异，3% 概率看到这样数据
   - 贝叶斯视角：P(Data|H₀) ≠ P(H₀|Data)

3. **Sample size 为什么重要？**
   - 直观理解：抛硬币的例子
   - 标准误：SE = σ/√n
   - 中心极限定理推导和模拟
   - 统计功效和样本量计算

4. **为什么模型一定会失真？**
   - 模型 = 现实的简化
   - 残差 = 观测值 - 预测值
   - 偏差-方差权衡
   - 信息论视角（KL 散度）

5. **Biological vs Technical Variability**
   - 如何分离两种方差？
   - 线性混合模型
   - 重复性危机：为什么只用 technical replicates 是危险的

6. **为什么 Multiple Testing 会毁掉 Naive Inference？**
   - Family-wise Error Rate (FWER)
   - False Discovery Rate (FDR)
   - BH 方法的数学证明
   - Bonferroni vs FDR vs 其他方法

7. **为什么小样本下 p-value 不稳定？**
   - 方差估计的不稳定性
   - 自由度和 t 分布
   - Bootstrap 方法
   - 贝叶斯小样本方法（limma 的 Empirical Bayes）

## 使用方法 | Usage

### 触发场景 | Trigger Scenarios

在 Claude Code 中使用以下任一方式：

```
我想理解统计学为什么存在
```

```
什么是 p-value？
```

```
为什么需要统计学？
```

```
用 figureya-inference-thinking 教我统计思维
```

### 学习路径 | Learning Path

**推荐顺序 | Recommended Order**:

1. **第一次使用**：从问题 1 开始，按顺序学习
2. **深入理解**：每个问题都包含 4 层，可以反复学习
3. **实践验证**：运行代码示例，修改参数观察变化
4. **建立思维**：回答每个问题的反思问题

**时间投入 | Time Investment**:

- 快速浏览：2-3 小时（第一层：数据感知）
- 深入理解：10-15 小时（包含所有四层）
- 完全掌握：20+ 小时（包含代码实践和反思）

## 与其他 Skill 的关系 | Relationship with Other Skills

### 与 figureya-learn-statistics 的对比

| 维度 | figureya-learn-statistics | figureya-inference-thinking |
|------|--------------------------|----------------------------|
| **定位** | 独立 skill：方法学习 | 独立 skill：思维建立 |
| **目标** | 学会使用统计方法 | 理解统计推断本质 |
| **内容** | 描述统计 → 回归 → 生存分析 | 深入理解核心概念 |
| **方法** | 教程式教学 | 苏格拉底式 + 理论推导 |
| **重点** | 如何做 | 为什么这样做 |
| **理论深度** | 应用导向 | 深入数学推导 |
| **前置要求** | 无 | 无（从零开始） |
| **代码示例** | 实际应用为主 | 理论推导为主 |

### 使用建议 | Recommendation

两个 skill **完全独立**，可以按任意顺序使用：

**建议 A：先建立思维，再学方法**
1. 先用 figureya-inference-thinking 理解统计本质
2. 再用 figureya-learn-statistics 学习具体方法

**建议 B：需要时查阅**
- 遇到概念不理解时：用 figureya-inference-thinking
- 需要使用方法时：用 figureya-learn-statistics

## 核心洞察 | Key Insights

### 统计学的本质 | Essence of Statistics

**不是找到确定性，而是在不确定性中做出有依据的判断**

Not finding certainty, but making informed judgments under uncertainty

### 火山图的深层含义 | Deeper Meaning of Volcano Plots

每个点告诉我们：
- **有效应**（logFC）：两组均值差异
- **有不确定性**（p-value, variance）：估计的不确定性
- **需要综合判断**：effect size + statistical significance

## 技术细节 | Technical Details

### 核心模块 | Core Module

- **主要依赖**：FigureYa59volcanoV2（火山图）
- **参考模块**：FigureYa135multiVolcano（多重检验）
- **数据路径**：`/Users/pro/FigureYa/FigureYa59volcanoV2/easy_input_limma.csv`

### 文件信息 | File Information

- **文件大小**：59 KB
- **行数**：2,204 行
- **语言**：中英双语
- **代码示例**：100+ 个 R 代码块
- **数学公式**：50+ 个 LaTeX 公式

## 理论深度 | Theoretical Depth

这个 skill 包含的深入理论：

### 数学推导 | Mathematical Derivations

- 标准差公式的推导
- 样本方差为什么用 n-1
- 中心极限定理的模拟
- t 统计量的构造
- p-value 的数学定义
- 贝叶斯公式
- 方差分解定理
- 样本量计算公式
- BH 方法的证明
- 偏差-方差权衡

### 高级主题 | Advanced Topics

- 信息论（熵、KL 散度）
- 贝叶斯视角（先验、后验、FDR）
- 自由度和 t 分布
- Bootstrap 和重采样理论
- Empirical Bayes（limma 的方法）
- 线性混合模型
- 误差传播理论

## 适用人群 | Target Audience

### 非常适合 | Highly Suitable For

- 🎓 **生物医学研究生**：想深入理解统计方法背后的原理
- 🔬 **研究人员**：想正确解读和设计实验
- 📊 **数据分析师**：想建立坚实的统计基础
- 🧠 **对统计有好奇心的人**：想超越公式，理解本质

### 需要基础 | Prerequisites

**零基础友好！** No prerequisites needed!

但如果有以下背景会理解更深：
- 基础概率论（概率、条件概率）
- 基础微积分（导数、积分）
- R 语言基础（会运行代码即可）

## 学习成果 | Learning Outcomes

完成这个 skill 后，你将能够：

✅ 用自己的话解释"统计学为什么存在"
✅ 从火山图看出 variance 的影响
✅ 区分 p-value 和"真理概率"
✅ 理解 sample size 对统计推断的影响
✅ 解释为什么模型一定会失真
✅ 理解 biological vs technical variability
✅ 解释为什么需要 multiple testing correction
✅ 理解小样本下 p-value 为什么不稳定
✅ 建立"在不确定性中做推断"的统计思维

## 延伸阅读 | Further Reading

### 经典教材 | Classic Textbooks

1. **"Statistics" by Freedman, Pisani, Purves**
   - 从数据出发，避免过早引入公式
   
2. **"The Cartoon Guide to Statistics"**
   - 直观的统计概念解释

3. **"Computer Age Statistical Inference"** by Efron & Hastie
   - 现代统计推断方法

### 重要论文 | Important Papers

- "The Future of p-values" (Nature, 2015)
- "A Closer Look at p-values" (American Statistician, 2018)
- "Empirical Bayes Methods" (Efron, 2010)

### 在线资源 | Online Resources

- **Seeing Theory**: https://seeingtheory.brown.edu/
- **StatQuest with Josh Starmer**: YouTube 频道
- **Nature Methods Points of Significance**: 统计专栏

## 常见问题 | FAQ

### Q: 这个 skill 适合我吗？

**A**: 如果你符合以下任一条件，这个 skill 适合你：
- 想深入理解统计学的本质
- 知道 p < 0.05 但不理解其真正含义
- 想建立坚实的统计思维
- 对统计学有好奇心

### Q: 需要多长时间才能学完？

**A**:
- **快速浏览**：2-3 小时（只看第一层：数据感知）
- **深入理解**：10-15 小时（包含所有四层）
- **完全掌握**：20+ 小时（包含代码实践和反思）

建议分多次学习，每次深入 1-2 个问题。

### Q: 需要数学基础吗？

**A**: 不需要！这个 skill 是"从零开始"的：
- 第一层完全不用术语
- 第二层用日常语言建立概念
- 第三层才引入公式，但会详细推导
- 第四层包含高级理论，但可以选择性学习

### Q: 与大学的统计课程有什么区别？

**A**:
| 大学课程 | 这个 skill |
|---------|-----------|
| 从公式开始 | 从数据感知开始 |
| 强调记忆 | 强调理解 |
| 抽象理论 | 火山图具体应用 |
| 被动接受 | 苏格拉底式提问 |
| 考试导向 | 思维建立 |

### Q: 需要安装 FigureYa 吗？

**A**: 推荐，但不是必须的：
- **推荐**：安装 FigureYa 可以运行代码示例，亲自探索数据
- **可选**：即使不安装，也可以理解所有概念和理论

如果安装 FigureYa：
```bash
git clone https://github.com/ying-ge/FigureYa.git
```

## 许可证 | License

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License

---

**版本 | Version**: 1.0.0  
**创建时间 | Created**: 2026-05-12  
**作者 | Author**: Claude Code with FigureYa Community  
**GitHub**: https://github.com/ying-ge/FigureYa-skills
