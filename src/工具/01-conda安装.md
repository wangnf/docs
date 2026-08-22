## 1. 下载
``` brew install miniconda ```

**注意：有可能下载完之后，没有添加到 PATH 中**

## 2. 验证是否安装成功
``` conda --version ```

## 3. 关闭自动激活
``` conda config --set auto_activate_base false ```

## 4. 创建虚拟环境
``` conda create -n langgraph python=3.13 ```

## 5. 激活当前环境
``` conda activate langgraph ```

## 6. 退出当前环境
``` conda deactivate ```