strokedata <- read.csv(file = '../data/healthcare-dataset-stroke-data-cleanbmi.csv')
head(strokedata)

model_age = glm(stroke ~ age, data=strokedata, family=binomial(link="logit"))
summary(model_age)

model_glucose = glm(stroke ~ avg_glucose_level, data=strokedata, family=binomial(link="logit"))
summary(model_glucose)

model_bmi = glm(stroke ~ bmi, data=strokedata, family=binomial(link="logit"))
summary(model_bmi)

final_model = glm(stroke ~ age + avg_glucose_level, data=strokedata, family=binomial(link="logit"))
summary(final_model)
