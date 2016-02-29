# 为什么我定义的 Class Hook 没有被运行？

#### 问题详情
在控制台通过在线定义函数或项目定义函数中的 Class Hook 在对象被更新后没有被运行。

#### 解决方案
首先确认一下 Hook 被调用的时机是否是你所期待的：

* beforeSave - 对象保存（创建）之前
* afterSave - 对象保存（创建）之后
* beforeUpdate - 对象更新之前
* afterUpdate - 对象更新之后
* beforeDelete - 对象删除之前
* afterDelete - 对象删除之后
* onVerified - 用户通过邮箱或手机验证后
* onLogin - 用户在进行登录操作时

然后检查 Hook 函数是否被执行过：

可以先在 Hook 函数的入口打印一行日志，然后进行操作，看日志是否被打出，如果没有看到日志原因可能包括：

* 没有部署代码到正确的应用
* 没有部署代码到生产环境（或没有部署成功）
* Hook 的类名不正确

如果日志已打出，则继续检查函数是否成功，检查控制台上是否有错误信息被打印出。如果是 before 类 Hook，需要保证 Hook 函数在 15 秒内调用 `response.success` 或 `response.error`, 否则会被系统认为超时。

#### 相关文档
* [云引擎指南：Hook 函数](https://leancloud.cn/docs/leanengine_guide-node.html#Hook_函数)
