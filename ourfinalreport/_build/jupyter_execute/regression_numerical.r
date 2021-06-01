strokedata <- read.csv(file = '../data/healthcare-dataset-stroke-data-cleanbmi.csv')
head(strokedata)

model_age = glm(stroke ~ age, data=strokedata, family=binomial(link="logit"))
summary(model_age)

model_glucose = glm(stroke ~ avg_glucose_level, data=strokedata, family=binomial(link="logit"))
summary(model_glucose)

model_bmi = glm(stroke ~ bmi, data=strokedata, family=binomial(link="logit"))
summary(model_bmi)

model_full = glm(stroke ~ age + avg_glucose_level + bmi, data=strokedata, family=binomial(link="logit"))
summary(model_full)

model_reduce = glm(stroke ~ age + avg_glucose_level, data=strokedata, family=binomial(link="logit"))
summary(model_reduce)

anova(model_reduce, model_full, test="LRT")

strokedata$age_greater_50 <- ifelse(strokedata$age>50, 1, 0)
strokedata$age_greater_60 <- ifelse(strokedata$age>60, 1, 0)
strokedata$age_greater_70 <- ifelse(strokedata$age>70, 1, 0)
strokedata$age_greater_80 <- ifelse(strokedata$age>80, 1, 0)
head(strokedata)

model_age_cate_full = glm(stroke ~ age_greater_50 + age_greater_60 + age_greater_70 + age_greater_80, data=strokedata, family=binomial(link="logit"))
summary(model_age_cate_full)

model_age_cate_selected = glm(stroke ~ age_greater_50 +  age_greater_70, data=strokedata, family=binomial(link="logit"))
summary(model_age_cate_selected)

strokedata$glc_greater_80 <- ifelse(strokedata$avg_glucose_level>80, 1, 0)
strokedata$glc_greater_110 <- ifelse(strokedata$avg_glucose_level>110, 1, 0)
strokedata$glc_greater_160 <- ifelse(strokedata$avg_glucose_level>160, 1, 0)
head(strokedata)

model_glc_cate_full = glm(stroke ~ glc_greater_80 + glc_greater_110 + glc_greater_160, data=strokedata, family=binomial(link="logit"))
summary(model_glc_cate_full)

model_glc_cate_selected = glm(stroke ~ glc_greater_160, data=strokedata, family=binomial(link="logit"))
summary(model_glc_cate_selected)

model_cate_final = glm(stroke ~ age_greater_50 +  age_greater_70 + glc_greater_160, data=strokedata, family=binomial(link="logit"))
summary(model_cate_final)
