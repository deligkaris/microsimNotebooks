library(lme4)

regressionData<-read.csv("/Users/deligkaris.1/OneDrive - The Ohio State University Wexner Medical Center/MICROSIM/NOTEBOOKS/DATA/regressionData.csv")

regressionData$treatment<-regressionData$treatment - 0.5 #without centering, I run into convergence issue

md<-lmer ( regressionData$outcome ~ regressionData$treatment + (1|regressionData$quantileIndex))

summary(md)

coef(md)

dd<-ranef(md)[["regressionData$quantileIndex"]]
dd <- cbind(quantileIndex=rownames(dd),dd)
rownames(dd) <- NULL
head(dd)

intercept<-fixef(md)[1]

intercept+dd$`(Intercept)`
