# 推送失败，invalidTokens 是什么意思?

#### 问题详情
有一些 iOS 设备收不到推送，到控制台查看推送记录，发现 invalidTokens 的 数量大于 0，是怎么回事？

#### 解决方案
invalidTokens 的数量由以下两部分组成：
1. 选择的设备与选择的证书不匹配时，会增加 invalidTokens 的数量，例如使用开发证书给生产证书的设备推送。
2. 目标设备移除或重装了对应的 App。

针对第一种情况，请检查 APNS 证书是否过期，并检查是否使用了正确的证书类型。

更多推送问题排查，请参考：
https://leancloud.cn/docs/push_guide.html#iOS_推送排查建议