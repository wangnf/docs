1. 下载依赖
```
flutter pub add flutter_riverpod
flutter pub get
```

2. 在根组件使用ProviderScope包裹组件
```js
import 'package:shared_preferences/shared_preferences.dart';
void main() {
  runApp(
    const ProviderScope(
      child: MyApp()
    )
  );
}
```

3. 创建共享数据
```js
// counter_provider.dart
final counterProvider = StateProvider<int>((ref) {
    return 0;
})
```

4. 修改组件的类
```js
class HomeScreen extends ConsumerStatefulWidget {
  const HomeScreen({super.key});

  @override
  ConsumerState<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends ConsumerState<HomeScreen> {}

```

4. 在build中监听公共数据
```js
final counter = ref.watch(counterProvider);


final counter = ref.read(counterProvider); //监听一次

```

5. 修改公共数据
```js
ref.read(counterProvider.notifier).state++
```

6. 监听数据变化
```js
ref.listen(counterProvider, (p, n) {
  print(p);
  print(n);
})
```