# coding=utf-8

import tkinter
import tkinter.messagebox

def main():

  flag = True

  def change_label_text():
    # 使用nonlocal关键字可以在一个嵌套的函数中修改嵌套作用域中的变量
    nonlocal flag
    flag = not flag
    color, msg = ('red', 'hello, koo') \
      if flag else ('blue', 'good bye')
    label.config(text = msg, fg = color)

  def confirm_to_quit():
    if tkinter.messagebox.askokcancel('remind', 'confirm exit?'):
      top.quit()

  # 创建顶层窗口
  top = tkinter.Tk()
  # 设置窗口大小
  top.geometry('240x160')
  # 设置窗口标题
  top.title('small game')
  # 创建标签对象并添加到顶层窗口
  label = tkinter.Label(top,\
                        text='Hello, world!',\
                        font='Arial -32',\
                        fg='red')
  label.pack(expand = 1)

  # 创建一个装按钮的容器
  panel = tkinter.Frame(top)
  # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
  button1 = tkinter.Button(panel, text = 'update', command = change_label_text)
  button1.pack(side = 'left')
  button2 = tkinter.Button(panel, text = 'exit', command = confirm_to_quit)
  button2.pack(side = 'right')
  panel.pack(side = 'bottom')
  # 开启主事件循环
  tkinter.mainloop()


  pass

if __name__ == '__main__':
  main()
