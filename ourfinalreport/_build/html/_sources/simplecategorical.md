簡單類別型解釋變數
=======================
## 中風與性別
- 基本假設:性別與中風沒有關聯

```{image} ./two_by_two_table/gender_stroke.png
:alt: gender_stroke
:class: bg-primary mb-1
:width: 800px
:align: center
```

- 註記: 有一個性別是Other，被拿掉了
- Odds ratio $\hat{\theta}=1.089$
- 95% Confidence Interval of $\log{(\hat{\theta})}=(-0.172, 0.342)$
- 結論:中風跟性別是獨立的，符合我們一開始的猜想

## 中風與居住環境
- 基本假設:只有一點點關聯，鄉下的中風比例可能比住在城市的低
```{image} ./two_by_two_table/resitype_stroke.png
:alt: resitype_stroke
:class: bg-primary mb-1
:width: 800px
:align: center
```

- Odds ratio $\hat{\theta}=0.866$
- 95% Confidence Interval of $\log{(\hat{\theta})}=(-0.400, 0.112)$
- 雖然資料符合我們的猜想，鄉下中風的比例比較低，但是95\%的信賴區間包含0，表示 $\log{(\hat{\theta})}$ 與0無顯著差異
- 結論:中風與居住環境是獨立的

## 中風與婚姻
- 基本假設:婚姻與中風沒有關聯
```{image} ./two_by_two_table/evermarry_stroke.png
:alt: evermarry_stroke
:class: bg-primary mb-1
:width: 800px
:align: center
```

- Odds ratio $\hat{\theta}=4.184$
- 95% Confidence Interval of $\log{(\hat{\theta})}=(1.040, 1.823)$
   - 95%的信賴區間不包含0，表示 $\log{(\hat{\theta})}$ 與0有顯著差異。
- 結論:跟我們的基本假設相反，中風跟"有無結過婚"有關聯
- Fix column比較:
   - 中風患者: $\frac{\text{Ever-Married}}{\text{Never-Married}}=7.59$
   - 非中風者: $\frac{\text{Ever-Married}}{\text{Never-Married}}=1.81$
   - 中風患者中"結婚與沒結婚"的比例高於非中風者


## 中風與高血壓
- 基本假設:高血壓愈大的人愈容易中風
```{image} ./two_by_two_table/hypert_stroke.png
:alt: hypert_stroke
:class: bg-primary mb-1
:width: 800px
:align: center
```

- Odds ratio $\hat{\theta}=3.698$
- 95% Confidence Interval of $\log{(\hat{\theta})}=(1.009, 1.606)$
   - 95%的信賴區間不包含0，表示 $\log{(\hat{\theta})}$ 與0有顯著差異。
- 結論:中風跟高血壓有關聯
- Fix column比較:
   - 中風患者: $\frac{\text{Hypertension}}{\text{Non-Hypertension}}=0.36$
   - 非中風者: $\frac{\text{Hypertension}}{\text{Non-Hypertension}}=0.10$
   - 符和基本假設，高血壓愈大的人愈容易中風

## 中風與心臟病
- 基本假設:中風是心血管疾病，要與心臟病相關
```{image} ./two_by_two_table/heartd_stroke.png
:alt: hypert_stroke
:class: bg-primary mb-1
:width: 800px
:align: center
```

- Odds ratio $\hat{\theta}=4.706$
- 95% Confidence Interval of $\log{(\hat{\theta})}=(1.205, 1.893)$
   - 95%的信賴區間不包含0，表示 $\log{(\hat{\theta})}$ 與0有顯著差異。
- 結論:中風跟心臟病有關聯
- Fix column比較:
    - 中風患者: $\frac{\text{Heart-Disease }}{\text{No-Heart-Disease}}=0.23$
    - 非中風者: $\frac{\text{Heart-Disease }}{\text{No-Heart-Disease}}=0.05$
    - 符和基本假設，中風患者中有心臟病的比例高


## 綜合比較
```{image} ./images/oddsratio_bar.png
:alt: oddsratio_bar
:class: bg-primary mb-1
:width: 400px
:align: center
```
- 與中風有相關性: 婚姻、高血壓、心臟病 