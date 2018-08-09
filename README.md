# fuck-python

## update brew source

```
$ cd "$(brew --repo)" && git remote set-url origin https://git.coding.net/homebrew/homebrew.git
$ cd $home
```

# install python

```
$ brew install python

$ pip install --upgrade pip
```

## Pyenv method

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

## note

* [数据结构 & 数据类型](./note/data-structure.md)

## mysql-note

```
mysql> desc users;
mysql> show index from users;
# 看看表是如何创建的
mysql> show create table users\G;
```

## 参考

* [Python Dev](http://sourabhbajaj.com/mac-setup/Python/)
