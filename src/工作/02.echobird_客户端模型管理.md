
1. 安装 echobird
https://github.com/edison7009/EchoBird/releases/tag/v5.1.9

2. 如果安装打开失败： “EchoBird”已被阻止使用，因为它来自身份不明的开发者
```bash
xattr -l /Applications/EchoBird.app

sudo xattr -rd com.apple.quarantine /Applications/EchoBird.app
```