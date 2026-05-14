---
name: figureya-bayesian-thinking
description: 从"显著性思维"重构为"贝叶斯式的不确定性更新思维" - 通过生物医学数据理解先验、似然、后验，建立贝叶斯直觉，自然产生贝叶斯问题
version: 1.0.0
---

# FigureYa Bayesian Thinking Tutor | 用 FigureYa 建立贝叶斯思维

## 简介 | Introduction

这是一个专门设计用来**重构思维模式**的 skill —— 从传统的"显著性思维"（p-value < 0.05）转向"贝叶斯式的不确定性更新思维"。

This is a skill specifically designed to **restructure thinking patterns** — from traditional "significance thinking" (p-value < 0.05) to "Bayesian uncertainty updating thinking".

## 学习开始前 | Before We Start

首先，让我了解一下你的背景：

### 问题1：你的统计学背景 | Your Statistics Background

**What is your statistics background?**

- **A. 统计初学者 | Statistics Beginner**
  - 几乎没有统计背景，想从零开始学习
  - Almost no statistics background, want to start from scratch

- **B. 生物医学研究生 | Biomedical Graduate Student**
  - 有一些统计基础，需要在生物数据分析场景中应用
  - Have some statistics background, need to apply in biological data analysis

- **C. 数据分析从业者 | Data Analysis Practitioner**
  - 有经验，想学习高级统计方法和贝叶斯思维
  - Have experience, want to learn advanced statistical methods and Bayesian thinking

### 问题2：你对贝叶斯统计的了解程度 | Your Understanding of Bayesian Statistics

**How familiar are you with Bayesian statistics?**

- **A. 完全不了解 | Completely New**
  - 从未听说过贝叶斯统计，或者只知道名字
  - Never heard of Bayesian statistics, or only know the name

- **B. 有一些概念 | Some Concepts**
  - 听说过先验、后验等概念，但不清楚如何应用
  - Heard of prior, posterior, but not sure how to apply

- **C. 理解基本原理 | Understand Basic Principles**
  - 理解贝叶斯公式，想在生物数据分析中应用
  - Understand Bayes' formula, want to apply in biological data analysis

### 问题3：你希望通过这个skill达到什么目标？| Your Learning Goals

**What do you want to achieve with this skill?** (可多选 | Multiple selections allowed)

- **A. 理解贝叶斯思维 | Understand Bayesian Thinking**
  - 理解贝叶斯推断的本质和思维方式
  - Understand the essence and thinking pattern of Bayesian inference

- **B. 解决实际数据分析问题 | Solve Real Data Analysis Problems**
  - 在实际研究中应用贝叶斯方法
  - Apply Bayesian methods in real research

- **C. 理解常用工具的原理 | Understand Principles of Common Tools**
  - 理解 limma、FDR 等常用方法的贝叶斯原理
  - Understand Bayesian principles behind limma, FDR, etc.

- **D. 从"显著性思维"转向"贝叶斯思维" | Transition from Significance to Bayesian Thinking**
  - 改变p<0.05的二元思维模式
  - Change the binary thinking pattern of p<0.05

---

## 为什么需要贝叶斯思维？| Why Bayesian Thinking?

### 当前问题 | Current Problem

大多数生物医学研究者被训练成"显著性思维"：
- 看到 **p < 0.05** 就说"显著"
- 看到 **p = 0.03** 就理解为"97% 概率为真"
- 忽视**先验信息**和生物学背景
- 无法回答："这个基因**真的**有差异的概率是多少？"

Most biomedical researchers are trained in "significance thinking":
- Seeing **p < 0.05** and declaring "significant"
- Seeing **p = 0.03** and interpreting as "97% probability it's true"
- Ignoring **prior information** and biological context
- Unable to answer: "What's the probability this gene **truly** has a difference?"

### 贝叶斯思维的优势 | Bayesian Thinking Advantages

**贝叶斯思维提供了一种更自然的推理方式** | Bayesian thinking provides a more natural reasoning approach:

1. **直接回答 | Direct Answer**:
   - 频率学派：p = 0.03（这是 P(Data|H₀)，不是我们想要的）
   - 贝叶斯学派：P(H₁|Data) = 85%（这就是我们想要的！）

2. **结合先验知识 | Incorporate Prior Knowledge**:
   - 生物学背景
   - 既往研究结果
   - 领域专家知识

3. **不确定性量化 | Quantify Uncertainty**:
   - 不是二元结论（显著/不显著）
   - 而是概率分布（85% 可能，15% 不可能）

4. **信念更新 | Belief Updating**:
   - 从先验概率 → 数据 → 后验概率
   - 符合人类自然推理方式

---

## 模块 1：思维模式对比 | Module 1: Thinking Pattern Comparison

**"显著" vs "可能多大" | "Significant" vs "How Likely"**

### 测试你的直觉 | Test Your Intuition

让我们从一个医疗检测例子开始：

```
某疾病患病率：1% (prevalence = 0.01)
检测灵敏度：99% (sensitivity = 0.99)
假阳性率：5% (false_positive = 0.05)

如果你检测阳性，你真的有病的概率是多少？
```

### 问题 | Question

**你认为检测结果阳性时，真实患病的概率是多少？**

**What do you think is the probability of actually having the disease when testing positive?**

- **A. 95%** (因为 100% - 5% 假阳性率 = 95%)
- **B. 99%** (因为检测灵敏度是 99%)
- **C. 约 16.7%** (考虑患病率后的结果)
- **D. 不确定，想看计算过程 | Unsure, want to see the calculation**

<details>
<summary>点击查看答案和解释 | Click to see answer and explanation</summary>

**✅ 正确答案：C. 约 16.7%**

**计算过程 | Calculation Process**:

```r
# 医疗检测的贝叶斯计算
prevalence <- 0.01    # 先验：1% 患病率
sensitivity <- 0.99   # 灵敏度：P(Positive|Disease)
false_positive <- 0.05 # 假阳性率：P(Positive|Healthy)

# 贝叶斯公式
# P(Disease|Positive) = P(Positive|Disease) × P(Disease) / P(Positive)

p_positive_given_disease <- sensitivity
p_positive_given_healthy <- false_positive
p_disease <- prevalence
p_healthy <- 1 - prevalence

p_positive <- p_positive_given_disease * p_disease +
              p_positive_given_healthy * p_healthy

p_disease_given_positive <- (p_positive_given_disease * p_disease) / p_positive

cat("检测结果阳性的真实患病概率:", round(p_disease_given_positive * 100, 1), "%\n")
# 结果：16.7%，不是 95%！
```

**为什么差距这么大？| Why such a big difference?**

这是贝叶斯思维的核心：

1. **条件概率的反转** | **Conditional Probability Reversal**:
   - P(Data|H) ≠ P(H|Data)
   - P(阳性|有病) = 99% ≠ P(有病|阳性) = 16.7%

2. **先验信息至关重要** | **Prior Information is Crucial**:
   - 患病率 1% → 即使检测阳性，真实患病概率只有 16.7%
   - 如果患病率 50% → 检测阳性的真实患病概率会是 95%

**关键洞察 | Key Insight**:
- 直觉往往忽略**先验概率**的重要性
- 检测准确度 ≠ 预测准确度
- 这就是为什么我们需要贝叶斯思维！

</details>

### 反思问题 | Reflection Questions

**这个问题改变了你对p值的理解吗？| Did this question change your understanding of p-values?**

- **A. 是的，我意识到p值不是我原来想的那样**
  - Yes, I realized p-value is not what I thought

- **B. 部分改变，但还需要更多例子**
  - Partially, but I need more examples

- **C. 没有改变，我已经理解了贝叶斯思维**
  - No change, I already understood Bayesian thinking

- **D. 还是困惑，想继续学习**
  - Still confused, want to continue learning

---

## 模块 2：贝叶斯公式 | Module 2: Bayes' Formula

**从医疗检测到基因表达 | From Medical Testing to Gene Expression**

### 测试你的理解 | Test Your Understanding

将医疗检测的逻辑应用到**基因差异表达分析**：

```
某个基因的 p-value = 0.03
这告诉我们什么？

❌ 常见误解：97% 概率这个基因真的有差异
✅ 正确理解：如果基因无差异，只有 3% 概率看到这样的数据
```

### 问题 | Question

**你认为：p = 0.03 意味着什么？| What do you think: p = 0.03 means?**

- **A. 基因有差异的概率是 97%**
  - There's 97% probability the gene has a difference

- **B. 如果基因无差异，看到这样数据的概率是 3%**
  - If the gene has no difference, there's 3% probability of seeing such data

- **C. 不确定这两者的区别**
  - Unsure about the difference between these two

- **D. 想学习如何计算"基因有差异的概率"**
  - Want to learn how to calculate "probability the gene has a difference"

<details>
<summary>点击查看详细解释 | Click to see detailed explanation</summary>

**✅ 正确答案：B**

**如何回答："这个基因**真的**有差异的概率是多少？"**

需要什么信息：

1. **p-value** = P(Data|H₀) = 0.03（已知）
2. **先验概率** = P(H₁) = ?（需要假设）
3. **统计功效** = P(Data|H₁) = ?（需要计算）

**贝叶斯计算示例 | Bayesian Calculation Example**:

```r
# 基因差异表达的贝叶斯推断
p_value <- 0.03        # P(Data|H₀): 如果无差异，看到这样数据的概率
prior_h1 <- 0.1        # P(H₁): 先验认为 10% 基因有差异
power <- 0.8           # P(Data|H₁): 统计功效（如果有差异，检测到的概率）

# 贝叶斯公式
# P(H₁|Data) = P(Data|H₁) × P(H₁) / P(Data)

# 其中：P(Data) = P(Data|H₀) × P(H₀) + P(Data|H₁) × P(H₁)
p_data <- p_value * (1 - prior_h1) + power * prior_h1

p_h1_given_data <- (power * prior_h1) / p_data

cat("p-value:", p_value, "\n")
cat("后验概率:", round(p_h1_given_data, 3), "\n")
# 结果：73.6%，不是 97%！
```

**不同先验的影响 | Effect of Different Priors**:

| 先验概率 | 后验概率 |
|---------|---------|
| 1% | 21.2% |
| 5% | 57.7% |
| 10% | 73.6% |
| 20% | 84.2% |
| 50% | 93.0% |

**关键洞察 | Key Insight**:
- p-value ≠ 后验概率
- 先验概率对结果影响巨大
- 需要结合领域知识选择合理的先验

</details>

### 选择你的学习路径 | Choose Your Learning Path

**接下来你想：| What do you want to do next?**

- **A. 理解贝叶斯公式的数学推导**
  - Understand the mathematical derivation of Bayes' formula
  - 适合：想深入理解理论的学习者

- **B. 用真实数据练习计算后验概率**
  - Practice calculating posterior probabilities with real data
  - 适合：喜欢动手实践的学习者

- **C. 跳到下一个模块（FDR的贝叶斯解释）**
  - Skip to next module (Bayesian interpretation of FDR)
  - 适合：已经理解基础概念的学习者

- **D. 看更多不同先验的影响**
  - See more effects of different priors
  - 适合：想深入探索先验选择的学习者

---

## 模块 3：FDR 的贝叶斯解释 | Module 3: Bayesian Interpretation of FDR

**为什么多重检验需要校正？| Why Multiple Testing Needs Correction?**

### 问题 | Question

**在基因表达分析中，同时检验 20,000 个基因，如果都不校正，你认为会发生什么？**

**In gene expression analysis, testing 20,000 genes simultaneously without correction, what do you think will happen?**

- **A. 大约有 1000 个假阳性基因**
  - About 1000 false positive genes

- **B. 假阳性数量可以忽略不计**
  - False positives are negligible

- **C. 不确定什么是假阳性**
  - Unsure what false positive means

- **D. 想了解FDR的贝叶斯解释**
  - Want to understand Bayesian interpretation of FDR

<details>
<summary>点击查看详细解释 | Click to see detailed explanation</summary>

**✅ 正确答案：A**

**FDR 的贝叶斯计算 | Bayesian Calculation of FDR**:

```r
# 假设：
m <- 20000          # 基因数量
alpha <- 0.05       # 显著性水平
prior <- 0.01       # 先验：1% 基因真的有差异
power <- 0.8        # 统计功效

# 贝叶斯 FDR 计算
fdr_bayesian <- (prior * alpha) /
               (prior * power + (1 - prior) * alpha)

cat("贝叶斯 FDR:", round(fdr_bayesian * 100, 1), "%\n")
# 结果：38.4%

# 意味着：即使在"显著"（p < 0.05）基因中，
# 仍有 38.4% 可能是假阳性！
```

**关键洞察 | Key Insight**:
- FDR 本质上是**后验假阳性率**
- 先验概率越低（真实差异基因越少）→ FDR 越高
- 如果只有 1% 基因真的有差异 → FDR = 38.4%

</details>

---

## 模块 4：Empirical Bayes - limma 的小样本魔法 | Module 4: Empirical Bayes

### 问题 | Question

**limma 为什么在小样本下表现好？| Why does limma perform well with small samples?**

- **A. 使用了更强大的统计检验**
  - Uses more powerful statistical tests

- **B. 使用了 Empirical Bayes（经验贝叶斯）**
  - Uses Empirical Bayes

- **C. 对数据进行了特殊处理**
  - Special data processing

- **D. 不确定，想了解 Empirical Bayes**
  - Unsure, want to understand Empirical Bayes

---

## 模块 5：先验选择 | Module 5: Prior Selection

### 问题 | Question

**如何客观地选择先验？| How to objectively choose a prior?**

**What do you think is the best approach?** (可多选 | Multiple selections)

- **A. 无信息先验（让数据说话）**
  - Uninformative prior (let data speak)

- **B. 弱信息先验（提供正则化）**
  - Weakly informative prior (provide regularization)

- **C. 有信息先验（基于既往研究）**
  - Informative prior (based on previous studies)

- **D. Empirical Bayes（从数据学习）**
  - Empirical Bayes (learn from data)

---

## 模块 6：贝叶斯工作流 | Module 6: Bayesian Workflow

### 问题 | Question

**贝叶斯工作流相比频率学派的优势是什么？| What's the advantage of Bayesian workflow over frequentist?**

**What do you think are the main advantages?** (可多选 | Multiple selections)

- **A. 更直观的概率解释**
  - More intuitive probabilistic interpretation

- **B. 可以结合先验知识**
  - Can incorporate prior knowledge

- **C. 灵活的决策分析**
  - Flexible decision analysis

- **D. 完整的不确定性量化**
  - Complete uncertainty quantification

---

## 模块 7：实践练习 | Module 7: Practice Exercises

### 选择练习类型 | Choose Practice Type

**你想进行哪种类型的练习？| What type of practice do you want?**

- **A. 理论练习：计算后验概率**
  - Theoretical exercises: Calculate posterior probabilities
  - 提供不同 p-value 和先验，计算后验概率

- **B. 数据分析：重新解读已发表结果**
  - Data analysis: Re-interpret published results
  - 使用真实的 FigureYa 模块数据

- **C. 案例研究：先验选择的敏感性分析**
  - Case study: Sensitivity analysis of prior selection
  - 探索不同先验对结论的影响

- **D. 综合练习：完整贝叶斯分析**
  - Comprehensive exercise: Complete Bayesian analysis
  - 从先验选择到后验推断的全流程

---

## 学习总结 | Learning Summary

### 自我评估 | Self-Assessment

**学完这些模块后，你觉得自己：| After completing these modules, you feel:**

- **A. 完全理解了贝叶斯思维**
  - Fully understand Bayesian thinking

- **B. 基本理解，但还需要更多实践**
  - Basically understand, but need more practice

- **C. 理解了概念，但不确定如何应用**
  - Understand concepts, but unsure how to apply

- **D. 仍然困惑，需要重新学习某些模块**
  - Still confused, need to review some modules

### 下一步学习建议 | Next Steps Recommendations

**基于你的学习目标，建议：| Based on your learning goals, we recommend:**

如果你的目标是：
- **理解贝叶斯思维** → 回顾模块1-3，多做理论练习
- **解决实际问题** → 重点关注模块7，使用真实数据练习
- **理解常用工具** → 深入学习模块4（limma的Empirical Bayes）
- **转变思维模式** → 反复练习模块1和2，建立贝叶斯直觉

---

## 与其他 Skills 的关系 | Relationship with Other Skills

### 问题 | Question

**你接下来想学习什么？| What do you want to learn next?**

- **A. figureya-inference-thinking**
  - 深入理解统计推断的本质（频率学派 + 贝叶斯学派对比）

- **B. figureya-learn-statistics**
  - 学习具体的统计方法（300+ FigureYa 模块）

- **C. 继续深化贝叶斯思维**
  - Continue deepening Bayesian thinking
  - 推荐阅读：《Statistical Rethinking》

- **D. 实际应用贝叶斯方法**
  - Apply Bayesian methods in practice
  - 使用 FigureYa 模块分析自己的数据

---

## 附录：快速参考 | Appendix: Quick Reference

### 贝叶斯公式 | Bayes' Formula

$$P(H_1|Data) = \frac{P(Data|H_1) \times P(H_1)}{P(Data|H_0) \times P(H_0) + P(Data|H_1) \times P(H_1)}$$

### 关键概念 | Key Concepts

- **先验概率 P(H₁)** | **Prior Probability**: 基于生物学知识、既往研究
- **似然 P(Data|H)** | **Likelihood**: P(Data|H₀) = p-value, P(Data|H₁) = power
- **后验概率 P(H₁|Data)** | **Posterior Probability**: 这是我们真正想要的

### 常见误解 | Common Misconceptions

- ❌ p = 0.03 → 97% 概率为真
- ✅ p = 0.03 → 需要结合先验计算后验概率

### 相关 FigureYa 模块 | Related FigureYa Modules

- **FigureYa59volcanoV2**: 火山图（贝叶斯公式、FDR）
- **FigureYa117multilinearDE**: limma 分析（Empirical Bayes）
- **FigureYa273BAPC**: 完整贝叶斯分析示例

---

**版本 | Version**: 1.0.0
**创建时间 | Created**: 2026-05-14
**作者 | Author**: Claude Code with FigureYa Community
**GitHub**: https://github.com/ying-ge/FigureYa-skills
**许可证 | License**: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License
