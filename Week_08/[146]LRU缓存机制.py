# 运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。 
# 
#  获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。 
# 写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在
# 写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。 
# 
#  
# 
#  进阶: 
# 
#  你是否可以在 O(1) 时间复杂度内完成这两种操作？ 
# 
#  
# 
#  示例: 
# 
#  LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得关键字 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得关键字 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
#  
#  Related Topics 设计


# leetcode submit region begin(Prohibit modification and deletion)
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.dict = OrderedDict()
        self.remain = capacity

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        v = self.dict.pop(key)
        self.dict[key] = v
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dict.popitem(last=False)
        self.dict[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
