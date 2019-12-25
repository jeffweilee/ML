# Flutter + VMware Airwatch SDK

## Table of contents

- [Flutter + VMware Airwatch SDK](#flutter--vmware-airwatch-sdk)
  - [Table of contents](#table-of-contents)
  - [Overview](#overview)
  - [Flutter](#flutter)
  - [Workspace ONE (Airwatch) SDK](#workspace-one-airwatch-sdk)
  - [Integrate Airwatch SDK with Flutter Project](#integrate-airwatch-sdk-with-flutter-project)
  - [Xcode for Flutter Notes](#xcode-for-flutter-notes)
  - [Copyright](#copyright)

## Overview

This article will go through how to integrate **Flutter** and **Airwatch SDK** to build a enterprise hybrid-native app since that VMware does not officially support.

Notice that this article uses Flutter iOS Swift project for example. It is assumed you have basic Flutter knowledge. Also, it is assumed that your organization already have VMware Mobile Application Management solution ready.

## Flutter

> Flutter is Google’s UI toolkit for building beautiful, natively compiled applications for mobile, web, and desktop from a single codebase.

- [Official Website](https://flutter.dev)
- [Install](https://flutter.dev/docs/get-started/install)
  - [macOS install](https://flutter.dev/docs/get-started/install/macos)
  - ```flutter create -i swift your_project_name```

- Architecture
  
```
.
├── android
├── assets
├── ios
│   ├── Flutter
│   ├── Podfile
│   ├── Runner
│   │   ├── AppDelegate.swift
│   │   ├── Assets.xcassets
│   │   │   ├── splash_logo.imageset
│   │   ├── GeneratedPluginRegistrant.h
│   │   ├── GeneratedPluginRegistrant.m
│   │   ├── Info.plist
│   │   ├── Runner-Bridging-Header.h
│   │   ├── Runner.entitlements
│   ├── Runner.xcodeproj
│   ├── Runner.xcworkspace
├── lib
├── pubspec.yaml
```

## Workspace ONE (Airwatch) SDK

> The VMware Workspace ONE® SDK is a set of tools allowing organizations to incorporate a host of features and functionality into their custom-built iOS applications. The Workspace ONE SDK enhances the security and functionality of those applications and in turn helps save application development time and money.<sup>1</sup><br><br>
<sup>1</sup><sub>1 VMware Workspace ONE SDK for iOS (Swift) by VMware Workspace ONE UEM</sub>

Workspace ONE SDK v19.8.1
- iOS 9 or later
- Workspace ONE UEM Console 9.5 or later
- Xcode 10.1 and 10.2 (iOS 12.2)

Architecture
  
```
.
├─────────────────────────────│
├── Application               │
├── Flutter SDK               │
├── Airwatch SDK              │
├─────────────────────────────│
│               ├─────────────│
├── Platform ───|ACE AppConfig│
│               ├─────────────│
├── EMM (MAM, VPN, Profiles)  │
├─────────────────────────────│
├── Mobile Operating System ──│
├─────────────────────────────│
.
```

ACE AppConfig
- MAM will send per app config key-value pair to device (e.g. domain, user)

  ```
  let managedConfigDict = UserDefaults.standard.dictionary(forKey: "com.apple.configuration.managed"){
              if let userNamekeyValue = managedConfigDict["userName"]{
                  print("KEY : userNamekeyValue \nVALUE : \(userNamekeyValue)")
                  username = userNamekeyValue as! String
              }
              if let domainkeyValue = managedConfigDict["domainName"]{
                  print("KEY : domainkeyValue \nVALUE : \(domainkeyValue)")
                  domain = domainkeyValue as! String
              }
  }
  ```

Branding splash logo

- Drag icon to Xcode ```/Assets.xcassets```, and will generate XXX.imageset resource folder
- Copy AWSDKDefaults.bundle from VMware Airwatch sample project to Runner
- Revise AWSDKDefaultsSettins.plist

    ```
    ├── Branding        [dictionary]
    │   ├── SplashLogo_1x   [string]
    │   │   ├── (icon file name without path and extension)
    │   ├── SplashLogo_2x   [string]
    │   │   ├── (icon file name without path and extension)

    ```

## Integrate Airwatch SDK with Flutter Project

AppDelegate.swift

- import AWSDK and Flutter SDK

```
import UIKit
import Flutter
import AWSDK
```

- UIApplicationMain
  - Decompose Flutter component to avoid dependency with AWSDK
  - Inherit
    - UIResponder
    - UIApplicationDelegate
    - UIWebViewDelegate
    - FlutterAppLifeCycleProvider
    - AWControllerDelegate

```
@UIApplicationMain
@objc class AppDelegate: UIResponder,UIApplicationDelegate,UIWebViewDelegate,FlutterAppLifeCycleProvider,AWControllerDelegate {

    /* Flutter Engine */
    let lifeCycleDelegate = FlutterPluginAppLifeCycleDelegate()
    var flutterEngine : FlutterEngine?;
    func add(_ delegate: FlutterApplicationLifeCycleDelegate & NSObjectProtocol) {
        lifeCycleDelegate.add(delegate)
    }

    /* Flutter View */
    var rootFlutterViewController:FlutterViewController? {
        let viewController = UIApplication.shared.keyWindow?.rootViewController
        if viewController!.isKind(of: FlutterViewController.self) {
            return viewController as? FlutterViewController
        }
        return nil
    }

    /* AW Launch */
    func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
        ) -> Bool {
            let controller : FlutterViewController = window?.rootViewController as! FlutterViewController

            // Get the singleton instance for the Workspace ONE SDK's Controller.
            let controllerAW = AWController.clientInstance()
            // Set callback scheme(URL Scheme) that Workspace ONE SDK should use to communication with Workspace ONE anchor applications.
            // This callback scheme should be one of the supported URL Schemes by this application.
            // This string should match with the entry in the info.plist.
            // Replace this with one of your application's supported URL Schemes.
            controllerAW.callbackScheme = ""
            // Modify the Retry Timeout and Maximum Number of Retry Attempts: the timeout value defaults to 5 milliseconds and the maximum number of retry attempts defaults to 10.
            let success = controllerAW.setPendingCertificateRetry(timeout: 5.0, maxAttempts: 10)
            // Set the delegate for Workspace ONE SDK's Controller. This delegate will recieve events from Workspace ONE SDK as callbacks.
            controllerAW.delegate = self
            // Finally. Start the Workspace ONE SDK.
            // Note: You need to start Workspace ONE SDK's Controller at most once per application launch.
            // Workspace ONE SDK's Controller will monitor for the application lifecycle and refreshes access, authorization.
            // So starting Workspace ONE SDK everytime just duplicates this and may not look nice from UI perspective as well.

            controllerAW.start()
            AWLogVerbose("Starting Workspace ONE SDK")
            os_log("Starting Workspace ONE SDK")
        }

}
```

- HTTP Request
  - To Tunnel HTTP request via VMware Tunnel Proxy (MAG), requests have to go through native layer. 
    > VMware Tunnel for App Tunneling by Proxy Components:<br>
The proxy components of the VMware Tunnel provides a secure method for individual applications that use the VMware Workspace ONE SDK to access corporate resources.
The Tunnel proxy component uses HTTPS tunneling to use a single port to filter traffic through an encrypted HTTPS tunnel for connecting to internal sites such as SharePoint or a wiki. The Workspace ONE SDK for iOS (Swift) provides app tunneling without adding code to the application. However, you need to configure app tunneling in the Workspace ONE UEM console.

  - Limitation
    > Due to platform and other technical limitations, only network traffic made from certain network classes can tunnel. Consider the purpose of the listed classes and review their known limitations.<br>
    * NSURLConnection – Calls made with NSURLConnection tunnel. There is one exception to this behavior. If calls are made synchronously on the main thread, they do not tunnel.<br>
    * NSURLSession – Calls made using NSURLSession tunnel only on iOS 8+ devices and depending on the configuration used. Default and ephemeral configuration types tunnel. However, background configuration types do not tunnel.<br>
    * CFNetwork – Most calls made using CFNetwork tunnel. However, CFSocketStream do not tunnel.<br>
    * URLs that contain .local – Requests with URLs containing .local do not tunnel. Various Apple services on the device use this .local string pattern. The SDK does not tunnel these requests through the VMware Tunnel to avoid interfering with these services.<br>
    * WKWebView - Requests made with WKWebView do not tunnel so use UIWebView.

  - Solution
    - Build Swift HTTP Request function with Flutter native channel
    - Flutter native channel
      - Create channel **httprequest** with method **http_get** and **http_post**
  
        ```
        /* Http Request */
        let httpChannel = FlutterMethodChannel(name: "httprequest",  binaryMessenger: controller as! FlutterBinaryMessenger)
        httpChannel.setMethodCallHandler({
            (call: FlutterMethodCall, result: @escaping FlutterResult) -> Void in
            guard (call.method == "http_get" || call.method == "http_post") else {
                result(FlutterMethodNotImplemented)
                return
            }

            if let myArgs = call.arguments as? [String: Any],
                let url = myArgs["url"] as? String,
                let json = myArgs["json"] as? String,
                let parm = myArgs["parm"] as? String,
                let token = myArgs["token"] as? String {
                print("httpChannel arguments url: \(url),")

                if (call.method == "http_get") {
                    self.createRequest(qMes:"", location:url, method:"GET", isJson:false) { (output) in  result(output)}
                }else if(call.method == "http_post"){
                    var body = ""
                    var isJson = false
                    if(!json.isEmpty){
                        body = json
                        isJson = true
                    }else if(!parm.isEmpty){
                        body = parm
                    }
                    self.createRequest(qMes:body, location:url, method:"POST", isJson:isJson) { (output) in result(output)}
                }
            } else {
                result("Swift could not extract flutter arguments in method: (sendParams)")
            }
        })
        ```

    - Swift **createRequest** function
  
        ```
        public func createRequest(qMes:String, location:String, method:String, isJson:Bool, completionBlock: @escaping (String) -> Void) -> Void
        {
            let requestURL = URL(string: location)
            var request = URLRequest(url: requestURL!)
            request.cachePolicy = .reloadIgnoringLocalAndRemoteCacheData
            request.httpMethod = method

            /* handle request header and body */
            if(!qMes.isEmpty){
                if(isJson){
                    request.setValue("application/json", forHTTPHeaderField: "Content-Type")
                    let data = qMes.data(using: .utf8)!
                    do {
                        if let json = try JSONSerialization.jsonObject(with: data, options: .allowFragments) as? [String: AnyObject]
                        {
                            let jsonData = try? JSONSerialization.data(withJSONObject: json)
                            request.httpBody = jsonData
                        }else {
                            print("createRequest: bad json")
                        }
                    } catch let error as NSError {
                        print("createRequest Failed to load: \(error.localizedDescription)")
                    }
                }else{
                    request.setValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")
                    request.httpBody = qMes.data(using: .utf8)
                }
            }

            /* send request */
            request.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
            let sessionConfig = URLSessionConfiguration.default
            sessionConfig.requestCachePolicy = .reloadIgnoringLocalAndRemoteCacheData
            sessionConfig.timeoutIntervalForRequest = 5.0
            sessionConfig.timeoutIntervalForResource = 30.0
            let session = URLSession(configuration: sessionConfig, delegate: self, delegateQueue: OperationQueue.main)
            let requestTask = session.dataTask(with: request){
                (data: Data?, response: URLResponse?, error: Error?) in
                if(error != nil) {
                    print("[[createRequest]: request data task error: \(self.deviceReqErr)")
                    os_log("[createRequest]: request data task error: %{public}@", self.deviceReqErr)
                    AWLogError("createRequest]: request data task error: \(self.deviceInitErr)")
                    completionBlock("")
                }else{
                    let outputStr  = String(data: data!, encoding: String.Encoding.utf8)
                    print("res: \(outputStr!)")
                    os_log("[actr] createRequest outputStr res  %@", String(describing: outputStr))
                    completionBlock(outputStr ?? "")
                }
            }
            requestTask.resume()
        }
        ```

    - Force to trust domain over SSL
      - NSURLConnectionDelegate
  
        ```
        extension AppDelegate: NSURLConnectionDelegate{
            func connection(_ connection: NSURLConnection, canAuthenticateAgainstProtectionSpace protectionSpace: URLProtectionSpace) -> Bool{
                return true
            }
            func connection(_ connection: NSURLConnection, didReceive challenge: URLAuthenticationChallenge){
                if challenge.protectionSpace.authenticationMethod == NSURLAuthenticationMethodServerTrust  {
                    print("NSURLAuthenticationMethodServerTrust")
                    if challenge.protectionSpace.host.contains("yourdomain.com"){
                        let credential = URLCredential(trust: challenge.protectionSpace.serverTrust!)
                        //challenge.sender!.use(credential, for: challenge)
                        challenge.sender!.use(credential, for: challenge)
                    }
                }else{
                    challenge.sender!.performDefaultHandling!(for: challenge)
                }
            }
        }
        ```

      - URLSessionDelegate

        ```
        extension AppDelegate: URLSessionDelegate{
            func urlSession(_ session: URLSession, didReceive challenge: URLAuthenticationChallenge, completionHandler: @escaping (URLSession.AuthChallengeDisposition, URLCredential?) -> Void) {
                if challenge.protectionSpace.host.contains("yourdomain.com") {
                    completionHandler(.useCredential, URLCredential(trust: challenge.protectionSpace.serverTrust!))
                } else {
                    completionHandler(.performDefaultHandling, nil)
                }
            }
        }
        ```

    - Flutter Plugins
  
        Because Flutter SDK has decomposed for inherit due to the needs to inherit AWSDK, extra manual effort is required to let Flutter package work with native layer (only some of the packages related to native behavior require this)

        E.g. Flutter packages *[connectivity](https://pub.dev/packages/connectivity)* (Refer to class import declamation in ```/ios/Classes``` of the [package](https://github.com/flutter/plugins/tree/master/packages/connectivity/ios/Classes)'s GitHub repository))

      - **Runner-Bridging-Header.h** and **GeneratedPluginRegistrant.m**: 
        - Add package native class import declamation

            ```#import <connectivity/ConnectvityPlugin.h>```

      - **GeneratedPluginRegistrant.m**
        - Add package's interface  

            ```[FLTConnectivityPlugin registerWithRegistrar:[registry registrarForPlugin:@"FLTConnectivityPlugin"]];```

      - **AppDelegate.swift**
        - Check if **handleMethodCall** method exists in package's native class *.m so that Flutter channel can access the class via this entry point
  
            ```
            - (void)handleMethodCall:(FlutterMethodCall*)call result:(FlutterResult)result {}
            ```

        - Add FlutterMethodChannel

            ```
            let connectivityChannel = FlutterMethodChannel(name: "plugins.flutter.io/connectivity", binaryMessenger: controller as! FlutterBinaryMessenger)

            connectivityChannel.setMethodCallHandler {(call: FlutterMethodCall, result: @escaping FlutterResult) in
                print("connectivityChannel \(call.method)")
                let fls = FLTConnectivityPlugin()
                fls.handle(call, result: result)
            }
            ```


## Xcode for Flutter Notes

BUILD & ARCHIVE *.ipa

- Go to flutter project directory
  - ```flutter build ios —release```
- Open Xcode (Runner.xcworkspace)
  - KeyChain: allow all access
    - Import certificate private key
  - Set unique bundle ID
  - Xcode > Product > Archive

BUILD & RUN

- Run on device
  - Product > Edit Scheme > Release
- Run on Simulator
  - Product > Edit Scheme > Debug
- Stop print log
  - Product > Edit Scheme > Argument > Environment variable > OS_ACTIVITY_MODE : disabled

DEFAULT XCODE COMPILER

- Xcode 10.2
    - ```sudo xcode-select --switch /Users/icmdtsmc/Documents/Xcode/Xcode10.2/Xcode.app/Contents/ Developer```

- Xcode in /Application:
    - ```sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer```

## Copyright

All rights belongs to the respective product.
