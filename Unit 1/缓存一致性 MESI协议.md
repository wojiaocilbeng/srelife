### **cpu缓存**





为什么会产生cpu缓存？

由于cpu处理能力远比内存强，当内存进行一次读写操作的时间内，足够cpu处理上百条数据。

为了弥补两者之间的差距，于是产生了cpu缓存（高速缓存cache）

高速缓存是存在层次结构的，即一级缓存二级缓存



cpu的读数据操作实际就是将数据从缓存中读取到寄存器中，如果在缓存中没有数据，那么就会依照层级关系一级一级的往下读，直到所以的缓存中都没有数据，才会到内存中寻找并将副本保存到cpu缓存中。



+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++





### **什么是cpu缓存？**



CPU缓存就是cpu与内存之间临时的用来存储数据的交换器，即高速缓存cache

其位置通常与cpu集合在一起，或者独立为一个芯片



+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++





### **cpu缓存的意义**





因为cpu往往需要处理相同的数据或指令，如果能将这部分数据与指令存储到cpu缓存中，那么下次就不需要再次从内存中读取数据，从而加快cpu工作效率



缓存的意义满足以下两种局部性原理：



​    时间局部性（Temporal Locality）：如果一个信息项正在被访问，那么在近期它很可能还会被再次访问。

​     空间局部性（Spatial Locality）：如果一个存储器的位置被引用，那么将来他附近的位置也会被引用。



\##################################################################################################





### **缓存一致性协议 - MESI协议**





M 修改：该缓存行有效，数据被修改了，和内存中的数据不一致，数据只存在于本缓存中



E  独享、互斥：该缓存行有效，数据和内存中的数据一致，数据只存在于本缓存中



S  共享：该缓存行有效，数据和内存中的数据一致，数据存在于很多缓存中。



I 无效：该缓存行无效。



+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



首先不同CPU之间也是需要沟通的，这里的沟通是通过在消息总线上传递message实现的。这些在总线上传递的消息有如下几种：



​    Read ：带上数据的物理内存地址发起的读请求消息； 



​    Read Response（读取响应）：Read 请求的响应信息，内部包含了读请求指向的数据；



​    Invalidate（无效）：该消息包含数据的内存物理地址，意思是要让其他如果持有该数据缓存行的 CPU 直接失效对应的缓存行；



​    Invalidate Acknowledge（无效确认）：CPU 对Invalidate 消息的响应，目的是告知发起 Invalidate 消息的CPU，这边已经失效了这个缓存行啦；



​    Read Invalidate（读取无效）：这个消息其实是 Read 和 Invalidate 的组合消息，与之对应的响应自然就是一个Read Response 和 一系列的 Invalidate Acknowledge；



​    Writeback：该消息包含一个物理内存地址和数据内容，目的是把这块数据通过总线写回内存里。



+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

例子：

现在有cpu0 cpu1 变量a

现在cpu0 对变量a进行修改为a=1

假如变量a不在cpu0缓存中，则需要发送Read Invalidate信号，再等待此信号返回Read Response 和 Invalidte Acknowledge，之后再写入到缓存中



假如变量a在cpu0 缓存中，如果当前的状态是 M 则直接更改发送Writeback 最后修改成E 。而如果状态是 S 则需要发送 Invalidate 消息让其它 CPU 感知到这一更改后再更改。

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



一般情况下，CPU 在对某个缓存行修改之前务必得让其他 CPU 持有的相同数据缓存行失效，这是基于 Invalidate Acknowledge 消息反馈来判断的；



缓存行为 M 状态，意味着该缓存行指向的物理内存里的数据，一定不是最新；



在修改变量之前，如果CPU持有该变量的缓存，且为 E 状态，直接修改；若状态为 S ，需要在总线上广播 Invalidate；若CPU不持有该缓存行，则需要广播 Read Invalidate。



\##################################################################################################





### **Store Buffers**

（存储缓冲池）





  当一部分cpu处于S状态时，这时如果有一个cpu要进行修改，则需要等待其他cpu响应并将共同的数据失效，那么这样cpu就会出现一个等待时间，导致降低了cpu的效率。



  为了避免这种cpu运算能力的浪费，因此引入了store buffer（存储缓冲池）这一概念

![file://C:/Users/34362/AppData/Local/Temp/.9E7CV1/1.png](file://C:/Users/34362/AppData/Local/Temp/.9E7CV1/1.png)





cpu可以将想要修改的数据先写入store buffer（缓存池）中，自己可以先去处理别的事情，当接收到所有的无效确认时，数据才会被提交到cache中，避免了cpu的浪费。



存在两个风险：

①有可能cpu已将数据变量a变更并将其存入store buffer中，但还没有提交到cache中。这时如果使用变量a的话，就会从cache中提取旧数据的变量a，从而导致结果错误。



②无法保证保存什么时候会完成。



\##################################################################################################





### **Store Forwarding**

（存储转发）





因此store forwarding就是为了来解决上述问题的



其原理是在对于同一个cpu时，在读取变量a时，如果发现store buffer中还有没有写入缓存的数据a，那么就会直接从store buffer 中读取。

这样就解决了单个cpu的执行顺序和内存可见性。



\##################################################################################################





### **Invalidate Queues**

（失效队列）





原因：由于执行失效需要cpu去处理，并且存储缓存的空间有限，因此有时cpu还是需要等待失效响应返回，这样会降低cpu的性能。于是引出了失效队列



![file://C:/Users/34362/AppData/Local/Temp/.9E7CV1/2.png](file://C:/Users/34362/AppData/Local/Temp/.9E7CV1/2.png)



其原理是：

①当接收到invalidate（失效）请求时，需要立即将invalidate acknowledge（失效响应）消息发出。*虽然会立即发送失效消息，但也只是发送消息通知已经失效确认，有可能该cpu正在处理重要任务，不会立即生效*



② invalidate 不会真正的执行，而是会放在一个类似消息队列的地方，等待其他cpu有空的时候再来处理



③处理器不会发送任何消息给所处理的缓存条目，直到它处理 Invalidate。



这样每个 CPU 都有一个 Invalidate Queue，用以把需要失效的数据物理地址存储起来，根据这个物理地址，我们可以对缓存行的失效行为 “延后执行” 。



\##################################################################################################





### **Memory Barrier**

（内存屏障）





因为大多数现代计算机为了提高性能而采取乱序执行，这使得需要内存屏障



写屏障 **SMB、smp_wmb**：

因为Store Buffer导致读写的顺序不一致，因此需要加上写屏障



处理器在执行这条指令之前，就需要将store buffer 中的失效指令全部用完



在执行写指令之前，先执行写屏障



读屏障 **RMB、smp_rmb**：



读是读数据，为了防止读的是失效的数据，因此有必要在处理器在读取数据之前，就先要将invalidate queue （失效队列）中的指令处理完，然后再去加载





### **内存和硬盘**





物理上，一个用磁铁存一个用电容存，两者之间只有存储速度和价格的区别



内存和硬盘存储数据都有一个临界值，不能无限存储，因此内存和硬盘都可以看作为一个**线性空间**

​    

**线性空间**可以看作一个线段，假如存储空间有3G,如果已经存入了1.5G，那么之后就只能再存入小于或等于1.5G的数据.

![file://C:/Users/34362/AppData/Local/Temp/.9E7CV1/3.png](file://C:/Users/34362/AppData/Local/Temp/.9E7CV1/3.png)

内存插上电以后数据是没有规律的，因为有的电容有电，有的电容没电，所以需要初始化为零，因此申请释放空间无论内存、硬盘都需要时间



因此无论对内存编程还是对硬盘编程，其本质都是申请数组，申请完就会初始化





### **额外内容**

：





网卡是硬件设备，也是通信设备



网卡不是线性空间，但网卡上有存储



Google的TCPBBR算法，当排满后就会将多余的信息丢掉，之后再重发，这是一个速度优化算法



打印机USB设备、火线Fire设备、雷电DP设备、网卡PCI设备都是**块设备**，读数据是以块为单位去读



键盘、鼠标是字符设备、tty（终端）设备，因为都是一个一个发出去的



声卡是块设备