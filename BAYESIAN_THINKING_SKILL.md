# FigureYa Bayesian Thinking Tutor Skill

## 简介 | Introduction

这是一个专门设计用来**重构思维模式**的 Claude Code skill —— 从传统的"显著性思维"（p-value < 0.05）转向"贝叶斯式的不确定性更新思维"。它不是教你"如何使用贝叶斯方法"，而是帮助你"建立贝叶斯思维"。

This is a Claude Code skill specifically designed to **restructure thinking patterns** — from traditional "significance thinking" (p-value < 0.05) to "Bayesian uncertainty updating thinking". It doesn't just teach you "how to use Bayesian methods", but helps you "build Bayesian thinking".

## 核心特点 | Key Features

### 🔄 思维模式重构 | Mindset Restructuring

从 **"显著性思维"** → **"贝叶斯式的不确定性更新思维"**

**From "Significance Thinking"** → **"Bayesian Uncertainty Updating Thinking"**

| 显著性思维 | Significance Thinking | → | 贝叶斯思维 | Bayesian Thinking |
|-----------|----------------------|---|-----------|------------------|
| 接受/拒绝假设 | Accept/Reject hypothesis | → | 更新信念分布 | Update belief distribution |
| 二元结论 | Binary conclusion | → | 连续概率 | Continuous probability |
| p-value | p-value | → | 后验概率 | Posterior probability |
| 长期频率 | Long-run frequency | → | 当前信念 | Current belief |

### 🎯 7 个核心模块 | 7 Core Modules

1. **思维模式对比**
   - 医疗检测：16.7% vs 95% 的误解
   - 理解条件概率反转：P(Data|H) ≠ P(H|Data)

2. **贝叶斯公式**
   - 从医疗检测到基因差异表达
   - 计算后验概率：P(H₁|Data) = ?

3. **FDR 的贝叶斯解释**
   - 为什么多重检验需要校正
   - FDR 作为后验假阳性率

4. **Empirical Bayes**
   - limma 的小样本魔法
   - Shrinkage 和 Borrowing strength

5. **先验选择**
   - 无信息先验 vs 有信息先验
   - 如何编码生物学知识

6. **贝叶斯工作流**
   - 从数据到决策的完整流程
   - 可信区间 vs 置信区间

7. **实践练习**
   - 重新解读已发表的结果
   - 用贝叶斯思维分析真实数据

### 📚 直觉到实践 | From Intuition to Practice

- **从直观例子开始**：医疗检测的误解（16.7% vs 95%）
- **建立贝叶斯直觉**：理解信念更新和条件概率反转
- **应用到基因表达**：计算基因差异表达的后验概率
- **连接实际工具**：limma、FDR、完整贝叶斯分析

### 🔗 连接真实工具 | Connect to Real Tools

- **FigureYa59volcanoV2**：火山图（p-value vs 后验概率）
- **FigureYa117multilinearDE**：limma Empirical Bayes
- **FigureYa273BAPC**：完整贝叶斯分析示例

## 为什么需要贝叶斯思维？| Why Bayesian Thinking?

### 当前问题 | Current Problem

大多数生物医学研究者被训练成"显著性思维"：

❌ **常见误解** | **Common Misconceptions**:
1. p = 0.03 = "97% 概率真的有差异"
2. p < 0.05 = "显著"（不需要进一步思考）
3. 忽视先验信息和生物学背景
4. 无法回答："这个基因**真的**有差异的概率是多少？"

### 贝叶斯思维的优势 | Bayesian Thinking Advantages

✅ **直接回答** | **Direct Answer**:
- 频率学派：p = 0.03（P(Data|H₀)，不是我们想要的）
- 贝叶斯学派：P(H₁|Data) = 85%（这就是我们想要的！）

✅ **结合先验知识** | **Incorporate Prior Knowledge**:
- 生物学背景
- 既往研究结果
- 领域专家知识

✅ **不确定性量化** | **Quantify Uncertainty**:
- 不是二元结论（显著/不显著）
- 而是概率分布（85% 可能，15% 不可能）

✅ **信念更新** | **Belief Updating**:
- 从先验概率 → 数据 → 后验概率
- 符合人类自然推理方式

## 使用方法 | Usage

### 触发场景 | Trigger Scenarios

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
小样本时如何稳定估计？
```

```
用 figureya-bayesian-thinking 帮我理解贝叶斯推断
```

### 学习路径 | Learning Path

**推荐顺序** | **Recommended Order**:

1. **第一次使用**：从模块 1 开始，按顺序学习
2. **理解贝叶斯公式**：模块 1-2 建立基础直觉
3. **深入应用**：模块 3-5 理解 FDR、Empirical Bayes、先验选择
4. **实践验证**：模块 6-7 学习完整工作流并分析真实数据

**时间投入** | **Time Investment**:

- **快速浏览**：2-3 小时（理解思维模式对比）
- **深入理解**：6-8 小时（包含所有 7 个模块）
- **完全掌握**：12-15 小时（包含代码实践和反思）

**前置要求** | **Prerequisites**:

- ✅ **零基础友好**！不需要统计学背景
- 📚 建议先了解 figureya-inference-thinking（统计推断基础）
- 💻 基础 R 语言知识（会运行代码即可）

## 与其他 Skills 的关系 | Relationship with Other Skills

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

## 核心模块详解 | Core Modules Detailed

### 模块 1：思维模式对比 | Module 1: Thinking Pattern Comparison

**"显著" vs "可能多大"** | **"Significant" vs "How Likely"**

#### 核心问题 | Core Question

为什么 p < 0.05 不意味着 95% 概率为真？

Why does p < 0.05 NOT mean 95% probability it's true?

#### 学习内容 | Learning Content

1. **医疗检测的误解** | **Medical Testing Misconception**:
   - 患病率 1%，检测灵敏度 99%，假阳性率 5%
   - 检测阳性 → 真实患病概率只有 16.7%，不是 95%！

2. **条件概率的反转** | **Conditional Probability Reversal**:
   - P(阳性|有病) = 99% ≠ P(有病|阳性) = 16.7%
   - P(Data|H₀) ≠ P(H₀|Data)

3. **先验信息的重要性** | **Importance of Prior Information**:
   - 患病率 1% 是关键先验信息
   - 忽视先验会导致严重误解

#### 实践练习 | Practice Exercise

```r
# 计算医疗检测的后验概率
prevalence <- 0.01
sensitivity <- 0.99
false_positive <- 0.05

p_disease_given_positive <- (sensitivity * prevalence) /
  (sensitivity * prevalence + false_positive * (1 - prevalence))

# 结果：16.7%
```

---

### 模块 2：贝叶斯公式 | Module 2: Bayes' Formula

**从医疗检测到基因表达** | **From Medical Testing to Gene Expression**

#### 核心问题 | Core Question

如何回答："这个基因**真的**有差异的概率是多少？"

How to answer: "What's the probability this gene **truly** has a difference?"

#### 学习内容 | Learning Content

1. **贝叶斯公式推导** | **Bayes' Formula Derivation**:
   $$P(H_1|Data) = \frac{P(Data|H_1) \times P(H_1)}{P(Data|H_0) \times P(H_0) + P(Data|H_1) \times P(H_1)}$$

2. **应用到基因差异表达** | **Apply to Gene Differential Expression**:
   - p-value = 0.03（P(Data|H₀)）
   - 先验概率 = 10%（假设 10% 基因有差异）
   - 统计功效 = 80%（P(Data|H₁)）
   - 后验概率 = 73.6%（不是 97%！）

3. **不同先验的影响** | **Effect of Different Priors**:
   - 先验 1% → 后验 21.2%
   - 先验 10% → 后验 73.6%
   - 先验 50% → 后验 93.0%

#### 实践练习 | Practice Exercise

```r
# 计算基因差异表达的后验概率
p_value <- 0.03
prior_h1 <- 0.1
power <- 0.8

p_h1_given_data <- (power * prior_h1) /
  (p_value * (1 - prior_h1) + power * prior_h1)

# 结果：73.6%
```

---

### 模块 3：FDR 的贝叶斯解释 | Module 3: Bayesian FDR

**为什么多重检验需要校正？** | **Why Multiple Testing Needs Correction?**

#### 核心问题 | Core Question

为什么在 20000 个基因中，p < 0.05 不可靠？

Why is p < 0.05 unreliable among 20,000 genes?

#### 学习内容 | Learning Content

1. **假阳性累积** | **False Positive Accumulation**:
   - 单次检验：5% 假阳性
   - 20000 次检验：约 1000 个假阳性（即使所有基因都无差异）

2. **FDR 的贝叶斯解释** | **Bayesian Interpretation of FDR**:
   $$FDR \approx \frac{\text{prior} \times \alpha}{\text{prior} \times \text{power} + (1-\text{prior}) \times \alpha}$$
   - FDR 本质上是**后验假阳性率**
   - 先验 1% → FDR = 38.4%（在显著基因中，38.4% 可能是假阳性！）

3. **先验概率的影响** | **Effect of Prior Probability**:
   - 先验越低（真实差异基因越少）→ FDR 越高
   - 这符合直觉：如果大海捞针，找到的"石头"会很多

#### 实践练习 | Practice Exercise

```r
# 计算 FDR
alpha <- 0.05
prior <- 0.01
power <- 0.8

fdr_bayesian <- (prior * alpha) /
               (prior * power + (1 - prior) * alpha)

# 结果：38.4%

# 对比 BH 方法的 FDR 校正
x <- read.csv("easy_input_limma.csv")
sig_raw <- sum(x$P.Value < 0.05)
sig_adj <- sum(x$adj.P.Val < 0.05)
```

---

### 模块 4：Empirical Bayes | Module 4: Empirical Bayes

**limma 的小样本魔法** | **limma's Small Sample Magic**

#### 核心问题 | Core Question

如何在只有 3 个重复时稳定估计方差？

How to stabilize variance estimation with only 3 replicates?

#### 学习内容 | Learning Content

1. **小样本问题** | **Small Sample Problem**:
   - 方差估计不稳定
   - p-value 波动很大
   - 假阳性和假阴性增加

2. **Empirical Bayes 解决方案** | **Empirical Bayes Solution**:
   - 从所有基因学习**先验**方差分布
   - 用先验收缩每个基因的方差估计
   - 得到更稳定的 t 统计量

3. **核心概念** | **Core Concepts**:
   - **Borrowing strength**：用所有基因的信息改善单个基因的估计
   - **Shrinkage**：极端方差估计向全局均值收缩
   - **为什么 limma 在小样本下表现好**

#### 实践练习 | Practice Exercise

```r
# limma 自动应用 Empirical Bayes
library(limma)

# 标准流程：
# 1. fit <- lmFit(expr_data, design)
# 2. fit <- eBayes(fit)  # ← 这里应用 Empirical Bayes！
# 3. topTable(fit)

# 查看 moderated t-statistic（更稳定的 t 统计量）
```

---

### 模块 5：先验选择 | Module 5: Prior Selection

**如何编码生物学知识？** | **How to Encode Biological Knowledge?**

#### 核心问题 | Core Question

如何客观地选择先验？

How to objectively select priors?

#### 学习内容 | Learning Content

1. **先验类型** | **Types of Priors**:
   - **无信息先验**：让数据说话，但可能不稳定
   - **弱信息先验**【推荐】：提供正则化，但不强
   - **有信息先验**：结合既往研究，但需要透明

2. **先验选择原则** | **Prior Selection Principles**:
   - 基于科学知识
   - 透明报告选择理由
   - 做敏感性分析

3. **敏感性分析** | **Sensitivity Analysis**:
   - 尝试不同先验
   - 检查结论是否稳健
   - 如果结论改变 → 需要更多数据

#### 实践练习 | Practice Exercise

```r
# 比较不同先验的影响
priors <- c(0.01, 0.05, 0.1, 0.2)
for(prior in priors) {
  posterior <- (power * prior) /
              (p_value * (1 - prior) + power * prior)
  cat("Prior", prior, "→ Posterior", round(posterior, 3), "\n")
}
```

---

### 模块 6：贝叶斯工作流 | Module 6: Bayesian Workflow

**从数据到决策** | **From Data to Decision**

#### 核心问题 | Core Question

贝叶斯分析与频率学派分析有什么不同？

How does Bayesian analysis differ from frequentist analysis?

#### 学习内容 | Learning Content

1. **贝叶斯工作流步骤** | **Bayesian Workflow Steps**:
   - 数据准备
   - 设置先验
   - 拟合模型（MCMC 或解析解）
   - 检查后验分布
   - 做概率陈述
   - 决策分析

2. **关键区别** | **Key Differences**:
   - **参数**：固定（频率）vs 随机（贝叶斯）
   - **区间**：置信区间 vs 可信区间
   - **结论**：二元（显著/不显著）vs 概率（85% 可能）
   - **p-value**：P(Data|H₀) vs 不用 p-value

3. **优势** | **Advantages**:
   - 更直观的概率解释
   - 灵活的决策分析
   - 自然地整合先验知识
   - 完整的量化不确定性

#### 实践练习 | Practice Exercise

```r
# 简化的贝叶斯工作流
# 1. 计算后验分布
posterior_mean <- (observed_diff/se^2 + prior_mean/prior_sd^2) /
                  (1/se^2 + 1/prior_sd^2)

# 2. 95% 可信区间
ci_lower <- posterior_mean - 1.96 * posterior_sd
ci_upper <- posterior_mean + 1.96 * posterior_sd

# 3. 做概率陈述
p_positive <- 1 - pnorm(0, posterior_mean, posterior_sd)

# 4. 决策分析
if(p_positive > 0.9) {
  "有足够证据认为有差异"
}
```

---

### 模块 7：实践练习 | Module 7: Practice Exercises

**重新解读已发表的结果** | **Re-interpret Published Results**

#### 核心任务 | Core Task

选择一个 FigureYa 差异分析模块，用贝叶斯思维重新解读结果。

Select a FigureYa differential analysis module and re-interpret results with Bayesian thinking.

#### 实践步骤 | Practice Steps

1. 选择一个 FigureYa 模块（如 FigureYa59volcanoV2）
2. 读取差异表达结果
3. 假设合理的先验概率
4. 计算后验概率
5. 对比 p-value 和后验概率
6. 讨论差异和生物学意义

#### 扩展练习 | Extended Exercises

1. **效应大小和后验概率的关系**：
   - 高 logFC 但高假阳性的基因
   - 可视化效应大小 vs 后验概率

2. **FDR 的贝叶斯解释**：
   - 计算局部 FDR（后验假阳性概率）
   - 理解为什么 FDR 校正很重要

3. **敏感性分析**：
   - 尝试不同先验
   - 检查结论是否稳健

#### 实践代码 | Practice Code

```r
# 读取数据
x <- read.csv("easy_input_limma.csv")

# 计算后验概率
prior <- 0.1
power <- 0.8
x$posterior <- (power * prior) /
              (x$P.Value * (1 - prior) + power * prior)

# 对比
sig_raw <- sum(x$P.Value < 0.05)
sig_posterior <- sum(x$posterior > 0.8)

cat("p < 0.05:", sig_raw, "\n")
cat("后验 > 0.8:", sig_posterior, "\n")
```

## 学习成果 | Learning Outcomes

完成这个 skill 后，你将能够：

After completing this skill, you will be able to:

✅ **解释贝叶斯思维的价值**
   - 为什么需要从"显著性思维"转向"贝叶斯思维"
   - 贝叶斯思维如何改变结果解读

✅ **区分 p-value 和后验概率**
   - P(Data|H₀) ≠ P(H₀|Data)
   - p = 0.03 ≠ 97% 概率为真

✅ **计算简单的后验概率**
   - 使用贝叶斯公式
   - 理解先验、似然、后验的关系

✅ **理解 FDR 的贝叶斯解释**
   - FDR 作为后验假阳性率
   - 先验概率对 FDR 的影响

✅ **解释 limma 的 Empirical Bayes**
   - 为什么 limma 在小样本下表现好
   - Shrinkage 和 Borrowing strength

✅ **讨论先验选择的影响**
   - 不同先验类型
   - 敏感性分析

✅ **建立"不确定性更新"的贝叶斯思维**
   - 信念更新：先验 → 数据 → 后验
   - 量化不确定性：概率分布而非二元结论

✅ **用贝叶斯思维重新解读 p-value 结果**
   - 结合先验知识
   - 计算后验概率
   - 做更合理的决策

## 适用人群 | Target Audience

### 非常适合 | Highly Suitable For

- 🎓 **生物医学研究生**：想建立正确的统计思维
- 🔬 **研究人员**：想深入理解统计方法
- 📊 **数据分析师**：想学习贝叶斯方法
- 🧠 **对统计学有好奇心的人**：想超越 p-value，理解贝叶斯推断

### 需要基础 | Prerequisites

**零基础友好！** No prerequisites needed!

但如果有以下背景会理解更深：
- 建议先了解 figureya-inference-thinking（统计推断基础）
- 基础概率论（概率、条件概率）
- R 语言基础（会运行代码即可）

## 延伸阅读 | Further Reading

### 经典教材 | Classic Textbooks

1. **"Statistical Rethinking" by Richard McElreath**
   - 最佳贝叶斯入门教材
   - 从直觉到数学，循序渐进
   - 包含大量 R 代码示例

2. **"Bayesian Data Analysis" by Gelman et al.**
   - 贝叶斯分析的权威教材
   - 更理论化和深入

3. **"Doing Bayesian Data Analysis" by John Kruschke**
   - 实践导向
   - 包含大量 R 代码示例

### 重要论文 | Important Papers

1. "The Bayesian New Statistics" (2015)
2. "Reforming the P-value" (2019)
3. "Empirical Bayes methods" (Efron, 2010)

### 在线资源 | Online Resources

- **StatQuest with Josh Starmer**: Bayesian Statistics 系列（YouTube）
- **Coursera**: "Bayesian Statistics: From Concept to Data Analysis"
- **Seeing Theory**: 贝叶斯推断交互式可视化

## 常见问题 | FAQ

### Q: 这个 skill 适合我吗？

**A**: 如果你符合以下任一条件，这个 skill 适合你：
- 想理解贝叶斯推断的本质
- 知道 p < 0.05 但不理解其真正含义
- 想从"显著性思维"转向"贝叶斯思维"
- 想学习如何结合先验知识
- 想理解 limma 为什么在小样本下表现好

### Q: 需要多长时间才能学完？

**A**:
- **快速浏览**：2-3 小时（理解思维模式对比）
- **深入理解**：6-8 小时（包含所有 7 个模块）
- **完全掌握**：12-15 小时（包含代码实践和反思）

建议分多次学习，每次深入 1-2 个模块。

### Q: 需要数学基础吗？

**A**: 不需要！这个 skill 是"从零开始"的：
- 模块 1-2：完全不用复杂公式
- 模块 3-5：引入公式，但会详细推导
- 模块 6-7：实践应用和深入理论

### Q: 与大学的统计课程有什么区别？

**A**:
| 大学课程 | 这个 skill |
|---------|-----------|
| 从公式开始 | 从直觉和例子开始 |
| 强调计算 | 强调思维模式 |
| 抽象理论 | 生物医学实例 |
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

## 技术细节 | Technical Details

### 核心模块 | Core Modules

1. **FigureYa59volcanoV2**（主要模块）
   - 路径：`/Users/pro/FigureYa/FigureYa59volcanoV2/`
   - 数据文件：`easy_input_limma.csv`
   - 用途：模块 2、3、7

2. **FigureYa117multilinearDE**
   - 路径：`/Users/pro/FigureYa/FigureYa117multilinearDE/`
   - 用途：模块 4（Empirical Bayes）

3. **FigureYa273BAPC**
   - 路径：`/Users/pro/FigureYa/FigureYa273BAPC/`
   - 用途：模块 5、6（先验选择、贝叶斯工作流）

### 文件信息 | File Information

- **主 skill 文件**：`~/.claude/skills/figureya-bayesian-thinking.md`
- **文件大小**：约 19KB
- **行数**：约 600 行
- **语言**：中英双语
- **代码示例**：30+ 个 R 代码块
- **数学公式**：10+ 个 LaTeX 公式

## 许可证 | License

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License

---

**版本 | Version**: 1.0.0
**创建时间 | Created**: 2026-05-13
**作者 | Author**: Claude Code with FigureYa Community
**GitHub**: https://github.com/ying-ge/FigureYa-skills
