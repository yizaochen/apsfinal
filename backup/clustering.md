Cluster analysis: 測試與中風組內分群
=======================
## 資料前置處理
### 隨機抽樣
1. 將中風的人分組看關聯性，但是如果做180個人可能會跑出密密麻麻的樹，所以我們從中抽20人，如下
   - ![](https://i.imgur.com/NQ4NJXL.jpg)
2. 並把數值跟類別變數換成成二元變數。
3. 分組依據: 參考前面分類，大致分成正常跟不正常。
4.  只有工作型態把兒童跟工作者分開。
#### 轉換後的資料：
  - ![](https://i.imgur.com/nYT6ZYx.png)

## 相似矩陣與距離矩陣
根據12章講義，我是用$\frac{a+d}{p}$的公式，也就是把兩個人相同的變數數量除以總變數量，在這裡總共有8個變數，所以是除以8就是兩個人之間的相似度。距離矩陣就是用1去減相似度矩陣得到的。

## 群聚樹
### 最大距離:
   - ![](https://i.imgur.com/uROuQjN.png)
### 平均距離：
   - ![](https://i.imgur.com/Bv95vx7.png)
### 最小距離：
   - ![](https://i.imgur.com/tDTuB0s.png)

## 分析
### Complete-linkage
![](https://i.imgur.com/CLfsYmG.png)
* 依照Complete-linkage cluster dendrogram可大致分成五群，以下為各群的詳細抽樣內容說明：
    * <font color="#3433FF">第一群：共通點為「無心臟疾病、大於50歲、已婚、有工作、BMI異常」</font>
        1. 第一層有兩小群：兩小群合併於第三層，一個差異在於<font color="#9133FF">”血糖是否正常“</font>
            - (8, 1, 7): 高血壓、無心臟疾病、大於50歲、已婚、有工作、血糖正常、BMI異常、有抽煙史
            - (17, 5, 15): 高血壓、無心臟疾病、大於50歲、已婚、有工作、血糖異常、BMI異常、有抽煙史
        2. 第二層：(2)與(8, 1, 7)合併，一個差異在於<font color="#9133FF">”有無高血壓“</font>
            - (2): 無高血壓、無心臟疾病、大於50歲、已婚、有工作、血糖正常、BMI異常、有抽煙史
        3. 第三層：(6)與(2, 8, 1, 7)和(17, 5, 15)合併，三個差異在於<font color="#9133FF">“有無高血壓”、“血糖是否正常”、“有無抽菸史”</font>
            - (6): 高血壓、無心臟疾病、大於50歲、已婚、有工作、血糖正常、BMI異常、無抽煙史
    * <font color="#3433FF">第二群：共通點為「高血壓、無心臟疾病、大於50歲、已婚、有工作、血糖異常、無抽煙史」</font>
        1. 第一層：
            - (3, 10): 高血壓、無心臟疾病、大於50歲、已婚、有工作、血糖異常、BMI正常、無抽煙史
        2. 第二層：(18)與(3, 10)合併，一個差異在於<font color="#9133FF">“BMI是否正常”</font>
            - (18): 高血壓、無心臟疾病、大於50歲、已婚、有工作、血糖異常、BMI異常、無抽煙史
    * <font color="#3433FF">第三群：共通點為「無高血壓、大於50歲、已婚、有工作、血糖異常、BMI異常、有抽煙史」</font>
        1. 第一層有兩小群：兩小群合併於第二層，一個差異在於<font color="#9133FF">“有無心臟疾病”</font>
           - (4, 16): 無高血壓、有心臟疾病、大於50歲、已婚、有工作、血糖異常、BMI異常、有抽煙史
           - (20, 14, 12, 13): 無高血壓、無心臟疾病、大於50歲、已婚、有工作、血糖異常、BMI異常、有抽煙史
    * <font color="F83344">以上，第一、二、三群合併於第四層，共通點為「大於50歲、已婚、有工作」</font>
    *  <font color="#3433FF">第四群：共通點為「高血壓、有心臟疾病、大於50歲、未婚、有工作、BMI正常、有抽煙史」</font>
        1. 第一層：在整體的第二層出現，一個差異在於<font color="#9133FF">“血糖是否異常”</font>
            - (9): 高血壓、有心臟疾病、大於50歲、未婚、有工作、血糖異常、BMI正常、有抽煙
            - (19): 高血壓、有心臟疾病、大於50歲、未婚、有工作、血糖正常、BMI正常、有抽煙
    * <font color="F83344">以上，第四群與第一、二、三群合併於第五層，共通點為「大於50歲、有工作」</font>
    * <font color="#3433FF">第五群：</font>
        1. 第一層：只有一位
            - (11): 無高血壓、無心臟疾病、小於50歲、未婚、有工作、血糖正常、BMI正常、有抽煙史
    * <font color="F83344">全圖，第五群與第一、二、三、四群合併於第六層，共通點為「有工作」</font>
* 各群的第一個決策點：
    1. 第一群中，(2)與(8, 1, 7)的決策為「是否有高血壓」
    2. 第二群中，(18)與(3, 10)的決策為「BMI是否正常」
    3. 第三群中，(4, 16)與(20, 14, 12, 13)的決策為「有無心臟疾病」
    4. 第四群中，(9)與(19)的決策為「是否有高血壓」

### Average-linkage
![](https://i.imgur.com/YEtZkus.png)
* 在Average-linkage cluster dendrogram中，可以發現與Complete-linkage cluster dendrogram只有些微的不同。
    - (6)被提出到更下一層: 代表(6)、(17, 5, 15)、(2, 8, 1, 7)這三小群的最大距離相同，但在平均距離上，(6)與其他兩小群的平均距離比(17, 5, 15)和(2, 8, 1, 7)的平均距離更大。
    - (9, 19)也被提出到更下一層
