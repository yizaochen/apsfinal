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

strokedata$age_group <- with(strokedata, ifelse(
    age < 50, '0-49', ifelse(
    age >= 50 & age < 60, '50-59', ifelse(
    age >= 60 & age < 70, '60-69', '>=70'))))
strokedata$age_group <- factor(strokedata$age_group, levels= c('0-49', '50-59', '60-69', '>=70'))
head(strokedata)

model_age_cate = glm(stroke ~ age_group, data=strokedata, family=binomial(link="logit"))
summary(model_age_cate)

strokedata$glc_group <- with(strokedata, ifelse(avg_glucose_level < 160, '<160', '>=160'))
strokedata$glc_group <- factor(strokedata$glc_group, levels= c('<160', '>=160'))
head(strokedata)

model_glc_cate = glm(stroke ~ glc_group, data=strokedata, family=binomial(link="logit"))
summary(model_glc_cate)

model_cate_final = glm(stroke ~ age_group + glc_group, data=strokedata, family=binomial(link="logit"))
summary(model_cate_final)
