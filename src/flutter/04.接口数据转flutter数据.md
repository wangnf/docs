1. mock数据返回
{name: "xxx", age: 12}

2. flutter中 创建 User 类，接受json数据
```js
Class User{

  final name;
  final age;

  User({
    required this.name,
    required this.age,
  })

  factory User.fromJson(Map<String, dynamic> json) {
    return User(
      name: json["name"],
      age: json["age"]
    )
  }

  Map(String,dynamic) toJson() {
    return {
      'name': name,
      'age': age
    }
  }
}


final res = await _getUser();
final user = User.fromJson(res);
```


3. flutter接受 array
```js
final res = await getUsers();

final users = res.map((e) => User.fromJson(e)).toList();
```


