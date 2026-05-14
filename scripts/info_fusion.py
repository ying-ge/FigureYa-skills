#!/usr/bin/env python3
"""
信息融合脚本 - 综合视觉识别和文本信息
Information Fusion - Combine visual recognition and text information

功能 | Features:
- 融合视觉识别和文本挖掘结果 | Fuse visual recognition and text mining results
- 计算置信度 | Calculate confidence scores
- 确定最终图表类型 | Determine final chart type
- 提供决策依据 | Provide decision rationale
"""

import json
import yaml
from typing import Dict, List, Any
from pathlib import Path


class InfoFusion:
    """信息融合类 | Information Fusion class"""

    def __init__(self, chart_config_path: str = None, method_config_path: str = None):
        """
        初始化信息融合器
        Initialize information fusion

        参数 | Parameters:
            chart_config_path: 图表类型配置文件路径 | Chart type config file path
            method_config_path: 方法关键词配置文件路径 | Method keywords config file path
        """
        self.chart_config = self._load_config(chart_config_path, "chart_type_mapping.yaml")
        self.method_config = self._load_config(method_config_path, "method_keywords.yaml")
        self.weights = self.method_config.get("confidence_weights", {})

    def _load_config(self, config_path: str, default_name: str) -> Dict:
        """
        加载配置文件
        Load configuration file

        参数 | Parameters:
            config_path: 配置文件路径 | Configuration file path
            default_name: 默认文件名 | Default file name

        返回 | Returns:
            配置字典 | Configuration dictionary
        """
        if config_path is None:
            # 默认路径
            # Default path
            base_dir = Path(__file__).parent.parent
            config_path = base_dir / default_name

        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def calculate_confidence(self, figure_data: Dict[str, Any]) -> Dict[str, float]:
        """
        计算图表类型识别的置信度
        Calculate confidence for chart type identification

        参数 | Parameters:
            figure_data: 包含视觉识别和文本挖掘数据的字典
                        Dictionary containing visual recognition and text mining data

        返回 | Returns:
            置信度分数字典 | Confidence score dictionary
        """
        visual_recognition = figure_data.get("visual_recognition", {})
        text_mining = figure_data.get("text_mining", {})
        figure_info = figure_data.get("figure_info", {})

        scores = {}

        # 遍历所有可能的图表类型
        # Iterate through all possible chart types
        all_chart_types = self._get_all_chart_types()

        for chart_type in all_chart_types:
            score = 0.5  # 基础分 | Base score

            # 1. 视觉识别分数
            # Visual recognition score
            visual_confidence = visual_recognition.get("confidence", 0)
            if visual_confidence > 0:
                visual_weight = self.weights.get("visual_recognition", {}).get("max", 0.4)
                score += visual_confidence * visual_weight

            # 2. Figure legend 提及
            # Figure legend mention
            figure_num = figure_info.get("figure_number", "")
            if figure_num:
                legend_text = text_mining.get("figure_mentions", {}).get(f"Figure {figure_num}", [])
                if legend_text:
                    legend_weight = self.weights.get("text_mention", {}).get("figure_legend", 0.3)
                    score += legend_weight

            # 3. Methods 中的工具匹配
            # Tool match in Methods
            mentioned_packages = text_mining.get("r_packages", [])
            chart_packages = self._get_chart_packages(chart_type)

            for pkg in mentioned_packages:
                if pkg.lower() in [p.lower() for p in chart_packages]:
                    methods_weight = self.weights.get("methods_section", {}).get("tool_match", 0.2)
                    score += methods_weight
                    break

            # 4. 文本中的图表类型匹配
            # Chart type match in text
            text_scores = text_mining.get("chart_type_scores", {})
            if chart_type in text_scores:
                text_confidence = text_scores[chart_type].get("confidence", 0)
                supplementary_weight = self.weights.get("supplementary", {}).get("method_match", 0.1)
                score += text_confidence * supplementary_weight

            scores[chart_type] = min(score, 1.0)

        return scores

    def _get_all_chart_types(self) -> List[str]:
        """
        获取所有图表类型
        Get all chart types

        返回 | Returns:
            图表类型列表 | Chart type list
        """
        types = []
        for category in self.chart_config.values():
            if isinstance(category, dict) and "synonyms" not in str(category):
                for chart_type, chart_info in category.items():
                    if isinstance(chart_info, dict) and "name" in chart_info:
                        types.append(chart_type)
        return types

    def _get_chart_packages(self, chart_type: str) -> List[str]:
        """
        获取图表类型对应的 R 包
        Get R packages for chart type

        参数 | Parameters:
            chart_type: 图表类型 | Chart type

        返回 | Returns:
            R 包列表 | R package list
        """
        for category in self.chart_config.values():
            if isinstance(category, dict) and chart_type in category:
                return category[chart_type].get("r_packages", [])
        return []

    def determine_chart_type(self, figure_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        融合信息并确定最终图表类型
        Fuse information and determine final chart type

        参数 | Parameters:
            figure_data: 包含所有相关数据的字典
                        Dictionary containing all relevant data

        返回 | Returns:
            包含最终判定和依据的字典
            Dictionary containing final decision and rationale
        """
        # 计算置信度
        # Calculate confidence
        confidence_scores = self.calculate_confidence(figure_data)

        # 找到最高分的图表类型
        # Find highest scoring chart type
        best_chart_type = max(confidence_scores, key=confidence_scores.get)
        best_score = confidence_scores[best_chart_type]

        # 收集证据
        # Collect evidence
        evidence = self._collect_evidence(figure_data, best_chart_type)

        # 确定推荐模块
        # Determine recommended module
        recommended_module = self._get_recommended_module(best_chart_type)

        result = {
            "chart_type": best_chart_type,
            "confidence": best_score,
            "evidence": evidence,
            "recommended_module": recommended_module,
            "all_scores": confidence_scores,
            "decision_level": self._get_decision_level(best_score)
        }

        return result

    def _collect_evidence(self, figure_data: Dict[str, Any], chart_type: str) -> Dict[str, Any]:
        """
        收集决策证据
        Collect decision evidence

        参数 | Parameters:
            figure_data: 数据字典 | Data dictionary
            chart_type: 图表类型 | Chart type

        返回 | Returns:
            证据字典 | Evidence dictionary
        """
        visual_recognition = figure_data.get("visual_recognition", {})
        text_mining = figure_data.get("text_mining", {})
        figure_info = figure_data.get("figure_info", {})

        evidence = {
            "visual": {
                "identified_type": visual_recognition.get("chart_type", "Unknown"),
                "confidence": visual_recognition.get("confidence", 0)
            },
            "text": {
                "figure_mentions": [],
                "r_packages": [],
                "methods": []
            },
            "package_match": []
        }

        # Figure legend 提及
        # Figure legend mentions
        figure_num = figure_info.get("figure_number", "")
        if figure_num:
            mentions = text_mining.get("figure_mentions", {}).get(f"Figure {figure_num}", [])
            evidence["text"]["figure_mentions"] = mentions

        # R 包匹配
        # R package matching
        mentioned_packages = text_mining.get("r_packages", [])
        chart_packages = self._get_chart_packages(chart_type)

        for pkg in mentioned_packages:
            if pkg.lower() in [p.lower() for p in chart_packages]:
                evidence["package_match"].append(pkg)

        evidence["text"]["r_packages"] = mentioned_packages

        # 统计方法
        # Statistical methods
        evidence["text"]["methods"] = text_mining.get("statistical_methods", {})

        return evidence

    def _get_recommended_module(self, chart_type: str) -> Dict[str, Any]:
        """
        获取推荐的 FigureYa 模块（增强版）
        Get recommended FigureYa module (enhanced)

        参数 | Parameters:
            chart_type: 图表类型 | Chart type

        返回 | Returns:
            包含模块信息和相似模块的字典
            Dictionary containing module info and similar modules
        """
        # 精确匹配
        # Exact match
        for category in self.chart_config.values():
            if isinstance(category, dict) and chart_type in category:
                return {
                    "module": category[chart_type].get("module"),
                    "found": True,
                    "confidence": 1.0,
                    "similar_modules": []
                }

        # 未找到精确匹配，查找相似模块
        # No exact match found, search for similar modules
        similar_modules = self._find_similar_modules(chart_type)

        return {
            "module": None,
            "found": False,
            "confidence": 0.0,
            "similar_modules": similar_modules
        }

    def _find_similar_modules(self, chart_type: str) -> List[Dict[str, str]]:
        """
        查找相似的模块
        Find similar modules

        参数 | Parameters:
            chart_type: 图表类型 | Chart type

        返回 | Returns:
            相似模块列表 | List of similar modules
        """
        similar = []
        chart_type_lower = chart_type.lower()

        for category in self.chart_config.values():
            if isinstance(category, dict):
                for mod_chart_type, mod_info in category.items():
                    if isinstance(mod_info, dict) and "name" in mod_info:
                        # 检查关键词重叠
                        # Check keyword overlap
                        mod_chart_type_lower = mod_chart_type.lower()

                        # 包含关系
                        # Containment relationship
                        if chart_type_lower in mod_chart_type_lower or \
                           mod_chart_type_lower in chart_type_lower:
                            similar.append({
                                "chart_type": mod_chart_type,
                                "module": mod_info.get("module"),
                                "name": mod_info.get("name"),
                                "match_reason": "keyword_overlap"
                            })

                        # 关键词匹配
                        # Keyword matching
                        keywords = mod_info.get("keywords", [])
                        for keyword in keywords:
                            if keyword.lower() in chart_type_lower:
                                similar.append({
                                    "chart_type": mod_chart_type,
                                    "module": mod_info.get("module"),
                                    "name": mod_info.get("name"),
                                    "match_reason": f"keyword_match_{keyword}"
                                })
                                break

        # 去重并限制数量
        # Deduplicate and limit count
        seen = set()
        unique_similar = []
        for item in similar:
            if item["module"] not in seen:
                unique_similar.append(item)
                seen.add(item["module"])

        return unique_similar[:5]  # 返回前5个相似模块

    def _get_decision_level(self, score: float) -> str:
        """
        根据分数确定决策级别
        Determine decision level based on score

        参数 | Parameters:
            score: 置信度分数 | Confidence score

        返回 | Returns:
            决策级别 | Decision level
        """
        thresholds = self.weights.get("threshold", {})

        if score >= thresholds.get("high_confidence", 0.85):
            return "high"
        elif score >= thresholds.get("medium_confidence", 0.70):
            return "medium"
        elif score >= thresholds.get("low_confidence", 0.50):
            return "low"
        else:
            return "very_low"

    def batch_fusion(self, figures_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        批量信息融合
        Batch information fusion

        参数 | Parameters:
            figures_data: 图表数据列表 | List of figure data

        返回 | Returns:
            融合结果列表 | List of fusion results
        """
        results = []

        print(f"Performing information fusion for {len(figures_data)} figures...")

        for i, figure_data in enumerate(figures_data, 1):
            figure_num = figure_data.get("figure_info", {}).get("figure_number", i)
            print(f"[{i}/{len(figures_data)}] Processing Figure {figure_num}...")

            result = self.determine_chart_type(figure_data)
            result["figure_number"] = figure_num
            results.append(result)

        print(f"Completed information fusion for {len(results)} figures")

        return results


def main():
    """主函数 | Main function"""
    import argparse

    parser = argparse.ArgumentParser(
        description="融合视觉识别和文本信息 | Fuse visual recognition and text information"
    )
    parser.add_argument(
        "input_json",
        help="输入 JSON 文件路径（包含视觉识别和文本挖掘结果）| Input JSON file path"
    )
    parser.add_argument(
        "-o", "--output",
        default="fusion_results.json",
        help="输出 JSON 文件路径 | Output JSON file path"
    )

    args = parser.parse_args()

    # 检查输入文件是否存在
    # Check if input file exists
    if not Path(args.input_json).exists():
        print(f"Error: File not found: {args.input_json}")
        return 1

    # 读取输入数据
    # Read input data
    with open(args.input_json, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    # 创建融合器并融合
    # Create fusion and fuse
    fusion = InfoFusion()

    if isinstance(input_data, list):
        results = fusion.batch_fusion(input_data)
    else:
        result = fusion.determine_chart_type(input_data)
        results = [result]

    # 保存结果
    # Save results
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\nResults saved to: {args.output}")

    return 0


if __name__ == "__main__":
    exit(main())
