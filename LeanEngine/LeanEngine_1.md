# Maximum call stack size exceeded

#### 问题详情
云代码函数总是报错：`Maximum call stack size exceeded`，这是什么情况？如何解决？

#### 解决方案
`AV.Object.extend` 产生的对象会作为全局变量保存（即定义在 `AV.Cloud.define` 方法之外）。每调用一次，就会产生一个新的类的实例，并且和之前创建的实例形成一个链表。调用次数过多后（几万次）就会堆栈溢出。如果你的应用时不时出现 `Maximum call stack size exceeded` 错误，请确认是否误用了 `AV.Object.extend` 方法。

#### 相关文档：
https://leancloud.cn/docs/cloud_code_faq.html#Maximum_call_stack_size_exceeded_如何解决_
https://leancloud.cn/docs/js_guide.html#AV_Object