### Problem 2 

a) No, you can only transmit one packet at a time over a shared bus. 

b) No, as discussed in the text, only one memory read/write can be done at a time over the shared system bus.  

c) No, in this case the two packets would have to be sent over the same output bus at the same time, which is not possible.  

### Problem 3  

a) (n-1)D 

b) (n-1)D 

c) 0 



### Problem 5 

a) 

| Prefix Match       | Link Interface |
| ------------------ | -------------- |
| 11100000  00       | 0              |
| 11100000  01000000 | 1              |
| 1110000            | 2              |
| 11100001  1        | 3              |
| otherwise          | 3              |

​                                              

b)   Prefix match for first address is 5th entry: link interface 3       

​	Prefix match for second address is 3nd  entry: link interface 2       

​	Prefix match for third address is 4th  entry: link interface 3 

### Problem 6 

| Destination Address Range | Link Interface     |
| ------------------------- | ------------------ |
| 00000000                  |                    |
|                           | through         0  |
| 00111111                  |                    |
| 01000000                  |                    |
|                           | through         1  |
| 01011111                  |                    |
| 01100000                  |                    |
|                           | through         2  |
| 01111111                  |                    |
| 10000000                  |                    |
|                           | through          2 |
| 10111111                  |                    |
| 11000000                  |                    |
|                           | through          3 |
| 11111111                  |                    |

number of addresses for interface 0 =2^6= 64 
number of addresses for interface 1 = 2^5=32 
number of addresses for interface 2 = 2^5+2^6=96
number of addresses for interface 3 = 2^6=64

 

### Problem 9

| Destination Address | Link Interface |
| ------------------- | -------------- |
| 200.23.16/21        | 0              |
| 200.23.24/24        | 1              |
| 200.23.24/21        | 2              |
| otherwise           | 3              |