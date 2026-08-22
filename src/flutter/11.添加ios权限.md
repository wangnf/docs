ios/Runner/Info.plist

使用系统标准加密
这样上传 IPA 后，苹果一般不会再反复询问加密声明。

```xml
<key>ITSAppUsesNonExemptEncryption</key>
<false/>
```




```xml
<key>ITSAppUsesNonExemptEncryption</key>
<false/>

<key>NSCameraUsageDescription</key>
<string>用于拍摄图片和视觉识别。</string>

<key>NSPhotoLibraryUsageDescription</key>
<string>用于选择和保存图片。</string>

<key>NSBluetoothAlwaysUsageDescription</key>
<string>用于发现和连接机器人设备。</string>

<key>NSLocalNetworkUsageDescription</key>
<string>用于发现和连接局域网中的机器人设备。</string>

<key>NSMicrophoneUsageDescription</key>
<string>用于语音相关功能。</string>
```