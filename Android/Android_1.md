#client.open() 操作没有响应

#### 解决方案：
检查 receiver 和 service 是不是没有写在 application 标签里，并且与 activity 平级。它们与 activity 同为四大组件之一，自然需要写在一起。

#### 错误示范：
```
...
<uses-permission android:name="android.permission.READ_CONTACTS" />

<service
    android:name="com.avos.avoscloud.PushService"
    android:exported="true" />

<receiver android:name="com.avos.avoscloud.AVBroadcastReceiver">
    <intent-filter>
    <action android:name="android.intent.action.BOOT_COMPLETED" />
    <action android:name="android.intent.action.USER_PRESENT" />
    <action android:name="android.net.conn.CONNECTIVITY_CHANGE" />
    </intent-filter>
</receiver>

<application
    android:name=".app.LeanDemoApplication"
...
```