## 环境设置

### 安装 python2

```sh
sudo apt install python2
```

### 安装 venv

```sh
virtualenv --python=$(which python2) ~/cinfo/venv 
```

## 安装依赖

1. 进入 venv 环境。

```
pip install -r requirements.txt
```

2. python2 下安装 newspaper 时会报错，需要自己安装 nltk，这里使用第三方提供的 nltk（建议自己下源码修改）

```sh
pip install https://s3-us-west-2.amazonaws.com/jdimatteo-personal-public-readaccess/nltk-2.0.5-https-distribute.tar.gz
```

NLTK 数据下载地址：[NLTK :: Installing NLTK Data](https://www.nltk.org/data.html)，不需要可以不下。

## 本地运行

```sh
python manager.py 
```

## 在服务器上运行

### 使用 supervisor 做进程守护

#### 安装 supervisor

使用 `sudo` 安装 `pip` 才可以使用 `sudo pip` 安装模块，而且也是在 `/usr/local/*` 目录下，方便使用

```shell
sudo pip install supervisor
```

#### 创建 supervisord.conf 配置文件

```shell
# 创建配置文件目录
sudo mkdir /etc/supervisor
```

执行下面这个命令会提示没有权限，官方文档也给出了解决方案，就是先将配置文件释放到有权限的目录中，然后再移动。

```shell
# 会报权限问题
echo_supervisord_conf > /etc/supervisor/supervisord.conf
```

分步骤执行

```shell
# 释放到用户目录下
echo_supervisord_conf > ~/supervisord.conf

# 移动到 /etc/supervisor 目录下
sudo mv ~/supervisord.conf /etc/supervisor/supervisord.conf
```

#### 创建进程配置文件夹

```shell
sudo mkdir -p /etc/supervisor/conf.d
```

#### 修改 supervisord.conf 配置

```shell
vim /etc/supervisor/supervisord.conf
```

添加如下内容，`.conf` 或者 `.ini` 都可以，进程配置文件的后缀名与之相同即可

```ini
[include]
files = /etc/supervisor/conf.d/*.conf
```

#### 添加 supervisor.service 服务

其实就是手动把 `apt` 安装过程执行一边

```shell
vim /lib/systemd/system/supervisor.service
```

添加以下内容

> ExecStart、ExecStop、ExecReload 要指定可执行文件 `supervisord` 和 `supervisorctl` 的路径和配置文件 `supervisord.conf` 的路径。

```ini
[Unit]
Description=Supervisor process control system for UNIX
Documentation=http://supervisord.org
After=network.target

[Service]
ExecStart=/usr/local/bin/supervisord -n -c /etc/supervisor/supervisord.conf
ExecStop=/usr/local/bin/supervisorctl $OPTIONS shutdown
ExecReload=/usr/local/bin/supervisorctl -c /etc/supervisor/supervisord.conf $OPTIONS reload
KillMode=process
Restart=on-failure
RestartSec=50s

[Install]
WantedBy=multi-user.target
```

#### 注册 supervisor.service 服务

两个命令的效果一致

```shell
sudo systemctl enable supervisor.service
# 或者
sudo ln -s /usr/lib/systemd/system/supervisor.service /etc/systemd/system/multi-user.target.wants/supervisor.service


### 创建 start.sh

```sh
#!/bin/bash
pushd /home/ubuntu/cinfo
source venv/bin/activate
exec python prod.py
popd
```

### 配置 supervisor

```
sudo vim /etc/supervisor/conf.d/myapp.conf
```

```sh
[program:myapp]
command = /home/ubuntu/start.sh
autostart=true
autorestart=true
stderr_logfile=/var/log/myapp.err.log
stdout_logfile=/var/log/myapp.out.log
```

## 其他

venv 下无法使用 sudo python，使用 psudo 解决，以下 shell 加入 .bashrc

```sh
psudo() { sudo env PATH="$PATH" "$@"; }
```
