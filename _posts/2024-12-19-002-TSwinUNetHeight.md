---
layout: post
title: "第二集 - 基于Sentinel数据的建筑物高度估测：T-SwinUNet模型"
date: 2024-12-19
categories: podcast
file: https://moguyun.ognai.com/api/shares/Y1OTQ0N/files/3f9d8bbe-67ca-4c87-b6d9-8ba0a3f57941
length: 53765804  # 文件大小(bytes)
duration: "18:40" # 时长
type: audio/wav
description: "基于Sentinel数据的建筑物高度估测：T-SwinUNet模型"
episode: 2
season: 1
episodeType: full
explicit: "no"
cover: "https://loongfee.github.io/soars-podcast/assets/images/artificial-intelligence.png"
---

# 太阳诱导叶绿素荧光遥感

## 本集概要

这篇论文提出了一种名为T-SwinUNet的深度学习模型，用于利用Sentinel-1 SAR和Sentinel-2 MSI时间序列数据进行大规模建筑物高度估算。该模型结合了卷积神经网络和Swin Transformer的优点，并引入了时间注意力机制来学习多模态时间序列数据的时空特征。实验结果表明，T-SwinUNet在10米空间分辨率下取得了最先进的建筑物高度估算精度，并在泛化能力方面表现出色，能够应用于欧洲不同城市，甚至优于现有的全球建筑物高度产品GHSL-Built-H R2023A。 该研究还进行了消融实验，验证了模型各个组件的贡献。

## 收听方式

- [在线收听](https://moguyun.ognai.com/api/shares/Y1OTQ0N/files/3f9d8bbe-67ca-4c87-b6d9-8ba0a3f57941)
- [下载音频](https://moguyun.ognai.com/api/shares/Y1OTQ0N/files/3f9d8bbe-67ca-4c87-b6d9-8ba0a3f57941)

## 内容提要

基于多源时序数据的建筑物高度估测：T-SwinUNet 模型综述
本文基于 Yadav 等人在《遥感环境》期刊上发表的论文“How high are we? Large-scale building height estimation at 10 m using Sentinel-1 SAR and Sentinel-2 MSI time series”，对其主要内容、重要观点和事实进行详细的解读和分析。

## 一、研究背景及意义

准确的建筑物高度估测对于城市化监测、环境影响分析和可持续城市规划至关重要。
现有的建筑物高度估测研究大多集中在小范围区域，缺乏针对大规模高度估测的深度学习模型，尤其是在使用开源地球观测数据时。
开源卫星影像，如 Sentinel-1 和 Sentinel-2，提供了免费的全球 SAR 和多光谱数据，具有较高的空间分辨率和频繁的重访周期，是进行大规模三维测绘的理想数据源。

## 二、研究目标和贡献

本文旨在利用开源的 Sentinel-1 SAR 和 Sentinel-2 MSI 时序数据，开发一种名为 T-SwinUNet 的先进深度学习模型，用于大规模建筑物高度估测，并填补现有模型的以下空白：

缺乏利用多光谱和 SAR 数据长时间序列中时空特征的深度学习模型。
现有的深度学习模型，即使是那些基于高分辨率商业化卫星数据提出的模型，也使用 CNN 编码器进行特征提取，这在学习全局特征和远程依赖方面存在局限性。
现有的 10 米空间分辨率的建筑物高度估测最多只能应用于国家尺度。
现有的深度学习模型缺乏消融实验，难以评估不同学习技术或架构修改的贡献。
本文的主要贡献如下：

提出了 T-SwinUNet 模型，该模型结合了 EfficientNet 特征提取器对细粒度模式的捕获能力和 Swin Transformer 对全局/局部特征的学习能力，并通过多头时间注意力模块学习多模态时序数据的时空特征。
提出了一种新的多任务解码器架构和一种新的训练方法，有效地利用了建筑物分割的补充任务。
通过全面的比较、消融和泛化实验，证明了 T-SwinUNet 模型的贡献。结果表明，该模型在 10 米空间分辨率下实现了最先进的建筑物高度估测，并在 100 米空间分辨率下优于全球建筑物高度产品 GHSL-Built-H R2023A。
证明了将预测的建筑物高度与现有的建筑物多边形合并可以产生精确的实例级建筑物高度估测，从而将 RMSE 提高到 1.60 米。

## 三、研究方法

3.1 数据和研究区域

研究区域涵盖荷兰、瑞士、爱沙尼亚和德国的特定地区（汉堡、勃兰登堡、萨克森和北莱茵-威斯特法伦），并收集了来自其他十个欧洲城市的 OOD 测试集数据，以评估模型在欧洲范围内的泛化能力。
参考数据来自航空立体影像或机载激光雷达点云，空间分辨率为 1 米至 2 米，并重新采样至 10 米分辨率。
Sentinel-1 SAR 数据为经过预处理的双波段 VV+VH 月平均值，以减少斑点噪声。Sentinel-2 MSI 数据为经过大气校正的 Level-2A 产品，每月生成一次最小云量合成影像。
数据集被划分为训练集、ID 测试集和 OOD 测试集，以评估模型在不同数据分布情况下的性能。
3.2 T-SwinUNet 模型架构

T-SwinUNet 模型采用编码器-解码器架构，主要模块包括：

共享 CNN 编码器: 提取 Sentinel-1 SAR 和 Sentinel-2 MSI 时序数据的特征，并生成多尺度特征图。
时间注意力模块: 学习时序特征之间的相关性，并为每个时间戳生成像素级注意力掩码，突出显示显著特征。
Swin Transformer 编码器: 学习全局和局部特征，并通过移位窗口技术实现多头注意力。
多任务解码器: 包含两个分支，分别预测建筑物高度和分割图，并通过一致性损失来增强高度特征和足迹特征之间的空间对齐。
3.3 训练目标和评价指标

模型采用监督回归损失、监督分割损失和无监督一致性损失进行训练，并通过权重参数来平衡不同任务的学习。
模型性能评估指标包括 RMSE、R² 分数、召回率、精度、F1 分数和 IoU。

## 四、主要结果

ID 测试集: T-SwinUNet 模型在 ID 测试集上取得了良好的性能，RMSE 为 1.89 米，R² 为 0.534，IoU 为 0.58。
与其他模型的比较: T-SwinUNet 模型优于 U-Net、TransUnet、SwinUNETR、U-TAE、MBHR-Net 和 BHE-Net 等其他模型。
消融实验: 消融实验结果表明，时间注意力模块、多任务学习和时序数据输入对模型性能的提升至关重要。
与 GHSL-Built-H R2023A 全球产品的比较: 在 100 米分辨率下，T-SwinUNet 模型的性能优于 GHSL-Built-H R2023A 产品。
欧洲范围内的泛化能力: T-SwinUNet 模型在 OOD 测试集上也取得了良好的性能，证明了其在欧洲范围内的泛化能力。
实例级评估: 通过使用参考建筑物多边形对像素级预测进行后处理，可以获得更精确的实例级建筑物高度估测。

## 五、讨论

T-SwinUNet 模型能够利用开源的 Sentinel 数据在不同城市环境下准确地估测建筑物高度，并具有大规模应用的潜力。
模型存在低估高层建筑物高度的局限性，这可能是由于 SAR 和光学数据的饱和效应以及数据集中高层建筑物样本数量较少所导致。
未来工作将扩展训练数据集，并探索域自适应技术来提高模型在不同地理区域的性能。

## 六、结论

T-SwinUNet 模型是一种先进的深度学习模型，能够利用 Sentinel-1 SAR 和 Sentinel-2 MSI 时序数据进行精确的建筑物高度估测和分割。该模型具有广泛的应用前景，可用于城市发展监测、灾害影响分析、人口动态和能源消耗评估等领域。

## 七、其他重要信息

本研究得到了瑞典斯德哥尔摩数字未来基金会的 EO-AI4GlobalChange 项目资助。
数据将根据要求提供。

## 参考资料

- [相关论文和资料链接]
1. Yadav, R., Nascetti, A. & Ban, Y. How high are we? Large-scale building height estimation at 10 m using sentinel-1 SAR and sentinel-2 MSI time series. Remote Sensing of Environment 318, 114556 (2025).


音频内容由AI自动生成，仅供参考。