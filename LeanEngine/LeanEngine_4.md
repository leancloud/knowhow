# connect ECONNREFUSED

#### 问题详情
在使用命令行工具部署项目时收到报警：启动检测失败: `connect ECONNREFUSED`，此外没有更详细的信息。

#### 解决方案
这是由于项目中使用了 `ECMAScript 6` 所提供的新语法，而当前云引擎版本尚不支持 `Node.js 4.x` 版本。
如果希望使用 `ECMAScript 6` 所提供的新语法，请在项目的 `package.json` 中为 node 加入 `--harmony` 参数，例如：
```
"scripts": {
  "start": "node --harmony server.js"
},
```
当云引擎开始支持 `Node.js 4.x` 版本时，`--harmony` 参数可以去掉。

另外，与云引擎项目相关的详细报错信息会记录在 **控制台** > **存储** > **云引擎** > **日志** 中，在那里可以发现比 `connect ECONNREFUSED` 更有用的信息来帮助诊断。