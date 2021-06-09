Cluster analysis: 中風者與非中風者做分群
=======================
<style>
.blue {
    color: blue;
}

.awk {
    color: #b6b4cf;
}
</style>

<span class="blue">*在這部份，我們從中風與非中風的樣本中各隨機抽樣10人進行分群分類，觀察前面列聯表分析與回歸分析中顯示對中風具有相關性的變數，能造成中風與非中風者的分群。在分群距離計算方法中方法中，我們一開始考慮了single linkage、complete linkage、average linkage clustering，然而，single-linkage分群結果較不顯著，complete linkage與average-linkage的結果類似，我們最後採用complete linkage完成後續分析。*</span>

## 中風者與非中風者各抽樣10人進行分組分析
* 隨機抽樣資料
    - 1-10號是有中風的人，11-20號是抽樣無中風的人
    ![](https://i.imgur.com/9MD58ie.png)
    - 原始數據
    ![](https://i.imgur.com/Ptmqx54.png)
    
* 群聚樹分析：
    1. Single-linkage cluster dendrogram
        ![](https://i.imgur.com/xppKwGa.jpg)
        - 用最小距離分群的結果看起來很怪異，沒有一個分群的感覺。

    2. Complete-linkage cluster dendrogram
        ![](https://i.imgur.com/43crdm1.jpg)
        - 由上圖可以大致分成三組：
        ![](https://i.imgur.com/MBMvqWk.jpg)
            1. 第一群：含有<font color="#F71E86">9個中風者(81.8%)</font>、<font color="#0517B7">2個無中風者(18.2%)</font>，屬「高風險族群」
                - 共通點為「大於50歲」、「已婚」、「有工作」
                - 這組混雜了較多的抽樣，因此共通點較少。但看細一點可發現此群可以再細分為三小群。若只依照這幾個健康數據分析，當中
                    (1)最右邊的小群其身體狀況最差，皆為中風患者，皆有血糖異常與抽菸史
                    (2)中間的小群中含有一個非中風樣本，健康狀況中等，雖也皆有血糖異常與抽菸史，但全部皆無高血壓
                    (3)左邊的小群含有一個非中風樣本，身體狀況大部分正常，只有一個有BMI的問題
                - 這群較特別的是涵蓋了所有有抽菸史的樣本
            2. 第二群：含有<font color="#F71E86">1個中風者(25%)</font>、<font color="#0517B7">3個無中風者(75%)</font>，屬「中風險族群」
                - 共通點為「高血壓」、「大於50歲」、「有工作」、「BMI異常」、「無抽煙」
                - 雖然這群也混雜了中風與非中風樣本，但可以發現唯一的一位中風患者被分在最外層，是這群中較不一樣的，最大距離最遠。
            3. 第三群：含有<font color="#0517B7">5個無中風者(100%)</font>，屬「低風險族群」
                - 共通點為「無高血壓」、「無心臟疾病」、「小於50歲」、「血糖正常」、「BMI正常」、「無抽菸史」
                - 這群皆為非中風樣本，可以明顯地發現他們的身體狀況與生活型態皆較健康
        - 綜合結果：以最大距離分群可以初略得將樣本歸類在高風險、中風險與低風險等三族群，但單以分群似乎無法作出準確的判斷是否中風
        

    3. Average-linkage cluster dendrogram
        ![](https://i.imgur.com/eY0RS00.jpg)
        - 與Complete-linkage cluster dendrogram比較，大部分分群結果相似：
            1. (9)從高風險族群跑到中風險族群，但仍在較外層，因此仍然屬於中風險族群中較不健康的樣本
            2. 低風險族群的樣本都沒變

## Ten Trees
```
＊抽樣方法：從中風與非中風的兩群人中，個別隨機抽樣10組不重複的10個人。
＊分群資料：每顆群聚樹含有中風與非中風各一組隨機抽樣樣本，共20人。
        (1-10為有中風，11-20為沒中風)
＊分群方法：Complete-linkage cluster dendrogram
＊比例計算：同群裡去算多少比例有中風、多少比例沒中風。
          例如某一個小群裡有10人(100%)，有2人中風(20%)，有8人沒中風(80%)。

＊初步結論：只有Tree1, 2, 3, 8, 9有較明顯的中風與非中風分群
```
### Tree 1 👍
* 隨機抽樣資料：
![](https://i.imgur.com/UdQGtoU.png)
![](https://i.imgur.com/maGCLmZ.png)

* 群聚樹分析：
![](https://i.imgur.com/gmJ4fBh.jpg)
    - 最外層可分為兩群：
        - 左：含有<font color="#F71E86">10個中風者(76.9%)</font>、<font color="#0517B7">3個無中風者(23.1%)</font>
            - 共通點：已婚、有工作
            - 其他重點：92.3%大於50歲、92.3%BMI異常、84.6%有抽煙
        - 右：含有<font color="#0517B7">7個無中風者(100%)</font>
            - 共通點：無高血壓、無心臟疾病、有工作、血糖正常
            - 其他重點：71.4%小於50歲
    - 綜合此組抽樣的數據，此群聚樹的分群重點為<font color="F83344">有無高血壓、有無心臟疾病、血糖是否正常</font>。當樣本的這三項數據皆正常時，將會被準確的分到無中風風險的族群，相反的，若是有其中一項異常則會有中風的風險。另外，左群高中風風險的族群大部分大於50歲，而右群無中風風險的族群大部分小於50歲，因此認為<font color="F83344">年齡是否大於50歲</font>也是個關鍵的變數。

### Tree 2 👍
* 隨機抽樣資料：
![](https://i.imgur.com/nV5wYOP.png)
![](https://i.imgur.com/IS9pHxW.png)

* 群聚樹分析：
![](https://i.imgur.com/kXm5XuT.jpg)
    - 最外層可分為兩群：
        - 左：含有<font color="#F71E86">6個中風者(85.7%)</font>、<font color="#0517B7">1個無中風者(14.3%)</font>
            - 共通點：大於50歲、已婚、有工作、血糖異常
            - 其他重點：71.4%BMI異常
        - 右：含有<font color="#F71E86">4個中風者(30.8%)</font>、<font color="#0517B7">9個無中風者(69.2%)</font>
            - 共通點：無心臟疾病、有工作、血糖正常
            - 其他重點：53.8%小於50歲、92.3%BMI異常
    - 綜合此組抽樣的數據，此群聚樹的分群重點為<font color="F83344">血糖是否異常</font>。另外，在左群的皆大於50歲，而右群的一半以上小於50歲，因此<font color="F83344">年齡是否大於50歲</font>似乎也是分群的潛在關鍵因素之一。

### Tree 3 👍
* 隨機抽樣資料：
![](https://i.imgur.com/bBcdDZk.png)
![](https://i.imgur.com/6n9Dc0L.png)

* 群聚樹分析：
![](https://i.imgur.com/SBXhdxe.jpg)
    - 最外層可分為兩群：
        - 左：含有<font color="#F71E86">6個中風者(85.7%)</font>、<font color="#0517B7">1個無中風者(14.3%)</font>
            - 共通點：大於50歲、已婚、有工作、BMI異常、有抽菸史
            - 其他重點：57.1%有高血壓
        - 右：含有<font color="#F71E86">4個中風者(30.8%)</font>、<font color="#0517B7">9個無中風者(69.2%)</font>
            - 共通點：無心臟疾病、有工作
            - 其他重點：92.3%無高血壓、53.8%無抽菸史
    - 綜合此組抽樣的數據，此群聚數沒有很明顯的分群因素，但可以發現<font color="F83344">是否大於50歲、BMI是否正常、是否有抽煙史</font>是可能影響分群的關鍵變數，因當此三者同時異常時，將會被分到具有較高比例中風者的族群。另外，在未中風較多的右群中，大部分的樣本皆無高血壓，同時也都沒有心臟疾病，因此推論<font color="F83344">是否有高血壓與是否有心臟疾病</font>也是分群的潛在因素。

### Tree 4 ☠️
* 隨機抽樣資料：
![](https://i.imgur.com/FHQ3MqH.png)
![](https://i.imgur.com/weam0Oa.png)

* 群聚樹分析：
![](https://i.imgur.com/zwQnp3F.jpg)
    - 此棵樹沒有明顯的中風與非中風分群關係
    - 最外層可分為兩群：
        - 左：含有<font color="#F71E86">2個中風者(40%)</font>、<font color="#0517B7">3個無中風者(60%)</font>
        - 右：含有<font color="#F71E86">8個中風者(53.3%)</font>、<font color="#0517B7">7個無中風者(46.7%)</font>

### Tree 5 ☠️
* 隨機抽樣資料：
![](https://i.imgur.com/zEAqYX4.png)
![](https://i.imgur.com/OoLZ5YX.png)

* 群聚樹分析：
![](https://i.imgur.com/RkTtwOD.jpg)
    - 此棵樹沒有明顯的中風與非中風分群關係

### Tree 6 ☠️
* 隨機抽樣資料：
![](https://i.imgur.com/SDLlOWw.png)
![](https://i.imgur.com/zcw0Dtv.png)

* 群聚樹分析：
![](https://i.imgur.com/HNQyQaE.jpg)
    - 此棵樹沒有明顯的中風與非中風分群關係

### Tree 7 ☠️
* 隨機抽樣資料：
![](https://i.imgur.com/hQQjqJb.png)
![](https://i.imgur.com/lxPIWjj.png)

* 群聚樹分析：
![](https://i.imgur.com/7GPOzP6.jpg)
    - 此棵樹沒有明顯的中風與非中風分群關係
    - 最外層可分為兩群：
        - 左：含有<font color="#F71E86">7個中風者(50%)</font>、<font color="#0517B7">7個無中風者(50%)</font>
        - 右：含有<font color="#F71E86">3個中風者(50%)</font>、<font color="#0517B7">3個無中風者(50%)</font>

### Tree 8 👍
* 隨機抽樣資料：
![](https://i.imgur.com/FoKXj3R.png)
![](https://i.imgur.com/B1pG8eg.png)

* 群聚樹分析：
![](https://i.imgur.com/SVCuMNs.jpg)
    - 最外層可分為兩群：
        - 左：含有<font color="#F71E86">4個中風者(100%)</font>
            - 共通點：有高血壓、無心臟疾病、大於50歲、已婚、有工作
            - 其他重點：75%有抽煙史
        - 右：含有<font color="#F71E86">6個中風者(37.5%)</font>、<font color="#0517B7">10個無中風者(62.5%)</font>
            - 共通點：無心臟疾病、有工作、血糖正常
            - 其他重點：87.5%無高血壓、87.5%無抽菸史
    - 綜合此組抽樣的數據，此群聚數的分群重點為<font color="F83344">有無高血壓、有無抽菸史</font>，因為這兩項數據在兩群中是相對立的：在左群皆是中風者的族群中皆有高血壓且高比例有抽煙史，而在右群無中風者比例較高的族群中大部分為無高血壓且無抽菸史。

### Tree 9 👍
* 隨機抽樣資料：
![](https://i.imgur.com/cpTRuDx.png)
![](https://i.imgur.com/kHR84Cn.png)

* 群聚樹分析：
![](https://i.imgur.com/AgnXfN4.jpg)
    - 最外層可分為兩群：
        - 左：含有<font color="#0517B7">3個無中風者(100%)</font>
            - 共通點：無高血壓、無心臟疾病、小於50遂、未婚、有工作、無抽菸史
            - 其他重點：66.7%BMI正常
        - 右：含有<font color="#F71E86">10個中風者(58.8%)</font>、<font color="#0517B7">7個無中風者(41.2%)</font>
            - 共通點：已婚、有工作
            - 其他重點：88.2%大於50歲、64.7%BMI異常
    - 綜合此組抽樣的數據，此群聚數沒有很明顯的分群因素，但可以發現<font color="F83344">是否大於50歲、BMI是否正常</font>是可能影響分群的潛在因素。因左群皆為無中風族群裡的樣本皆小於50歲且高比例BMI正常，而右群中中風比例較高的族群大部分大於50歲且高比例BMI異常。

### Tree 10 ☠️
* 隨機抽樣資料：
![](https://i.imgur.com/SkHF6II.png)
![](https://i.imgur.com/04hovCr.png)

* 群聚樹分析：
![](https://i.imgur.com/q9lpaWv.jpg)
    - 此棵樹沒有明顯的中風與非中風分群關係
    - 最外層可分為兩群：
        - 左：含有<font color="#F71E86">2個中風者(50%)</font>、<font color="#0517B7">2個無中風者(50%)</font>
        - 右：含有<font color="#F71E86">8個中風者(50%)</font>、<font color="#0517B7">8個無中風者(50%)</font>

### 總結論
* 這部分做了十次不重複抽樣的cluster analysis，想知道分群方法能否適用於分析此筆數據。
* 從結果發現此方法沒有辦法將中風與非中風準確的分成兩群，且其中只有50%的群聚樹能夠較明顯的將中風與非中風分群。但仍然可以透過分析有較明顯分群的群聚數去與迴歸分析的結果做比較。
* 在最終選擇的迴歸模型中，使用的變數為高血壓、心臟疾病、年齡與血糖。而在cluster analysis中，高血壓、心臟疾病、血糖、年齡、BMI、抽菸史等五個分群變數都曾出現在五顆有明顯分群的群聚樹中，其中以年齡這個變數出現的次數最多，其次為高血壓。
* 因此，cluster analysis雖無法準確得分開中風與非中風，但是有機會能分出像高中風風險族群或低中風風險族群的分群，且分群的關鍵因素也能與最終迴歸模型取的變數相呼應。