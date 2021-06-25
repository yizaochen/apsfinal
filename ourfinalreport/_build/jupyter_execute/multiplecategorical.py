#!/usr/bin/env python
# coding: utf-8

# Chapter 4: 列聯表分析2-多重類別型
# =======================
# 在列聯表分析的第二部份，主要是探討兩個類別型變數，抽煙狀態與工作。這兩個變數都含有兩個以上的類別。下面主要使用的統計方法為卡方檢定。

# ## A. 中風與抽煙習慣
# ### 抽煙習慣的分佈與比例
# ```{image} https://i.imgur.com/wn6c5i3.png
# :alt: smoking
# :class: bg-primary mb-1
# :width: 800px
# :align: center
# ```
# - <span style="color:blue">在這筆資料中，不曾抽煙者佔了54%，曾抽過煙但戒掉的人佔了24.5%，現在抽煙者佔了21.5%</span>

# ### Contingency table
# ```{image} ./images/contingency_table_smoke.png
# :alt: contingency_table_smoke
# :class: bg-primary mb-1
# :width: 1000px
# :align: center
# ```
# 
# ### Chi-square:
# - $\chi^2$ = 6.03, df=2, p-value=4.906e-02
# - <span style="color:blue">p-value$<$0.05，顯示抽煙狀態與中風具有高度相關性</span>
# - <span style="color:blue">由Contingency Table的期望值可以發現，造成統計顯著性的是"Never smoke"與"Formerly Smoke"</span>
# - <span style="color:blue">Never Smoke的觀測值比期望值低，表示不抽煙者中風的機率較低</span>
# - <span style="color:blue">Formerly Smoke的觀測值比期望值高，表示戒煙者中風的機率提高</span>
# - <span style="color:blue">Bar圖也指出，Formerly Smoke的中風機率是最高的。這個結果讓我們懷疑戒煙者是不是也隱含著年齡比較大的資訊，這在後續的分析會一併討論</span>

# ## B. 中風與工作
# ### 工作的分佈與比例
# ```{image} ./images/worktype_distribution.png
# :alt: worktype
# :class: bg-primary mb-1
# :width: 800px
# :align: center
# ```
# - <span style="color:blue">在這筆資料中，私人企業工作佔了64%，self-employed的人佔了18%，政府機關工作的人佔了15%，剩下的則是不曾工作者與小孩</span>
# - <span style="color:gray">我們會在下面的Contigency Table跟卡方分析把"孩童"與"未曾工作"的資料點清理掉</span>
# 
# ### Contingency table
# ```{image} ./images/contingency_table_worktype.png
# :alt: contingency_table_worktype
# :class: bg-primary mb-1
# :width: 1000px
# :align: center
# ```
# 
# ### Chi-square:
# - $\chi^2$ = 7.87, df=2, p-value=1.959e-02
# - <span style="color:blue"> p-value $<$ 0.05，顯示工作與中風具有高度相關性</span>
# - <span style="color:blue"> 在私人企業與政府單位工作的人的中風觀測值都比中風期望值低。然而，對於自己開業的人，中風的觀測值比期望值高。從右方條件機率的Bar圖也顯示自己開業的人中風的機率最高</span>
# - <span style="color:blue"> 我們猜測背後的原因是，自行創業的壓力比領人薪水的壓力大，以致於中風的機率高</span>
# <p style="page-break-before: always">
