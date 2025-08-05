---
categories: podcast
cover: https://loongfee.github.io/soars-podcast/assets/images/artificial-intelligence.png
date: 2024-12-30
description: 植被物候对夜间人造光各向异性影响
duration: '14:02'
episode: 4
episodeType: full
explicit: 'no'
file: https://moguyun.ognai.com/api/shares/MxMzY3O/files/56272275-6fec-475e-a333-00b9c699980b
layout: post
length: 40433324
season: 1
title: 第四集 - 植被物候对夜间人造光各向异性影响
type: audio/wav
---

## 本集概要

这篇论文利用多角度卫星观测数据（VIIRS DNB），研究了植被物候对夜间人工光（ALAN）各向异性的影响。研究发现，ALAN的各向异性具有明显的季节性变化，与植被指数NDVI显著正相关。植被生长会降低ALAN的各向异性，使其在不同方向上的光线分布更均匀。该研究结果有助于改进夜间灯光时间序列数据的质量，并更好地构建城市辐射函数（CEF）来模拟天文光污染。

## 收听方式

- [在线收听]({{ page.file }})
- [下载音频]({{ page.file }})

## 内容提要

本研究探讨了植被物候对夜间人造光 (ALAN) 各向异性的影响，并利用多角度卫星观测数据验证了这一假设。

## 主要发现:

ALAN 的各向异性具有季节性变化。区域尺度上，CI 值 (表征 ALAN 各向异性的指标) 在一年中呈现规律性波动，通常在 7-8 月达到峰值。
像素尺度上，大部分像素在植被生长季的 CI 值高于落叶季。
植被生长会降低 ALAN 的各向异性。区域尺度上，NDVI (表征植被生长状况的指标) 与 CI 值呈显著正相关 (0.56 < r < 0.92)，表明植被越茂盛， ALAN 各向异性越弱。
像素尺度上，大部分 NDVI 与 CI 值显著相关的像素也呈现正相关 (0.41 < r < 0.79)，支持了上述结论。

## 可能原因:

夜间，人造光源发出的光子进入植被冠层后会发生多次散射。随着植被叶片生长，光子在穿过冠层之前经历更多次散射，导致光子分布更加均匀，从而降低了 ALAN 各向异性。

## 研究意义:

提高夜间灯光数据质量: 通过结合季节性和角度信息，可以更准确地模拟多角度夜间遥感观测，从而提高日间夜间灯光产品的质量，更好地反映社会经济动态。
"This finding provides a new perspective for improving the quality of daily NTL products to better reflect socioeconomic dynamics."
改进城市灯光排放函数 (CEF): 研究结果有助于更好地模拟 CEF，从而更准确地模拟天文光污染，为城市规划者管理和提升城市环境质量提供更有价值的参考。
"The finding helps to better model City Emission Function (CEF) so as to better model the astronomic light pollution in future studies."

## 研究局限:

数据精度: Black Marble 产品的不确定性可能增加时间序列 CI 的波动。未来可采用更高空间分辨率的观测方法进行进一步分析。
观测次数: 晴朗无雪的 Suomi-NPP/VIIRS 观测次数有限，限制了 CI 时间序列的长度。未来可利用 JPSS-1/VIIRS 和 JPSS-2/VIIRS 数据增加晴朗夜间观测次数。
模型简化: 本研究采用线性 VZA-强度模型来表征 ALAN 的能量方向分布，这可能存在一定的局限性。未来随着对各向异性机制认识的深入，将会出现更精确的量化指标。

## 未来研究方向:

利用无人机进行多角度长期观测实验，更精确地量化树木和草地物候对 ALAN 各向异性的影响。
采用 3D 计算机模拟模型，设计不同生长季的光源和植被场景，以排除其他环境因素的影响，直接揭示植被物候对各向异性的影响。
研究不同因素（如汽车前灯）对夜间灯光和 ALAN 各向异性的影响。

## 结论:

本研究证实了植被物候对 ALAN 各向异性的影响，为改进夜间灯光数据质量和模拟天文光污染提供了理论依据，对城市规划和环境管理具有重要意义。


音频内容由AI自动生成，仅供参考。