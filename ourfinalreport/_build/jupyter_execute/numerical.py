#!/usr/bin/env python
# coding: utf-8

# Chapter 5: 列聯表分析3-數值型
# =======================
# 在第三部份，我們把數值型的三種變數想辦法分類，以便做出列聯表。再利用列聯表做卡方檢定跟算出條件機率。

# ## A. 中風與年齡
# 在這部份的分析，我們用10歲當間距，把年齡歸成8個分類(10-20,20-30,...,80-90)
# 
# ### 年齡的分佈與比例
# ```{image} ./images/age_distribution.png
# :alt: age_distribution
# :class: bg-primary mb-1
# :width: 600px
# :align: center
# ```
# - <span style="color:blue">在這筆資料中，最多人是介於50-60歲，佔了19.3%。最年輕的族群是10-20，佔了6.7%。最年長的是80-90，佔了4.4%</span>
# 
# ### Contigency Table
# ```{image} ./images/contigency_table_age1.png
# :alt: contigency_table_age1
# :class: bg-primary mb-1
# :width: 800px
# :align: center
# ```
# - <span style="color:gray">從上方表格發現，10-20與20-30歲的人都屬於非中風族群。因此，為了做卡方分析，我們會把10-20,20-30,30-40,40-50合併成一組</span>
# - <span style="color:blue">從上方條件機率Bar圖來看，中風的機率顯然是隨著年齡而增加</span>
# 
# ### Contigency Table(合併組別後)
# ```{image} ./images/contigency_table_age2.png
# :alt: contigency_table_age2
# :class: bg-primary mb-1
# :width: 800px
# :align: center
# ```
# 
# ### Chi-square:
# - $\chi^2$ = 242.12, df=4, p-value=3.243e-51 
# - <span style="color:blue"> p-value $<$ 0.05，顯示年齡與中風具有高度相關性</span>
# - <span style="color:red"> 觀測值與期望值的差別、條件機率Bar圖都指出，年齡愈大，中風機率愈高</span>

# ## B. 中風與血糖
# ### 血糖的分佈
# *註: 雖然不確定收集資料時是取飯前(FPG)或是飯後血糖(OGTT)，本報告仍先採用空腹血糖做為參考標準。*
# ```{image} https://i.imgur.com/5Gwb4HB.png
# :alt: avg_glucose
# :class: bg-primary mb-1
# :width: 600px
# :align: center
# ```
# - <span style="color:blue">可以看到血糖的分佈呈現雙峰，左邊高峰與正常血糖範圍(80-110)交疊，而右邊的高峰是血糖過高的區域</span>
# 
# ### Contigency Table
# 我們接著參考日本糖尿病協會的分類標準(Appendix)，把血糖分為四群
# ```{image} ./images/contingency_table_glucose.png
# :alt: contingency_table_glucose
# :class: bg-primary mb-1
# :width: 800px
# :align: center
# ```
# 
# ### Chi-square:
# - $\chi^2$ = 79.24, df=3, p-value=4.478e-17
# - <span style="color:blue"> p-value $<$ 0.05，顯示血糖與中風具有高度相關性</span>
# - <span style="color:blue"> 由條件機率可以發現，血糖小於160對於中風的機率都差不多</span>
# - <span style="color:red"> 血糖大於160的組別，中風的機率特別高。對照上面的分佈圖，右邊高血糖的族群就是容易中風的族群</span>

# ## C. 中風與BMI
# ### BMI的分佈
# ```{image} ./images/bmi_distribution.png
# :alt: bmi_distribution
# :class: bg-primary mb-1
# :width: 800px
# :align: center
# ```
# - 首先，我們把BMI分成三類，18.5與25這兩個數值是分類的切點，如上圖
# - <span style="color:blue">由上面的分佈圖大概可以知道，這組資料集大部分的人是過胖的</span>
# 
# ```{image} ./images/bmi_distri_compare.png
# :alt: bmi_distribution
# :class: bg-primary mb-1
# :width: 800px
# :align: center
# ```
# - 這組資料是麥肯錫這間美國企業舉辦活動釋出的，因此我們比較了一下這組資料BMI與美國十萬個成人的BMI分佈，最後還找了台灣人的分佈
# - <span style="color:blue">由上圖，這組資料集的確是比較符合美國人的分佈，甚至胖上許多。所以拿這組資料研究中風可能就有偏差，因為大部份人是過胖的</span>
# 
# 
# ### Contigency Table
# ```{image} ./images/contingency_table_bmi.png
# :alt: contingency_table_bmi
# :class: bg-primary mb-1
# :width: 800px
# :align: center
# ```
# - 因為Underweight-stroke那一欄是1，表示這樣的分組不適合做卡方，因此在這裡我們就只看條件機率
# - <span style="color:blue"> 由條件機率可以發現，過胖的人，中風機率是比較高的</span>
# 
# ### 討論: 過輕族群的唯一一個中風者
# - 我們把過輕族群唯一一個中風者的資料抓出來看
# - <span style="color:blue"> 她是: 81歲女性，沒有高血壓，沒有心臟病，有結婚，自營事業者，住在鄉村，血糖82，不曾抽煙</span>
# - <span style="color:blue"> 由上面所有的分析，她只俱備年紀大這個風險因素，所以我們推測以下種可能</span>
#     - 年紀大，容易中風
#     - 她可能基因上有中風因子
#     - 可能因為中風，生病後才變瘦的
# <p style="page-break-before: always">
