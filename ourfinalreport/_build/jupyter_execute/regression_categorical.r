strokedata <- read.csv(file = '../data/healthcare-dataset-stroke-data-cleanbmi.csv')
head(strokedata)

nrow(strokedata)

model_hypert = glm(stroke ~ hypertension, data=strokedata, family=binomial(link="logit"))
summary(model_hypert)

model_heartd = glm(stroke ~ heart_disease, data=strokedata, family=binomial(link="logit"))
summary(model_heartd)

model_marry = glm(stroke ~ ever_married, data=strokedata, family=binomial(link="logit"))
summary(model_marry)

model_worktype = glm(stroke ~ work_type, data=strokedata, family=binomial(link="logit"))
summary(model_worktype)

strokedata$smoking_status <- factor(strokedata$smoking_status, levels= c('never smoked', 'formerly smoked', 'smokes'))
model_smoke = glm(stroke ~ smoking_status, data=strokedata, family=binomial(link="logit"))
summary(model_smoke)

model_full = glm(stroke ~ hypertension + heart_disease + ever_married + smoking_status, data=strokedata, family=binomial(link="logit"))
summary(model_full)

model_reduce = glm(stroke ~ hypertension + heart_disease + ever_married, data=strokedata, family=binomial(link="logit"))
summary(model_reduce)

anova(model_reduce, model_full, test="LRT")

summary(model_reduce)


