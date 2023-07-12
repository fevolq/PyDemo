# 介绍
批量开启cmd窗口，执行一系列命令。
```shell
# 如：需要开启3个窗口，执行一系列命令。
python script_demo.py -n "a"
python script_demo.py -n "b"
python script_demo.py -n "c"
```

# 启动
* 主入口：`main.py`
* 启动命令：`python main.py -f <file_path>`
* 测试：`python main.py -f demo.json`

# 配置文件
* option: 系统配置
  * exe
  * echo: 是否打印命令。true
  * cwd: 执行路径
* lines: 命令
  * process: 当前命令重复的次数
  * scripts: 需要执行的命令操作。