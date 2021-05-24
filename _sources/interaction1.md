因素之間交互作用
=======================
## 其他因素與心臟病的關聯
### 心臟病與性別
#### Odds Ratio
  - ![](https://i.imgur.com/k7QT2XQ.png)
  - Odds ratio $\hat{\theta}=2.129$
  - 95% Confidence Interval of $\log{(\hat{\theta})}=(0.509, 1.002)$
#### Chi-square
|          |Female|Male  |Sum |
| -------- |------|------|--- |
| HeartD   |113   |162   |206 |
| Normal   |2881  |1952  |3112|
| Sum      |2994  |2114  |5108|
>gender of others were not included
- $X^2$ = 36.031,  df = 1,  p-value = 1.942e-09
   - 故性別與心臟病關係並不獨立，與odds ratio結果相符
- 且根據residual下表顯示，女性較不容易罹患心臟疾病，男性則有較高機會罹患心臟病
* round(result_cvdGender$residuals, 3)
    |          | Female | Male   |
    | -------- | ------ | ------ |
    | HeartD   | -3.796 | 4.517  |
    | Normal   | 0.905  | -1.077 |

### 心臟病與居住環境
#### Odds Ratio
  - ![](https://i.imgur.com/tdhkXh9.png)
  - Odds ratio $\hat{\theta}=0.973$
  - 95% Confidence Interval of $\log{(\hat{\theta})}=(-0.270, 0.215)$
#### Chi-square
- 以下範圍為年紀>=16之統計

| Residence | Rural  | Urban  |Sum |
| --------- | ------ | ------ |--- |
| HeartD    | 134    | 141    |275 |
| normal    | 2013   | 2078   |4091|
| Sum       | 2147   | 2219   |4366|

- $X^2$ = 0.0083308,  df = 1,  p-value = 0.9273
- 故居住地與心臟病關係並**無顯著相關性**，與odds ratio結果相符
> 若將資料涵蓋小於16歲的樣本，也可見同樣的趨勢

* round(result_CVDresid$residuals, 3)
    | Residence | Rural  | Urban  |
    | --------- | ------ | ------ |
    | HeartD    | -0.106 | 0.104  |
    | Normal    | 0.027  | -0.027 |

### 心臟病與婚姻
#### Odds Ratio
  - ![](https://i.imgur.com/E0kh7xu.png)
  - Odds ratio $\hat{\theta}=  4.231$
  - 95% Confidence Interval of $\log{(\hat{\theta})}=(1.069, 1.816)$
#### Chi-square
- 以下範圍為年紀>=16之統計

| EverMarr |Yes   | No   |Sum |
| -------- |------|------|--- |
| HeartD   |244   |31    |275 |
| normal   |3109  |982   |4091|
| Sum      |206   |3113  |4366|

- $X^2$ = 22.73,  df = 1,  p-value = 1.864e-06
-故結婚經驗有否與心臟病關係並不獨立，與odds ratio結果相符，且根據residual下表顯示，有婚姻經驗較容易罹患心臟病

* round(result_cvdGender$residuals, 3)
    | EverMarr | Yes    | No     |
    | -------- | ------ | ------ |
    | HeartD   | 2.257  | -4.107 |
    | Normal   | -0.585 | 1.065  |

### 心臟病與高血壓
#### Odds Ratio
  - ![](https://i.imgur.com/yRSczJF.png)
  - Odds ratio $\hat{\theta}=3.061$
  - 95% Confidence Interval of $\log{(\hat{\theta})}=(0.822, 1.415)$
#### Chi-square

| Residence | Hyper  | Normal |Sum |
| --------- | ------ | ------ |--- |
| HeartD    | 64     | 434    |498 |
| normal    | 212    | 4400   |4612|
| Sum       | 276    | 4834   |5110|
- $X^2$ = 58.337,  df = 1,  p-value = 2.209e-14
- 故高血壓與心臟病關係**具顯著相關性**，與odds ratio結果相符，且具高血壓的患者易伴隨有心臟病。
* round(result_HDhyper$residuals, 3)
    | Residence | Hyper  | Normal |
    | --------- | ------ | ------ |
    | HeartD    | 7.154  | -1.709 |
    | Normal    | -2.351 | 0.562  |


### 心臟病與抽煙
#### Odds Ratio
  - ![](https://i.imgur.com/YNKlrv7.png)
  - Odds ratio $\hat{\theta}=1.799$
  - 95% Confidence Interval of $\log{(\hat{\theta})}=(0.313, 0.861)$

#### Chi-square
>smoking status of unknown is removed

| smoking | smokes | formerly | never | Sum   |
| ------- | ------ | -------- | ----- | ----- |
| HeartD  | 61     | 77       | 90    | 228   |
| Normal  | 728    | 808      | 1802  | 3338  |
| Sum     | 789    | 885      | 1892  | 3566  |
- $X^2$ = 18.698,  df = 2,  p-value = 8.707e-05
- 故抽菸習慣與心臟病關係**具顯著相關性**，與odds ratio結果相符，由residual觀察曾有抽菸習慣者，甚至比正在抽菸者有更高機會罹患心臟病，與中風傾向相同。

* round(result_HDsmoke$residuals, 3)
    | smoking | smokes | formerly | never  |
    | ------- | ------ | -------- | ------ |
    | HeartD  | 1.486  | 2.714    | -2.816 |
    | Normal  | -0.388 | -0.709   | 0.736  |


## 其他因素與婚姻的關聯
### 婚姻與性別
#### Odds Ratio
  - ![](https://i.imgur.com/FHIOPXF.png)
  - Odds ratio $\hat{\theta}= 0.879$，表示**婚姻與性別有相關**。
  - 95% Confidence Interval of $\log{(\hat{\theta})}=(-0.245, -0.012)$
     - 95%的信賴區間不包含0
#### Chi-square
> remove the gender of others

| gender  | Female | Male  |Sum |
| ------- | ------ | ----- |--- |
| Married | 2001   | 1352  |3353|
| NevMarr | 1352   | 370   |1012|
| Sum     | 2643   | 1722  |4365|
$X^2$ = 4.4469, df = 1, p-value = 0.03497
* round(result_MarGender$residuals, 3)
    | gender  | Female | Male  |
    | ------- | ------ | ----- |
    | Married | -0.649 | 0.804 |
    | NevMarr | 1.181  | -1.463|
    
- 結果顯示**婚姻與性別關係不獨立**，女性較傾向單身，男性易有結婚經驗。然而須注意的是，在如此巨大的樣本數下，多種情況即便差異不大也會顯示具有統計顯著性，而在本檢定中，p-value僅稍稍小於0.05，且我們不確定採樣的母體是否位於同性婚姻合法化的地區，或是樣本是否為自願受試，而婚姻經驗又與受試意願不夠獨立。倘若同性婚姻合法為否，男女結婚狀況比例應一致，倘若為是，依據下面連結所示，女性具有婚姻經驗的結果應較高，residual應為正，故本檢定結果可能在本報告中無法被解釋。
   - [Gay marriage data shows more women are tying the knot](https://www.abc.net.au/news/2019-11-29/same-sex-gay-marriage-women-more-likely-to-wed-marry/11555456)

### 婚姻與高血壓
#### Odds Ratio
  - ![](https://i.imgur.com/njZCKOB.png)
  - Odds ratio $\hat{\theta}= 4.920$，表示**婚姻與高血壓不是獨立的**。
  - 95% Confidence Interval of $\log{(\hat{\theta})}=(1.302, 1.884)$
#### Chi-square
| hyperT  | hyperT | Normal |Sum |
| ------- | ------ | ------ |--- |
| Married | 445    | 2908   |3353|
| NevMarr | 53     | 960    |1013|
| Sum     | 498    | 3868   |4366|
$X^2$ = 48.969, df = 1, p-value =2.601e-12
* round(result_MarHypertension$residuals, 3)
    | hyperT  | hyperT | Normal |
    | ------- | ------ | ------ |
    | Married | 3.198  | -1.148 |
    | NevMarr | -5.819 | 2.088  |

- 結果顯示**婚姻經驗與高血壓相關**，婚姻經驗者傾向有高血壓。
  
### 婚姻與抽煙
#### Odds Ratio
  - ![](https://i.imgur.com/NWC2Dxp.png)
  - Odds ratio $\hat{\theta}= 1.609$，表示**婚姻與抽煙不是獨立的**。
  - 95% Confidence Interval of $\log{(\hat{\theta})}=(0.318, 0.633)$
#### Chi-square
> data with unknown smoking status were not taken into consideration

| smoking | smokes | formerly | never | Sum   |
| ------- | ------ | -------- | ----- | ----- |
| Married | 610    | 738      | 1362  | 2710  |
| NevMarr | 176    | 128      | 443   | 747   |
| Sum     | 786    | 866      | 866   | 3457  |
$X^2$  = 33.295, df = 2, p-value = 5.891e-08
- 與odds ration結果相近，**婚姻與抽菸習慣並不獨立**，針對下表或許我們可以這樣解讀：對於曾有結婚經驗者，他們有較高機會成為成功戒菸者(formerly smoked)，對於單身者而言，則明顯較難，但他們與已婚者(或離婚失婚者相比)更有可能從未有抽菸習慣。
* round(result_HDsmoke$residuals, 3)
    | smoking | smokes | formerly | never  |
    | ------- | ------ | -------- | ------ |
    | Married | -0.248 | 2.269    | -1.408 |
    | NevMarr | 0.473  | -4.322   | 2.682  |

### 婚姻與bmi
#### Chi-square
>移除BMI unknown值

| Category    | BMI     | Married | NevMarri | Sum  |
| ----------- | ------- | ------- | -------- | ---- |
| underWeight | <18.5   | 26      | 16       | 42   |
| healthy     | 18.5-24 | 422     | 285      | 707  |
| overWeight  | 24-27   | 584     | 175      | 759  |
| slightObesi | 27-30   | 655     | 165      | 820  |
| mid-Obesity | 30-35   | 793     | 165      | 958  |
| heaviObesi  | >35     | 724     | 172      | 896  |
| Sum         |         | 3204    | 978      | 4182 |
$X^2$ = 152.12,  df = 5,  p-value < 2.2e-16

結果顯示**婚姻與BMI不獨立**，曾有結婚經驗者有高傾向成為肥胖，單身者同時體態健康則較為容易。-->幸福肥？
* round(result_bmiMarital$residuals, 3)
    | Category    | BMI     | Married | NevMarri |
    | ----------- | ------- | ------- | -------- |
    | underWeight | <18.5   | -1.089  | 1.971    |
    | healthy     | 18.5-24 | -5.142  | 9.306    |
    | overWeight  | 24-27   | 0.104   | -0.188   |
    | slightObesi | 27-30   | 1.068   | -1.933   |
    | mid-Obesity | 30-35   | 2.179   | -3.944   |
    | heaviObesi  | >35     | 1.433   | -2.593   |


## BMI & Age
### Chi-square
- BMI的計算本不適用於嬰兒，故移除小於(含)兩歲之嬰兒，並移除BMI unknown值
- Since sample size of youth was too small, heavily obesity was then merged into mid-Obesity.

| BMI/Age | Age Range | UnderWei | Healthy | OverWei | slight Obe | Obesity | Sum  |
| ------- | --------- | -------- | ------- | ------- | ---------- | ------- | ---- |
| BMI Ran |           | <18.5    | 18.5-24 | 24-27   | 27-30      | >30     |      |
| youth   | 02 - 12   | 186      | 135     | 16      | 13         | 10      | 360  |
| teen    | 13 - 17   | 31       | 135     | 54      | 30         | 57      | 307  |
| youngAd | 18 - 35   | 12       | 276     | 207     | 171        | 347     | 1013 |
| mid-Age | 36 - 55   | 18       | 194     | 287     | 356        | 741     | 1469 |
| elder   | 56-       | 8        | 190     | 247     | 283        | 736     | 1591 |
| Sum     |           | 255      | 930     | 811     | 853        | 1891    | 4740 |
$X^2$ = 2194.1,  df = 16,  p-value < 2.2e-16
- 登燈，驚不驚喜？意不意外？**年齡與BMI有顯著相關性**
* round(result_bmiAge$residuals, 3)
    | BMI/Age | Age Range | UnderWei | Healthy | OverWei | slight Obe | Obes    |
    | ------- | --------- | -------- | ------- | ------- | ---------- | ------- |
    | BMI Ran |           | <18.5    | 18.5-24 | 24-27   | 27-30      | >30     |
    | youth   | 02 - 12   | ==37.864==|==7.659==| -5.810  | -6.434    | -11.150 |
    | teen    | 13 - 17   | ==3.564==|==9.633== | 0.203   | -3.397    | -5.916  |
    | youngAd | 18 - 35   | -5.757   | ==5.479==|==2.558==| -0.837    | -2.842  |
    | mid-Age | 36 - 55   | -7.990   | -5.786  | -0.274  | ==1.147==  | ==6.401== |
    | elder   | 56-       | -7.306   | -6.688  | 0.896   | ==4.118==  | ==4.020== |
 
 - MURMUR: 就演化或是人類生長週期(?)的角度而言，其實這樣的分布狀況是可以理解的，青少年以前，生長快速，代謝的迅速程度讓身體無暇儲存養分，青少年後段至青壯年時期，生長停滯，且處於人生巔峰期，體態自然維持在最佳狀態，故而可見體重趨勢在青少年由過輕，漸漸往健康移動，到了中年與老年，細胞本身工作能力已降低，對於細胞本身而言，更趨向休眠狀態，更遑論已趨衰老抵抗氧化壓力等等能力大幅降低下，會自然更趨向儲存能量，故而在人體反應肥胖狀態。