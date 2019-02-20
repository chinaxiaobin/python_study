## 安装pyenv管理python
```
项目地址： https://github.com/pyenv/pyenv-installer

默认系统自带的python版本为系统提供依赖，尽量不要使用系统自带的python版本

pyenv（bash写的）:
    安装python解释器
    管理python版本
    管理python虚拟环境（相当于一个独立版本，虚拟环境间的python版本依赖不会有冲突）

aliyun:安装aliyun镜像库

mv /etc/yum.repos.d/CentOS-Base.repo    /etc/yum.repos.d/CentOS-Base.repo_backup
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo


1. 安装git  `yum -y install git`
2. 安装依赖 yum install gcc make patch gdbm-devel openssl-devel sqlite-devel zlib-devel bzip2-devel readline-devel

3. 安装pyenv

普通用户安装步骤：
#yum install git -y  #依赖git，需要提前安装git
#curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
#ls ~/.pyenv/

#安装完成后提示安装环境变量
vim ~/.bash_profile
export PATH="/root/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

#source ~/.bash_profile 使其生效


root用户安装：
export PYENV_ROOT=/opt/pyenv
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
vim /etc/profile.d/pyenv.sh
安装完成后提示安装环境变量
vim ~/.bash_profile
export PATH="/opt/pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

#source /etc/profiled.d/pyenv.sh  #这样对所有用户都生效


#pyenv使用

#pyenv help  列出常用命令
#pyenv version
#pyenv versions 
#pyenv install --list |less 列出可安装的步骤
#pyenv install 3.5.2   安装3.5.2版本python
#pyenv update 更新pyenv,如果之前安装的没有最新python版本的话

国内下载慢的化，我们可以使用国内的下载，找个国内地址，下载完放到 ~/.pyenv/cache/目录下
https://www.python.org/ftp/python/
在服务器先wget下来放到cache目录
pyenv install 3.5.2 

下面路径定义下载的文件的格式
 vim /root/.pyenv/plugins/python-build/share/python-build/3.5.2

格式根据里面定义，一般python install  3.5.2默认会显示格式，在cache之前操作

切换成3.5.2版本
pyenv version 
pyenv  local 3.5.2 #只对当前目录和子目录下设置版本号
pyenv local system 使用系统版本
pyenv version
python -V

pyenv global 3.5.2 更改全局python版本，不建议大家执行


python基于site，整个机器的依赖放在一个地方，而virtualenv类似于project,,为了减少项目之间的冲突，推荐每个项目使用一个虚拟env

java基于project ,每个project管理自己的依赖

使用virtualenv
pyenv  virtualenv 3.5.2 magedu
pyenv versions
pyenv local 3.5.2/envs/magedu
pyenv versions
pyenv local 3.5.2 回到虚拟env外面
pyenv uninstall magedu 卸载虚拟的magedu

## 使用pyenv

### local命令
local命令切换当前目录及其子目录的Python版本， 可以通过删除 `.python-version`恢复默认Python版本

### global命令
global名切换全局默认Python版本

**永远不要使用global命令**

### virtualenv命令
创建虚拟环境 `pyenv virtualenv $bash_version $name`

### uninstall命令
卸载某个版本， 包括虚拟环境
```
