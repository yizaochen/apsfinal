Chapter 12: Cluster analysis 1-使用全部的變數去計算
=======================
## 資料及計算方法
* Data: 
    * 使用清理後的資料，共3425筆。其中180筆為有中風樣本，3245筆為無中風樣本。
    * Variables in the calculation: gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status
* Distance Matrix: 使用Gower's Distance計算。
    * Gower’s distance can be used to measure how different two records are. The records may contain combinations of logical, numerical, categorical or text data. The distance is always a number between 0 (identical) and 1 (maximally dis- similar).
    > [Gower, J. C. "A General Coefficient of Similarity and Some of Its Properties." Biometrics 27, no. 4 (1971): 857-71. Accessed June 22, 2021. doi:10.2307/2528823.]
* Hierarchical Clustering:
    * 使用Complete-linkage clustering做計算
* Prunes a Hierarchical Cluster Tree:
    * 使用package "maptree"的functions:
        1. clip.clust
        2. group.clust

## 分群結果
![](https://i.imgur.com/QZMBzbY.png)
* 上圖虛線由下至上分別為：
    1. 黃線：切在Height=0.9處，此線可將資料分成5群。
    2. 橘線：切在Height=0.95處，此線可將資料分成4群。
    3. 紅線：切在Height=0.98處，此線可將資料分成2群。
* 下面將對上述三種剪切分群做更細的探討。

## Cut Tree: 各別圖表分析
1. 黃線：Height=0.9, Group=5
    * 剪枝圖:
    ![](https://i.imgur.com/o4lh7zJ.png)
    * 各群中中風與非中風的比例圖:
    ![](https://i.imgur.com/JrIHsWu.png)
    * 中風樣本在各群的分布狀況圖:
    ![](https://i.imgur.com/a5Q9Be1.png)
2. 橘線：Height=0.95, Group=4
    * 剪枝圖:
    ![](https://i.imgur.com/TBlYQug.png)
    * 各群中中風與非中風的比例圖:
    ![](https://i.imgur.com/hv6N2sc.png)
    * 中風樣本在各群的分布狀況圖:
    ![](https://i.imgur.com/sJeSQFb.png)
3. 紅線：Height=0.98, Group=2
    * 各群中中風與非中風的比例圖:
    ![](https://i.imgur.com/o7xUTUM.png)
    * 中風樣本在各群的分布狀況圖:
    ![](https://i.imgur.com/9zkv9df.png)

## 結果討論
* 由各群中中風與非中風的比例圖可發現，由於非中風樣本數遠大於中風樣本數，因此非中風在各群中所佔的比例都很大。而這樣的結果也表示此cluster analysis並無法有效地將中風與非中風樣本做分群，推測可能的原因是因為納入過多的變數，其中或許參雜了較無貢獻的變數而影響了結果。
* 由中風樣本在各群的分布狀況圖可見：分成五群的結果相當的不好，其中群2, 3, 5分配到差不多的中風樣本數，感覺中風樣本相當的均勻分布。在分成四群的結果中，其中群2的中風樣本數佔總中風樣本的51.11%，其他三群的比例總中風樣本的1/4，因此推測群2中的非中風樣本似乎有較高的中風機率。最後，在分成兩群的結果中，群1的中風樣本數佔總中風樣本的66.67％，因此推測群1中的非中風樣本似乎有較高的中風機率。

<p style="page-break-before: always">