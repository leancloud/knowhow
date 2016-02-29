# 云函数如何获取 Header、如何响应 GET 方法？

#### 问题详情
希望云函数可以响应 POST 之外的方法、希望可以获取 HTTP 请求头。

#### 解决方案
不建议在 Header 中传递信息，云函数可以说是 LeanCloud 所提供的一种 RPC 的封装，这种封装希望隐藏掉底层使用 HTTP 协议的细节，所以建议将所有的参数都放在 Body 中、只使用 POST 方法请求。

如果希望能够充分利用 HTTP 提供的语义化特征，可以考虑使用云引擎的「网站托管」功能，自行来处理 HTTP 请求。

#### 相关文档
* [云引擎指南：网站托管](https://leancloud.cn/docs/leanengine_guide-node.html#使用框架)
* [云引擎指南：云函数](https://leancloud.cn/docs/leanengine_guide-node.html#云函数)
