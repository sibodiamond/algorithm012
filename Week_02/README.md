###### 学习笔记
===========
1. hashMap  
- hashcode -> index
- Java 通过链地址方式解决hash冲突
- 对于链表过长，Java1.8引入红黑树以减小查询的时间复杂度；
2. 堆 Binary Heap  
- 完全二叉树
- 可由数组存储
- 对于节点i，其left_child_index = 2 * i + 1； right_child_index = 2 * i + 2
- i_parent_index = (i  - 1) // 2 
- n = len(heap)
- 大顶堆，任何一个父节点值大于左右子树的值
- 小顶堆， 任何一个父节点值均小于其左右子树的值
