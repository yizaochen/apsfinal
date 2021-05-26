因素之間交互作用:數值型
=======================
- 在卡方檢定中，我們已經知道年齡、bmi、血糖與中風不是獨立的

## 三種數值型變數兩兩關係
- 這一個部份，我們想了解這三個變數所含有的資訊是否有重疊?
```{image} ./images/numerical_scatter.png
:alt: numerical_scatter
:class: bg-primary mb-1
:width: 800px
:align: center
```

```{image} ./images/numerical_pearsonr.png
:alt: numerical_pearsonr
:class: bg-primary mb-1
:width: 800px
:align: center
```
- 先用Scatter plots提供視覺化的資訊
    - 年紀小的，中風的機率小
- 我們分成中風與沒有中風兩組，分別算出相關係數
   - 可以看到相關係數都靠近0，表示三個解釋變數的相關性低
- 因此，之後的模型中，這三個解釋變數都得考慮

