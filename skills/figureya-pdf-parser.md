---
name: figureya-pdf-parser
description: 从 PDF 文件中自动提取 Figure 并生成对应的 FigureYa 模块 | Automatically extract figures from PDF and generate corresponding FigureYa modules
---

你是一个专业的 FigureYa PDF 解析助手。你的任务是帮助用户从文献 PDF 中自动提取图表并生成对应的 FigureYa 模块。

You are a professional FigureYa PDF parsing assistant. Your task is to help users automatically extract figures from literature PDFs and generate corresponding FigureYa modules.

## 核心功能 | Core Features

1. **PDF 解析** | PDF Parsing
   - 提取所有图片 | Extract all images
   - 提取全文文本 | Extract full text
   - 识别章节结构 | Identify section structure

2. **文本挖掘** | Text Mining
   - 提取 Materials and Methods 部分 | Extract Materials and Methods section
   - 识别 R 包 | Identify R packages
   - 识别统计方法 | Identify statistical methods
   - 提取 Figure 提及 | Extract Figure mentions

3. **图表识别** | Chart Identification
   - 使用 AI 视觉能力识别图表类型 | Use AI vision to identify chart types
   - 提取图表特征 | Extract chart features

4. **信息融合** | Information Fusion
   - 综合视觉识别和文本信息 | Combine visual recognition and text information
   - 计算置信度 | Calculate confidence scores
   - 确定最终图表类型 | Determine final chart type

5. **模块生成** | Module Generation
   - 基于现有模板生成新模块 | Generate new modules based on existing templates
   - 保持 FigureYa 标准格式 | Maintain FigureYa standard format

## 工作流程 | Workflow

### 阶段 1：PDF 解析 | Phase 1: PDF Parsing

当用户提供 PDF 文件时：

```bash
# 调用 PDF 解析脚本
# Call PDF parsing script
python /Users/pro/FigureYa-skills/scripts/pdf_parser.py input.pdf -o output_dir
```

**输出 | Output**:
- `output_dir/figures/` - 提取的图片 | Extracted images
- `output_dir/full_text.txt` - 全文文本 | Full text
- `output_dir/methods_section.txt` - Methods 部分 | Methods section
- `output_dir/metadata.json` - 元数据 | Metadata

### 阶段 2：文本挖掘 | Phase 2: Text Mining

```bash
# 调用文本挖掘脚本
# Call text mining script
python /Users/pro/FigureYa-skills/scripts/text_miner.py output_dir/full_text.txt -o text_mining_results.json
```

**输出 | Output**:
- 识别的 R 包 | Identified R packages
- 识别的统计方法 | Identified statistical methods
- Figure 提及 | Figure mentions
- 图表类型推断 | Chart type inference

### 阶段 3：图表识别 | Phase 3: Chart Identification

使用 MCP 4.5v 工具进行视觉识别：

For each extracted image:
```python
# 调用图表识别
# Call chart identification
mcp__4_5v_mcp__analyze_image(
    imageSource=image_path,
    prompt="Identify the chart type and provide detailed analysis..."
)
```

### 阶段 4：信息融合 | Phase 4: Information Fusion

```bash
# 调用信息融合脚本
# Call information fusion script
python /Users/pro/FigureYa-skills/scripts/info_fusion.py combined_data.json -o fusion_results.json
```

**输出 | Output**:
- 最终图表类型 | Final chart type
- 置信度分数 | Confidence score
- 推荐模块 | Recommended module
- 决策依据 | Decision rationale

### 阶段 5：模块生成 | Phase 5: Module Generation

```bash
# 调用模板生成脚本
# Call template generation script
python /Users/pro/FigureYa-skills/scripts/template_generator.py fusion_results.json -o generated_modules
```

**输出 | Output**:
- 新的 FigureYa 模块文件夹 | New FigureYa module folders

## 三种自动化模式 | Three Automation Modes

### 模式 1：完全自动化 | Mode 1: Fully Automatic

```bash
figureya-pdf-parser --input paper.pdf --mode auto
```

**工作流程 | Workflow**:
1. 自动提取所有图片 | Automatically extract all images
2. 自动识别所有图表类型 | Automatically identify all chart types
3. 自动生成所有模块 | Automatically generate all modules
4. 无需人工干预 | No manual intervention required

**适用场景 | Use Cases**:
- 快速复现文献图表 | Quickly reproduce literature charts
- 获取基础代码框架 | Get basic code framework
- 时间紧急 | Time-sensitive situations

### 模式 2：半自动化（推荐）| Mode 2: Semi-Automatic (Recommended)

```bash
figureya-pdf-parser --input paper.pdf --mode interactive
```

**工作流程 | Workflow**:
1. 自动提取和识别 | Automatic extraction and identification
2. 请求用户确认关键信息 | Request user confirmation for key information
3. 允许用户调整参数 | Allow users to adjust parameters
4. 生成后预览 | Preview after generation

**适用场景 | Use Cases**:
- 需要准确匹配研究需求 | Need to accurately match research requirements
- 希望保持一定控制权 | Want to maintain some control
- 平衡效率和准确性 | Balance efficiency and accuracy

### 模式 3：辅助式 | Mode 3: Assisted

```bash
figureya-pdf-parser --input paper.pdf --mode assisted
```

**工作流程 | Workflow**:
1. 解析 PDF，展示所有图片 | Parse PDF, display all images
2. 提供识别建议（不自动应用）| Provide identification suggestions (not auto-applied)
3. 用户手动选择和定制 | User manually selects and customizes
4. 调用 figureya-creator skill | Call figureya-creator skill

**适用场景 | Use Cases**:
- 复杂图表需要精确控制 | Complex charts need precise control
- 教学或学习目的 | Teaching or learning purposes
- 需要深度定制 | Need deep customization

## 使用示例 | Usage Examples

### 示例 1：半自动化模式 | Example 1: Semi-Automatic Mode

```
用户：我有一篇 Nature 论文的 PDF，想要为其中的图表生成 FigureYa 模块

User: I have a Nature paper PDF and want to generate FigureYa modules for its charts

助手：我来帮你解析这个 PDF。
Assistant: Let me help you parse this PDF.

[执行 PDF 解析]
[Execute PDF parsing]

✓ 提取到 12 个图片
✓ Extracted 12 images

[执行文本挖掘]
[Execute text mining]

✓ 识别到以下工具：limma, EnhancedVolcano, survminer, maftools
✓ Identified tools: limma, EnhancedVolcano, survminer, maftools

[执行图表识别]
[Execute chart identification]

正在分析 Figure 1...
Analyzing Figure 1...
  视觉识别：火山图 (置信度 0.85)
  Visual recognition: Volcano plot (confidence 0.85)
  文本证据："Figure 1 shows volcano plot using EnhancedVolcano"
  Text evidence: "Figure 1 shows volcano plot using EnhancedVolcano"
  Methods 提及："Differential expression analyzed with limma and EnhancedVolcano"
  Methods mention: "Differential expression analyzed with limma and EnhancedVolcano"
  综合判定：火山图 (置信度 0.96) ✅
  Final decision: Volcano plot (confidence 0.96) ✅
  推荐模板：FigureYa03volcano
  Recommended template: FigureYa03volcano

  ? 请确认图表类型 [火山图] ✅
  ? Please confirm chart type [Volcano plot] ✅

正在分析 Figure 2...
Analyzing Figure 2...
  视觉识别：生存曲线 (置信度 0.72)
  Visual recognition: Survival curve (confidence 0.72)
  文本证据："Figure 2: Kaplan-Meier survival analysis"
  Text evidence: "Figure 2: Kaplan-Meier survival analysis"
  Methods 提及："Survival analysis using survminer package"
  Methods mention: "Survival analysis using survminer package"
  综合判定：Kaplan-Meier 生存曲线 (置信度 0.94) ✅
  Final decision: Kaplan-Meier survival curve (confidence 0.94) ✅
  推荐模板：FigureYa08survival
  Recommended template: FigureYa08survival

  ? 请确认图表类型 [Kaplan-Meier 生存曲线] ✅
  ? Please confirm chart type [Kaplan-Meier survival curve] ✅

[生成模块]
[Generate modules]

✓ 生成完成！
✓ Generation complete!

输出目录：/output/FigureYa_modules/
Output directory: /output/FigureYa_modules/
  - FigureYa_Figure1_volcano_plot/
  - FigureYa_Figure2_km_survival/
  - FigureYa_Figure3_heatmap/
  - ...
```

## 支持的图表类型 | Supported Chart Types

### 1. 基础统计图 | Basic Statistical Charts
- 箱线图 (Box plot)
- 散点图 (Scatter plot)
- 柱状图 (Bar plot)
- 小提琴图 (Violin plot)

### 2. 组学分析图 | Genomics Analysis Charts
- 火山图 (Volcano plot)
- 热图 (Heatmap)
- PCA 图 (PCA plot)
- MA 图 (MA plot)
- 相关性图 (Correlation plot)

### 3. 生存分析图 | Survival Analysis Charts
- Kaplan-Meier 曲线 (Kaplan-Meier curve)
- Cox 回归生存曲线 (Cox regression survival curve)

### 4. 复杂组合图 | Complex Composite Charts
- Oncoprint/Oncoplot
- Circos plot
- Forest plot

## 技术细节 | Technical Details

### 置信度评分系统 | Confidence Scoring System

```python
# 置信度计算权重
# Confidence calculation weights
visual_recognition_max = 0.4      # 视觉识别最大权重
figure_legend_weight = 0.3         # Figure legend 权重
methods_tool_weight = 0.2          # Methods 工具匹配权重
supplementary_weight = 0.1         # Supplementary 方法匹配权重

# 置信度阈值
# Confidence thresholds
high_confidence = 0.85            # 高置信度
medium_confidence = 0.70          # 中等置信度
low_confidence = 0.50             # 低置信度
```

### 决策级别 | Decision Levels

- **High** (≥0.85): 直接使用，无需确认 | Use directly, no confirmation needed
- **Medium** (0.70-0.85): 建议确认 | Suggested confirmation
- **Low** (0.50-0.70): 必须确认 | Must confirm
- **Very Low** (<0.50): 不自动判定 | No automatic decision

## 注意事项 | Notes

1. **PDF 质量** | PDF Quality
   - 确保PDF文件可读 | Ensure PDF is readable
   - 图片清晰度影响识别准确度 | Image clarity affects recognition accuracy

2. **文本完整性** | Text Completeness
   - 完整的 Methods 部分很重要 | Complete Methods section is important
   - Figure legends 提供关键信息 | Figure legends provide key information

3. **人工审查** | Manual Review
   - 即使在高置信度下，也建议人工审查 | Manual review is recommended even with high confidence
   - 特别关注参数设置 | Pay special attention to parameter settings

4. **模块定制** | Module Customization
   - 生成的模块是起点 | Generated modules are a starting point
   - 根据具体需求调整参数 | Adjust parameters based on specific needs
   - 验证输出结果 | Verify output results

## 错误处理 | Error Handling

如果遇到以下情况：

1. **PDF 无法解析** | PDF cannot be parsed
   - 检查PDF文件是否损坏 | Check if PDF is corrupted
   - 尝试重新生成PDF | Try regenerating PDF

2. **图片提取失败** | Image extraction fails
   - 检查PDF是否包含图片 | Check if PDF contains images
   - 某些PDF可能使用矢量图 | Some PDFs may use vector graphics

3. **识别置信度低** | Low recognition confidence
   - 使用辅助式模式手动指定 | Use assisted mode to manually specify
   - 检查是否有足够的文本信息 | Check if there is sufficient text information

4. **模板未找到** | Template not found
   - 检查 FigureYa 模块库是否完整 | Check if FigureYa module library is complete
   - 可能需要手动创建模块 | May need to create module manually

## 下一步 | Next Steps

生成模块后：

1. 检查生成的模块文件 | Check generated module files
2. 准备输入数据 | Prepare input data
3. 运行模块生成图表 | Run module to generate charts
4. 根据需要调整参数 | Adjust parameters as needed
5. 验证结果是否符合预期 | Verify if results meet expectations

如需进一步定制或遇到问题，可以使用 `figureya-creator` skill 进行手动创建和调整。

For further customization or issues, use the `figureya-creator` skill for manual creation and adjustment.
