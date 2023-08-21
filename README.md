# 囧(go_away)小游戏

### 准备

首先你得有 `python` 并确保有 `pygame` 库

没有, 打开终端, 输入 `pip install pygame`

### 游戏规则

用 `a` 左移, `d` 右移, `w` 跳跃, 空格潜行(就是走得慢)

**祝你在最短时间内吃到小旗子**

### 额外篇

在 `congfig.py` 里, 你自定义可以调参数, 应该都看得懂吧

其中 `g` 是重力, `min_intersection` 是最小交集判断碰撞

你可以在 `choose_rooms.py` 中自己点击并创建关卡

其中参数在 `config.py` 中

选好后按下 `ok` 键即可在终端里复制一大堆 `room.append((x, y))`

将这些替换为 `levels.py` 里的一大堆即可, 记得保存哟

### 文件内容

`main.py` 主(运行)程序

`sprites.py` 角色的程序

`levels.py` 存放关卡

`choose_rooms.py` 自定义关卡

`config.py` 配置文件

`image in img` 图像

`README.md` 就是你在读的