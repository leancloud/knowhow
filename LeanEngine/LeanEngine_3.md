# timerAction short-circuited and no fallback available

#### 问题详情
定时器报错：`timerAction short-circuited and no fallback available`

#### 解决方案
这个意思是指某个定时器触发的 cloud 函数因为太多次超时而停止触发，所以请检查相应的 cloud 函数。