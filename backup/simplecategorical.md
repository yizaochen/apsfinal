列聯表分析:簡單類別型
=======================
<style>
.blue {
    color: blue;
}

.awk {
    color: #b6b4cf;
}
</style>

## 中風與性別
- 基本假設:性別與中風沒有關聯

|            | Female  | Male | Sum  |
| ---------- | ------- | ---- | ---- |
| Stroke     | 141     | 108  | 249  |
| Non-stroke | 2853    | 2007 | 4860 |
| Sum        | 2994    | 1225 | 5109 |

### Odds Ratio:
   - $\hat{\theta}=1.089$
   - 95% Confidence Interval of $\log{(\hat{\theta})}=(-0.172, 0.342)$
### Chi-square:
   - $\chi^2$ = 0.34, df = 1, p-value = 0.5598

<span class ="blue">*性別與中風的關係在兩項檢定中均未有證據支持具有相關性*</span>

## 中風與居住環境
- 基本假設:只有一點點關聯，鄉下的中風比例可能比住在城市的低

|            | Urban | Rural | Sum  |
| ---------- | ----- | ----- | ---- |
| Stroke     | 135   | 141   | 249  |
| Non-stroke | 2461  | 2400  | 4861 |
| Sum        | 2596  | 2514  | 5110 |

### Odds Ratio:
   - $\hat{\theta}=0.866$
   - 95% Confidence Interval of $\log{(\hat{\theta})}=(-0.400, 0.112)$
   - 雖然資料符合我們的猜想，鄉下中風的比例比較低，但是95\%的信賴區間包含0，表示 $\log{(\hat{\theta})}$ 與0無顯著差異
### Chi-square:
   - $\chi^2$ = 1.0816, df = 1, p-value = 0.2983

<span class ="blue">*居住環境與中風的關係在兩項檢定中均未有證據支持具有相關性*</span>

## 中風與婚姻
- 基本假設:婚姻與中風沒有關聯

|            | Married | NevMar | Sum  |
| ---------- | ------- | ------ | ---- |
| Stroke     | 220     | 27     | 247  |
| Non-stroke | 3133    | 986    | 4119 |
| Sum        | 3353    | 1013   | 4366 |

### Odds Ratio:
   - $\hat{\theta}=2.564$
   - 95% Confidence Interval of $\log{(\hat{\theta})}=(0.536, 1.348)$
   - 95%的信賴區間不包含0，表示 $\log{(\hat{\theta})}$ 與0有顯著差異。
### Chi-square:
   - $\chi^2$ = 21.4, df = 1, p-value = 3.728e-06  

<span class ="blue">*婚姻經驗與中風的在本檢定中顯示具有相關性，如同odds ratio所顯示，進一步分析殘差瞭解其分布：*</span> 
```
round(result_StrokeMarri$residuals, 3)
```

|            | Married | NevMar |
| ---------- | ------- | ------ |
| Stroke     | 2.201   | -4.004 |
| Non-stroke | -0.539  | 0.980  |

<span class ="blue">*發現未曾有婚姻經驗者，較不容易中風，而婚姻經驗除了在附表(?)中可見與高血壓有關連性之外，相對於未結婚者也較容易中風*</span>

## 中風與高血壓
- 基本假設:高血壓愈大的人愈容易中風

|            | hypertension | Normal | Sum  |
| ---------- | ------------ | ------ | ---- |
| Stroke     | 66           | 183    | 249  |
| Non-stroke | 432          | 4429   | 4861 |
| Sum        | 498          | 4612   | 5110 |

### Odds Ratio:
   - $\hat{\theta}=3.698$
   - 95% Confidence Interval of $\log{(\hat{\theta})}=(1.009, 1.606)$
   - 95%的信賴區間不包含0，表示 $\log{(\hat{\theta})}$ 與0有顯著差異。
### Chi-square:
   - $\chi^2$ = 81.605, df = 1, p-value < 2.2e-16

<span class ="blue">*高血壓與中風的在本檢定中顯示具有高度相關性，如同odds ratio所顯示，進一步分析殘差了解其分布：*</span>
```
>round(result_StrokeHyper$residuals, 3)
```

|            | hypertension | Normal |
| ---------- | ------------ | ------ |
| Stroke     | 8.472        | -2.784 |
| Non-stroke | -1.917       | 0.630  | 

<span class ="blue">*高血壓與中風的發生有高度相關性，殘差顯示血壓正常者與高血壓者在中風條件下有最大的差異。*</span>

## 中風與心臟病
- 基本假設:中風是心血管疾病，要與心臟病相關

|            | heart D | Normal | Sum  |
| ---------- | ------- | ------ | ---- |
| Stroke     | 47      | 202    | 249  |
| Non-stroke | 229     | 4632   | 4861 |
| Sum        | 276     | 4834   | 5110 |

### Odds Ratio:
   - $\hat{\theta}=4.706$
   - 95% Confidence Interval of $\log{(\hat{\theta})}=(1.205, 1.893)$
   - 95%的信賴區間不包含0，表示 $\log{(\hat{\theta})}$ 與0有顯著差異。
### Chi-square:
   - $\chi^2$ = 90.26, df = 1, p-value < 2.2e-16  

<span class ="blue">*心臟病與中風的在本檢定中顯示具有高度相關性，如同odds ratio所顯示，進一步分析殘差瞭解其分布：*</span>
```
>round(result_StrokeHD$residuals, 3)
```

|            | heart D | Normal |
| ---------- | ------- | ------ |
| Stroke     | 9.149   | -2.186 |
| Non-stroke | -2.071  | 0.495  | 

<span class ="blue">*心臟病與中風的發生有高度相關性，殘差與$X^2$顯示心臟病患者與中風的關聯性甚至比高血壓之於中風要高。*</span>

## 綜合比較
```{image} ./images/oddsratio_bar.png
:alt: oddsratio_bar
:class: bg-primary mb-1
:width: 400px
:align: center
```
- 與中風有相關性: 婚姻、高血壓、心臟病 