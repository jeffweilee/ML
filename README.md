## ML
### RapidMiner Blog case
http://www.simafore.com/blog/author/bala-deshpande
### ML Mind Map
https://jixta.wordpress.com/2015/07/17/machine-learning-algorithms-mindmap/
### slides
http://www.slideshare.net/tw_dsconf/practical-issues-in-machine-learning
http://www.slideshare.net/tw_dsconf/feature-engineering-in-machine-learning
### deep learning
http://deeplearning4j.org/eigenvector.html
### Spark
https://0x0fff.com/spark-architecture/
https://0x0fff.com/spark-architecture-shuffle/
https://0x0fff.com/spark-memory-management/
https://jaceklaskowski.gitbooks.io/mastering-apache-spark/content/spark-mllib.html
https://www.quora.com/What-is-the-difference-between-Apache-Spark-and-Apache-Hadoop-Map-Reduce

##Data science
https://github.com/donnemartin/data-science-ipython-notebooks
http://machine-learning-python.kspax.io/

##scikit
https://github.com/scikit-learn/scikit-learn

##PCA
http://www.let.rug.nl/nerbonne/teach/rema-stats-meth-seminar/presentations/Ke-Tran-PCA-2011-May-24.pdf

## Neural
http://neuralnetworksanddeeplearning.com/chap1.html
http://i.stack.imgur.com/oy2Bc.png

## Time Series
http://a-little-book-of-r-for-time-series.readthedocs.io/en/latest/src/timeseries.html
http://ucanalytics.com/blogs/step-by-step-graphic-guide-to-forecasting-through-arima-modeling-in-r-manufacturing-case-study-example/
http://www.forecastingsolutions.com/arima.html
http://www.simafore.com/blog/bid/110752/Time-Series-Forecasting-from-windowing-to-predicting-in-RapidMiner
http://www.simafore.com/blog/bid/109051/Time-Series-Forecasting-comparing-RapidMiner-and-R-for-analysis
http://www.simafore.com/blog/bid/106430/Using-RapidMiner-for-time-series-forecasting-in-cost-modeling-1-of-2

https://www.otexts.org/fpp/6
https://www.otexts.org/fpp/6/5
https://blog.pivotal.io/data-science-pivotal/products/forecasting-time-series-data-with-multiple-seasonal-periods
http://dasanlin888.pixnet.net/blog/post/34468877-%E5%AD%98%E6%B4%BB%E5%88%86%E6%9E%90%EF%BC%88survival-analysis%EF%BC%89%E4%BB%8B%E7%B4%B9%EF%BC%8D%E2%85%A0~%E6%99%A8%E6%99%B0%E7%B5%B1%E8%A8%88


## RapidMiner
### Operators
http://docs.rapidminer.com/studio/operators/
http://docs.rapidminer.com/studio/operators/rapidminer-studio-operator-reference.pdf
http://docs.rapidminer.com/downloads/rapidminer-radoop-operator-reference.pdf
http://docs.rapidminer.com/downloads/rapidminer-radoop-manual.pdf
### sweep parameter
http://docs.rapidminer.com/studio/operators/modeling/optimization/parameters/optimize_parameters_evolutionary.html
http://docs.rapidminer.com/studio/operators/modeling/optimization/parameters/optimize_parameters_grid.html
http://docs.rapidminer.com/studio/operators/modeling/optimization/parameters/set_parameters.html

## Supply Chain
http://cdn2.hubspot.net/hub/153059/file-1347479975-pdf/pdfs/Analytics_for_supply_chain_and_operations_7-2014_(1)_FINAL.pdf?t=1406638949368&submissionGuid=8e99a8b1-fdef-42c9-b56d-e61693546734
https://logisticsviewpoints.com/2016/06/08/machine-learning-for-supply-chain-efficiencies/
http://www.cs.waikato.ac.nz/ml/publications/1995/Mitchell95-Time-Series.pdf
http://www.ulb.ac.be/di/map/gbonte/ftp/time_ser.pdf
http://cs.stackexchange.com/questions/13937/which-machine-learning-algorithms-can-be-used-for-time-series-forecasts
https://www.quora.com/Data-Science-Can-machine-learning-be-used-for-time-series-analysis
https://www.accenture.com/us-en/analytics-index

## PPM
https://www.lce.com/pdfs/The-PMPdM-Program-124.pdf

## Predictive Maintenance
https://gallery.cortanaintelligence.com//Experiment/Predictive-Maintenance-Step-2A-of-3-train-and-evaluate-regression-models-2
http://www.slideshare.net/MSAdvAnalytics/cortana-analytics-workshop-predictive-maintenance-in-the-iot-era

## Share Econ

https://theinitium.com/article/20160716-opinion-books-airbnb/
https://theinitium.com/article/20160108-international-whatsmineisyours/



```
  Iterable<Widget> nowListTitles;
  Iterable<Widget> listTitles;
  
  
    bool isSortByName = false;
  bool isSortByTotalCount = true;
  
   MenuChoice(title: 'Sort by name', icon: Icons.sort),
    MenuChoice(title: 'Sort by count', icon: Icons.sort),
    
    
    
    case 'Sort by name':
        print('[appPage] menu click Sort by name');

        int listCount = 0;
        if (isSortByName) {
          items.sort((a, b) => a.sysName.compareTo(b.sysName));
          nowListTitles = items.map(
              (AppListInfo item) => buildListTile(context, item, listCount++));
          isSortByName = false;
        } else {
          items.sort((a, b) => b.sysName.compareTo(a.sysName));
          nowListTitles = items.map(
              (AppListInfo item) => buildListTile(context, item, listCount++));
          isSortByName = true;
        }
        setState(() {});
        break;
      case 'Sort by count':
        print('[appPage] menu click Sort by task count');

        int listCount = 0;
        if (isSortByTotalCount) {
          items.sort((a, b) => a.totalTaskCount.compareTo(b.totalTaskCount));
          nowListTitles = items.map(
              (AppListInfo item) => buildListTile(context, item, listCount++));
          isSortByTotalCount = false;
        } else {
          items.sort((a, b) => b.totalTaskCount.compareTo(a.totalTaskCount));
          nowListTitles = items.map(
              (AppListInfo item) => buildListTile(context, item, listCount++));
          isSortByTotalCount = true;
        }
        setState(() {});
        break;
  
```

