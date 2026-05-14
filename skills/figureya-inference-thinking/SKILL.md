---
name: figureya-inference-thinking
description: 通过火山图理解统计推断的本质 - 从零开始，深入探索 variance、p-value、sample size 的真实含义，建立"在不确定性中做推断"的统计思维。包含完整的数学推导和理论解释。
version: 1.0.0
---

# 用 FigureYa 理解数据推断 | Understand Statistical Inference with FigureYa

## 学习开始前 | Before We Start

### 问题 1：你的统计学习目标 | Your Statistics Learning Goal

**你希望通过这个 skill 达到什么目标？** (可多选 | Multiple selections)

- **A. 理解统计学的本质**
  - Understand the essence of statistics
  - 为什么需要统计学？它解决什么问题？

- **B. 深入理解核心概念**
  - Deeply understand core concepts
  - variance, p-value, sample size 的真实含义

- **C. 建立统计思维**
  - Build statistical thinking
  - 在不确定性中做推断的能力

- **D. 提升研究中的统计应用能力**
  - Improve statistical application in research
  - 更好地设计和分析实验

### 问题 2：你对这些概念的理解程度 | Your Understanding of These Concepts

**请诚实评估你对以下概念的理解程度 | Please honestly assess your understanding of these concepts:**

**A. Variance（方差）**
- **完全不懂 | Completely new**
- **有一些概念 | Some concepts**
- **理解但不会应用 | Understand but can't apply**
- **理解并能应用 | Understand and can apply**

**B. p-value**
- **完全不懂 | Completely new**
- **有一些概念 | Some concepts**
- **理解但不会应用 | Understand but can't apply**
- **理解并能应用 | Understand and can apply**

**C. Sample Size**
- **完全不懂 | Completely new**
- **有一些概念 | Some concepts**
- **理解但不会应用 | Understand but can't apply**
- **理解并能应用 | Understand and can apply**

---

## 7 个核心问题 | 7 Core Questions

这个 skill 通过 7 个核心问题深入理解统计推断的本质：

1. **Variance 为什么存在？** | Why does variance exist?
2. **p-value 为什么不是"真理概率"？** | Why is p-value not "truth probability"?
3. **Sample Size 为什么重要？** | Why does sample size matter?
4. **为什么模型一定会失真？** | Why do models always distort?
5. **Biological vs Technical Variability**
6. **为什么 Multiple Testing 会毁掉 Naive Inference？** | Why does multiple testing ruin naive inference?
7. **为什么小样本下 p-value 不稳定？** | Why is p-value unstable with small samples?

---

## 问题 1：Variance 为什么存在？| Question 1: Why Does Variance Exist?

### 🎯 学习目标 | Learning Objectives

- 理解 variance 的本质来源
- 认识到 variance 是数据的基本属性，不是"噪声"
- 理解为什么统计学存在

### 📊 数据观察 | Data Observation

想象你看到了 FigureYa59volcanoV2（火山图）上的点。

**观察提问 | Observation Questions:**

**Q1: 看着火山图，你注意到了什么？**
**What do you notice when looking at the volcano plot?**

- **A. 点的分布很有规律**
  - Points are distributed regularly
  - 大多数点在中间，少数点在两边

- **B. 点的分布看起来很随机**
  - Points appear randomly distributed
  - 看不出明显规律

- **C. 有些点很突出**
  - Some points stand out
  - 极端的 logFC 和极小的 p-value

- **D. 不确定应该关注什么**
  - Unsure what to focus on

<details>
<summary>点击查看解释 | Click to see explanation</summary>

**引导思考 | Guided Thinking:**
- 注意大多数点聚集在中间（logFC 接近 0）
- 两边的点较少，但往往更"重要"
- 这个分布形状本身就包含了信息

</details>

**Q2: 最关键的问题：为什么同样 logFC 的基因，p-value 差异巨大？**
**Most critical question: Why do genes with similar logFC have very different p-values?**

- **A. 因为测量误差**
  - Because of measurement error
  - 有些基因测量更准确

- **B. 因为 variance 不同**
  - Because of different variance
  - 有些基因的表达波动更大

- **C. 因为样本量不同**
  - Because of different sample sizes
  - 有些基因的数据点更多

- **D. 不确定原因**
  - Unsure of the reason

<details>
<summary>点击查看详细解释 | Click to see detailed explanation</summary>

**✅ 正确答案：B. 因为 variance 不同**

**深入解释 | Deep Explanation:**

```r
# 假设有两个基因：
# Gene A: logFC = 2, variance 小
# Gene B: logFC = 2, variance 大

# 即使 logFC 相同，Gene A 的 p-value 会更小
# 因为 variance 小 → 标准误小 → t-statistic 大 → p-value 小
```

**关键洞察 | Key Insight:**
- Variance 不是"噪声"，而是**数据的基本属性**
- 每个基因的表达稳定性不同
- 这是生物学特性，不是测量误差
- 统计学的目标：在 variance 中"发现"真实差异

</details>

### 🤔 反思问题 | Reflection Questions

**这个问题改变了你对 variance 的理解吗？**
**Did this question change your understanding of variance?**

- **A. 是的，我意识到 variance 是数据的基本属性**
  - Yes, I realized variance is a fundamental property of data

- **B. 部分改变，但还需要更多例子**
  - Partially, but I need more examples

- **C. 没有改变，我已经理解了**
  - No change, I already understood

- **D. 还是困惑，想继续探索**
  - Still confused, want to continue exploring

---

## 问题 2：p-value 为什么不是"真理概率"？| Question 2: Why is P-value Not "Truth Probability"?

### 🎯 学习目标 | Learning Objectives

- 理解 p-value 的真实含义
- 认识到 P(Data|H₀) ≠ P(H₁|Data)
- 理解条件概率的反转

### 🧪 直觉测试 | Intuition Test

**假设你做了一个基因差异表达分析，得到 p = 0.03**

**Assume you performed a differential expression analysis and got p = 0.03**

**Q1: 你认为这意味着什么？**
**What do you think this means?**

- **A. 基因有差异的概率是 97%**
  - There's 97% probability the gene has a difference

- **B. 如果基因无差异，看到这样数据的概率是 3%**
  - If the gene has no difference, there's 3% probability of seeing such data

- **C. 基因有差异的概率是 3%**
  - There's 3% probability the gene has a difference

- **D. 不确定 p-value 的含义**
  - Unsure of the meaning of p-value

<details>
<summary>点击查看详细解释 | Click to see detailed explanation</summary>

**✅ 正确答案：B**

**数学表达 | Mathematical Expression:**

```
p-value = P(Data | H₀)

这意味着：
- 条件：假设基因无差异（H₀ 为真）
- 事件：观察到当前数据（或更极端的数据）
- 概率：这个事件发生的概率
```

**常见的误解 | Common Misconceptions:**

❌ **误解 1**: "p = 0.03 意味着 97% 概率基因有差异"
- 这是：P(H₁ | Data)
- 但 p-value 是：P(Data | H₀)

❌ **误解 2**: "p = 0.03 意味着 3% 概率原假设成立"
- 这也是：P(H₀ | Data)
- p-value 不是后验概率

**为什么会有这个误解？| Why is this misunderstanding common?**

1. **直觉上的条件概率反转**
   - 我们想知道：P(H₁ | Data)
   - 但 p-value 给我们：P(Data | H₀)
   - 这两个完全不同！

2. **频率学派 vs 贝叶斯学派**
   - 频率学派：避免讨论"假设的概率"
   - 贝叶斯学派：直接计算"假设的概率"

**关键洞察 | Key Insight:**
- p-value 不告诉我们"真理的概率"
- 它告诉我们"在假设无差异的情况下，看到这样数据的罕见程度"
- 这就是为什么需要贝叶斯思维！

</details>

**Q2: 如果你想知道"基因真的有差异的概率"，你需要什么信息？**
**If you want to know "the probability the gene truly has a difference", what information do you need?**

- **A. 只需要 p-value**
  - Only need p-value

- **B. 需要 p-value 和先验概率**
  - Need p-value and prior probability

- **C. 需要 p-value、先验概率和统计功效**
  - Need p-value, prior probability, and statistical power

- **D. 需要重新做实验**
  - Need to redo the experiment

<details>
<summary>点击查看答案 | Click to see answer</summary>

**✅ 正确答案：C**

**贝叶斯公式 | Bayes' Formula:**

```
P(H₁|Data) = P(Data|H₁) × P(H₁) / P(Data)

其中：
- P(Data|H₁) = power（统计功效）
- P(H₁) = prior（先验概率）
- P(Data) = P(Data|H₀) × P(H₀) + P(Data|H₁) × P(H₁)
```

**所以你需要：**
1. p-value = P(Data|H₀)
2. 先验概率 = P(H₁)
3. 统计功效 = P(Data|H₁)

</details>

### 📊 连接到 FigureYa 模块 | Connect to FigureYa Module

**实践练习 | Practical Exercise:**

打开 `/Users/pro/FigureYa/FigureYa59volcanoV2/`

```r
# 读取火山图数据
x <- read.csv("easy_input_limma.csv")

# 选择 p-value 在 0.03 附近的基因
genes_p_03 <- x[abs(x$P.Value - 0.03) < 0.01, ]

# 查看 logFC 的范围
range(genes_p_03$logFC)

# 思考：
# 1. 为什么这些基因的 p-value 相似但 logFC 不同？
# 2. 如果要计算"基因真的有差异的概率"，需要什么信息？
```

### 🤔 反思问题 | Reflection Questions

**这个问题澄清了你对 p-value 的理解吗？**
**Did this question clarify your understanding of p-value?**

- **A. 是的，我现在理解了 p-value 的真实含义**
  - Yes, I now understand the true meaning of p-value

- **B. 部分澄清，但还需要实践**
  - Partially clarified, but need practice

- **C. 还是困惑，想看更多例子**
  - Still confused, want to see more examples

- **D. 想跳到下一个问题**
  - Want to skip to the next question

---

## 问题 3：Sample Size 为什么重要？| Question 3: Why Does Sample Size Matter?

### 🎯 学习目标 | Learning Objectives

- 理解 sample size 如何影响统计推断
- 认识到 sample size 不是"越大越好"
- 理解 variance 和 sample size 的权衡

### 🧪 直觉测试 | Intuition Test

**假设你有两个实验：**
**Assume you have two experiments:**

**实验 A**: n = 3（每组 3 个样本）
**实验 B**: n = 30（每组 30 个样本）

**其他条件完全相同，得到相同的 logFC = 2**

**Q1: 你认为哪个实验的 p-value 会更小？**
**Which experiment do you think will have a smaller p-value?**

- **A. 实验 A（n=3）**
  - Because smaller sample size gives more precise results

- **B. 实验 B（n=30）**
  - Because larger sample size gives more precise results

- **C. 两者 p-value 相似**
  - Similar p-values in both

- **D. 不确定**
  - Unsure

<details>
<summary>点击查看详细解释 | Click to see detailed explanation</summary>

**✅ 正确答案：B**

**数学解释 | Mathematical Explanation:**

```r
# t-statistic 的计算：
t = logFC / SE

# 标准误 SE 的计算：
SE = SD / sqrt(n)

# 所以：
# n = 3: SE = SD / sqrt(3) ≈ 0.58 × SD
# n = 30: SE = SD / sqrt(30) ≈ 0.18 × SD

# 因此：
# n = 3: t = logFC / (0.58 × SD)
# n = 30: t = logFC / (0.18 × SD)

# n 越大 → SE 越小 → t 越大 → p-value 越小
```

**关键洞察 | Key Insight:**
- Sample size 通过影响标准误来影响统计推断
- **更大的样本 → 更小的 SE → 更大的 t-statistic → 更小的 p-value**
- 但这不意味着"更大样本 = 更好的科学"

</details>

**Q2: 是否"样本越大越好"？**
**Is "larger sample always better"?**

- **A. 是的，样本越大越好**
  - Yes, larger samples are always better

- **B. 不是，需要考虑成本和收益**
  - No, need to consider cost-benefit

- **C. 不是，有时小样本也能得到好的结果**
  - No, sometimes small samples can give good results

- **D. 不确定**
  - Unsure

<details>
<summary>点击查看详细讨论 | Click to see detailed discussion</summary>

**这需要权衡 | This Requires Trade-offs:**

**支持大样本的理由 | Reasons for Large Samples:**
- 更高的统计功效
- 更精确的估计
- 能检测到更小的效应

**支持小样本的理由 | Reasons for Small Samples:**
- 成本更低
- 更快的实验周期
- 有时生物学限制（如稀有样本）

**关键问题 | Key Question:**
- **你能承受的样本量是多少？**
- **你需要检测的效应大小是多少？**
- **你能接受的第一类和第二类错误率是多少？**

**实际应用 | Practical Application:**
- 样本量计算应该在实验**设计阶段**完成
- 基于预期的效应大小和可接受的错误率
- 而不是简单地"越大越好"

</details>

### 🤔 反思问题 | Reflection Questions

**这个问题改变了你对 sample size 的理解吗？**
**Did this question change your understanding of sample size?**

- **A. 是的，我理解了样本量和统计功效的关系**
  - Yes, I understand the relationship between sample size and statistical power

- **B. 部分改变**
  - Partially changed

- **C. 想看更多实际例子**
  - Want to see more practical examples

- **D. 想跳到下一个问题**
  - Want to skip to the next question

---

## 问题 4：为什么模型一定会失真？| Question 4: Why Do Models Always Distort?

### 🎯 学习目标 | Learning Objectives

- 理解所有模型都是对现实的简化
- 认识到"模型失真"的必然性
- 学会在"欠拟合"和"过拟合"之间权衡

### 🧪 直觉测试 | Intuition Test

**Q1: 你认为"完美的模型"可能存在吗？**
**Do you think a "perfect model" can exist?**

- **A. 可能存在，只要有足够的数据**
  - Possible, if there's enough data

- **B. 可能存在，如果模型足够复杂**
  - Possible, if the model is complex enough

- **C. 不可能存在，所有模型都是对现实的简化**
  - Impossible, all models are simplifications of reality

- **D. 不确定**
  - Unsure

<details>
<summary>点击查看详细解释 | Click to see detailed explanation</summary>

**✅ 正确答案：C**

**名言 | Famous Quote:**
> "All models are wrong, but some are useful." 
> —— George Box

**为什么所有模型都失真？| Why Do All Models Distort?**

1. **简化假设 | Simplifying Assumptions**
   - 线性回归假设线性关系
   - t-test 假设正态分布
   - 这些假设在现实中很少完全成立

2. **测量误差 | Measurement Error**
   - 所有测量都有误差
   - 误差会被模型"吸收"

3. **遗漏变量 | Omitted Variables**
   - 我们永远无法包含所有相关变量
   - 遗漏的变量会影响模型结果

4. **数据限制 | Data Limitations**
   - 样本总是有限的
   - 无法捕捉所有变异

**关键洞察 | Key Insight:**
- 模型的目标不是"完美"，而是"有用"
- 好的模型在简单性和准确性之间找到平衡
- 统计学是关于"在不确定性中做出最好的推断"

</details>

**Q2: 应该如何选择模型的复杂度？**
**How should you choose model complexity?**

- **A. 越简单越好**
  - Simpler is always better

- **B. 越复杂越好**
  - More complex is always better

- **C. 在欠拟合和过拟合之间权衡**
  - Trade-off between underfitting and overfitting

- **D. 不确定**
  - Unsure

<details>
<summary>点击查看详细讨论 | Click to see detailed discussion</summary>

**✅ 正确答案：C**

**偏差-方差权衡 | Bias-Variance Trade-off:**

```
简单模型（欠拟合）:
- 高偏差，低方差
- 无法捕捉数据的真实模式
- 例如：用线性模型拟合非线性关系

复杂模型（过拟合）:
- 低偏差，高方差
- 捕捉了噪声而非信号
- 例如：用高阶多项式拟合简单关系

最优模型:
- 在偏差和方差之间找到平衡
- 捕捉真实模式，避免拟合噪声
```

**实际应用 | Practical Application:**
- 交叉验证来选择模型复杂度
- 信息准则（AIC, BIC）来比较模型
- 领域知识来指导模型选择

</details>

### 🤔 反思问题 | Reflection Questions

**这个问题改变了你对模型的看法吗？**
**Did this question change your perspective on models?**

- **A. 是的，我理解了模型的局限性**
  - Yes, I understand the limitations of models

- **B. 部分改变**
  - Partially changed

- **C. 想看更多实际例子**
  - Want to see more practical examples

- **D. 想跳到下一个问题**
  - Want to skip to the next question

---

## 问题 5：Biological vs Technical Variability | Question 5

### 🎯 学习目标 | Learning Objectives

- 理解 biological variability 和 technical variability 的区别
- 学会在分析中区分这两种变异
- 认识到减少 technical variability 的重要性

### 🧪 直觉测试 | Intuition Test

**Q1: 你认为以下哪些是 biological variability？| Which of the following are biological variability?**

**可多选 | Multiple selections:**

- **A. 不同个体之间基因表达的差异**
  - Gene expression differences between individuals

- **B. 同一样本重复测量之间的差异**
  - Differences between repeated measurements of the same sample

- **C. 不同处理组之间的差异**
  - Differences between different treatment groups

- **D. 实验操作造成的差异**
  - Differences caused by experimental procedures

<details>
<summary>点击查看答案和解释 | Click to see answer and explanation</summary>

**✅ 正确答案：A, C**

**Biological Variability | 生物学变异:**
- **A. 不同个体之间的差异**: 是
  - 这是真实的生物学差异
  - 反映了群体的异质性

- **C. 不同处理组之间的差异**: 是
  - 这是实验想要检测的效应
  - 是生物学上有意义的差异

**Technical Variability | 技术变异:**
- **B. 重复测量的差异**: 否
  - 这是测量误差
  - 应该尽可能减小

- **D. 实验操作的差异**: 否
  - 这是技术噪声
  - 应该通过标准化操作来减小

**关键区别 | Key Distinction:**
```
Biological Variability:
- 我们想研究的
- 不能消除（它是研究目标的一部分）
- 需要充分估计

Technical Variability:
- 我们不想要的
- 应该最小化
- 通过实验设计和技术改进来减小
```

</details>

**Q2: 如何区分 biological 和 technical variability？**
**How to distinguish between biological and technical variability?**

- **A. 通过重复实验**
  - Through replicate experiments

- **B. 通过统计模型**
  - Through statistical models

- **C. 通过实验设计**
  - Through experimental design

- **D. 以上都是**
  - All of the above

<details>
<summary>点击查看答案 | Click to see answer</summary>

**✅ 正确答案：D**

**实际方法 | Practical Methods:**

1. **实验设计 | Experimental Design**
   - Technical replicates: 同一样本重复测量
   - Biological replicates: 不同个体的测量
   - 通过对比这两种 replicates 来区分变异来源

2. **统计模型 | Statistical Models**
   - ANOVA 可以分解不同的变异来源
   - Mixed-effects models 可以同时建模固定效应和随机效应

3. **重复实验 | Replicate Experiments**
   - 独立重复验证结果的可靠性
   - 评估 variability 的稳定性

</details>

### 🤔 反思问题 | Reflection Questions

**这个问题帮助你理解 variability 的来源了吗？**
**Did this question help you understand the sources of variability?**

- **A. 是的，我现在能区分 biological 和 technical variability**
  - Yes, I can now distinguish between biological and technical variability

- **B. 部分理解**
  - Partially understand

- **C. 想看更多实际例子**
  - Want to see more practical examples

- **D. 想跳到下一个问题**
  - Want to skip to the next question

---

## 问题 6：为什么 Multiple Testing 会毁掉 Naive Inference？| Question 6: Why Does Multiple Testing Ruin Naive Inference?

### 🎯 学习目标 | Learning Objectives

- 理解多重检验的问题
- 认识到为什么需要校正
- 学会使用 FDR 等校正方法

### 🧪 直觉测试 | Intuition Test

**Q1: 假设你检验了 20,000 个基因，每个都使用 α = 0.05。如果所有基因都没有差异，你预计会发现多少"显著"基因？**
**Assume you test 20,000 genes, each using α = 0.05. If all genes have no difference, how many "significant" genes do you expect to find?**

- **A. 大约 0-1 个**
  - About 0-1 genes

- **B. 大约 100 个**
  - About 100 genes

- **C. 大约 1000 个**
  - About 1000 genes

- **D. 不确定**
  - Unsure

<details>
<summary>点击查看详细解释 | Click to see detailed explanation</summary>

**✅ 正确答案：C**

**计算 | Calculation:**
```r
# 假设：
m <- 20000          # 基因数量
alpha <- 0.05       # 显著性水平

# 如果所有基因都没有差异（H₀ 全部为真）：
# 每个基因假阳性的概率 = alpha = 0.05
# 期望假阳性数量 = m × alpha = 20000 × 0.05 = 1000
```

**这意味着什么？| What Does This Mean?**
- 即使所有基因都没有差异
- 你也会"发现"约 1000 个"显著"基因
- 这些都是假阳性（False Positives）

**关键洞察 | Key Insight:**
- Multiple testing 会产生大量的假阳性
- 需要校正来控制总体错误率
- FDR（False Discovery Rate）是常用的校正方法

</details>

**Q2: 你应该使用哪种校正方法？**
**Which correction method should you use?**

- **A. 不需要校正**
  - No correction needed

- **B. Bonferroni 校正**
  - Bonferroni correction

- **C. FDR（BH 方法）**
  - FDR (BH method)

- **D. 取决于研究目标**
  - Depends on research goals

<details>
<summary>点击查看详细讨论 | Click to see detailed discussion</summary>

**✅ 正确答案：D**

**不同校正方法的适用场景 | Different Correction Methods for Different Scenarios:**

**Bonferroni 校正:**
```
α_corrected = α / m
非常严格，控制家族错误率（FWER）
适用于：少量检验，且假阳性后果严重
例如：临床试验的主要终点
```

**FDR（False Discovery Rate）:**
```
控制在"显著"结果中假阳性的比例
较宽松，允许一定比例的假阳性
适用于：大量检验，探索性研究
例如：基因组学、蛋白质组学筛选
```

**关键问题 | Key Questions:**
1. 你做多少次检验？（少量 vs 大量）
2. 假阳性的后果是什么？（严重 vs 可接受）
3. 你的研究目标是什么？（验证 vs 探索）

</details>

### 🤔 反思问题 | Reflection Questions

**这个问题帮助你理解多重检验了吗？**
**Did this question help you understand multiple testing?**

- **A. 是的，我理解了为什么需要校正**
  - Yes, I understand why correction is needed

- **B. 部分理解**
  - Partially understand

- **C. 想看更多实际例子**
  - Want to see more practical examples

- **D. 想跳到下一个问题**
  - Want to skip to the next question

---

## 问题 7：为什么小样本下 p-value 不稳定？| Question 7: Why is P-value Unstable with Small Samples?

### 🎯 学习目标 | Learning Objectives

- 理解小样本下 p-value 的不稳定性
- 认识到重复实验的重要性
- 学会评估结果的可靠性

### 🧪 直觉测试 | Intuition Test

**Q1: 假设你做了一个实验（n=3），得到 p = 0.03。如果你重复这个实验，你认为会得到什么结果？**
**Assume you did an experiment (n=3) and got p = 0.03. If you repeat this experiment, what result do you think you'll get?**

- **A. 应该也会得到 p ≈ 0.03**
  - Should also get p ≈ 0.03

- **B. 可能在 0.001 到 0.10 之间**
  - Likely between 0.001 and 0.10

- **C. 可能在 0.001 到 0.50 之间**
  - Likely between 0.001 and 0.50

- **D. 完全不确定**
  - Completely unsure

<details>
<summary>点击查看详细解释 | Click to see detailed explanation</summary>

**✅ 正确答案：C**

**模拟研究 | Simulation Study:**
```r
# 假设真实情况：logFC = 1, SD = 1
set.seed(123)
p_values <- replicate(100, {
  control <- rnorm(3, mean = 0, sd = 1)
  treatment <- rnorm(3, mean = 1, sd = 1)
  t.test(treatment, control)$p.value
})

# 结果：
# p 值范围：0.0001 到 0.48
# p < 0.05 的比例：约 60%（不是 100%！）
```

**这意味着什么？| What Does This Mean?**
- 即使真实效应存在
- 小样本（n=3）下 p-value 波动很大
- 单次实验的 p-value 不可靠

**关键洞察 | Key Insight:**
- 小样本 → 方差估计不稳定 → p-value 不稳定
- 需要重复实验验证结果
- 或者使用能"借用信息"的方法（如 limma）

</details>

**Q2: 如何提高小样本研究的可靠性？**
**How to improve reliability of small-sample studies?**

- **A. 重复实验**
  - Replicate experiments

- **B. 使用能"借用信息"的方法（如 limma）**
  - Use methods that "borrow information" (like limma)

- **C. 增加样本量**
  - Increase sample size

- **D. 以上都是**
  - All of the above

<details>
<summary>点击查看答案 | Click to see answer</summary>

**✅ 正确答案：D**

**提高可靠性的方法 | Methods to Improve Reliability:**

1. **重复实验 | Replication**
   - 独立重复验证结果
   - 元分析结合多次研究

2. **Empirical Bayes 方法 | Empirical Bayes Methods**
   - limma 通过"借用信息"稳定方差估计
   - 即使小样本也能得到可靠结果

3. **增加样本量 | Increase Sample Size**
   - 最直接的方法
   - 需要在实验设计阶段考虑

</details>

### 🤔 反思问题 | Reflection Questions

**这个问题帮助你理解小样本问题了吗？**
**Did this question help you understand small-sample issues?**

- **A. 是的，我理解了小样本的问题**
  - Yes, I understand the issues with small samples

- **B. 部分理解**
  - Partially understand

- **C. 想看更多实际例子**
  - Want to see more practical examples

- **D. 想结束学习**
  - Want to finish learning

---

## 学习总结 | Learning Summary

### 自我评估 | Self-Assessment

**学完这 7 个问题，你觉得自己：**
**After completing these 7 questions, you feel:**

- **A. 完全理解了统计推断的本质**
  - Fully understand the essence of statistical inference

- **B. 建立了统计思维的基础**
  - Built the foundation of statistical thinking

- **C. 对某些概念理解更深，但还需要实践**
  - Deeper understanding of some concepts, but need practice

- **D. 想重新学习某些问题**
  - Want to review some questions

### 下一步学习建议 | Next Steps Recommendations

**如果你想：**
- **深入理解贝叶斯思维** → 使用 `figureya-bayesian-thinking`
- **学习具体统计方法** → 使用 `figureya-learn-statistics`
- **实践数据分析** → 使用 FigureYa 模块分析自己的数据

---

## 附录：快速参考 | Appendix: Quick Reference

### 7 个核心问题总结 | 7 Core Questions Summary

| 问题 | 核心洞察 |
|------|---------|
| 1. Variance 为什么存在？ | Variance 是数据的基本属性，不是噪声 |
| 2. p-value 为什么不是"真理概率"？ | P(Data\|H₀) ≠ P(H₁\|Data)，条件概率的反转 |
| 3. Sample Size 为什么重要？ | 通过影响标准误来影响统计推断 |
| 4. 为什么模型一定会失真？ | 所有模型都是简化，目标是"有用"而非"完美" |
| 5. Biological vs Technical Variability？ | 需要区分并分别处理 |
| 6. 为什么 Multiple Testing 会毁掉 Naive Inference？| 产生大量假阳性，需要校正 |
| 7. 为什么小样本下 p-value 不稳定？ | 方差估计不稳定，需要重复或借用信息 |

### 相关 FigureYa 模块 | Related FigureYa Modules

- **FigureYa59volcanoV2**: 火山图（主要使用模块）
- **FigureYa117multilinearDE**: limma 分析
- **FigureYa135multiVolcano**: 多重检验可视化

---

**版本 | Version**: 1.0.0
**创建时间 | Created**: 2026-05-14
**作者 | Author**: Claude Code with FigureYa Community
**GitHub**: https://github.com/ying-ge/FigureYa-skills
**许可证 | License**: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License
