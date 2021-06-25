#!/usr/bin/env python
# coding: utf-8

# Chapter 7: Age as Confounding Factor
# =======================

# ## Age and Gender
# ```{image} ./images/age_gender.png
# :alt: age_gender
# :class: bg-primary mb-1
# :width: 600px
# :align: center
# ```
# 
# - barplot的部分是該年齡層某個性別的中風百分比 lineplot的部分是該性別的中風人數中每加一個年齡層的百分比
# - <span style="color:blue">性別會對年齡和中風的機率構成影響，美國平均女性更年期是50~52歲，因此可見從50~69該區段的斜率較先前趨緩，而男性過了50歲到79歲這段區間幾乎呈現斜率一致，顯示男性邁入老年後除非已過80，年齡對中風造成的差異一致，然女性可能因為賀爾蒙波動等因素造成每個年齡區段罹患中風的機率不斷波動</span>

# ## Age and hypertension
# ```{image} ./images/age_ht.png
# :alt: age_ht
# :class: bg-primary mb-1
# :width: 600px
# :align: center
# ```
# - <span style="color:blue">對於未有高血壓的病患，在老年以前對於罹患中風的正影響較低，顯示累積機率之斜率較低。值得注意的是在50歲以前，未有高血壓者罹患中風的比例較高，但過了50歲之後由累積機率的上升斜率可見，50~69歲高血壓對於罹患中風的正影響較為明顯，然過了70歲之後，本表未見高血壓對於中風的是否有影響。</span>
# <p style="page-break-before: always">

# ## Age and Herat-Disease
# ```{image} ./images/age_HD.png
# :alt: age_HD
# :class: bg-primary mb-1
# :width: 600px
# :align: center
# ```
# - <span style="color:blue">同時具有心臟疾病與中風的人數有36人，不確定是否會影響判讀，但就上圖，年齡對中風與否的影響，有一部份取決於是否有心臟疾病，未有心臟疾病者，年齡的影響較大。但對於有先心臟疾病者，一旦過了更年期(50歲)之後，右表中的橘色實線的斜率變化顯示，年齡增長對於罹患中風未見其正向影響。</span>

# ## Age and Marry
# ```{image} ./images/age_marry.png
# :alt: age_marry
# :class: bg-primary mb-1
# :width: 600px
# :align: center
# ```
# - <span style="color:blue">未有婚姻經驗的人總共826人，但其中中風的僅有20人，人數過少，在連續型的line plot上，可見出現斷層。若忽略斷層，可見年齡上升對於有婚姻經驗者的中風貢獻較低，但其餘資訊由於未婚者中風人數過少而難以判讀。</span>
# <p style="page-break-before: always">

# ## Age and Smoking Status
# ```{image} ./images/age_smoke.png
# :alt: age_smoke
# :class: bg-primary mb-1
# :width: 600px
# :align: center
# ```
# - 三組均大於39人。
# - <span style="color:blue">對於維持抽菸習慣者，觀察右表斜率，年齡之於中風的影響大致可分為三個階段，壯年、(50歲)更年期後十年、邁入老年70歲以後。壯年時期維持抽菸的人口不多，不確定是否具有意義，但可以發現50歲以後之抽菸者，到七十歲以前這段區間若具有抽菸習慣對於罹患中風具有正向影響。然而值得注意的是，雖然在卡方檢定中，我們發現曾經有過抽菸習慣的成功戒菸者們，罹患中風的機會較高，但是本表中可以發現對於60多歲跳到70歲這個階級中，無論是成功戒菸者或是有抽菸習慣者，年齡均會影響其抽菸習慣增加中風機會，兩組斜率均出現變動，因此不排除在卡方檢定中的結果，受到年齡因素的干擾</span>
# <p style="page-break-before: always">
