0. 参考
https://codelabs.developers.google.com/codelabs/flutter-webview#2

1. 下载webview插件
```bash
flutter pub add webview_flutter
```

2. 查看 Android minSDK
```
<!-- android/app/build.gradle -->

android {
    //...

    defaultConfig {
        applicationId = "com.example.webview_in_flutter"
        minSdk = 20                                         // Modify this line
        targetSdk = flutter.targetSdkVersion
        versionCode = flutterVersionCode.toInteger()
        versionName = flutterVersionName
    }

```

3. 页面中使用

```dart
<!-- 01 跟组件使用 -->
import 'package:webview_flutter/webview_flutter.dart';

void main() {
    runApp(
        const MaterialApp(
            home: WebViewApp();
        )
    )
}

class WebViewApp extends StatefulWidget {
    const WebViewApp({ super.key })

    @override
    State<WebViewApp> createState() => _WebViewAppState();
}

class _WebViewAppState extends State<WebViewApp> {
    late final WebViewController controller;

    @override
    void initState() {
        super.initState();

        controller = WebViewController()
        ..loadRequest(Uri.parse("https://www.jaka.com"));
    }

    @override
    Widget build(BuildContext context) {
        return Scaffold(
        appBar: AppBar(title: const Text("WebView study")),
        body: WebViewWidget(controller: controller),
        );
    }
}
```


3. WebView组件中有