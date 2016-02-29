# 如何在本地调试依赖 LeanCache 的应用？

#### 问题详情
依赖 LeanCache 的应用在本地因缺少 Redis 无法运行。

#### 解决方案
首先你需要在本地运行一个 redis-server:

* Mac 运行 `brew install redis` 安装，然后用 `redis-server` 启动
* Debian/Ubuntu 运行 `apt-get install redis-server`, CentOS/RHEL 运行 `yum install redis`
* Windows 尚无官方支持，可以下载 [微软的分支版本](https://github.com/MSOpenTech/redis/releases) 安装包。

默认情况下，在本地运行时程序没有 LeanCache 的环境变量，因此会使用本地的 Redis 服务器。

```javascript
// `process.env['REDIS_URL_mycache']` 为 undefined, 会连接默认的 127.0.0.1:6379
var client = require('redis').createClient(process.env['REDIS_URL_mycache']);
```

#### 相关文档
* [Redis 官方文档](http://redis.io/documentation)
* [LeanCache 使用指南](https://leancloud.cn/docs/leancache_guide.html)
