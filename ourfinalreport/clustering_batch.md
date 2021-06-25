Chatper 13: Cluster analysis 2-使用迴歸分析final model中的變數去計算
=======================
## 資料及計算方法
* Data: 
    * 使用清理後的資料，共3425筆。其中180筆為有中風樣本，3245筆為無中風樣本。
    * Variables in the calculation: age, hypertension, heart_disease, avg_glucose_level
* Distance Matrix: 使用Gower's Distance計算。
* Hierarchical Clustering: 使用Complete-linkage clustering做計算
* Prunes a Hierarchical Cluster Tree:
    * 使用package "maptree"的functions:
        1. clip.clust
        2. group.clust

## 分群結果
![](https://i.imgur.com/S4mZ3tx.png)
* 上圖虛線由下至上分別為：
    1. 黃線：切在Height=0.5處，此線可將資料分成4群。
    2. 橘線：切在Height=0.7處，此線可將資料分成3群。
    3. 紅線：切在Height=0.8處，此線可將資料分成2群。
* 下面將對上述三種剪切分群做更細的探討。

## Cut Tree: 各別圖表分析
1. 黃線：Height=0.5, Group=4
    * 剪枝圖:
    ![](https://i.imgur.com/1Nmhvfe.png)
    * 各群中中風與非中風的比例圖:
    ![](https://i.imgur.com/YTbxLeK.png)
    * 中風樣本在各群的分布狀況圖:
    ![](https://i.imgur.com/YKnzFIv.png)
2. 橘線：Height=0.7, Group=3
    * 剪枝圖:
    ![](https://i.imgur.com/STROPQt.png)
    * 各群中中風與非中風的比例圖:
    ![](https://i.imgur.com/fqvmXYJ.png)
    * 中風樣本在各群的分布狀況圖:
    ![](https://i.imgur.com/EknHbl6.png)
3. 紅線：Height=0.8, Group=2
    * 各群中中風與非中風的比例圖:
    ![](https://i.imgur.com/AJ9hFgN.png)
    * 中風樣本在各群的分布狀況圖:
    ![](https://i.imgur.com/CrAa0mq.png)

## 結果討論
* 與first part有相同的問題：在各群中中風與非中風的比例圖，由於非中風樣本數遠大於中風樣本數，因此非中風在各群中所佔的比例都很大，也表示此cluster analysis也無法將中風與非中風完全的分群。
    * 在分成四群的結果中，群4涵蓋的樣本最多(83.65%)，因此導致中風樣本比例很小，但其實群4中風樣本佔了總樣本的54.44%；而分成三群的結果與分成四群的結果相似。
    * 最後是分成兩群的結果，在中風樣本在各群的分布狀況圖中發現，中風樣本被分成了20:80的狀態，而first part分成兩群的結果中風樣本是被分成67:33的狀態，因此此群聚樹結果雖然仍無法有效將中風與非中風完全的分群，但此部分可以將高比例的中風人口分到了同一群。

## 總結論
* Cluster analysis無法將中風與非中風樣本完整分群。
    * 雖無法準確預測是否會中風，但或許可以藉由該群是否含有較高比例的中風樣本去探討其健康狀態是否具有高中風風險。
    * 此部分分析的結果不如預期可能的原因為: 
        1. 中風與非中風的樣本數差異過大 
        2. 雖納入計算的變數可能導致中風，但可能需要更多詳細的健康資訊才能更準確地進行分群，例如：hypertension不要是binary variable，而是血壓的連續型數值。
        3. Gower distance計算易受到無標準化的連續型變量異常值影響，而此部分帶入計算的數據皆為無經過轉換的原始資料。
        
<p style="page-break-before: always">