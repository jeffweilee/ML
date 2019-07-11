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
(if [ -f /etc/system-release ]; then s=$(cat /etc/system-release); elif [ -f /etc/redhat-release ]; then s=$(cat /etc/redhat-release); elif [ -f /etc/os-release ]; then s=$(cat /etc/os-release | grep PRETTY | cut -d '=' -f2 | sed -e 's/^\"//' -e 's/\"$//'); fi; s=$(echo ${s} | tr '[:upper:]' '[:lower:]'); IFS=$'\n'; if [[ -n $(echo $s | grep 'centos' ) ]] || [[ -n $(echo $s | grep 'red') && -n $(echo $s | grep 'hat') ]]; then a=($(rpm -q kernel --last | awk -F '[[:space:]][[:space:]]+' '{printf "%s,%s\n",$1,$2}')); elif [[ -n $(echo $s | grep 'buntu' ) ]]; then a=($(dpkg --get-selections | grep linux-image | awk '{printf "%s,%s\n",$1,a}' a='NA')); else a='NA,NA'; fi; val=\"\"; for ((i = 0; i < ${#a[@]}; i++)); do p=\\\"HotFixID\\\":\\\"$(echo ${a[i]} | cut -d , -f1)\\\",\\\"InstalledOn\\\":\\\"$(d=$(echo ${a[i]} | cut -d , -f2); if [ $d == 'NA' ]; then echo NA; elif [ $(locale | grep 'LANG' | grep 'zh_') ]; then echo ${a[i]} | cut -d , -f2 | grep -Eo '[0-9]+' | tr '\\n' ' ' | awk '{print $1$2$3}' | { read gmt ; date +%m/%d/%Y -d ${gmt} ; }; else echo ${a[i]} | cut -d , -f2 | { read gmt ; date +%m/%d/%Y -d ${gmt} ; }; fi; )\\\"; val=${val}${p}~; done; echo ${val:0:${#val}-1};)
```



```
(dgateway=($(ip r | grep default | awk '{print$3}')); dgateway_device=($(ip r | grep default | awk '{print$5}')); all_mac_device_ip_mapping=($(ip a | grep -v inet6 | grep -v -E '127\.[[:digit:]]{1,3}\.[[:digit:]]{1,3}\.[[:digit:]]{1,3}' | grep inet -B 2 | sed 's:^[ \t]*::g' | grep [.:] | cut -d ' ' -f2 | cut -d '/' -f1)); val=\"\"; firstflag=0; for i in ${!all_mac_device_ip_mapping[@]}; do if [[ $(echo ${all_mac_device_ip_mapping[i]} | grep -o : | wc -l) -gt 1 ]]; then mac=${all_mac_device_ip_mapping[i]}; elif [[ $(echo ${all_mac_device_ip_mapping[i]} | grep -o : | wc -l) -eq 1 ]]; then mac_device=${all_mac_device_ip_mapping[i]}; mac_device=$(echo ${mac_device} | cut -d ':' -f1 | cut -d '@' -f1); else for k in ${!dgateway_device[@]}; do if [[ ${dgateway_device[k]} == ${mac_device} ]]; then gw=${dgateway[k]}; break; else gw=NA; fi; done; if [[ $(ip a | grep ${all_mac_device_ip_mapping[i]} | grep -c dynamic) -gt 0 ]]; then edhcp=Y; else edhcp=N; fi; if [[ $firstflag -ne 0 ]]; then val=${val}~; fi; firstflag=1; val=${val}\\\"ADDRESS\\\":\\\"${mac}\\\",\\\"IP\\\":\\\"${all_mac_device_ip_mapping[i]}\\\",\\\"W_NICCONFIG_DefaultIPGateway\\\":\\\"${gw}\\\",\\\"DHCP_ENABLE\\\":\\\"${edhcp}\\\"; fi; done; echo ${val};)

```



```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <unistd.h>
#include <time.h>

#define contentLen3096 3096

#define SHELLSCRIPT "\
#!/bin/bash \n \
a=(1 2 3); echo ${a[1]};"

FILE *fcmd1;
char cmdResult1[contentLen3096];
fcmd = popen(SHELLSCRIPT, "r");
if (fgets(cmdResult1, sizeof(cmdResult1), fcmd1) != NULL) {
	printf("[~~~] %s ===== \n", cmdResult1);
}
```


```
let deviceTokenString = deviceToken.reduce("") {
            return $0 + String(format: "%02x", $1)
        }
        print("deviceTokenString: \(deviceTokenString)")
        let json: [String: Any] = ["device_token": deviceTokenString]
        let jsonData = try? JSONSerialization.data(withJSONObject: json)
        
        let url:NSURL = NSURL(string: "https://echo.apps.paas.nctu.me/")!;
        let request:NSMutableURLRequest = NSMutableURLRequest(url: url as URL, cachePolicy: NSURLRequest.CachePolicy.reloadIgnoringLocalCacheData, timeoutInterval: 10);
        request.httpMethod = "POST";
        
        request.httpBody = jsonData;
        
        let task = URLSession.shared.dataTask(with: request as URLRequest) {
            data, response, error in
            
            if error != nil {
                print("error=\(error)")
                return
            }
            
            print("response = \(response)")
            
            //將收到的資料轉成字串print出來看看
            let responseString = NSString(data: data!, encoding: String.Encoding.utf8.rawValue)
            print("responseString = \(responseString)")
        }
        task.resume();

```




# taskList
```
import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter_view/common/common_util.dart';
import 'package:flutter_view/component/loading.dart';
import 'package:flutter_view/config/application_model.dart';
import 'package:flutter_view/service/todo_app_service.dart';
import 'package:flutter_view/service/todo_model.dart';
import 'package:flutter_view/to/menu_choice.dart';
import 'package:flutter_view/to/task_info.dart';
import 'package:flutter_view/to/task_list_info.dart';
import 'package:flutter_view/to/tphone_app_action.dart';
import 'package:flutter_view/component/cus_expansion_tile.dart';
import 'package:flutter_view/util/todo_util.dart';
import 'package:flutter_view/view/app_list_view.dart';
import 'package:flutter_view/view/detail_approval_view.dart';
import '../main.dart';

class TaskListView extends StatefulWidget {
  const TaskListView({Key key, @required this.appName}) : super(key: key);
  final String appName;
  //下面用widget.appName就可以拿到

  @override
  _TaskListViewState createState() {
    return new _TaskListViewState();
//    return new _TaskListViewState(appName: this.appName);
  }
}

class _TaskListViewState extends State<TaskListView> {
  _TaskListViewState({Key key});

  //  _TaskListViewState({Key key, this.appName});
  //  String appName;

  //  bool isUniqueKeyForExpanded = false; //如果是true的話 讓expandListTile強制重新執行 執行完要記得設定回false
  TodoAppService todoAppService;
  TaskInfo taskInfo;
  TodoUtil todoUtil;
  Model model;
  CommonUtil commonUtil;
  List<TaskListInfo> taskItems;
  Loading loading;
  String errCd = '';
  bool _isCheckBoxCheckAll = false;
  //control show approve/reject btn and checkbox
  bool _isShowSignOff = false;
  bool _isInit = true;
  //for search
  Icon searchActionIcon = new Icon(Icons.search);
  Widget appBarTitle;
  bool _isSearching = false;
  List<TaskListInfo> searchTaskItems = new List<TaskListInfo>();

  //右上角select menu
  static String signinAs = ApplicationModel.user.ntAccount ?? '';
  List<MenuChoice> taskListChoice = <MenuChoice>[
    MenuChoice(title: signinAs, icon: Icons.account_circle),
    MenuChoice(title: 'Select/Deselect all', icon: Icons.select_all),
    //MenuChoice(title: 'Sign out', icon: Icons.exit_to_app),
  ];
  //右上角select menu被選擇行為
  void _selectedChoice(MenuChoice choice) {
    switch (choice.title) {
      case "Select/Deselect all":
        setState(() {
          List<TaskListInfo> nowList = new List<TaskListInfo>();
          _isSearching ? nowList = searchTaskItems : nowList = taskItems;

          for (TaskListInfo t in nowList) {
            _isCheckBoxCheckAll ? t.isCheck = false : t.isCheck = true;
          }
          _isCheckBoxCheckAll = !_isCheckBoxCheckAll;
          print('[taskPage] menu click Select all');
        });
        break;
      case 'Sign out':
        print('[taskPage] menu click signout');
        Navigator.of(context).pushReplacementNamed('/login');
        break;
      default:
        break;
    }
  }

  @override
  void initState() {
    super.initState();
    /* Initialize the service */
    todoAppService = new TodoAppService();
    todoUtil = new TodoUtil(context);
    model = ModelLocator.getInstance();
    commonUtil = new CommonUtil(context);
    taskInfo = new TaskInfo();
    taskItems = new List<TaskListInfo>();
    loading = new Loading(context);

    //Get AppList data
    //    new Timer(new Duration(milliseconds: 3000), () {
    //      _initGetTaskListData();
    //    });

    _initGetTaskListData();
  }

  @override
  void dispose() {
    super.dispose();
  }

  //for initial only, doesn't have loading progress
  Future<Null> _initGetTaskListData() async {
    todoAppService.getTaskInfo(widget.appName).then((taskInfoResult) {
      try {
        if (taskInfoResult == null) {
          print('[taskPage] _initGetTaskListData appName: ${widget.appName}');
          this.errCd = model.errCd;
          model.errCd = '';
          commonUtil.errHandle(this.errCd + '\n' + TodoUtil.SERVER_ERR_MSG);
        } else {
          taskInfo = taskInfoResult;
          print('[taskPage] taskInfo: ' + taskInfo.toJson().toString());
          taskItems = taskInfo.taskListInfo;

          /* check show approve/reject button and checkbox or not */
          if (taskInfo.hasAction == 'Y') {
            _isShowSignOff = true;
          }
        }
        setState(() {
          this._isInit = false;
          cancelSearch();
        });
      } on Exception {
        commonUtil.errHandle(this.errCd + '\n' + TodoUtil.SERVER_ERR_MSG);
      }
    });
  }

  Future<Null> _getTaskListData() async {
    bool isServiceRetunNull = false;

    await todoUtil
        .showProgress(
            todoAppService.getTaskInfo(widget.appName).then((taskInfoResult) {
      if (taskInfoResult == null) {
        print('[taskPage] _initGetTaskListData appName: ${widget.appName}');
        isServiceRetunNull = true;
        this.errCd = model.errCd;
        model.errCd = '';
      } else {
        taskInfo = taskInfoResult;
        taskItems = taskInfo.taskListInfo;

        /* check show approve/reject button and checkbox or not */
        if (taskInfo.hasAction == 'Y') {
          _isShowSignOff = true;
        }
      }

      setState(() {
        this._isInit = false;
        cancelSearch();
      });
    }))
        .then((Null) {
      if (isServiceRetunNull) {
        print(
            '[taskPage] _getTaskListData isServiceRetunNull: $isServiceRetunNull');
        commonUtil.errHandle(this.errCd + '\n' + TodoUtil.SERVER_ERR_MSG);
      }
    });
  }

//  _reloadExpansionTile() {
//    setState(() {
//      isUniqueKeyForExpanded = true;
//      print("!!!!" + isUniqueKeyForExpanded.toString());
//    });
//    isUniqueKeyForExpanded = false;
//  }

  Widget getItem(TaskListInfo taskListInfo) {
    return new Card(
        color: taskListInfo.isNew == "Y" ? Colors.white70 : Colors.white,
        child: new Column(
          children: <Widget>[
            new Padding(
              padding: new EdgeInsets.symmetric(vertical: 10.0),
              child: new Row(
                children: <Widget>[
                  _isShowSignOff == true
                      ? new Checkbox(
                          value: taskListInfo.isCheck,
                          onChanged: (bool value) {
                            setState(() {
                              taskListInfo.isCheck = value;
                            });
                          })
                      : new Container(),
                  new Expanded(
                    child: new CusExpansionTile(
                      test: "test",
                      onTapExpandFunction: () {
                        print(taskListInfo.isNew);
                        /* Change to N before call REST */
                        taskListInfo.isNew = "N";
                        //call update isNew's REST ==> "../cxf/MyToDoUIPCRestService/todo/insertUsageHist"
                        todoAppService.insertUsageHist(
                            taskInfo.typeCd, taskListInfo.taskId);
                        setState(() {});
                      },
//                key: isUniqueKeyForExpanded == true ? new UniqueKey() : null,
//                      key: new UniqueKey(),
//                  leading: new Icon(Icons.announcement),
                      title: new Text(
                        todoUtil.unicodeToChinese(taskListInfo.subject),
                        style: new TextStyle(
                            fontSize: 18.0,
                            color: Colors.black87,
                            fontWeight: FontWeight.w600),
                      ),

                      children: <Widget>[
                        new Padding(
                          padding: new EdgeInsets.only(top: 10.0),
                          child: new Column(
                            children: buildExpandableContent(taskListInfo),
                          ),
                        ),
                      ],
                    ),
                  ),
                  new FlatButton(
                      onPressed: () {
                        print('[taskPage] Task item Container clicked');
                        taskListInfo.isNew = "N";
                        //call update isNew's REST ==> "../cxf/MyToDoUIPCRestService/todo/insertUsageHist"
                        todoAppService.insertUsageHist(
                            taskInfo.typeCd, taskListInfo.taskId);

                        if (_isShowSignOff == true) {
                          print('[taskPage] Task item clicked -> Detail page');
                          Navigator.push(
                            context,
                            new MaterialPageRoute(
                                builder: (context) => new DetailApproval(
                                    typeCd: taskInfo.typeCd,
                                    taskId: taskListInfo.taskId,
                                    isFromRoute: false)),
                          );
                        } else {
                          print(
                              '[taskPage] Task item clicked -> Open browser: ${taskListInfo.appUrl}');
                          ApplicationModel.platformUtil.launchWebViewByUrl(
                              'com.tsmc.mgrapprovalapp',
                              'com.tsmc.mgrapprovalapp.MainActivity',
                              taskListInfo.appUrl);
                        }
                      },
                      padding: new EdgeInsets.symmetric(vertical: 40.0),
                      child: new Column(
                        mainAxisSize: MainAxisSize.max,
                        children: <Widget>[
                          new Icon(
                            _isShowSignOff == true
                                ? Icons.play_arrow
                                : Icons.open_in_browser,
                            size: 28.0,
                            color: Colors.black38,
                          ),
                        ],
                      )),
                ],
              ),
            ),
//        new Divider(
//          color: Colors.grey[5000],
//          height: 20.0,
//        ),
          ],
        ));
  }

  List<Widget> buildExpandableContent(TaskListInfo taskListInfo) {
    List<Widget> columnContent = [];

    columnContent.add(
      new ListTile(
        title: new Text(
          "Description",
          style: new TextStyle(fontSize: 16.0, color: Colors.black54),
        ),
        subtitle: new Text(
          todoUtil.unicodeToChinese(taskListInfo.description),
          style: new TextStyle(fontSize: 16.0, color: Colors.black54),
        ),
      ),
    );
    columnContent.add(
      new ListTile(
        title: new Text(
          "Create Date",
          style: new TextStyle(fontSize: 16.0, color: Colors.black54),
        ),
        subtitle: new Text(
          taskListInfo.createDate,
          style: new TextStyle(fontSize: 16.0, color: Colors.black54),
        ),
      ),
    );

    return columnContent;
  }

  /* click action when signOff btn click */
  _signOffBtnClick(String actionName) {
    bool isSelectAnyCheckbox = false;
    String actionParas = "";

    /* check if any checkbox select, if not, show remind dialog, also prepare actionParas as sign-off needed parameter(list of selected checkbox) */
    for (TaskListInfo t in taskItems) {
      if (t.isCheck) {
        isSelectAnyCheckbox = true;
        actionParas += (t.actionPara + ",");
      }
    }
    /* remove last ',' to match input criteria */
    if (actionParas != "") {
      actionParas = actionParas.substring(0, actionParas.length - 1);
    }
    print('[taskPage] _signOffBtnClick actionParas: $actionParas');

    /* if no task select */
    if (!isSelectAnyCheckbox) {
      commonUtil.infoHandle("Please select task.", () {});
    }
    ////////////////////////////
    //Run sign-off process part
    ///////////////////////////
    else {
      //check if need to show sign-off dialog
      if (taskInfo.isCmmtReq == "Y") {
        /* show sign-off dialog: Add isCommentRequired logic(need to type input comment) */
        bool isRequiredComment = false;
        if (taskInfo.isCmmtContChk == 'Y' ||
            (taskInfo.isCmmtContChk == 'S' &&
                actionName == taskInfo.secondActionName)) {
          isRequiredComment = true;
        }
        /* show sign-off dialog */
        commonUtil.commentHandle(actionName, () {
          sendAppAction(actionParas, actionName, model.commentMsg);
        }, () {}, isRequiredComment);
      }
      /* direct call rest */
      else {
        sendAppAction(actionParas, actionName, "");
      }
    }

    /* 參考下面的approve那段的code 統一做法
    首先先判斷有沒有勾任何東西 沒有的話彈窗告訴說要勾選東西
    不管是不是UI ACKED了 後面會判斷好? 統一call appAction
    首先要判斷的應該是 有沒有要show dialog 如果沒有就直接call appAction(給那三個參數 其中兩個塞空值?)
    如果有的話 call show dialog的common 然後裡面要去判斷 Y/S之類的(html邏輯) 有沒有一定要打comment這件事
    有要打comment的話 jeff的彈窗 沒有的話 預設給空值
    無論如何 call appAction都給那三個參數
    然後關掉dialog並reload list */
  }

  TphoneAppAction appActionResult;
  Future<String> sendAppAction(
      String actionParas, String actionName, String comment) async {
    bool isServiceRetunNull = false;

    await todoUtil
        .showProgress(todoAppService
            .tPhoneAppAction(actionParas, actionName, comment)
            .then((TphoneAppAction result) {
      if (result == null) {
        isServiceRetunNull = true;
        this.errCd = model.errCd;
        model.errCd = '';
      } else {
        appActionResult = result;
      }
    }))
        .then((dynamic) {
      if (isServiceRetunNull) {
        commonUtil.errHandle(this.errCd + '\n' + TodoUtil.SERVER_ERR_MSG);
      } else {
        appActionResult.status == TodoUtil.SUCCESS
            ? commonUtil.infoHandle(appActionResult.resultMsg, _getTaskListData)
            : commonUtil.errHandle(appActionResult.resultMsg,
                funOK: _getTaskListData);
      }
    });
  }

  Widget buildButtonSection() {
    /* check if first or second actionName exist. If exist, add to list to generate button */
    List<String> activeActionName = [];
    if (taskInfo.firstActionName != "") {
      activeActionName.add(taskInfo.firstActionName);
    }
    if (taskInfo.secondActionName != "") {
      activeActionName.add(taskInfo.secondActionName);
    }
    // print("!!!!" + activeActionName.toString());
    List<Widget> _listBtn = activeActionName.map<Widget>((String actionName) {
      return new Expanded(
        child: new FlatButton(
            onPressed: () {
              _signOffBtnClick(actionName);
            },
            child: new Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                new Icon(
                  actionName == "Approve" ? Icons.check_circle : Icons.cancel,
                  color: Colors.white,
                ),
                new Padding(padding: EdgeInsets.symmetric(horizontal: 3.0)),
                new Text(actionName,
                    style: new TextStyle(fontSize: 20.0, color: Colors.white)),
              ],
            )),
      );
    }).toList();

    var _listBtnSize = _listBtn.length;
    for (var i = 1; i < _listBtnSize; i++) {
      _listBtn.insert(
          2 * i - 1,
          new Container(
            width: 1.0,
            height: 55.0,
            color: Colors.white,
          ));
    }
    /* Add btn height */
    _listBtn.insert(
        0,
        new Container(
          height: 55.0,
        ));

    return new BottomAppBar(
      color: Colors.blue,
      child: new Row(
        children: _listBtn,
      ),
    );
  }

  void clearCheckbox() {
    setState(() {
      for (TaskListInfo t in taskItems) {
        t.isCheck = false;
      }
      print("[taskPage]: clearCheckbox Clear all checkbox");
    });
  }

  void cancelSearch() {
    searchTaskItems.clear();
    _isSearching = false;
    this.searchActionIcon = new Icon(Icons.search);
  }

  Widget _buildAppBar() {
    //set title
    appBarTitle = searchActionIcon.icon == Icons.search
        ? new Text(taskInfo.typeCd == null ? "" : taskInfo.typeCd,
            style: new TextStyle(
              fontSize: 22.0,
            ))
        : appBarTitle;

    return new AppBar(
      leading: new IconButton(
          icon: new Icon(Icons.arrow_back),
          onPressed: () {
            Navigator.push(context,
                new MaterialPageRoute(builder: (context) => new AppListView()));
          }),
      title: appBarTitle,
      actions: <Widget>[
        new IconButton(
          icon: searchActionIcon,
          onPressed: () {
            setState(() {
              clearCheckbox();

              if (this.searchActionIcon.icon == Icons.search) {
                searchTaskItems.clear();
                _isSearching = true;
                this.searchActionIcon = new Icon(Icons.close);

                this.appBarTitle = new TextField(
                  style: new TextStyle(
                    color: Colors.white,
                  ),
                  autofocus: true,
                  decoration: new InputDecoration(
                      prefixIcon: new Icon(Icons.search, color: Colors.white),
                      hintText: "Search...",
                      hintStyle: new TextStyle(color: Colors.white)),
                  onChanged: (text) {
                    clearCheckbox();
                    searchTaskItems.clear();
                    text = text.toLowerCase();
                    for (TaskListInfo nowTask in taskItems) {
//                      if (nowTask.subject.toLowerCase().contains(text) ||
//                          nowTask.createDate.toLowerCase().contains(text) ||
//                          nowTask.description.toLowerCase().contains(text)) {
                      if ((nowTask.subject.toLowerCase().contains(text) ||
                              nowTask.description
                                  .toLowerCase()
                                  .contains(text)) &&
                          text != "") {
                        searchTaskItems.add(nowTask);
                      }
                    }

                    setState(() {});
                  },
                );
              } else {
                /* Cancel search button */
                cancelSearch();
              }
            });
          },
        ),

        /* action button */
        IconButton(
            icon: Icon(Icons.autorenew),
            onPressed: () {
              setState(() {
                /* reset serviceDelegate */
                todoAppService = new TodoAppService();
                /* for search bar */
                cancelSearch();
                /* end for search bar */
                _getTaskListData();
              });
            }),
        IconButton(
            icon: Icon(Icons.select_all),
            onPressed: () {
              setState(() {
                List<TaskListInfo> nowList = new List<TaskListInfo>();
                _isSearching ? nowList = searchTaskItems : nowList = taskItems;

                for (TaskListInfo t in nowList) {
                  _isCheckBoxCheckAll ? t.isCheck = false : t.isCheck = true;
                }
                _isCheckBoxCheckAll = !_isCheckBoxCheckAll;
                print('[taskPage] app bar click Select all');
              });
            }),
        PopupMenuButton<MenuChoice>(
          onSelected: _selectedChoice,
          itemBuilder: (BuildContext context) {
            return taskListChoice.map((MenuChoice choice) {
              return PopupMenuItem<MenuChoice>(
                value: choice,
                child: Row(children: <Widget>[
                  Padding(
                      padding: EdgeInsets.fromLTRB(0.0, 0.0, 8.0, 0.0),
                      child: Icon(choice.icon)),
                  Text(choice.title)
                ]),
              );
            }).toList();
          },
        ),
      ],
    );
  }

  @override
  Widget build(BuildContext context) {
    List<TaskListInfo> nowItems;
    _isSearching ? nowItems = searchTaskItems : nowItems = taskItems;

    return new Scaffold(
      // appBar: _isSearching ?  : _buildAppBar(),
      appBar: _buildAppBar(),
      body: this._isInit
          ? loading.cirPgs
          : new Column(children: <Widget>[
              new Expanded(
                child: new ListView.builder(
                  itemCount: nowItems.length,
                  itemBuilder: (context, index) {
                    return getItem(nowItems[index]);
                  },
                ),
              ),
            ]),
      /* Approve & Reject Button, if didn't have check box, do not show them */
      bottomNavigationBar: _isShowSignOff == true ? buildButtonSection() : null,
    );
  }
}

```

# Detail

```
import "dart:async";
import 'package:flutter/material.dart';
import 'package:flutter_view/common/common_util.dart';
import 'package:flutter_view/config/application_model.dart';
import 'package:flutter_view/service/todo_app_service.dart';
import 'package:flutter_view/component/loading.dart';
import 'package:flutter_view/service/todo_model.dart';
import 'package:flutter_view/to/detail_approval_info.dart';
import 'package:flutter_view/to/detail_button.dart';
import 'package:flutter_view/to/detail_info.dart';
import 'package:flutter_view/to/tphone_app_action.dart';
import 'package:flutter_view/util/show_progress.dart';
import 'package:flutter_view/util/todo_util.dart';
import 'package:flutter_view/view/task_list_view.dart';

const kAndroidUserAgent =
    "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Mobile Safari/537.36";

class DetailApproval extends StatefulWidget {
  DetailApproval({Key key, this.typeCd, this.taskId, this.isFromRoute})
      : super(key: key);
  final String typeCd;
  final String taskId;
  final bool isFromRoute;

  @override
  State<StatefulWidget> createState() => new _DetailApprovalState();
}

class _DetailApprovalState extends State<DetailApproval> {
  _DetailApprovalState({Key key});

  String errCd = "";
  String resMsg = "";
  String resMsgId = "";
  String btnPressedText = "";

  ThemeData themeData;
  TodoAppService todoAppService;
  CommonUtil commonUtil;
  TodoUtil todoUtil;
  Model model;
  bool _isInit = true;
  Loading loading;
  String subject = "";
  Map<String, IconData> iconList = {
    "edit": Icons.edit,
    "add": Icons.add,
    "remove": Icons.remove,
    "delete": Icons.delete,
    "check": Icons.check_circle,
    "cancel": Icons.cancel,
  };

  @override
  void initState() {
    super.initState();
    /* Initialize the service */
    todoAppService = new TodoAppService();
    model = ModelLocator.getInstance();
    commonUtil = new CommonUtil(context);
    todoUtil = new TodoUtil(context);
    loading = new Loading(context);
    print("widget.isFromRoute: " + widget.isFromRoute.toString());
    _calc();
  }

  @override
  void dispose() {
    super.dispose();
  }

  Future<Null> _calc() async {
    todoAppService
        .getDetailApprovalInfo(widget.typeCd, widget.taskId)
        .then((_) {
      try {
        setState(() {
          this._isInit = false;
          if (model != null &&
              model.detailApprovalInfo != null &&
              model.detailApprovalInfo.typeCd != null &&
              model.detailApprovalInfo.taskId != null &&
              model.errCd.isEmpty) {
            subject = model?.detailApprovalInfo?.subject;
            print("[detailPage] subject:" + subject);
          } else {
            this.errCd = model.errCd;
            model.errCd = '';
            this.resMsg = this.errCd + '\n' + TodoUtil.SERVER_ERR_MSG;
            commonUtil.errHandle(this.resMsg);
          }
        });
      } on Exception {
        commonUtil.errHandle(this.errCd + '\n' + TodoUtil.SERVER_ERR_MSG);
      }
    });
  }

  Future<Null> submit() async {
    print(
        '[detailPage] submit: actionPara ~ actionName ~ Comment: ${model.detailApprovalInfo.actionPara} ~ ${this.btnPressedText} ~ ${model.commentMsg}');
    todoUtil
        .showProgress(todoAppService
            .tPhoneAppAction(model.detailApprovalInfo.actionPara,
                this.btnPressedText, model.commentMsg)
            .then((TphoneAppAction res) {
      if (res == null) {
        this.errCd = model.errCd;
        model.errCd = '';
        this.resMsg = this.errCd + '\n' + TodoUtil.SERVER_ERR_MSG;
        this.resMsgId = TodoUtil.FAIL;
      } else {
        this.resMsgId = res.status;
        this.resMsg = res.resultMsg;
      }
    }))
        .then((_) {
      this.resMsgId == TodoUtil.SUCCESS
          ? commonUtil.infoHandle(this.resMsg, () {
              this.resMsgId == TodoUtil.SUCCESS
                  ? Navigator.pushReplacement(
                      context,
                      new MaterialPageRoute(
                          builder: (context) => new TaskListView(
                                appName: widget.typeCd,
                              )),
                    )
                  : null;
            })
          : commonUtil.errHandle(this.resMsg);
    });
  }

  _actionDispatch(String text, bool isShowDialog, bool isCommentNecessary) {
    print(
        '##### Button pressed: $text isShowDialog: $isShowDialog isCommentNecessary:$isCommentNecessary');
    this.btnPressedText = text;
    isShowDialog
        ? commonUtil.commentHandle(text, submit, () {}, isCommentNecessary)
        : commonUtil.confirmHandle('Are you sure to $text?', submit, () {});
  }

  Future<void> _openURL(DetailInfo info) async {
    try {
      print(
          '[detailPage] type: ${info.type}, _openURL: ${info.url}, dest: ${info.browser}');
      if (info.url.startsWith('http')) {
        if (info.type == TodoUtil.DETAIL_ATTACH &&
            (info.browser == TodoUtil.DETAIL_BROWSER_EMB ||
                info.browser == TodoUtil.DETAIL_BROWSER_EXT)) {
          ApplicationModel.platformUtil.launchWebViewByUrl(
              'com.tsmc.mgrapprovalapp',
              'com.tsmc.mgrapprovalapp.MainActivity',
              info.url);
        } else {
          ApplicationModel.platformUtil.openBrowser(info.url);
        }
      }
    } on Exception catch (e) {
      print('[detailPage] _openURL error: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    themeData = Theme.of(context);
    print('[detailPage] typeCd: ${widget.typeCd}, taskId:${widget.taskId}');
    Widget _buildListTile(BuildContext context, DetailInfo info, int index) {
      return new ListTile(
//      isThreeLine: true,
//        leading: new ExcludeSemantics(
//            child: new CircleAvatar(
////          child: new Text(index.toString(),
////              style: themeData.primaryTextTheme.title),
//          radius: 5.0,
//          backgroundColor: Colors.lightBlue,
//        )),
        title: new Text(todoUtil.unicodeToChinese(info.header),
            style: themeData.textTheme.title),
        subtitle: info.type == TodoUtil.DETAIL_TEXT ||
                info.type == TodoUtil.DETAIL_LINK ||
                info.type == TodoUtil.DETAIL_ATTACH
            ? new Text("${todoUtil.unicodeToChinese(info.text)}",
                style: themeData.textTheme.subhead)
            : info.type == TodoUtil.DETAIL_IMG && info.text.contains('tsmc.com')
                ? new Padding(
                    padding: EdgeInsets.symmetric(vertical: 10.0),
                    child: new Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          new Expanded(
                            child: new Image.network(
                              info.text,
                              fit: BoxFit.fitWidth,
                              alignment: Alignment.center,
                            ),
                          )
                        ]))
                : null,
        trailing: (info.type != TodoUtil.DETAIL_LINK &&
                    info.type != TodoUtil.DETAIL_ATTACH) ||
                info.url.isEmpty ||
                !info.url.startsWith('http')
            ? null
            : info.browser == TodoUtil.DETAIL_BROWSER_EMB &&
                    TodoUtil.OS == TodoUtil.iOS
                ? new Icon(
                    Icons.chevron_right,
                    color: Colors.blueGrey,
                  )
                : new Icon(
                    Icons.launch,
                    color: Colors.blueGrey,
                  ),
        onTap: () => (info.type == TodoUtil.DETAIL_LINK ||
                    info.type != TodoUtil.DETAIL_ATTACH) &&
                info.url != ""
            ? _openURL(info)
            : null,
      );
    }

    Widget _buildDetailList() {
      if (model.detailApprovalInfo == null) {
        return new Center(
            child: new Padding(
                padding:
                    EdgeInsets.symmetric(vertical: 200.0, horizontal: 30.0),
                child: new Column(children: <Widget>[
                  new Icon(
                    Icons.error_outline,
                    size: 50.0,
                  ),
                  new Text(
                    TodoUtil.SERVER_ERR_MSG,
                    style: themeData.textTheme.headline,
                    textAlign: TextAlign.center,
                  )
                ])));
      }
      int index = 0;
      List<Widget> _listView =
          model.detailApprovalInfo.detailInfos.map<Widget>((dynamic info) {
        index++;
        return new Column(children: <Widget>[
          _buildListTile(context, info, index),
          new Container(
              margin: EdgeInsets.symmetric(vertical: 8.0),
              decoration: new BoxDecoration(
                  border: new Border.all(width: 0.1, color: Colors.grey))),
        ]);
      }).toList();

      if (_listView.length == 0)
        _listView.insert(
            0,
            new ListTile(
              title: new Center(
                  child: new Padding(
                      padding: EdgeInsets.symmetric(vertical: 250.0),
                      child: new Text(
                        TodoUtil.NO_DETAIL_INFO,
                        style: themeData.textTheme.headline,
                        textAlign: TextAlign.center,
                      ))),
            ));

      return new ListView(
          padding: new EdgeInsets.symmetric(vertical: 4.0),
          children: _listView);
    }

    Widget buttonSection() {
      if (model.detailApprovalInfo == null) return null;
      if (model.detailApprovalInfo.detailInfos.length == 0) return null;

      var btnTextCount = 0;
      for (DetailButton i in model.detailApprovalInfo.detailButtons) {
        btnTextCount += i.text.length + 1;
      }
      List<Widget> _listBtn = model.detailApprovalInfo.detailButtons
          .map<Widget>((DetailButton info) {
        return new Expanded(
            child: new FlatButton(
                onPressed: () {
                  _actionDispatch(
                      info.text, info.isShowDialog, info.isCommentNecessary);
//                  showDialog(
//                      context: context,
//                      child: new AlertDialog(
//                        title: new Text(info.text),
//                        content: new Container(
//                            width: 100.0,
//                            child: new TextField(
//                              maxLines: 5,
//                              style: new TextStyle(
//                                  fontSize: 20.0, color: Colors.black),
//                              onChanged: (value) {
//                                this.submitMsg = value;
//                              },
//                              decoration:
//                                  new InputDecoration(hintText: "Comment"),
//                            )),
//                        actions: <Widget>[
//                          new FlatButton(
//                            onPressed: () {},
//                            child: new Text("OK"),
//                          ),
//                          new FlatButton(
//                            onPressed: () {
//                              Navigator.of(context).pop(true);
//                            },
//                            child: new Text("Cancel"),
//                          ),
//                        ],
//                      ));
                },
                child: new Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      new Icon(
                        iconList[info.style],
                        color: Colors.white,
                      ),
                      new Padding(
                          padding: EdgeInsets.symmetric(horizontal: 3.0)),
                      new Text(info.text,
                          style: new TextStyle(
                              fontSize: 300 / btnTextCount > 20.0
                                  ? 20.0
                                  : 300 / btnTextCount,
                              color: Colors.white)),
                    ])));

//        return new RaisedButton(
//            onPressed: null,
//            textColor: Colors.blue,
//            color: Colors.blue,
//            padding: EdgeInsets.symmetric(horizontal: 24.0, vertical: 8.0),
//            child: new Text(info.text, style: themeData.textTheme.title),
//            shape: new RoundedRectangleBorder(
//                borderRadius: new BorderRadius.circular(20.0)));
      }).toList();

      var _listBtnSize = _listBtn.length;
      if (_listBtnSize == 1) {
        _listBtn.insert(
            1,
            new Container(
              width: 1.0,
              height: 55.0,
            ));
      }
      for (var i = 1; i < _listBtnSize; i++) {
        _listBtn.insert(
            2 * i - 1,
            new Container(
              width: 1.0,
              height: 55.0,
              color: Colors.white,
            ));
      }

      return new BottomAppBar(
//        color: themeData.buttonColor,
        color: themeData.primaryColor,
        child: new Row(
          children: _listBtn,
        ),
      );
    }

    return new Scaffold(
      //key: scaffoldKey,
      appBar: new AppBar(
        automaticallyImplyLeading: !widget.isFromRoute,
        actions: <Widget>[
          IconButton(
              icon: Icon(Icons.home),
              onPressed: () {
                Navigator.pushReplacementNamed(context, '/AppListView');
              }),
        ],
        title: new Text(subject),
      ),
      body: this._isInit ? loading.linPgs : _buildDetailList(),
      bottomNavigationBar: this._isInit ? null : buttonSection(),
    );
  }
}

```
