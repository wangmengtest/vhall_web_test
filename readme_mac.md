## 安装虚拟环境（可选）
### 安装python3.8.* & pip
https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py

### 添加虚拟环境扩展包 
pip3 install virtualenv

### 创建虚拟环境
python3 -m venv .venv 

### 激活虚拟环境 Mac
source .venv/bin/activate


## 导入项目 (在项目根目录下执行,需要配好python环境)
python ./require/setup.py install 

## 导入依赖
pip3 install -r requirements.txt

## 配置准备
cp config.conf.example config.conf



  
