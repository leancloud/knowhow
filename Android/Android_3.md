# installationId 一直变化

#### 问题详情
设备每次启动时，installationId 都会改变，造成无法定向推送

#### 解决办法
可能有以下两种情况导致：
1. SDK 版本过旧导致，installationId 的生成逻辑在版本更迭中有修改。请更新至最新版本即可。
2. 代码混淆引起的，注意在 proguard 文件中添加 LeanCloud SDK 的混淆排除。
