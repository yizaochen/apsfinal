迴歸分析
=======================

## 變數關聯性分析
- 由上一章的列聯表分析，我們總結出了下面這張圖
   - "+"代表有關聯
   - "-"代表無關連 
```{image} ./images/all_vari_corre.jpg
:alt: all_vari_corre
:class: bg-primary mb-1
:width: 800px
:align: center
```
- 從表中可看出中風與性別及住處型態無關，因此先剔除。
- BMI與avg_glucose_level的分類根據上一章的建議
   - BMI $\rightarrow$ fitness
   - avg_glucose_level $\rightarrow$ diabetes

## 中風迴歸分析


先給程式碼
```
data<-read.csv(file='~/Desktop/Applied_Statistics/stroke-data.csv',header = TRUE)
data1<-data[which(data$smoking_status!='Unknown' & data$bmi!=
                    'N/A'),-c(2,8)]

#classifying BMI as 'fitness' factor
fitness<-data.frame(rep('NULL',times=length(data1$id)))
names(fitness)<-'fitness'
data2<-cbind(data1,fitness)
data2$fitness[which(data2$bmi<24)]<-'normal'
data2$fitness[which(data2$bmi>=24 & data2$bmi<27)]<-'overweight'
data2$fitness[which(data2$bmi>=27 & data2$bmi<30)]<-'light obesity'
data2$fitness[which(data2$bmi>=30 & data2$bmi<35)]<-'medium obesity'
data2$fitness[which(data2$bmi>=35)]<-'heavy obesity'

#classifying glucose into diabetes level
diabetes<-data.frame(rep('NULL',times=length(data2$id)))
names(diabetes)<-'diabetes'
data3<-cbind(data2,diabetes)
data3$diabetes[which(data3$avg_glucose_level<110)]<-'normal'
data3$diabetes[which(
  data3$avg_glucose_level>=110 & 
    data3$avg_glucose_level<130)]<-'pre-diabetes'
data3$diabetes[which(
  data3$avg_glucose_level>=130 & 
    data3$avg_glucose_level<160)]<-'diabetes'
data3$diabetes[which(
  data3$avg_glucose_level>=160)]<-'heavy diabetes'

#Logistic regression with relevant variables
stroke_full<-glm(stroke~age+factor(hypertension)
                 +factor(heart_disease)+factor(ever_married)
                 +factor(work_type)+factor(diabetes)
                 +factor(fitness)+factor(smoking_status),
    family=binomial(link = logit),data=data3)
summary(stroke_full)

```
先說結論，中風只跟年齡及高血壓有關。如果去掉其他變數，也會讓心臟病的關聯變顯著。其他變數都無顯著相關性。
我有嘗試做partial F-test，但是無法像講義一般跑出p-value，有興趣的可以跑看看

* Full model
假設不管顯著性，看一下結果：
Call:
glm(formula = stroke ~ age + factor(hypertension) + factor(heart_disease) + factor(ever_married) + factor(work_type) + factor(diabetes) +factor(fitness) + factor(smoking_status),family = binomial(link = logit), data = data3)
![](https://i.imgur.com/Tcvbt0T.png)
![](https://i.imgur.com/3YQpOVJ.png)

dummy variable的baseline分別是:
hypertension:no
heart_disease:no
evermarried:no
work_type:children
diabetes:diabetes
fitness:heavy obesity
smoking_status:ever_smoked

對照來看，年齡增加會增加中風機率；有高血壓會讓中風機率增加；有心臟病會增加中風機率；有結過婚會減少中風機率；私人公司上班中風機率最大，其次為公務人員，再其次為自雇者？，不工作者的中風機率甚至低於兒童（？）；嚴重糖尿病者會增加中風機率，而前期糖尿病及正常者中風機率降低；體態(BMI)只要不是嚴重肥胖都會降低中風機率；抽煙會增加中風機率，從不抽菸會降低中風機率

但是以上只有年齡跟高血壓有顯著性，心臟病在顯著邊緣。其他只能參考




* Significant reduced model
先給結果：
Call:
glm(formula = stroke ~ age + factor(hypertension) + factor(heart_disease), family = binomial(link = logit), data = data3)
![](https://i.imgur.com/32RnHtV.png)

可以看出年齡增加、有高血壓、有心臟病都會讓中風機率增加，且這三個變數都有顯著性。

* Partial F-test選變數
GLM如何應用的相關問題我有問老師，有興趣的可以跑一下看看：
```
#backward elimination via partial F-test
#stroke_reduced_1:eliminating work_type

stroke_reduced_1<-glm(stroke~age+factor(hypertension)
                 +factor(heart_disease)
                 ,
                 family=binomial(link = logit),data=data3)
summary(stroke_reduced_1)

anova(stroke_reduced_1,stroke_full)
```

### 簡單結論
會有這麼多變數不顯著的原因可能是中風人數跟沒中風人數的比例太懸殊(180:3426，約19倍)，因此一般推論會增加中風機率的變數都不太顯著。如果要改善可能要做case control，從沒中風的人中抽樣與中風人數相同的樣本來做回歸可能會比較正常。

###### tags: `apply_statistics`