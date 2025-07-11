# 贪吃蛇游戏（Python版）
# Python小项目---贪吃蛇游戏，适合刚学Python的小伙伴们练手的小项目

注意：该项目还未完成，等待作者后续完成
================================================================================

### 代码介绍 
- 引入`turtle`--海龟绘图模块的所有函数，首先封装了一个squer函数，里面装着生成‘苹果’的方法，调用了random库中的range函数，使苹果在画布的位置是随机生成的
- 封装了一个Applelook的函数 ，生成蛇的身体，再调用递归使蛇头部生成一个方块，尾部去掉一个方块的方法来模仿蛇的移动
- 封装了一个 change函数 ，可以在键盘上用`a`,`w`,`s`,`d`操作蛇的身体

### 功能介绍
- 可以实现用键盘方向键移动蛇的身体，吃到苹果，蛇的尾巴就会加长，利用最简单的代码去实现贪吃蛇这个游戏

### 运行环境
- python 3.17版
- Python 3.11/3.12
  
- 环境下载和模块下载

```bash
环境下载 > https://www.python.org/downloads/

turtle模块下载 > pip install turtle

openpyxl 模块下载 >pip install openpyxl

random 模块下载 > pip install random
```


### 游戏效果
!<img width="489" height="659" alt="Image" src="https://github.com/user-attachments/assets/429032d9-badd-4ae4-bb1a-508ac278723e" />

!<img width="489" height="659" alt="Image" src="https://github.com/user-attachments/assets/77262a7f-b1b8-4063-9e23-7a1b55c48dff" />

### 游戏规则
- 玩家需按键盘`w`, `s` ,`a`,`d`操控蛇的身体吃到苹果，蛇头撞到墙壁后游戏失败，吃苹果过后会使蛇的身体+1，蛇的身体会无限延长

## 部署
> [!WARNING]
> 该项目为作者个人练手项目，不适合所有人且项目还未完成

下载地址：
```bash
> https://github.com/tingzai-004/day/archive/refs/heads/main.zip
```
### 作者
> 婷仔
