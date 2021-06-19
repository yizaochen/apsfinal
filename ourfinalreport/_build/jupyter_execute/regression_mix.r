strokedata <- read.csv(file = '../data/healthcare-dataset-stroke-data-cleanbmi.csv')
head(strokedata)

model1 = glm(stroke ~ hypertension + heart_disease + ever_married + age + avg_glucose_level, data=strokedata, family=binomial(link="logit"))
summary(model1)

model2 = glm(stroke ~ hypertension + heart_disease + age + avg_glucose_level, data=strokedata, family=binomial(link="logit"))
summary(model2)

anova(model1, model2, test="LRT")

summary(model2)

model_age_hypert = glm(stroke ~ ever_married + hypertension, data=strokedata, family=binomial(link="logit"))
summary(model_age_hypert)

model_age_heartd = glm(stroke ~ ever_married + heart_disease, data=strokedata, family=binomial(link="logit"))
summary(model_age_heartd)

model_age_marry = glm(stroke ~ ever_married + age, data=strokedata, family=binomial(link="logit"))
summary(model_age_marry)

model_age_glc = glm(stroke ~ ever_married + avg_glucose_level, data=strokedata, family=binomial(link="logit"))
summary(model_age_glc)
