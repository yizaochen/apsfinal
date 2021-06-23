資料探討
=======================
<style>
.blue {
    color: blue;
}

.grey {
    color: grey;
}

.awk {
    color: #b6b4cf;
}
</style>

## 資料來源
- 我們選擇了一筆2018年釋出的網路資料
  - [McKinsey Analytics: Online Hackathon on Healthcare](https://datahack.analyticsvidhya.com/contest/mckinsey-analytics-online-hackathon/)

## 資料清理
- 我們將符合以下條件的資料清掉
   - Gender為Other
   - BMI為N/A
   - Smoking status為Unknown

## 資料基本型態
- 資料總數: 3425個人 (清理前為5110)
- 類別型: gender, hypertension, heart_disease, ever_married, work_type, Residence_type, smoking_status, stroke
- 數值型: age, avg_glucose_level, bmi

## 單變數分析: 類別型
### Stroke
```{image} https://i.imgur.com/BJbNHxr.png
:alt: strokebar
:class: bg-primary mb-1
:width: 800px
:align: center
```

## 單變數分析: 數值型
### 所有中風的人:年紀與性別的分佈
```{image} https://i.imgur.com/eHOKXqd.png
:alt: age
:class: bg-primary mb-1
:width: 800px
:align: center
```
### BMI
#### 整體資料BMI分佈
```{image} https://i.imgur.com/UoOZ8vh.png
:alt: bmi_distribution
:class: bg-primary mb-1
:width: 800px
:align: center
```
#### 分成中風與非中風
- 下圖呈現條件機率 $P(\text{stroke}|\text{BMI:group})$ 與 $P(\text{Non-stroke}|\text{BMI:group})$
- ![](https://i.imgur.com/DMvA9b9.png)  
  

## 資料綜觀
![](https://i.imgur.com/KF0MfYP.png)

<span class="grey">*註: 以上資料在類別變數分析中，均會依據狀況刪去部分資料，因此各項初步分析中的資料數可能不盡一致。但在分群分析與迴歸分析中，若有任一欄為「unknown」、「N/A」、或「null」，該筆資料會整筆刪除，採用內容一致的資料集。*</span>
