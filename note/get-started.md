
```
# which python
python3 --version

# use python
python3

# Installing with get-pip.py
# To install pip, securely download
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# Inspect get-pip.py for any malevolence. Then run the following:
sudo python get-pip.py

# Install Pipenv
# 尽管 pip 可以安装 Python 包， 但仍推荐使用 Pipenv，因为它是一种更高级的工具，可简化依赖关系管理的常见使用情况。
pip install --user pipenv

# 这进行了 用户安装，以防止破坏任何系统范围的包。如果安装后, shell 中没有 pipenv，则需要将 用户基础目录 的 二进制文件目录添加到 PATH 中。
# 通过运行 python -m site --user-base 找到 用户基础目录，然后把 bin 加到目录末尾。
# 然后将 ~/.local/bin 添加到 PATH 中。


```









