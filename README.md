(dgateway=($(ip r | grep default | awk '{print$3}')); dgateway_device=($(ip r | grep default | awk '{print$5}')); all_mac_device_ip_mapping=($(ip a | grep -v inet6 | grep -v -E '127\.[[:digit:]]{1,3}\.[[:digit:]]{1,3}\.[[:digit:]]{1,3}' | grep inet -B 2 | sed 's:^[ \t]*::g' | grep [.:] | cut -d ' ' -f2 | cut -d '/' -f1)); val=\"\"; firstflag=0; for i in ${!all_mac_device_ip_mapping[@]}; do if [[ $(echo ${all_mac_device_ip_mapping[i]} | grep -o : | wc -l) -gt 1 ]]; then mac=${all_mac_device_ip_mapping[i]}; elif [[ $(echo ${all_mac_device_ip_mapping[i]} | grep -o : | wc -l) -eq 1 ]]; then mac_device=${all_mac_device_ip_mapping[i]}; mac_device=$(echo ${mac_device} | cut -d ':' -f1 | cut -d '@' -f1); else for k in ${!dgateway_device[@]}; do if [[ ${dgateway_device[k]} == ${mac_device} ]]; then gw=${dgateway[k]}; break; else gw=NA; fi; done; if [[ $(ip a | grep ${all_mac_device_ip_mapping[i]} | grep -c dynamic) -gt 0 ]]; then edhcp=Y; else edhcp=N; fi; if [[ $firstflag -ne 0 ]]; then val=${val}~; fi; firstflag=1; val=${val}\\\"ADDRESS\\\":\\\"${mac}\\\",\\\"IP\\\":\\\"${all_mac_device_ip_mapping[i]}\\\",\\\"W_NICCONFIG_DefaultIPGateway\\\":\\\"${gw}\\\",\\\"DHCP_ENABLE\\\":\\\"${edhcp}\\\"; fi; done; echo ${val};)

(s=$(cat /etc/system-release); if [[ -z $s ]]; then s=$(cat /etc/redhat-release); fi; if [[ -z $s ]]; then s=$(cat /etc/os-release | grep PRETTY | cut -d '=' -f2 | sed -e 's/^\"//' -e 's/\"$//'); fi; s=$(echo ${s} | tr '[:upper:]' '[:lower:]'); IFS=$'\n'; if [[ -n $(echo $s | grep 'centos' ) ]] || [[ -n $(echo $s | grep 'red') && -n $(echo $s | grep 'hat') ]]; then a=($(rpm -q kernel --last | awk -F '[[:space:]][[:space:]]+' '{printf "%s,%s\n",$1,$2}')); elif [[ -n $(echo $s | grep 'buntu' ) ]]; then a=($(dpkg --get-selections | grep linux-image | awk '{printf "$s,%s\n",$1,NA}' )); else a='NA,NA'; fi; val=\"\"; for ((i = 0; i < ${#a[@]}; i++)); do echo ${a[i]}; p=\\\"HotFixID\\\":\\\"$(echo ${a[i]} | cut -d , -f1)\\\",\\\"InstalledOn\\\":\\\"$(d=$(echo ${a[i]} | cut -d , -f2); if [ $d == 'NA' ]; then echo NA; elif [ $(locale | grep 'LANG' | grep 'zh_') ]; then echo ${a[i]} | cut -d , -f2 | grep -Eo '[0-9]+' | tr '\\n' ' ' | awk '{print $1$2$3}' | { read gmt ; date +%m/%d/%Y -d ${gmt} ; }; else echo ${a[i]} | cut -d , -f2 | { read gmt ; date +%m/%d/%Y -d ${gmt} ; }; fi; )\\\"; val=${val}${p}~; done; echo ${val:0:${#val}-1};)



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




2019-05-31T10:00:57Z [INFO] [/replication/adapter/harbor/adapter.go:41]: the factory for adapter harbor registered
2019-05-31T10:00:57Z [INFO] [/replication/adapter/dockerhub/adapter.go:24]: Factory for adapter docker-hub registered
2019-05-31T10:00:57Z [INFO] [/replication/adapter/native/adapter.go:30]: the factory for adapter docker-registry registered
2019-05-31T10:00:57Z [INFO] [/replication/adapter/huawei/huawei_adapter.go:25]: the factory of Huawei adapter was registered
2019-05-31T10:00:57Z [INFO] [/common/config/store/driver/rest.go:24]: get configuration from url: http://harbor180-harbor-core/api/internal/configurations 
2019-05-31T10:00:57Z [INFO] [/common/dao/base.go:84]: Registering database: type-PostgreSQL host-harbor180-harbor-database port-5432 databse-registry sslmode-"disable"
2019-05-31T10:00:57Z [INFO] [/common/dao/base.go:89]: Register database completed
2019-05-31T10:00:57Z [INFO] [/jobservice/worker/cworker/c_worker.go:415]: Register job *gc.GarbageCollector with name IMAGE_GC
2019-05-31T10:00:57Z [INFO] [/jobservice/worker/cworker/c_worker.go:415]: Register job *replication.Replication with name REPLICATION
2019-05-31T10:00:57Z [INFO] [/jobservice/worker/cworker/c_worker.go:415]: Register job *replication.Scheduler with name IMAGE_REPLICATE
2019-05-31T10:00:57Z [INFO] [/jobservice/worker/cworker/c_worker.go:415]: Register job *sample.Job with name DEMO
2019-05-31T10:00:57Z [INFO] [/jobservice/worker/cworker/c_worker.go:415]: Register job *scan.ClairJob with name IMAGE_SCAN
2019-05-31T10:00:57Z [INFO] [/jobservice/worker/cworker/c_worker.go:415]: Register job *scan.All with name IMAGE_SCAN_ALL
2019-05-31T10:00:57Z [INFO] [/jobservice/period/basic_scheduler.go:64]: Basic scheduler is started
2019-05-31T10:00:57Z [INFO] [/jobservice/period/policy_store.go:285]: Load 1 periodic job policies
2019-05-31T10:00:57Z [INFO] [/jobservice/period/enqueuer.go:82]: Periodic enqueuer is started
2019-05-31T10:00:57Z [INFO] [/jobservice/period/policy_store.go:168]: Periodical job policy store is serving with policy auto sync enabled
2019-05-31T10:00:57Z [INFO] [/jobservice/worker/cworker/c_worker.go:151]: Redis worker is started
2019-05-31T10:00:57Z [INFO] [/jobservice/lcm/controller.go:74]: Status restoring loop is started
2019-05-31T10:00:57Z [INFO] [/jobservice/hook/hook_agent.go:153]: Hook event retrying loop is started
2019-05-31T10:00:57Z [INFO] [/jobservice/hook/hook_agent.go:157]: Basic hook agent is started
2019-05-31T10:00:57Z [INFO] [/jobservice/runtime/bootstrap.go:182]: API server is serving at 8080 with [http] mode at node [harbor180-harbor-jobservice-575b975b4d-lq9sf:130.11.6.58]
2019-05-31T10:00:57Z [INFO] [/jobservice/period/policy_store.go:156]: Subscribe redis channel {harbor_job_service_namespace}:period:policies:notifications
2019-05-31T10:01:52Z [ERROR] [/jobservice/api/handler.go:288]: Serve http request 'GET /api/v1/jobs/26035525d8e775d848776692/log' error: 500 {"code":10009,"message":"failed to get the job log","details":"no log data getter is configured"}
2019-05-31T10:02:33Z [INFO] [/jobservice/worker/cworker/c_worker.go:70]: Job incoming: {"name":"IMAGE_GC","id":"fd64d3dc3d8a2b0f04fe0a28","t":1559296950,"args":{"redis_url_reg":"redis://harbor180-harbor-redis:6379/2"},"unique":true}
2019-05-31T10:02:33Z [INFO] [/common/config/store/driver/rest.go:24]: get configuration from url: http://harbor180-harbor-core/api/internal/configurations 
2019-05-31T10:02:33Z [INFO] [/common/config/store/driver/rest.go:24]: get configuration from url: http://harbor180-harbor-core/api/internal/configurations 
2019-05-31T10:02:33Z [INFO] [/common/registryctl/client.go:41]: initializing client for reigstry http://harbor180-harbor-registry:8080 ...
2019-05-31T10:02:33Z [INFO] [/common/config/store/driver/rest.go:24]: get configuration from url: http://harbor180-harbor-core/api/internal/configurations 
2019-05-31T10:02:33Z [INFO] [/jobservice/runner/redis.go:161]: start to run gc in job.
2019-05-31T10:05:14Z [ERROR] [/registryctl/client/client.go:94]: Failed to start gc: 500
2019-05-31T10:05:14Z [ERROR] [/jobservice/runner/redis.go:161]: failed to get gc result: Failed to start GC: 500
2019-05-31T10:05:14Z [ERROR] [/jobservice/runner/redis.go:63]: |@_@| Job 'IMAGE_GC:fd64d3dc3d8a2b0f04fe0a28' exit with error: Failed to start GC: 500
