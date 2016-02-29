# 本地调试 Error: listen EADDRINUSE :::3000

#### 问题详情
使用命令行工具在本地调试时提示 `Error: listen EADDRINUSE :::3000`, 无法访问应用

#### 解决方案
`listen EADDRINUSE :::3000` 表示你的程序默认使用的 3000 端口被其他应用占用了，可以按照下面的方法找到并关闭占用 3000 端口的程序：

* [Mac 使用 lsof 和 kill](http://stackoverflow.com/questions/3855127/find-and-kill-process-locking-port-3000-on-mac)
* [Linux 使用 fuser](http://stackoverflow.com/questions/11583562/how-to-kill-a-process-running-on-particular-port-in-linux)
* [Windows 使用 netstat 和 taskkill](http://stackoverflow.com/questions/6204003/kill-a-process-by-looking-up-the-port-being-used-by-it-from-a-bat)

#### 相关文档
* [云引擎命令行工具](https://leancloud.cn/docs/cloud_code_commandline.html)
