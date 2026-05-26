1. 创建项目
npx create-react-app robot-3d --template typescript

2. 下载依赖
npm i three @react-three/fiber @react-three/drei

3. 
threejs typescript 版本与 create-react-app 版本不一致；
升级typescript到最新版本
npm i --save-dev typescript@latest

4. 遇到css报错：因为typescript不识别css
在src/types中添加css.d.ts
declare module '*.css';
declare module '*.scss';
declare module '*.sass';

5. webgl简单的知识
webgl可以让你在网页上使用js渲染3D图形；

顶点： Vertex, 顶点决定了物体的形状
几何体： Geometry, 由顶点组成的形状
材质：Material, 决定物体外观：颜色，纹理，反光
光照：Light, 让物体看起来有立体感
    - AmbientLight：环境光，整体亮度
    - DirectionaLight: 平行光，像太阳
    - PointLight: 点光源，像灯泡
相机：Camera：视野角度
网格：Mesh, 真正出现在画面里面的3D物体

WEBGL渲染流程
    1. 创建几何体
    2. 给集合体添加材质
    3. 放在场景里面
    4. 放一个视角
    5. 添加光源
    6. 调用Renderer渲染出来
    7. GPU把顶点变成像素，显示在浏览器中

6. 加载模型（glb / gltf）
下载 three-stdlib
npm i three-stdlib

如果报类型错误，降低typescript版本 
npm install typescript@4.9 --save-dev
rm -rf node_modules package-lock.json

npm uninstall three three-stdlib
npm install three@0.159 three-stdlib@2.33
npm install @types/three@0.159.0 --save-dev
npm i


在public中加入glb模型大文件，放到public中，就不会被打包编译
```javascript
import { useGLTF } from '@react-three/drei';
function RobotModel() {
  const gltf = useGLTF('/A12/joint-00.glb', true);
  return <primitive object={gltf.scene} position={[0, 0, 0]} rotation={[-Math.PI / 2, 0, 0]} />
}
```
useGLTF第二个参数是缓存的意思
position位置，x,y,z； y为0表示放在地上
rotation旋转，Math.PI 是选装180度

如果是机械臂运动，嵌套是关键

根据服务端的x,y,z来进行旋转