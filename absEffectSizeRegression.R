library(lme4)

dataDir<-"/Users/deligkaris.1/OneDrive - The Ohio State University Wexner Medical Center/MICROSIM/NOTEBOOKS/DATA"
setwd(dataDir)
dataFile<-"regressionData.csv"
regressionData<-read.csv(dataFile)

head(regressionData)
attach(regressionData)

treatment<-treatment-0.5 #without centering, there may be convergence issues
#regressionData$treatment<-regressionData$treatment - 0.5 #without centering, I run into convergence issue

str(regressionData)
head(regressionData)
regressionData

md<-glmer( outcome ~ treatment + (1|quantileIndex), family=binomial(link = "logit"))

summary(md)

coef(md)

regressionResults<-as.data.frame(coef(md)[[1]])

resultsFile<-"regressionResults.csv"
write.csv(regressionResults, resultsFile) # cwd is still the same

dd<-ranef(md)[["quantileIndex"]]
dd <- cbind(quantileIndex=rownames(dd),dd)
rownames(dd) <- NULL
head(dd)

intercept<-fixef(md)[1]

intercept+dd$`(Intercept)`

fixef(md)
