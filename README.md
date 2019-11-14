# fuck-python

## update brew source

```
$ cd "$(brew --repo)" && git remote set-url origin https://git.coding.net/homebrew/homebrew.git
$ cd $home
```

## pyenv method

```
$ brew install pyenv
$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
$ exec $SHELL

$ pyenv install --list
$ pyenv install 2.7.12
$ pyenv install 3.5.2

$ pyenv global 2.7.12 3.5.2
$ pyenv rehash
```

## venv

```
# 创建虚拟环境
$ python3 -m venv venv
# 激活虚拟环境
$ source venv/bin/activate
# 退出虚拟环境
$ deactivate

# 更新包管理工具pip
(venv)$ python -m pip install --upgrade pip

# 生成requirements.txt
(venv)$ pip freeze > requirements.txt

# 安装requirements.txt依赖
(venv)$ pip install -r requirements.txt
```

# pip

```
$ curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
$ sudo python get-pip.py
```

## pip --help

```
$ python3 -m pip == pip3
$ python3 -m pip install Django==1.7
$ python3 -m pip install --upgrade package
$ python3 -m pip uninstall package
$ python3 -m pip search package
$ python3 -m pip show
$ python3 -m pip show -f packagename
$ python3 -m pip list
$ python3 -m pip list -o
```

## 参考

* [Python Dev](http://sourabhbajaj.com/mac-setup/Python/)
