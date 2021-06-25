Chapter 2: 資料集基本介紹
=======================
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

## 中風的分佈
```{image} https://i.imgur.com/BJbNHxr.png
:alt: strokebar
:class: bg-primary mb-1
:width: 800px
:align: center
```
- 在這組資料裏面，中風的人佔了5%，非中風的人佔了95%
<p style="page-break-before: always">

## 其他變數分佈
```{image} https://i.imgur.com/ShTO5La.png
:alt: strokebar
:class: bg-primary mb-1
:width: 800px
:align: center
```
<p style="page-break-before: always">