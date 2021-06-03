strokedata <- read.csv(file = '../data/healthcare-dataset-stroke-data-cleanbmi.csv')
head(strokedata)

model1_full = glm(stroke ~ hypertension + heart_disease + ever_married + age + avg_glucose_level, data=strokedata, family=binomial(link="logit"))
summary(model1_full)

model1_reduce = glm(stroke ~ hypertension + heart_disease + age + avg_glucose_level, data=strokedata, family=binomial(link="logit"))
summary(model1_reduce)

anova(model1_reduce, model1_full, test="LRT")

strokedata$age_group <- with(strokedata, ifelse(
    age < 50, '0-49', ifelse(
    age >= 50 & age < 60, '50-59', ifelse(
    age >= 60 & age < 70, '60-69', '>=70'))))
strokedata$age_group <- factor(strokedata$age_group, levels= c('0-49', '50-59', '60-69', '>=70'))
strokedata$glc_group <- with(strokedata, ifelse(avg_glucose_level < 160, '<160', '>=160'))
strokedata$glc_group <- factor(strokedata$glc_group, levels= c('<160', '>=160'))
head(strokedata)

model2_full = glm(stroke ~ hypertension + heart_disease + ever_married + age_group + glc_group, data=strokedata, 
                  family=binomial(link="logit"))
summary(model2_full)

model2_reduce = glm(stroke ~ hypertension + heart_disease +  age_group + glc_group, data=strokedata, family=binomial(link="logit"))
summary(model2_reduce)

anova(model2_reduce, model2_full, test="LRT")


