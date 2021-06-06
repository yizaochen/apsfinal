列聯表分析:多重類別型
=======================
<style>
.blue {
    color: blue;
}

.awk {
    color: #b6b4cf;
}
</style>

## 中風與抽煙習慣
### 分類成兩組
- smoke包含smokes與formerly smoked
- never smoke自己一組
- 註記: unknown有1544個資料點，被拿掉了
- 基本假設:有抽煙的人比較容易中風


|            | Smoke   | Never Smoke | Sum  |
| ---------- | ------- | ----------- | ---- |
| Stroke     | 112     | 90          | 202  |
| Non-stroke | 1562    | 1802        | 3364 |
| Sum        | 1674    | 1892        | 3566 |

#### Odds Ratio:
   - $\hat{\theta}=1.436$
   - 95% Confidence Interval of $\log{(\hat{\theta})}=(0.076, 0.647)$
   - 95%的信賴區間不包含0，表示 $\log{(\hat{\theta})}$ 與0有顯著差異。

<span class ="blue">*中風跟抽煙有關聯。但相比於婚姻、壓力與心臟病，抽煙的$\hat{\theta}$比較靠近$1$，表示抽煙相對來說不是一個重要的因子*</span>

##### Fix Row比較:
   - 中風患者: $\frac{\text{Smoke}}{\text{Never smoke}}=1.24$
   - 非中風者: $\frac{\text{Smoke}}{\text{Never smoke}}=0.87$

<span class ="blue">*符和基本假設，中風患者中有抽煙的比例高*</span>

### 三組分開做
#### Chi-square
|          |Stroke|No Stroke|Sum |
| -------- |------|---------|--- |
| smokes   |42    |747      |789 |
| formerly |70    |815      |885 |
| never    |90    |1802     |1892|
| Sum      |202   |3364     |3566|

$\chi^2$ = 11.436, df = 2, p-value = 0.003285

```
> round(smokeStroke_chi$residuals, 3)
```

|          | Stroke   | No Stroke|
| -------- | -------- | -------- |
| smokes   | -0.403   | 0.099    |
| formerly | **2.806**| -0.688   |
| never    | -1.659   | 0.407    |

- 結論: 
   - **曾經抽菸者甚至比正有抽菸習慣者更容易中風**
   - **應該要區分formely與smokes**
   - 從不抽菸者還是最不容易中風
   - 即便右欄未大於0.5，要說未曾抽菸者不容易中風可能較勉強，但前一項odds ratio已能補足這結論


## 中風與工作
### 資料清理

|            | Stroke | No Stroke | Sum  |
| ---------- | ------ | --------- | ---- |
| Government | 23     | 491       | 514  |
| Private    | 109    | 2092      | 2201 |
| Self-empl  | 48     | 581       | 629  |
| children   | **2**  | 685       | 687  |
| NeverWork  | **0**  | 22        | 22   |
| Sum        | 108    | 3164      | 3344 |

<span class ="blue">*孩童與未曾工作者的樣本數不適用於卡方檢定*</span>

### Chi-square

|            | Stroke | No Stroke | Sum  |
| ---------- | ------ | --------- | ---- |
| Government | 23     | 491       | 514  |
| Private    | 109    | 2092      | 2201 |
| Self-empl  | 48     | 581       | 629  |
| Sum        | 108    | 3164      | 3344 |

- $\chi^2$ = 7.8764, df = 2, p-value = 0.01948

```
> round(workStroke_chi$residuals, 3)
```

|            | Stroke | No Stroke |
| ---------- | ------ | --------- |
| Government | -0.887 | 0.212     |
| Private    | -0.870 | 0.208     |
| Self-empl  | **2.430**| -0.580    |

<span class="blue">*創業者在兩種分類的卡方檢定中，均顯示較容易中風，且具有統計意義，故在後續迴歸分析中，仍會考慮是否將工作類型作為解釋變數*</span>

### 兩兩分組做chi-square
#### Private
```
Work Type 1: children, Govt_job, Self-employed, Never_worked
Work Type 2: Private
```
|             |Stroke|No Stroke|    |
| ----------- |------|---------|--- |
| Work type 1 |100   |2085     |2185|
| Work type 2 |149   |2776     |2925|
|             |249   |4861     |5110|
- $\chi^2$ = 0.6149, df = 1, p-value = 0.4329
- 因此工作類型是否是私人企業(Private)與中風沒有顯著的關聯性

#### Self-employed
```
Work Type 1: children, Govt_job, Private, Never_worked
Work Type 2: Self-employed
```
|             |Stroke|No Stroke|    |
| ----------- |------|---------|--- |
| Work type 1 |184   |4107     |4291|
| Work type 2 |65    |754      |819 |
|             |249   |4861     |5110|
- $\chi^2$ = 18.97, df = 1, p-value = 1.328e-05
- 因此工作類型是否是自行創業者(Self-employed)與中風有顯著的關聯性

#### Govt_job
```
Work Type 1: children, Self-employed, Private, Never_worked
Work Type 2: Govt_job
```
|             |Stroke|No Stroke|    |
| ----------- |------|---------|--- |
| Work type 1 |216   |4237     |4453|
| Work type 2 |33    |624      |657 |
|             |249   |4861     |5110|
- $\chi^2$ = 0.0088896, df = 1, p-value = 0.9249
- 因此工作類型是否在政府機關(Govt_job)與中風沒有顯著的關聯性