data <- read.csv("tomat1.csv",header = FALSE)
datas1 <- data

oversampling1 <- datas1[which(datas1$V9 == 'belum matang' | datas1$V9 == 'Setengah matang'),]
oversampling1$V9 <- as.character(oversampling1$V9)
oversampling1$V9[oversampling1$V9 == "Setengah matang"] <- 0
oversampling1$V9[oversampling1$V9 == "belum matang"] <- 1
oversampling1$V9 <- as.factor(oversampling1$V9)


oversampling2 <- datas1[which(datas1$V9 == 'matang' | datas1$V9 == 'Setengah matang'),]
oversampling2$V9 <- as.character(oversampling2$V9)
oversampling2$V9[oversampling2$V9 == "Setengah matang"] <- 0
oversampling2$V9[oversampling2$V9 == "matang"] <- 1
oversampling2$V9 <- as.factor(oversampling2$V9)


#Balancing data 1
library(unbalanced)
n<-ncol(oversampling1)  #ambil jumlah variabel
output<-oversampling1$V9 #ambil V9 nya, simpan di output
input<-oversampling1[ ,-(n-1)] #ambil atribut
#balance the dataset 
data<-ubBalance(X= input, Y=output, type="ubSMOTE", percOver=75, percUnder=250, verbose=TRUE)
balancedData<-cbind(data$X,data$Y)

balancedData$V9 <- as.factor(as.character(balancedData$`data$Y`))
balancedData$`data$Y` <- NULL



#balancing data 2
library(unbalanced)
n1<-ncol(oversampling2)  #ambil jumlah variabel
output1<-oversampling2$V9 #ambil V9 nya, simpan di output
input1<-oversampling2[ ,-(n-1)] #ambil atribut
#balance the dataset 
data1<-ubBalance(X= input1, Y=output1, type="ubSMOTE", percOver=75, percUnder=250, verbose=TRUE)
balancedData1<-cbind(data1$X,data1$Y)

balancedData1$V9 <- as.factor(as.character(balancedData1$`data1$Y`))
balancedData1$`data1$Y` <- NULL
plot(balancedData1$V9)

#balikin datanya
balancedData$V9 <- as.character(balancedData$V9)
balancedData$V9[balancedData$V9 == "0"] <- "Setengah Matang"
balancedData$V9[balancedData$V9 == "1"] <- "Belum Matang"
balancedData$V9 <- as.factor(balancedData$V9)


#balikin datanya
balancedData1$V9 <- as.character(balancedData1$V9)
balancedData1$V9[balancedData1$V9 == "0"] <- "Setengah Matang"
balancedData1$V9[balancedData1$V9 == "1"] <- "Matang"
balancedData1$V9 <- as.factor(balancedData1$V9)

data1  <- balancedData1[which(balancedData1$V9 == 'Matang'), ]


#data fix
data_fix <- rbind(balancedData, data1)
plot(data_fix$V9)


write.csv(data_fix, file = "afterOversampling.csv",row.names=FALSE)
