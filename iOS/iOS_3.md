# 离线消息推送应该怎么做？

#### 问题详情
iOS 实时消息离线推送应该怎么设置？

#### 解决方案
1. 首先请按照 「iOS 消息推送指南」进行设置，以保证手机可以收到来自控制台的推送。
2. 设置离线消息推送，有「静态内容」和「动态内容」两种方式。

##### 静态内容：
在控制台的「消息」>「实时消息」>「设置」里面的「iOS 用户离线推送设置」中填上 `{"alert":"您有新的消息", "badge":"Increment"}`，当用户收到离线消息后，会自动推送“您有新的消息”。

##### 动态内容：
有的用户会说，我不希望每次收到的消息都是一成不变的“您有新的消息”，我希望可以看到具体的消息内容。这种情况需要用到 云引擎 Hook 函数 _receiversOffline，这个 hook 在有收件人离线的情况下被触发，但发往暂态对话的消息不会触发此 hook。
比较简单的示例代码为：

``` 
AV.Cloud.define('_receiversOffline', function(request, response) {
    var params = request.params;

    var json = {
        // 自增未读消息的数目，不想自增就设为数字
        badge: "Increment",
        sound: "default",
        // 使用开发证书
        _profile: "dev",
        // content 为消息的实际内容
        alert: params.content
    };

    var pushMessage = JSON.stringify(json);

    response.success({"pushMessage": pushMessage});
})
```

设置完成后，当推送普通的文本消息时，具体的消息内容就可以在推送中被显示出来了。