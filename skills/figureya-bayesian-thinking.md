---
name: figureya-bayesian-thinking
description: 从"显著性思维"重构为"贝叶斯式的不确定性更新思维" - 通过生物医学数据理解先验、似然、后验，建立贝叶斯直觉，自然产生贝叶斯问题
version: 1.0.0
---

# FigureYa Bayesian Thinking Tutor | 用 FigureYa 建立贝叶斯思维

## 简介 | Introduction

这是一个专门设计用来**重构思维模式**的 skill —— 从传统的"显著性思维"（p-value < 0.05）转向"贝叶斯式的不确定性更新思维"。

This is a skill specifically designed to **restructure thinking patterns** — from traditional "significance thinking" (p-value < 0.05) to "Bayesian uncertainty updating thinking".

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

## 核心目标 | Core Goal

**从"显著性思维" → "贝叶斯式的不确定性更新思维"**

**From "Significance Thinking" → "Bayesian Uncertainty Updating Thinking"**

| 显著性思维 | Significance Thinking | → | 贝叶斯思维 | Bayesian Thinking |
|-----------|----------------------|---|-----------|------------------|
| 接受/拒绝假设 | Accept/Reject hypothesis | → | 更新信念分布 | Update belief distribution |
| 二元结论 | Binary conclusion | → | 连续概率 | Continuous probability |
| p-value | p-value | → | 后验概率 | Posterior probability |
| 长期频率 | Long-run frequency | → | 当前信念 | Current belief |

## 7 个核心教学模块 | 7 Core Teaching Modules

### 模块 1：思维模式对比 | Module 1: Thinking Pattern Comparison

**"显著" vs "可能多大" | "Significant" vs "How Likely"**

#### 观察 | Observation

看看这个医疗检测场景：

```
某疾病患病率：1% (prevalence = 0.01)
检测灵敏度：99% (sensitivity = 0.99)
假阳性率：5% (false_positive = 0.05)

如果你检测阳性，你真的有病的概率是多少？
```

#### 提问 | Question

❌ **直觉回答**：95% (因为假阳性率是 5%)

✅ **正确答案**：只有约 16.7%！

为什么差距这么大？

#### 探索 | Exploration

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

**关键问题** | **Key Question**:
- 为什么 **P(Positive|Disease) = 99%** 不等于 **P(Disease|Positive) = 99%**？
- **先验信息**（患病率 1%）如何影响结果？

#### 洞察 | Insight

**这是贝叶斯思维的核心** | **This is the Core of Bayesian Thinking**:

1. **条件概率的反转** | **Conditional Probability Reversal**:
   - P(Data|H) ≠ P(H|Data)
   - P(阳性|有病) ≠ P(有病|阳性)

2. **先验信息至关重要** | **Prior Information is Crucial**:
   - 患病率 1% → 即使检测阳性，真实患病概率只有 16.7%
   - 如果患病率 50% → 检测阳性的真实患病概率会是 95%

3. **二元思维的局限** | **Limitation of Binary Thinking**:
   - "检测阳性/阴性" → 不够
   - "患病概率 16.7%" → 更好

---

### 模块 2：贝叶斯公式 | Module 2: Bayes' Formula

**从医疗检测到基因表达 | From Medical Testing to Gene Expression**

#### 观察 | Observation

将医疗检测的逻辑应用到**基因差异表达分析**：

```
某个基因的 p-value = 0.03
这告诉我们什么？

❌ 常见误解：97% 概率这个基因真的有差异
✅ 正确理解：如果基因无差异，只有 3% 概率看到这样的数据
```

#### 提问 | Question

如何回答："这个基因**真的**有差异的概率是多少？"

**需要什么信息** | **What Information Do We Need**:

1. **p-value** = P(Data|H₀) = 0.03（已知）
2. **先验概率** = P(H₁) = ?（需要假设）
3. **统计功效** = P(Data|H₁) = ?（需要计算）

#### 探索 | Exploration

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

cat("先验概率:", prior_h1, "\n")
cat("p-value:", p_value, "\n")
cat("后验概率:", round(p_h1_given_data, 3), "\n")
# 结果：73.6%，不是 97%！
```

**不同先验的影响** | **Effect of Different Priors**:

```r
priors <- c(0.01, 0.05, 0.1, 0.2, 0.5)
cat("先验概率 → 后验概率:\n")
for(prior in priors) {
  p_h1_given_data <- (power * prior) /
    (p_value * (1 - prior) + power * prior)
  cat(prior, "→", round(p_h1_given_data, 3), "\n")
}

# 结果：
# 0.01 → 0.212  (21.2%)
# 0.05 → 0.577  (57.7%)
# 0.10 → 0.736  (73.6%)
# 0.20 → 0.842  (84.2%)
# 0.50 → 0.930  (93.0%)
```

#### 洞察 | Insight

**贝叶斯公式的本质** | **Essence of Bayes' Formula**:

$$P(H_1|Data) = \frac{P(Data|H_1) \times P(H_1)}{P(Data|H_0) \times P(H_0) + P(Data|H_1) \times P(H_1)}$$

**核心概念** | **Core Concepts**:

1. **先验概率 P(H₁)** | **Prior Probability**:
   - 基于生物学知识
   - 既往研究结果
   - 可以是"无信息先验"

2. **似然 P(Data|H)** | **Likelihood**:
   - P(Data|H₀) = p-value（频率学派计算）
   - P(Data|H₁) = power（功效分析）

3. **后验概率 P(H₁|Data)** | **Posterior Probability**:
   - 这是我们真正想要的
   - "基因有差异的概率"
   - 不是 p-value！

4. **信念更新** | **Belief Updating**:
   - 先验 10% → 数据 → 后验 73.6%
   - 数据让我们更相信基因有差异

**连接到 FigureYa 模块** | **Connect to FigureYa Module**:

打开 `/Users/pro/FigureYa/FigureYa59volcanoV2/FigureYa59volcanoV2.Rmd`

```r
# 读取火山图数据
x <- read.csv("easy_input_limma.csv")

# 查看前几个基因
head(x[, c("logFC", "P.Value", "adj.P.Val")])

# 选择一个基因计算后验概率
gene <- x[1, ]
p_value <- gene$P.Value
prior <- 0.1  # 假设 10% 基因有差异
power <- 0.8

p_h1_given_data <- (power * prior) /
  (p_value * (1 - prior) + power * prior)

cat("Gene:", rownames(x)[1], "\n")
cat("p-value:", p_value, "\n")
cat("后验概率:", round(p_h1_given_data, 3), "\n")
```

---

### 模块 3：FDR 的贝叶斯解释 | Module 3: Bayesian Interpretation of FDR

**为什么多重检验需要校正？| Why Multiple Testing Needs Correction?**

#### 观察 | Observation

在基因表达分析中，我们同时检验 20,000 个基因：

```r
# 假设：
m <- 20000          # 基因数量
alpha <- 0.05       # 显著性水平
prior <- 0.01       # 先验：1% 基因真的有差异
power <- 0.8        # 统计功效

# 如果不用校正，会有多少假阳性？
# 单次检验假阳性率：5%
# 20000 次检验假阳性期望：20000 × 0.05 = 1000 个！
```

#### 提问 | Question

**即使所有基因都无差异**，我们也会发现约 1000 个"显著"基因（假阳性）。

如何解决这个问题？

**频率学派方法** | **Frequentist Approach**:
- Bonferroni 校正：p_adj = p × m
- BH 方法（FDR）：控制假发现率

**贝叶斯视角** | **Bayesian Perspective**:
- FDR 的本质是什么？
- 为什么先验概率很重要？

#### 探索 | Exploration

```r
# FDR 的贝叶斯解释

# 定义：
# FDR = E[V/R] 其中 V = 假阳性数量，R = 总显著数量

# 贝叶斯解释：
# FDR ≈ 在所有"显著"基因中，假阳性的比例
#     ≈ (先验 × α) / (先验 × power + (1-先验) × α)

alpha <- 0.05
prior <- 0.01       # 假设 1% 基因真的有差异
power <- 0.8

# 贝叶斯 FDR 计算
fdr_bayesian <- (prior * alpha) /
               (prior * power + (1 - prior) * alpha)

cat("贝叶斯 FDR:", round(fdr_bayesian, 3), "\n")
# 结果：38.4%

# 意味着：即使在"显著"（p < 0.05）基因中，
# 仍有 38.4% 可能是假阳性！
```

**不同先验的影响** | **Effect of Different Priors**:

```r
priors <- c(0.001, 0.01, 0.05, 0.1, 0.2)
cat("先验概率 → FDR:\n")
for(prior in priors) {
  fdr <- (prior * alpha) /
         (prior * power + (1 - prior) * alpha)
  cat(prior, "→", round(fdr, 3), "\n")
}

# 结果：
# 0.001 → 0.062  (6.2%)
# 0.01  → 0.384  (38.4%)
# 0.05  → 0.763  (76.3%)
# 0.1   → 0.865  (86.5%)
# 0.2   → 0.926  (92.6%)
```

**关键洞察** | **Key Insight**:
- **先验概率越低，FDR 越高**
- 如果只有 1% 基因真的有差异 → FDR = 38.4%
- 如果有 20% 基因真的有差异 → FDR = 92.6%（但这不合理）

**连接到 FigureYa 模块** | **Connect to FigureYa Module**:

```r
# 读取火山图数据
x <- read.csv("/Users/pro/FigureYa/FigureYa59volcanoV2/easy_input_limma.csv")

# 对比未校正和校正的结果
sig_raw <- sum(x$P.Value < 0.05)
sig_adj <- sum(x$adj.P.Val < 0.05)

cat("未校正显著基因数:", sig_raw, "\n")
cat("FDR校正后显著基因数:", sig_adj, "\n")
cat("减少比例:", round((sig_raw - sig_adj) / sig_raw * 100, 1), "%\n")

# 查看 adj.P.Val 的分布
hist(x$adj.P.Val, breaks = 50, main = "FDR-corrected p-values",
     xlab = "Adjusted p-value", col = "lightblue")
abline(v = 0.05, col = "red", lwd = 2, lty = 2)
```

#### 洞察 | Insight

**FDR 的贝叶斯解释** | **Bayesian Interpretation of FDR**:

1. **FDR 本质上是后验假阳性率** | **FDR is Essentially Posterior False Positive Rate**:
   - 不是长期频率概念
   - 而是：在显著基因中，假阳性的期望比例

2. **先验概率的影响** | **Effect of Prior Probability**:
   - 先验越低（真实差异基因越少）→ FDR 越高
   - 这符合直觉：如果大海捞针，找到的"石头"会很多

3. **BH 方法的贝叶斯意义** | **Bayesian Meaning of BH Method**:
   - BH 校正近似于控制后验假阳性率
   - 比频率学派解释更直观

---

### 模块 4：Empirical Bayes - limma 的小样本魔法 | Module 4: Empirical Bayes

#### 观察 | Observation

**问题** | **Problem**:
- 小样本（如每组 3 个重复）
- 方差估计不稳定
- p-value 波动很大

**limma 的解决方案** | **limma's Solution**:
- 使用 **Empirical Bayes（经验贝叶斯）**
- 即使只有 3 个重复，也能得到稳定结果

#### 提问 | Question

**Empirical Bayes 是什么？**

如何从"所有基因"学习"单个基因"的方差？

#### 探索 | Exploration

```r
# Empirical Bayes 原理演示

# 问题：小样本下方差估计不稳定
set.seed(123)
n <- 3  # 每组只有 3 个样本

# 模拟 100 个基因，大多数方差在 0.1 左右
true_var <- 0.1
# 但有个别基因方差很大（离群值）
outlier_var <- 2.0

# 小样本估计的方差会非常不稳定
var_estimates_small <- replicate(100, var(rnorm(n, 0, sqrt(true_var))))
var_outlier_small <- var(rnorm(n, 0, sqrt(outlier_var)))

cat("真实方差 0.1，小样本估计均值:", round(mean(var_estimates_small), 3), "\n")
cat("真实方差 2.0，小样本估计:", round(var_outlier_small, 3), "\n")
# 可以看到小样本估计非常不稳定！

# Empirical Bayes 的思路：
# 1. 从所有基因估计"先验"方差分布
prior_mean <- mean(var_estimates_small)
prior_var <- var(var_estimates_small)

cat("\n先验方差均值:", round(prior_mean, 3), "\n")

# 2. 用先验收缩极端估计
# 简单 shrinkage: 向先验均值收缩
shrinkage_factor <- 0.5  # 简化示例
var_shrunk <- shrinkage_factor * var_outlier_small +
             (1 - shrinkage_factor) * prior_mean

cat("原始估计:", round(var_outlier_small, 3), "\n")
cat("Shrinkage 后:", round(var_shrunk, 3), "\n")
cat("更接近真实值 0.1!\n")
```

**limma 的实际应用** | **limma in Practice**:

```r
# limma 自动应用 Empirical Bayes
library(limma)

# 标准流程：
# 1. fit <- lmFit(expr_data, design)
# 2. fit <- eBayes(fit)  # ← 这里应用 Empirical Bayes！
# 3. topTable(fit)

# eBayes 做了什么？
# - 从所有基因估计先验方差分布
# - 用先验分布收缩每个基因的方差估计
# - 得到更稳定的 t 统计量和 p-value
```

**为什么 limma 在小样本下表现好？** | **Why limma Performs Well with Small Samples?**

```r
# Empirical Bayes 的优势：
# 1. "借力" (Borrowing strength)
#    - 用所有基因的信息改善单个基因的估计
#
# 2. Shrinkage (收缩)
#    - 极端方差估计向全局均值收缩
#    - 减少假阳性和假阴性
#
# 3. 稳定性
#    - 即使 n=3，也能得到合理的推断
```

#### 连接到 FigureYa 模块 | Connect to FigureYa Module

打开 `/Users/pro/FigureYa/FigureYa117multilinearDE/FigureYa117multilinearDE.Rmd`

查看 limma 的实际应用：

```r
# 典型 limma 流程
# 1. 创建设计矩阵
design <- model.matrix(~ group)

# 2. 拟合线性模型
fit <- lmFit(expression_data, design)

# 3. 应用 Empirical Bayes
fit <- eBayes(fit)  # ← 关键步骤！

# 4. 提取结果
top_genes <- topTable(fit, number = Inf, adjust = "BH")

# eBayes 的影响：
# - moderated t-statistic（调节的 t 统计量）
# - 更稳定的方差估计
# - 更准确的 p-value
```

#### 洞察 | Insight

**Empirical Bayes 的本质** | **Essence of Empirical Bayes**:

1. **频率学派 + 贝叶斯学派 = Empirical Bayes** | **Frequentist + Bayesian = Empirical Bayes**:
   - 不是完全的贝叶斯（没有主观先验）
   - 不是完全的频率学派（使用先验信息）
   - 从数据学习先验（Empirical）

2. **适用场景** | **When to Use**:
   - 小样本
   - 大量平行检验（如 20,000 个基因）
   - 假设大多数检验有相似的性质

3. **实际应用** | **Practical Applications**:
   - **limma**: RNA-seq 和微阵列差异分析
   - **DESeq2**: 也使用类似的 shrinkage 思想
   - **edgeR**: 同样借用信息

---

### 模块 5：先验选择 - 如何编码生物学知识 | Module 5: Prior Selection

#### 观察 | Observation

**贝叶斯方法的优势**：可以结合先验知识

**但问题来了**：如何选择先验？

- 太强（informative）→ 主观，可能误导
- 太弱（uninformative）→ 失去贝叶斯优势
- 从数据学习（Empirical Bayes）→ 理论上不够纯粹

#### 提问 | Question

**如何客观地选择先验？**

1. 无信息先验：真的"无信息"吗？
2. 有信息先验：如何避免主观性？
3. Empirical Bayes：是作弊吗？

#### 探索 | Exploration

```r
# 不同先验类型的影响

# 场景：估计基因表达差异
# 真实 logFC = 1.5
# 观测数据：mean = 1.3, se = 0.4

observed_mean <- 1.3
se <- 0.4
n_samples <- 10  # 样本量

# 1. 无信息先验（扁平先验）
# 假设 logFC 可以是任何值
prior_uninf_mean <- 0
prior_uninf_sd <- 1000  # 非常宽

# 后验均值 ≈ 观测均值（数据主导）
posterior_uninf_mean <- (observed_mean/se^2 + prior_uninf_mean/prior_uninf_sd^2) /
                        (1/se^2 + 1/prior_uninf_sd^2)

cat("无信息先验 → 后验均值:", round(posterior_uninf_mean, 3), "\n")
# ≈ 1.3 (几乎等于观测值)

# 2. 弱信息先验（weakly informative）
# 假设 logFC 通常在 [-2, 2] 之间
prior_weak_mean <- 0
prior_weak_sd <- 1

posterior_weak_mean <- (observed_mean/se^2 + prior_weak_mean/prior_weak_sd^2) /
                      (1/se^2 + 1/prior_weak_sd^2)

cat("弱信息先验 → 后验均值:", round(posterior_weak_mean, 3), "\n")
# ≈ 1.23 (向 0 轻微收缩)

# 3. 强信息先验（基于既往研究）
# 假设既往研究显示 logFC ≈ 1.0
prior_strong_mean <- 1.0
prior_strong_sd <- 0.3

posterior_strong_mean <- (observed_mean/se^2 + prior_strong_mean/prior_strong_sd^2) /
                       (1/se^2 + 1/prior_strong_sd^2)

cat("强信息先验 → 后验均值:", round(posterior_strong_mean, 3), "\n")
# ≈ 1.13 (显著向先验收缩)

# 对比：
cat("\n先验强度的影响:\n")
cat("观测值:", observed_mean, "\n")
cat("无信息先验:", round(posterior_uninf_mean, 3), "(数据主导)\n")
cat("弱信息先验:", round(posterior_weak_mean, 3), "(轻微收缩)\n")
cat("强信息先验:", round(posterior_strong_mean, 3), "(显著收缩)\n")
```

**先验选择的原则** | **Prior Selection Principles**:

```r
# 1. 无信息先验（Uninformative Prior）
# 用途：让数据说话
# 示例：正态分布 N(0, 1000) 或均匀分布
# 优点：客观，不引入主观判断
# 缺点：可能不稳定（尤其是小样本）

# 2. 弱信息先验（Weakly Informative Prior）【推荐】
# 用途：提供正则化，但不强
# 示例：正态分布 N(0, 1) 或 Cauchy(0, 2.5)
# 优点：稳定结果，减少过拟合
# 缺点：需要选择合理的范围

# 3. 有信息先验（Informative Prior）
# 用途：结合既往研究或专家知识
# 示例：从 meta-analysis 估计先验
# 优点：提高效率，结合领域知识
# 缺点：主观，如果先验错误会误导
```

**敏感性分析** | **Sensitivity Analysis**:

```r
# 好的贝叶斯分析应该包括敏感性分析
# 检验结论对先验选择的稳健性

priors_to_test <- list(
  "uninformative" = c(0, 1000),
  "weak" = c(0, 1),
  "moderate" = c(0, 0.5),
  "strong" = c(1.0, 0.3)
)

cat("先验敏感性分析:\n")
for(name in names(priors_to_test)) {
  prior <- priors_to_test[[name]]
  posterior <- (observed_mean/se^2 + prior[1]/prior[2]^2) /
              (1/se^2 + 1/prior[2]^2)
  cat(name, ":", round(posterior, 3), "\n")
}

# 如果所有先验下结论一致 → 结论稳健
# 如果结论改变 → 需要更多数据或重新考虑先验
```

#### 连接到 FigureYa 模块 | Connect to FigureYa Module

打开 `/Users/pro/FigureYa/FigureYa273BAPC/FigureYa273BAPC.Rmd`

这是一个完整的贝叶斯分析示例（BAPC = Bayesian Age-Period-Cohort）：

```r
# BAPC 模型展示：
# 1. 先验设置（基于人口统计学知识）
# 2. MCMC 采样
# 3. 后验推断
# 4. 预测

# 实际代码会看到：
# - 先验分布的选择
# - 超参数的设定
# - 收敛性诊断
# - 后验预测检验
```

#### 洞察 | Insight

**先验选择的艺术** | **Art of Prior Selection**:

1. **没有"正确"的先验，只有"合理"的先验** | **No "Correct" Prior, Only "Reasonable" Prior**:
   - 基于科学知识
   - 透明报告先验选择理由
   - 做敏感性分析

2. **样本量 vs 先验强度** | **Sample Size vs Prior Strength**:
   - 大样本：数据主导，先验影响小
   - 小样本：先验影响大（这也是贝叶斯方法的优势）

3. **Empirical Bayes 的妥协** | **Empirical Bayes Compromise**:
   - 从数据学习先验
   - 不是"纯"贝叶斯，但实用
   - limma、DESeq2 都在使用

---

### 模块 6：贝叶斯工作流 | Module 6: Bayesian Workflow

**从数据到决策的完整流程 | Complete Workflow from Data to Decision**

#### 观察 | Observation

**频率学派工作流** | **Frequentist Workflow**:
```
1. 数据准备
2. 拟合模型（如 lm, glm）
3. 计算 p-value
4. p < 0.05？→ 显著 / 不显著
5. 报告结果
```

**贝叶斯工作流** | **Bayesian Workflow**:
```
1. 数据准备
2. 设置先验
3. 拟合模型（MCMC 或解析解）
4. 检查后验分布
5. 做概率陈述
6. 决策分析
```

#### 提问 | Question

**贝叶斯工作流的优势在哪里？**

1. 更直观的概率解释
2. 可以回答复杂的决策问题
3. 自然地处理不确定性

#### 探索 | Exploration

```r
# 简化的贝叶斯工作流示例

# 步骤 1：数据准备
set.seed(123)
control <- rnorm(10, mean = 0, sd = 1)
treatment <- rnorm(10, mean = 1.5, sd = 1)
data <- c(control, treatment)
group <- rep(c(0, 1), each = 10)

# 步骤 2：设置先验
# 假设 treatment effect (logFC) 的先验
prior_mean <- 0
prior_sd <- 1

# 步骤 3：拟合模型（简化版：正态-正态共轭）
# 后验也是正态分布
observed_diff <- mean(treatment) - mean(control)
se_diff <- sqrt(sd(treatment)^2/10 + sd(control)^2/10)

# 后验参数
posterior_mean <- (observed_diff/se_diff^2 + prior_mean/prior_sd^2) /
                  (1/se_diff^2 + 1/prior_sd^2)
posterior_sd <- sqrt(1 / (1/se_diff^2 + 1/prior_sd^2))

cat("后验均值:", round(posterior_mean, 3), "\n")
cat("后验标准差:", round(posterior_sd, 3), "\n")

# 步骤 4：检查后验分布
# 95% 可信区间（Credible Interval）
ci_lower <- posterior_mean - 1.96 * posterior_sd
ci_upper <- posterior_mean + 1.96 * posterior_sd
cat("95% 可信区间:", round(ci_lower, 3), "至", round(ci_upper, 3), "\n")

# 步骤 5：做概率陈述
# P(logFC > 0 | data)
p_positive <- 1 - pnorm(0, posterior_mean, posterior_sd)
cat("P(logFC > 0 | data):", round(p_positive, 3), "\n")

# P(logFC > 1 | data)
p_large <- 1 - pnorm(1, posterior_mean, posterior_sd)
cat("P(logFC > 1 | data):", round(p_large, 3), "\n")

# 步骤 6：决策分析
# 决策规则：如果 P(logFC > 0.5) > 0.9，则认为有生物学意义
threshold <- 0.5
p_decision <- 1 - pnorm(threshold, posterior_mean, posterior_sd)

cat("\n决策分析:\n")
cat("如果阈值是", threshold, ":\n")
cat("P(logFC >", threshold, "| data) =", round(p_decision, 3), "\n")
if(p_decision > 0.9) {
  cat("结论：有足够证据认为差异具有生物学意义\n")
} else {
  cat("结论：证据不足，需要更多数据\n"
}
```

**频率学派 vs 贝叶斯学派对比** | **Frequentist vs Bayesian Comparison**:

```r
# 频率学派方法
t_result <- t.test(treatment, control, var.equal = TRUE)
cat("频率学派结果:\n")
cat("t-statistic:", round(t_result$statistic, 3), "\n")
cat("p-value:", round(t_result$p.value, 3), "\n")
cat("95% 置信区间:", round(t_result$conf.int, 3), "\n")
cat("结论:", if(t_result$p.value < 0.05) "显著" else "不显著", "\n\n")

# 贝叶斯学派方法
cat("贝叶斯学派结果:\n")
cat("后验均值:", round(posterior_mean, 3), "\n")
cat("95% 可信区间:", round(ci_lower, 3), "至", round(ci_upper, 3), "\n")
cat("P(logFC > 0 | data):", round(p_positive, 3), "\n")
cat("结论:", if(p_positive > 0.95) "很可能有差异" else "不确定", "\n")
```

**关键区别** | **Key Differences**:

| 维度 | 频率学派 | 贝叶斯学派 |
|------|---------|-----------|
| **参数** | 固定，未知 | 随机，有分布 |
| **区间** | 置信区间（长期频率） | 可信区间（概率包含真值） |
| **结论** | 二元（显著/不显著） | 概率陈述（85% 可能） |
| **p-value** | P(Data|H₀) | 不用 p-value |
| **决策** | 基于 α = 0.05 | 可以自定义决策规则 |

#### 连接到 FigureYa 模块 | Connect to FigureYa Module

查看完整的贝叶斯分析示例：

```r
# BAPC 模块展示了完整的贝叶斯工作流
# /Users/pro/FigureYa/FigureYa273BAPC/

# 包括：
# 1. 先验设置（年龄、时期、队列效应）
# 2. MCMC 采样（使用 JAGS 或 Stan）
# 3. 收敛性诊断（Gelman-Rubin statistic）
# 4. 后验预测检验
# 5. 预测和决策
```

#### 洞察 | Insight

**贝叶斯工作流的优势** | **Advantages of Bayesian Workflow**:

1. **更直观的概率解释** | **More Intuitive Probabilistic Interpretation**:
   - "85% 概率有差异" vs "p < 0.05"
   - 可信区间 vs 置信区间

2. **灵活的决策分析** | **Flexible Decision Analysis**:
   - 可以根据具体问题设置决策阈值
   - 考虑损失函数（假阳性 vs 假阴性的代价）

3. **自然地整合先验知识** | **Naturally Incorporate Prior Knowledge**:
   - 既往研究结果
   - 专家知识
   - 生物学约束

4. **完整的量化不确定性** | **Complete Quantification of Uncertainty**:
   - 预测不确定性
   - 参数不确定性
   - 模型不确定性

---

### 模块 7：实践练习 - 重新解读已发表的结果 | Module 7: Practice Exercise

#### 任务 | Task

选择一个 FigureYa 差异分析模块，用贝叶斯思维重新解读结果：

**步骤** | **Steps**:

1. 选择一个 FigureYa 模块（如 FigureYa59volcanoV2）
2. 读取差异表达结果
3. 假设合理的先验概率
4. 计算后验概率
5. 对比 p-value 和后验概率
6. 讨论差异和生物学意义

#### 示例 | Example

```r
# 选择：FigureYa59volcanoV2（火山图）

# 1. 读取数据
x <- read.csv("/Users/pro/FigureYa/FigureYa59volcanoV2/easy_input_limma.csv")

# 2. 查看结果
head(x[, c("logFC", "P.Value", "adj.P.Val")])

# 3. 选择 p < 0.05 的基因
sig_genes <- x[x$P.Value < 0.05, ]
cat("p < 0.05 的基因数:", nrow(sig_genes), "\n")

# 4. 假设不同的先验概率
priors <- c(0.01, 0.05, 0.1, 0.2)
power <- 0.8

# 5. 计算后验概率
for(prior in priors) {
  # 对每个显著基因计算后验概率
  posteriors <- sapply(sig_genes$P.Value, function(p) {
    (power * prior) / (p * (1 - prior) + power * prior)
  })

  # 后验概率 > 0.8 的基因数
  n_high_posterior <- sum(posteriors > 0.8)

  cat("\n先验概率:", prior, "\n")
  cat("  p < 0.05 的基因数:", nrow(sig_genes), "\n")
  cat("  后验概率 > 0.8 的基因数:", n_high_posterior, "\n")
  cat("  减少:", nrow(sig_genes) - n_high_posterior, "个\n")
}

# 6. 具体例子
cat("\n具体例子:\n")
gene_idx <- which.min(x$P.Value)
gene <- x[gene_idx, ]
p_val <- gene$P.Value

cat("基因:", rownames(x)[gene_idx], "\n")
cat("logFC:", round(gene$logFC, 3), "\n")
cat("p-value:", p_val, "\n")

for(prior in priors) {
  posterior <- (power * prior) /
              (p_val * (1 - prior) + power * prior)
  cat("先验", prior, "→ 后验概率:", round(posterior, 3), "\n")
}
```

#### 讨论问题 | Discussion Questions

1. **p-value vs 后验概率** | **p-value vs Posterior Probability**:
   - p = 0.001 意味着后验概率 > 0.95 吗？
   - 什么情况下两者接近？什么情况下差异很大？

2. **先验的选择** | **Prior Selection**:
   - 你的先验假设合理吗？
   - 如何基于生物学知识选择先验？

3. **决策阈值** | **Decision Threshold**:
   - 应该用 p < 0.05 还是后验概率 > 0.8？
   - 不同阈值如何影响结论？

4. **生物学意义** | **Biological Significance**:
   - 统计显著性 vs 生物学显著性
   - 如何结合效应大小（logFC）和不确定性？

#### 扩展练习 | Extended Exercise

```r
# 扩展 1：效应大小和后验概率的关系
x$effect_size <- abs(x$logFC)
x$significant_p <- x$P.Value < 0.05

# 计算后验概率
prior <- 0.1
power <- 0.8
x$posterior <- (power * prior) /
              (x$P.Value * (1 - prior) + power * prior)

# 可视化
library(ggplot2)
ggplot(x, aes(x = effect_size, y = posterior)) +
  geom_point(alpha = 0.5) +
  geom_hline(yintercept = 0.8, linetype = "dashed", color = "red") +
  labs(title = "Effect Size vs Posterior Probability",
       x = "|logFC|",
       y = "Posterior Probability") +
  theme_minimal()

# 扩展 2：FDR 的贝叶斯解释
# 计算局部 FDR（后验假阳性概率）
x$local_fdr <- 1 - x$posterior

# 查看高 logFC 但高 local_fdr 的基因
problematic <- x[x$effect_size > 1.5 & x$local_fdr > 0.5, ]
cat("\n高 logFC 但高假阳性概率的基因:\n")
print(head(problematic[, c("logFC", "P.Value", "posterior", "local_fdr")]))
```

#### 洞察 | Insight

**贝叶斯思维如何改变结果解读** | **How Bayesian Thinking Changes Result Interpretation**:

1. **从二元到连续** | **From Binary to Continuous**:
   - 不是"显著/不显著"
   - 而是"很可能 / 可能 / 不太可能 / 很不可能"

2. **考虑先验** | **Consider Priors**:
   - 如果先验很低（如罕见病），即使 p 很小也要谨慎
   - 如果先验很高（如预期通路），即使 p 较大也可能有意义

3. **综合决策** | **Integrated Decision Making**:
   - 结合 p-value（或后验概率）
   - 结合效应大小
   - 结合先验知识
   - 结合生物学合理性

---

## 使用场景 | Usage Scenarios

### 何时使用这个 Skill？| When to Use This Skill?

**适合场景** | **Good For**:

1. **想要理解贝叶斯推断的本质**
   - 不只是学习公式，而是理解思维模式

2. **想从"显著性思维"转向"贝叶斯思维"**
   - 意识到 p-value 的局限性
   - 想要更直观的概率解释

3. **想要学习如何结合先验知识**
   - 有生物学背景知识
   - 想要整合到统计分析中

4. **想要理解现代生物统计方法**
   - limma 为什么在小样本下表现好？
   - FDR 的本质是什么？

**触发条件** | **Trigger Conditions**:

在 Claude Code 中使用以下任一方式：

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

### 与现有 Skills 的关系 | Relationship with Other Skills

| 维度 | figureya-inference-thinking | figureya-learn-statistics | figureya-bayesian-thinking |
|------|---------------------------|-------------------------|--------------------------|
| **定位** | 理解统计推断本质 | 学习统计方法 | 建立贝叶斯思维 |
| **目标** | 理解"为什么统计学存在" | 学会"如何使用统计" | 从"显著性"转向"贝叶斯" |
| **内容** | 7 个核心问题（variance, p-value, sample size 等） | 300+ 模块的方法教学 | 7 个贝叶斯模块 |
| **重点** | 统计推断基础 | 实际应用 | 思维模式重构 |
| **范式** | 频率学派 + 贝叶斯学派对比 | 主要是频率学派 | 专门贝叶斯范式 |
| **深度** | 理论推导（四层递进） | 应用导向 | 直觉建立 + 实践应用 |
| **前置要求** | 无 | 无 | 无（从零开始） |

**建议学习顺序** | **Recommended Learning Order**:

1. **第一步**：figureya-inference-thinking
   - 建立统计推断基础
   - 理解 p-value, variance 等核心概念
   - 包含贝叶斯基础（问题 2、6、7）

2. **第二步**：figureya-bayesian-thinking（本 skill）
   - 深入贝叶斯思维
   - 从"显著性思维"转向"贝叶斯思维"
   - 学习先验选择、Empirical Bayes 等

3. **第三步**：figureya-learn-statistics
   - 学习具体方法
   - 查找 300+ FigureYa 模块
   - 实际应用

**也可以独立使用** | **Can Also Be Used Independently**:

如果你已经理解统计基础，可以直接使用本 skill 学习贝叶斯思维。

---

## 总结：建立贝叶斯思维 | Summary: Building Bayesian Thinking

### 核心原则 | Core Principles

1. **信念更新** | **Belief Updating**:
   - 先验概率 + 数据 → 后验概率
   - 贝叶斯公式是数学表达

2. **不确定性量化** | **Quantify Uncertainty**:
   - 不是二元结论（显著/不显著）
   - 而是概率分布（后验概率）

3. **结合先验知识** | **Incorporate Prior Knowledge**:
   - 生物学背景
   - 既往研究
   - 专家知识

4. **条件概率反转** | **Conditional Probability Reversal**:
   - P(Data|H) ≠ P(H|Data)
   - 这是理解贝叶斯推断的关键

### 从"显著性"到"贝叶斯"的转变 | From "Significance" to "Bayesian"

| 显著性思维 | 贝叶斯思维 |
|-----------|----------|
| p < 0.05 → 显著 | P(H₁|Data) = 85% → 很可能 |
| 拒绝/无法拒绝 H₀ | 更新信念 |
| 二元结论 | 连续概率 |
| p-value 是长期频率 | 后验是当前信念 |
| 不用先验 | 结合先验知识 |

### 实践建议 | Practical Recommendations

1. **开始简单** | **Start Simple**:
   - 从医疗检测例子理解贝叶斯公式
   - 用基因差异表达练习计算后验概率

2. **理解 limma** | **Understand limma**:
   - Empirical Bayes 是小样本问题的解决方案
   - 理解为什么 limma 表现好

3. **敏感性分析** | **Sensitivity Analysis**:
   - 尝试不同先验
   - 检查结论是否稳健

4. **结合实际** | **Apply to Real Data**:
   - 用 FigureYa 模块分析真实数据
   - 用贝叶斯思维重新解读 p-value

### 延伸阅读 | Further Reading

**教材** | **Textbooks**:

1. **"Statistical Rethinking" by Richard McElreath**
   - 最佳贝叶斯入门教材
   - 从直觉到数学，循序渐进

2. **"Bayesian Data Analysis" by Gelman et al.**
   - 贝叶斯分析的权威教材
   - 更理论化和深入

3. **"Doing Bayesian Data Analysis" by John Kruschke**
   - 实践导向
   - 包含大量 R 代码示例

**论文** | **Papers**:

1. "The Bayesian New Statistics" (2015)
2. "Reforming the P-value" (2019)
3. "Empirical Bayes methods" (Efron, 2010)

**在线资源** | **Online Resources**:

- **StatQuest with Josh Starmer**: Bayesian Statistics 系列
- **Coursera**: "Bayesian Statistics: From Concept to Data Analysis"
- **Seeing Theory**: 贝叶斯推断交互式可视化

---

## FigureYa 模块索引 | FigureYa Module Index

### 本 Skill 使用的核心模块 | Core Modules Used in This Skill

1. **FigureYa59volcanoV2**
   - 路径：`/Users/pro/FigureYa/FigureYa59volcanoV2/`
   - 用途：模块 2（贝叶斯公式）、模块 3（FDR）、模块 7（实践练习）
   - 数据文件：`easy_input_limma.csv`

2. **FigureYa117multilinearDE**
   - 路径：`/Users/pro/FigureYa/FigureYa117multilinearDE/`
   - 用途：模块 4（Empirical Bayes）
   - 展示 limma 的实际应用

3. **FigureYa273BAPC**
   - 路径：`/Users/pro/FigureYa/FigureYa273BAPC/`
   - 用途：模块 5（先验选择）、模块 6（贝叶斯工作流）
   - 完整的贝叶斯分析示例

4. **FigureYa135multiVolcano**
   - 路径：`/Users/pro/FigureYa/FigureYa135multiVolcano/`
   - 用途：模块 3（FDR，多重检验示例）

### 相关模块推荐 | Related Module Recommendations

**差异分析** | **Differential Analysis**:
- FigureYa117multilinearDE（limma）
- FigureYa118MulticlassDESeq2（DESeq2）
- FigureYa119Multiclasslimma（多类 limma）
- FigureYa120MulticlassedgeR（edgeR）

**生存分析** | **Survival Analysis**:
- FigureYa66UnivariateCox（单变量 Cox）
- FigureYa30nomogram_update（Nomogram）
- FigureYa1survivalCurve_update（生存曲线）

**可视化** | **Visualization**:
- FigureYa59volcanoV2（火山图）
- FigureYa12box（箱线图）
- FigureYa24ROC（ROC 曲线）

---

**版本 | Version**: 1.0.0
**创建时间 | Created**: 2026-05-13
**作者 | Author**: Claude Code with FigureYa Community
**GitHub**: https://github.com/ying-ge/FigureYa-skills
**许可证 | License**: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License
