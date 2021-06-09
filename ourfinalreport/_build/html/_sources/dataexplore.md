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


## 資料基本型態
- 資料總數: 5110個人
- 類別型: gender, hypertension, heart_disease, ever_married, work_type, Residence_type, smoking_status, stroke
- 數值型: age, avg_glucose_level, bmi

## 單變數分析: 類別型

### gender
```{image} ./images/gender_bar_pie.png
:alt: gender
:class: bg-primary mb-1
:width: 800px
:align: center
```
<span class="blue">*一筆資料被紀錄為Others，基於分析結果的可信度考量，後面關於性別的類別變數分析均不使用該筆資料*</span>

### Hypertension
```{image} ./images/hypert_bar_pie.png
:alt: hypertension
:class: bg-primary mb-1
:width: 800px
:align: center
```

### Heart Disease
```{image} ./images/heartd_bar_pie.png
:alt: heartdisease
:class: bg-primary mb-1
:width: 800px
:align: center
```

### Ever married
```{image} ./images/evermarry_bar_pie.png
:alt: evermarry
:class: bg-primary mb-1
:width: 800px
:align: center
```
<span class="blue">*簡單類別型解釋變數分析中，若用於分析婚姻經驗與其他變數的關係，剔除年齡小於16歲的資料*</span>

### Residence type
```{image} ./images/resit_bar_chart.png
:alt: residtype
:class: bg-primary mb-1
:width: 800px
:align: center
```

### Stroke
```{image} ./images/stroke_bar_pie.png
:alt: strokebar
:class: bg-primary mb-1
:width: 800px
:align: center
```

### Smoking status
```{image} ./images/smoking_bar_pie.png
:alt: smoking
:class: bg-primary mb-1
:width: 800px
:align: center
```
<span class="blue">*Unknown資料於使用到smoking_status的變數的類別型分析中均已剃除，值得注意的是，下面histogram紀錄所有抽菸狀態未知的資料總共1544筆，其中635筆為小於等於十六歲的樣本(虛線)，也就是說剔除的樣本約有一半屬於孩童或是青少年*</span>
![](https://i.imgur.com/qQdT9fT.png)

### Work type
```{image} ./images/worktype_bar_pie.png
:alt: worktype
:class: bg-primary mb-1
:width: 800px
:align: center
```

## 單變數分析: 數值型
### 年齡
#### 整體資料年齡分佈
```{image} ./images/age_distribution.png
:alt: age
:class: bg-primary mb-1
:width: 800px
:align: center
```
#### 分成中風與非中風
```{image} https://i.imgur.com/mwyEex0.png
:alt: age
:class: bg-primary mb-1
:width: 800px
:align: center
```

#### 所有中風的人:年紀與性別的分佈
```{image} https://i.imgur.com/eHOKXqd.png
:alt: age
:class: bg-primary mb-1
:width: 800px
:align: center
```

### Average glucose level
<span class="grey">*註: 雖然不確定收集資料時是取飯前(FPG)或是飯後血糖(OGTT)，本報告仍先採用空腹血糖做為參考標準。*</span>

#### 整體資料血糖分佈
```{image} ./images/avg_glucose_distribution.png
:alt: avg_glucose
:class: bg-primary mb-1
:width: 800px
:align: center
```
#### 分成中風與非中風
- 下圖呈現條件機率 $P(\text{stroke}|\text{Glu:group})$ 與 $P(\text{Non-stroke}|\text{Glu:group})$
- ![](https://i.imgur.com/Wf9P7xi.png)

### BMI
#### 整體資料BMI分佈
```{image} ./images/bmi_distribution.png
:alt: bmi_distribution
:class: bg-primary mb-1
:width: 800px
:align: center
```
#### 分成中風與非中風
- 下圖呈現條件機率 $P(\text{stroke}|\text{BMI:group})$ 與 $P(\text{Non-stroke}|\text{BMI:group})$
- ![](https://i.imgur.com/DMvA9b9.png)  
  
  
<span class="grey">*註: 以上資料在類別變數分析中，均會依據狀況刪去部分資料，因此各項初步分析中的資料數可能不盡一致。但在分群分析與迴歸分析中，若有任一欄為「unknown」、「N/A」、或「null」，該筆資料會整筆刪除，採用內容一致的資料集。*</span>
