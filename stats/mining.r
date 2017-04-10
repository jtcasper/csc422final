library(ggplot2)
library(readr)

# Read data
data_1 <- read.csv('../data/sms-call-internet-mi-2013-11-01.csv')
data_2 <- read.csv('../data/sms-call-internet-mi-2013-11-02.csv')
data_3 <- read.csv('../data/sms-call-internet-mi-2013-11-03.csv')
data_4 <- read.csv('../data/sms-call-internet-mi-2013-11-04.csv')
data_5 <- read.csv('../data/sms-call-internet-mi-2013-11-05.csv')
data_6 <- read.csv('../data/sms-call-internet-mi-2013-11-06.csv')
data_7 <- read.csv('../data/sms-call-internet-mi-2013-11-07.csv')

# Clean data -- remove rows which have NA values
clean_1 <- na.omit(data_1)
clean_2 <- na.omit(data_2)
clean_3 <- na.omit(data_3)
clean_4 <- na.omit(data_4)
clean_5 <- na.omit(data_5)
clean_6 <- na.omit(data_6)
clean_7 <- na.omit(data_7)

# Plots
qplot(data = clean_1[1:100,], clean_1$CellID[1:100], clean_1$smsin[1:100])
