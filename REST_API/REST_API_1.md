# 如何使用 REST API 更改会话名称？

#### 问题详情
如何使用 REST API 修改会话的名称？

#### 解决方案
可以通过 objectId（即客户端的 conversation Id）确认要修改的 Conversation，然后修改其相应的字段。
例如：

```
curl -X PUT \
  -H "X-LC-Id: oajBDaWcMO3Vhvx6TXprNXSe" \
  -H "X-LC-Key: pJxTh152fpqYxrG8OUzdvM6u" \
  -H "Content-Type: application/json" \
  -d '{"name": "1号聊天室"}' \
  https://api.leancloud.cn/1.1/classes/_Conversation/<objectId>
```
 
#### 相关文档：
https://leancloud.cn/docs/rest_api.html#更新对象