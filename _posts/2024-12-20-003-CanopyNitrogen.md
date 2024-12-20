---
layout: post
title: "第三集 - 哨兵2号冠层氮含量估算与制图优化"
date: 2024-12-20
categories: podcast
file: https://moguyun.ognai.com/api/shares/Q4ODUyM/files/852b55cc-1878-421c-8ebc-aeaa6075b168
length: 40433324  # 文件大小(bytes)
duration: "14:02" # 时长
type: audio/wav
description: "哨兵2号冠层氮含量估算与制图优化"
episode: 3
season: 1
episodeType: full
explicit: "no"
cover: "https://loongfee.github.io/soars-podcast/assets/images/artificial-intelligence.png"
---

## 本集概要

该研究提出了一种利用Sentinel-2卫星数据，结合PROSAIL-PRO辐射传输模型、高斯过程回归（GPR）和基于欧几里德距离的多样性主动学习技术，在大规模估算冠层氮含量（CNC）方面的优化方法。研究比较了基于蛋白质和叶绿素两种CNC计算方法，并在Google Earth Engine平台上实现了模型，验证结果显示该方法具有较高的精度和可扩展性，可用于大范围的CNC动态监测。

## 收听方式

- [在线收听]({{ page.file }})
- [下载音频]({{ page.file }})

## 内容提要

## 研究背景:

氮是植物生长发育必需的营养元素，对农业生产和生态系统健康至关重要。冠层氮含量 (CNC) 是评估植物健康、检测生态系统扰动和制定保护策略的重要指标。遥感技术为大尺度监测 CNC 提供了一种有效手段。

## 研究目的:

该研究旨在开发一个基于哨兵2号 (S2) 多光谱卫星影像估算 CNC 的优化混合模型，并将其应用于 Google Earth Engine (GEE) 平台，实现大规模 CNC 制图和监测。

## 研究方法:

该研究采用了一种混合建模方法，结合了叶片和冠层辐射传输模型 (RTM) 和机器学习回归算法 (MLRA)。主要步骤如下：

CNC 计算方法比较: 分别使用蛋白质-氮和叶绿素-氮关系计算 CNC，并评估其对预测精度的影响。
训练数据集选择: 利用 PROSAIL-PRO 模型生成模拟 S2 卫星数据的训练数据集，并通过欧氏距离多样性 (EBD) 方法优化训练数据集。
MLRA 选择: 比较了高斯过程回归 (GPR) 和其他 MLRA（如核岭回归、主成分回归等）的性能，最终选择 GPR 作为核心算法。
模型验证: 使用独立的实测数据验证了模型的准确性。
GEE 平台实现: 将优化后的模型集成到 GEE 平台，实现大规模 CNC 制图和时序分析。

## 主要结果:

研究发现，基于蛋白质-氮关系的 Cprot-LAI 模型和基于叶绿素-氮关系的 Cab-LAI 模型在 CNC 估算方面均取得了良好的效果。
Cab-LAI 模型的预测结果总体上更为稳健，其不确定性更低，因此被选为大规模制图的最佳模型。
在独立验证数据集中，模型的 R² 值分别为 0.58 和 0.71，NRMSE 分别为 21.47% 和 20.17%。
模型在不同生长季表现出高度一致性，表明其在 CNC 动态时序分析方面的潜力。
研究展示了模型在伊比利亚半岛大规模 CNC 制图中的应用，估算结果的相对不确定性低于 30%。

## 研究结论:

该研究开发的基于 S2 卫星数据的优化混合模型为大规模 CNC 制图和监测提供了一个有效工具。
EBD-GPR-CNC 方法在 GEE 平台上的实现支持可扩展的 CNC 估算，并为监测氮动态提供了可靠的工具。

## 研究意义:

该研究为农业评估、作物生长监测和施肥管理提供了重要的数据支持。
该研究促进了多光谱卫星数据在 CNC 估算和制图中的应用。
该研究为下一代多光谱和高光谱卫星任务（如 S2NG 和 CHIME）的数据应用奠定了基础。
以下是一些来自原文的引文，突出了研究的关键发现:

"The models revealed high consistency for an independent validation dataset of the Munich-North-Isar (Germany) test site, with R² values of 0.58 and 0.71 and NRMSEs of 21.47% and 20.17% for the Cprot-LAI model and Cab-LAI model, respectively."
"The models also demonstrated high consistency across growing seasons, indicating their potential for time series analysis of CNC dynamics."
"Application of the S2-based mapping workflow across the Iberian Peninsula, with estimates showing relative uncertainty below 30%, highlights the model's broad applicability and portability."
"The optimized EBD-GPR-CNC approach within GEE supports scalable CNC estimation and offers a robust tool for monitoring nitrogen dynamics."
总的来说，这项研究对利用遥感技术监测植物和生态系统健康做出了重要贡献。该研究开发的优化混合模型和 GEE 平台的实现为大规模 CNC 制图和时序分析提供了一种高效且可扩展的方法。


音频内容由AI自动生成，仅供参考。