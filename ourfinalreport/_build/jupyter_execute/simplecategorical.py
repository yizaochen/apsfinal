#!/usr/bin/env python
# coding: utf-8

# 列聯表分析1:簡單類別型
# =======================
# 列聯表分析的第一部份，會針對五個簡單類別變數做Two-by-two table的分析。簡單類別型變數只有兩個值，例如: 有高血壓就是1，沒高血壓就是0，也因此Two-by-two table跟Odds Ratio適合分析這種變數與中風的關係。

# ## A. 中風與性別
# 
# ### 性別的分佈與比例
# ```{image} https://i.imgur.com/VOikmMR.png
# :alt: gender
# :class: bg-primary mb-1
# :width: 800px
# :align: center
# ```
# - <span style="color:blue">在這筆資料中，女生佔了61%，男生佔了39%</span>

# ### Two-by-two table
# ```{image} ./images/twobytwo_table_gender.png
# :alt: twobytwo_table_gender
# :class: bg-primary mb-1
# :width: 800px
# :align: center
# ```

# ### Odds Ratio:
#    - $\hat{\theta}=1.119$
#    - 95% Confidence Interval of $\log{(\hat{\theta})}=(-0.192, 0.417)$
#    - <span style="color:blue">上面的信賴區間包含0，表示對於性別與中風，未有證據支持具有相關性</span>
#    - <span style="color:blue">雖然相關沒有統計顯著，但由上方的Bar圖，可以知道在這組資料中，如果已知是男生，那中風的機率是稍微高一點的</span>

# ## B. 中風與居住環境
# 
# ### 居住環境的分佈與比例
# ```{image} https://i.imgur.com/3UNDxmf.png
# :alt: residtype
# :class: bg-primary mb-1
# :width: 800px
# :align: center
# ```
# - <span style="color:blue">在這筆資料中，鄉下與城市的人們大約各佔一半，鄉下佔了49%，城市佔了51%</span>

# ### Two-by-two table
# ```{image} ./images/twobytwo_table_residence_type.png
# :alt: twobytwo_table_residence_type
# :class: bg-primary mb-1
# :width: 800px
# :align: center
# ```

# ### Odds Ratio:
#    - $\hat{\theta}=0.948$
#    - 95% Confidence Interval of $\log{(\hat{\theta})}=(-0.354, 0.247)$
#    - <span style="color:blue">95\%的信賴區間包含0，表示住在城市與鄉下與中風並無相關性</span>
#    - <span style="color:blue">由上方的Bar圖的條件機率，也顯示住在城市與鄉下得到中風的機率是類似的</span>

# ## C. 中風與高血壓
# 
# ### 高血壓的分佈與比例
# ```{image} https://i.imgur.com/V2ls7hO.png
# :alt: hypertension
# :class: bg-primary mb-1
# :width: 800px
# :align: center
# ```
# - <span style="color:blue">在這筆資料中，有高血壓的人佔了12%，沒高血壓的人佔了88%</span>

# ### Two-by-two table
# ```{image} ./images/twobytwo_table_hypertension.png
# :alt: residtype
# :class: bg-primary mb-1
# :width: 800px
# :align: center
# ```
# 
# ### Odds Ratio:
#    - $\hat{\theta}=3.821$
#    - 95% Confidence Interval of $\log{(\hat{\theta})}=(1.007, 1.673)$
#    - 95%的信賴區間不包含0，表示 $\log{(\hat{\theta})}$ 與0有顯著差異
#    - <span style="color:blue">表示中風與高血壓是顯著相關的</span>
#    - <span style="color:blue">由上方Bar圖，在高血壓患者中，中風的機率是0.14。然而，在非高血壓的人中，中風的機率是0.04。可以知道，有高血壓的人比沒有高血壓的人容易中風。</span>
#    
# ### Chi-square:
#    - $\chi^2$ = 81.605, df = 1, p-value < 2.2e-16
# 
# - 高血壓與中風的在本檢定中顯示具有高度相關性，如同odds ratio所顯示，進一步分析殘差了解其分布：
# ```
# >round(result_StrokeHyper$residuals, 3)
# ```
# 
# |            | hypertension | Normal |
# | ---------- | ------------ | ------ |
# | Stroke     | 8.472        | -2.784 |
# | Non-stroke | -1.917       | 0.630  | 
# 
# - <span style="color:blue"> 高血壓與中風的發生有高度相關性，殘差顯示血壓正常者與高血壓者在中風條件下有最大的差異</span>

# ## D. 中風與心臟病
# ### 心臟病的分佈與比例
# ```{image} https://i.imgur.com/IMe8y6F.png
# :alt: heartdisease
# :class: bg-primary mb-1
# :width: 800px
# :align: center
# ```
# - <span style="color:blue">在這筆資料中，有心臟病的人佔了6%，沒心臟病的人佔了94%</span>

# ### Two-by-two table
# ```{image} ./images/twobytwo_table_heartDisease.png
# :alt: heartDisease
# :class: bg-primary mb-1
# :width: 800px
# :align: center
# ```
# 
# ### Odds Ratio:
#    - $\hat{\theta}=4.522$
#    - 95% Confidence Interval of $\log{(\hat{\theta})}=(1.112, 1.905)$
#    - 95%的信賴區間不包含0，表示 $\log{(\hat{\theta})}$ 與0有顯著差異。
#    - <span style="color:blue">表示中風與心臟病是顯著相關的</span>
#    - <span style="color:blue">由上方Bar圖，在心臟病患者中，中風的機率是0.175。然而，在非心臟病患者中，中風的機率是0.045。可以知道，有心臟病的人比沒有心臟病的人容易中風。</span>
#    
# ### Chi-square:
# - $\chi^2$ = 90.26, df = 1, p-value < 2.2e-16  
# - 心臟病與中風的在本檢定中顯示具有高度相關性，如同odds ratio所顯示，進一步分析殘差瞭解其分布：
# 
# ```
# >round(result_StrokeHD$residuals, 3)
# ```
# 
# |            | heart D | Normal |
# | ---------- | ------- | ------ |
# | Stroke     | 9.149   | -2.186 |
# | Non-stroke | -2.071  | 0.495  | 
# 
# <span style="color:blue">心臟病與中風的發生有高度相關性，殘差與$\chi^2$: 顯示心臟病患者與中風的關聯性甚至比高血壓之於中風要高。</span>

# ## E. 中風與婚姻
# ### 結婚的分佈與比例
# ```{image} https://i.imgur.com/Pua54Dk.png
# :alt: evermarry
# :class: bg-primary mb-1
# :width: 800px
# :align: center
# ```
# - <span style="color:blue">在這筆資料中，有結婚的人佔了76%，未婚的人佔了24%</span>

# ### Two-by-two table
# ```{image} ./images/twobytwo_table_marry.png
# :alt: heartDisease
# :class: bg-primary mb-1
# :width: 800px
# :align: center
# ```
# 
# ### Odds Ratio:
#    - $\hat{\theta}=2.644$
#    - 95% Confidence Interval of $\log{(\hat{\theta})}=(0.501, 1.444)$
#    - 95%的信賴區間不包含0，表示 $\log{(\hat{\theta})}$ 與0有顯著差異。
#    - <span style="color:blue">表示中風與婚姻狀態是顯著相關的</span>
#    - <span style="color:blue">我們一開始認為婚姻不應該跟中風有關聯，上方Bar圖告訴我們有結過婚的人比較容易中風</span>
#    - <span style="color:blue">在後續的分析，我們會發現婚姻帶有年齡的資訊。換句話說，婚姻與中風關聯背後的Confounding factor是年齡</span>
#    
# ### Chi-square:
# - $\chi^2$ = 21.4, df = 1, p-value = 3.728e-06  
# - 婚姻經驗與中風的在本檢定中顯示具有相關性，如同odds ratio所顯示，進一步分析殘差瞭解其分布：
# 
# ```
# round(result_StrokeMarri$residuals, 3)
# ```
# 
# |            | Married | NevMar |
# | ---------- | ------- | ------ |
# | Stroke     | 2.201   | -4.004 |
# | Non-stroke | -0.539  | 0.980  |
# 
# - <span style="color:blue">發現未曾有婚姻經驗者，較不容易中風</span>

# ## 綜合比較
# ```{image} ./images/oddsratio_bar.png
# :alt: oddsratio_bar
# :class: bg-primary mb-1
# :width: 400px
# :align: center
# ```
# - <span style="color:blue"> 我們把這五個簡單變數的Odds Ratio 畫在一起做比較，如上圖。</span>
# - <span style="color:blue"> 與中風不相關的變數: 性別與居住地</span>
# - <span style="color:blue"> 與中風相關的三個變數: 婚姻、高血壓、心臟病 </span>
# - <span style="color:blue"> 婚姻與中風相關是比較意外的結果，下面會做年齡與婚姻相關的分析，就可以知道婚姻是帶有年齡的資訊的。</span>
