# 为什么要使用 LeanCache?

#### 问题详情
和自己在程序的全局作用域中维护一个 HashTable 比起来有什么优势？

#### 解答
和自己维护一个 Hash Table 比起来，Redis（LeanCache）可以提供的优势包括：

* 多实例之间的数据共享，云引擎后续可以运行多实例，自行维护的 HashTable 数据无法在实例中共享
* 持久化，在程序重启或重新部署后数据不会丢失，Redis 会帮你完成数据持久化的工作，LeanCache 还会为你的 Redis 做热备，具有非常高的可靠性。
* 原子操作和性能，Redis 提供了常见的数据结构和大量原子的操作符，在文档上清除地列出了每个操作符的时间复杂度，而自行实现的 HashTable 性能则很大程度地依赖于具体语言的实现（例如 V8 中 Array 其实是以 Hash Map 实现的）。

#### 相关文档
* [LeanCache 使用指南](https://leancloud.cn/docs/leancache_guide.html)
