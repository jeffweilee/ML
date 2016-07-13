# ML

## RapidMiner
### sweep parameter
http://docs.rapidminer.com/studio/operators/modeling/optimization/parameters/optimize_parameters_evolutionary.html

http://docs.rapidminer.com/studio/operators/modeling/optimization/parameters/optimize_parameters_grid.html

http://docs.rapidminer.com/studio/operators/modeling/optimization/parameters/set_parameters.html

## SC
http://cdn2.hubspot.net/hub/153059/file-1347479975-pdf/pdfs/Analytics_for_supply_chain_and_operations_7-2014_(1)_FINAL.pdf?t=1406638949368&submissionGuid=8e99a8b1-fdef-42c9-b56d-e61693546734

https://logisticsviewpoints.com/2016/06/08/machine-learning-for-supply-chain-efficiencies/

http://www.cs.waikato.ac.nz/ml/publications/1995/Mitchell95-Time-Series.pdf

http://www.ulb.ac.be/di/map/gbonte/ftp/time_ser.pdf

http://cs.stackexchange.com/questions/13937/which-machine-learning-algorithms-can-be-used-for-time-series-forecasts

https://www.quora.com/Data-Science-Can-machine-learning-be-used-for-time-series-analysis

https://www.accenture.com/us-en/analytics-index


## R
install.packages("forecast")
library(forecast)

  #data transform
  data.ts<-function(data,year,month){
    data<-ts(data=data,start=c(year,month),frequency=4)
  }
  
  #holtwinters function
  holtwinters<-function(data,year,month,n){
    data.f<-HoltWinters(data)  #data.f$fitted to view values 
    data.p<-predict(data.f, n) 
    a<-as.numeric(data.f$fitted[,1])
    a<-c(rep(NA,length(data)-length(a)),a)
    b<-as.numeric(data.p)
    all<- c(a,b)
    all<-ts(all,start = c(year,month),frequency = 4)
    return(all)
  }
  
  #ARIMA function
ARIMA<-function(data,year,month,n){  
    bestfit<-auto.arima(data)
    fit<-forecast(bestfit,7)
	data.f<-fitted(bestfit)
	for(z in 1:length(data.f)){
	if (data.f[z]<0)
		data.f[z]=0
	}
    data.e<-(data-data.f)^2
    SSE<-sum(data.e)
    
    fit1<-auto.arima(data,D=1)
    data.f1<-fitted(fit1)
	for(z in 1:length(data.f1)){
	if (data.f1[z]<0)
		data.f1[z]=0
	}
    data.e1<-(data-data.f1)^2
    SSE1<-sum(data.e1)
    
    if (SSE1<SSE){
      bestfit<-fit1
      data.f<-fitted(fit1)
    }
    
    data.p<-forecast(bestfit,n)
    data.p<-as.data.frame(data.p)
	data.p<-data.p[,1]
    a<-as.numeric(data.f)
    b<-as.numeric(data.p)
    all<-  c(a,b)
    all<-ts(all,start = c(year,month),frequency = 4)
    return(all)
  }
  
#---------- 

#best result
result<-function(data,year,month,n){
  data<-data.ts(data,year,month)
  a<-ARIMA(data,year,month,n)
  b<-holtwinters(data,year,month,n)
  
  bestfit<-a
    num<-length(data)
    a.residual<-data-a[1:num]
    b.residual<-data-b[1:num]
  if(sum(a.residual^2)/length(a.residual)>sum(na.omit(b.residual)^2)/length(na.omit(b.residual))){
    bestfit<-b
  }
  return(bestfit)
}
#----------
#start real predict
AP<-read.csv("D://Users/pysun/Desktop/GFK/Demand AP Vender Unit.csv", header=TRUE)
	
	name<-c()
	hist.data<-c()
	predict<-c()
	for(n in 2:(ncol(AP)-2)){
		data<-AP[,n]
		data<-data.ts(data,2013,1)
		data.p<-result(data,2013,1,8)
		predict<-cbind(predict,data.p)
		hist.data<-cbind(hist.data,data)
			if (n>ncol(AP)-2){
			colnam<-colnames(AP[,(ncol(AP)-2):ncol(AP)])
			colnam<-colnam[n-ncol(AP)+3]
			} else{	
			colnam<-colnames(AP[,n:(n+2)])
			colnam<-colnam[1]
			}	
		name<-c(name,colnam)		
	}
	colnames(predict)<-name
	colnames(hist.data)<-name
	
	plotline<-function(n){
		plot(predict[,n], main =paste(name[n]), ylab="Sale Unit")
		abline(v=2017,col="red")
		abline(h=0,col="red")
		lines(hist.data[,n],type="l",col="red")	
	}

for(n in 1:ncol(predict)){	
mypath <- file.path("D://Users/pysun/Desktop/GFK/",paste("AP_", name[n], ".jpg", sep = ""))
jpeg(file=mypath)
    mytitle = paste( name[n])
    plotline(n)
    dev.off()
}
AP.p<-predict
write.csv(AP.p, file = "D://Users/pysun/Desktop/GFK/Demand AP Vender_predict.csv")


