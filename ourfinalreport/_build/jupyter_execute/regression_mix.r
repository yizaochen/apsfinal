strokedata <- read.csv(file = '../data/healthcare-dataset-stroke-data-cleanbmi.csv')
head(strokedata)

model1_full = glm(stroke ~ hypertension + heart_disease + ever_married + age + avg_glucose_level, data=strokedata, family=binomial(link="logit"))
summary(model1_full)

model1_reduce = glm(stroke ~ hypertension + heart_disease + age + avg_glucose_level, data=strokedata, family=binomial(link="logit"))
summary(model1_reduce)

anova(model1_reduce, model1_full, test="LRT")

strokedata$age_greater_50 <- ifelse(strokedata$age>50, 1, 0)
strokedata$age_greater_60 <- ifelse(strokedata$age>60, 1, 0)
strokedata$age_greater_70 <- ifelse(strokedata$age>70, 1, 0)
strokedata$age_greater_80 <- ifelse(strokedata$age>80, 1, 0)
strokedata$glc_greater_80 <- ifelse(strokedata$avg_glucose_level>80, 1, 0)
strokedata$glc_greater_110 <- ifelse(strokedata$avg_glucose_level>110, 1, 0)
strokedata$glc_greater_160 <- ifelse(strokedata$avg_glucose_level>160, 1, 0)
head(strokedata)

model2_full = glm(stroke ~ hypertension + heart_disease + ever_married + age_greater_50 + age_greater_70 + glc_greater_160, data=strokedata, 
                  family=binomial(link="logit"))
summary(model2_full)

model2_reduce = glm(stroke ~ hypertension + heart_disease + age_greater_50 + age_greater_70 + glc_greater_160, data=strokedata, family=binomial(link="logit"))
summary(model2_reduce)

anova(model2_reduce, model2_full, test="LRT")


