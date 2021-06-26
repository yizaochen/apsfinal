Chapter 14: 結論與討論
=======================
## 資料探討、列聯表、機率分析
首先，根據列聯表、分佈圖還有機率分析，我們做了一張矩陣表格來總結變數之間的關係

```{image} ./images/all_vari_corre.jpg
:alt: all_vari_corre
:class: bg-primary mb-1
:width: 800px
:align: center
```
- 綠色+號格子代表，兩兩變數是有關聯的
- 灰色-號格子代表，兩兩變數不相關
- 在這裡，我們想了解其他解釋變數跟中風的關係，聚焦在第二個column
    - 與中風無關的解釋變數有兩個: 性別與居住地
    - <span style="color:blue"> 與中風高度相關的: 年齡、結婚、高血壓、心臟病、血糖 </span>
    - <span style="color:blue"> 與中風有相關但不是很顯著: 工作、抽煙、BMI </span>

## Age as Confounding Effect
- 如果已知年齡，高血壓對於中風提供的資訊相對就少
- 年齡與心臟病對中風的提升是相互加成，尤其是對於60-69歲,80-89歲這兩個區段
- 目前懷疑可能是因為中風人數小於50歲的過少，導致年齡最能觀察出的更年期現象在這次的分析中看不太出有什麼影響力。不過有趣的是，在多組分組分析中，過了60-69歲這個門檻，我們就姑且說70歲吧，到下一個年齡層的斜率會上升，可見年齡對於該組別中風的影響到了70歲之後越趨上升，例如戒菸者、未曾抽菸者、女性，但在心臟病者中，50~80歲，年齡對中風機會的影響幾無改變，但整體而言，年齡都會和這些類別變數產生交互作用。

## 累積機率探討交互作用
* 採用累積機率的方式探討不同變數因子對於中風是否具有交互作用。將其中一變數作為橫軸劃分區間，另一變數依類別個別畫出累積分佈曲線，經由累積分佈曲線的斜率變化可以判斷是否在不同的橫軸變數區間產生交互影響。而如果圖形大致重疊則可以判斷變數之間並無交互作用。
* 採用機率分佈取代實際數量的好處，在於可以去除不同族群個數的差異，將資料正規化(normalization)，比較可以看出不同族群間整體變化的趨勢進而做比較。
* 在實作過程中，若橫軸變數的類別順序固定的情況下，對於不同變數的累積分佈曲線，產生敏感變化的區間會不盡相同。因此對於橫軸類別順序的選擇必須隨著觀察資料適時調整，才比較能看出變化的趨勢。

## Logistic Regression
$$
\log{\left(\frac{P[\rm{stroke}=1]}{P[\rm{stroke}=0]}\right)} = \beta_0 + \beta_{\rm{hypert}}x_{\rm{hypert}}+ \beta_{\rm{heartd}}x_{\rm{heartd}}+ \beta_{\rm{age}}x_{\rm{age}} + \beta_{\rm{glucose}}x_{\rm{glucose}}
$$
- 最後考量的解釋變數為: 年齡、高血壓、心臟病、血糖，可以發現結婚這個變數被拿掉了。

## Cluster Analysis
綜合兩部分的cluster analysis，中風與非中風樣本皆無法完全地分群，但都有某個小群中涵蓋較多的中風比例，進而可推測該群的非中風樣本健康狀態有較高的中風風險。


#### [回到目錄](./tablecontent.md)
<p style="page-break-before: always">