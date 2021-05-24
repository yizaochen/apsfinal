多重類別型解釋變數
=======================

## 中風與抽煙習慣
### 分類成兩組
- smoke包含smokes與formerly smoked
- never smoke自己一組

- 基本假設:有抽煙的人比較容易中風
```{image} ./two_by_two_table/smoke_stroke.png
:alt: smoke_stroke
:class: bg-primary mb-1
:width: 800px
:align: center
```

- 註記: unknown有1544個資料點，被拿掉了
- Odds ratio $\hat{\theta}=1.436$
- 95% Confidence Interval of $\log{(\hat{\theta})}=(0.076, 0.647)$
   - 95%的信賴區間不包含0，表示 $\log{(\hat{\theta})}$ 與0有顯著差異。
- 結論:中風跟抽煙有關聯。但相比於婚姻、壓力與心臟病，抽煙的$\hat{\theta}$比較靠近$1$，表示抽煙相對來說不是一個重要的因子
- Fix column比較:
   - 中風患者: $\frac{\text{Smoke}}{\text{No smoke}}=1.24$
   - 非中風者: $\frac{\text{Smoke}}{\text{No smoke}}=0.87$
   - 符和基本假設，中風患者中有抽煙的比例高

### 三組分開做
#### Chi-square
|          |Stroke|No Stroke|Sum |
| -------- |------|---------|--- |
| smokes   |42    |747      |789 |
| formerly |70    |815      |885 |
| never    |90    |1802     |1892|
| Sum      |202   |3364     |3566|

$X^2$ = 11.436, df = 2, p-value = 0.003285

`> round(smokeStroke_chi$residuals, 3)`

|          | Stroke   | No Stroke|
| -------- | -------- | -------- |
| smokes   | -0.403   | 0.099    |
| formerly | **2.806**| -0.688   |
| never    | -1.659   | 0.407    |

- 結論: 
   - **曾經抽菸者甚至比正有抽菸習慣者更容易中風**
   - 從不抽菸者還是最不容易中風
   - 由於右欄未大於0.5，本表中較難以下結論，以下用odds ratio補足

#### Odds Ratio
首先，我們先計算Odds

$\rm{Odds}_{1} = \cfrac{P(\rm{stroke}|\rm{smokes})}{P(\rm{No stroke}|\rm{smokes})} = \cfrac{42}{747} = 0.056$ 

$\rm{Odds}_{2} = \cfrac{P(\rm{stroke}|\rm{former})}{P(\rm{No stroke}|\rm{former})} = \cfrac{70}{815} = 0.086$

$\rm{Odds}_{3} = \cfrac{P(\rm{stroke}|\rm{NevSmoke})}{P(\rm{No stroke}|\rm{NevSmoke})} = \cfrac{202}{3364} = 0.060$ 

Odds Ratio:
* formerly smoked to smokes
    1)   $\hat{OR}_{21} = \cfrac{0.086}{0.056} = 1.54$
    2)   95% Confidence Interval of $\ln(θ)： (0.037, 0.827)$，範圍不涵蓋0，故與odds ratio與1有顯著差異
    3)   formerly smoked 比 smokes 容易中風
* formerly smoked to never smokes
    1)   $\hat{OR}_{23} = \cfrac{0.086}{0.060} = 1.43$
    2)   95% Confidence Interval of $\ln(θ)： (0.035, 0.681)$，範圍不涵蓋0，故與odds ratio與1有顯著差異
* never smokes to smokes
    1)   $\hat{OR}_{13} = \cfrac{0.056}{0.060} = 0.93$
    2)   95% Confidence Interval of $\ln(θ)： (-0.45, 0.30)$，範圍涵蓋0，故與odds ratio與1**無**顯著差異，無法從本樣本區分出有吸菸習慣與未曾吸菸組的差異

- 討論: 
   - type I error要維持在0.05的話可能"95%"的數字要調整，但是我們沒有調
   - 猜測: 
      - Formerly 可能都是年紀比較大的
      - Smokes 可能都是年紀輕的
   - **應該要區分formely與smokes**

## 中風與工作
### Chi-squared test
* children 2 removed
* never-worked none removed

|            | Stroke | No Stroke | Sum  |
| ---------- | ------ | --------- | ---- |
| Government | 23     | 491       | 514  |
| Private    | 109    | 2092      | 2201 |
| Self-empl  | 48     | 581       | 629  |
| Sum        | 108    | 3164      | 3344 |

- $X^2$ = 7.8764, df = 2, p-value = 0.01948

`> round(workStroke_chi$residuals, 3)`

|            | Stroke | No Stroke |
| ---------- | ------ | --------- |
| Government | -0.887 | 0.212     |
| Private    | -0.870 | 0.208     |
| Self-empl  | **2.430**| -0.580    |

- 結論: 自行創業者較容易中風

### 兩兩分組做chi-square
#### Private
```
Work Type 1: children, Govt_job, Self-employed, Never_worked
Work Type 2': Private
```
|             |Stroke|No Stroke|    |
| ----------- |------|---------|--- |
| Work type 1 |100   |2085     |2185|
| Work type 2 |149   |2776     |2925|
|             |249   |4861     |5110|
- $X^2$ = 0.6149, df = 1, p-value = 0.4329
- 因此工作類型是否是私人企業(Private)與中風沒有顯著的關聯性

#### Self-employed
```
Work Type 1: children, Govt_job, Private, Never_worked
Work Type 2': Self-employed
```
|             |Stroke|No Stroke|    |
| ----------- |------|---------|--- |
| Work type 1 |184   |4107     |4291|
| Work type 2 |65    |754      |819 |
|             |249   |4861     |5110|
- $X^2$ = 18.97, df = 1, p-value = 1.328e-05
- 因此工作類型是否是自行創業者(Self-employed)與中風有顯著的關聯性

#### Govt_job
```
Work Type 1: children, Self-employed, Private, Never_worked
Work Type 2': Govt_job
```
|             |Stroke|No Stroke|    |
| ----------- |------|---------|--- |
| Work type 1 |216   |4237     |4453|
| Work type 2 |33    |624      |657 |
|             |249   |4861     |5110|
- $X^2$ = 0.0088896, df = 1, p-value = 0.9249
- 因此工作類型是否在政府機關(Govt_job)與中風沒有顯著的關聯性