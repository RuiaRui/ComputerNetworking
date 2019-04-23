## Problem 1

 the paths from y to u that do not contain any loops are: 

y-x-u, y-x-v-u, y-x-w-u, y-x-w-v-u, y-w-u, y-w-v-u, y-w-x-u, y-w-x-v-u, y-w-v-x-u, y-z-w-u, y-z-w-v-u, y-z-w-x-u, y-z-w-x-v-u, y-z-w-v-x-u



## problem 3

| step | N'      | D(t),p(t) | D(u),p(u) | D(v),p(v) | D(w),p(w) | D(y),p(y) | D(z),p(z) |
| ---- | ------- | --------- | --------- | --------- | --------- | --------- | --------- |
| 0    | x       | 正无穷    | 正无穷    | 3，x      | 6，x      | 6,x       | 8,x       |
| 1    | xv      | 7,v       | 6,v       | 3，x      | 6，x      | 6，x      | 8,x       |
| 2    | xvu     | 7,v       | 6,v       | 3，x      | 6，x      | 6，x      | 8,x       |
| 3    | xvuw    | 7,v       | 6,v       | 3，x      | 6，x      | 6，x      | 8,x       |
| 4    | xvuwy   | 7,v       | 6,v       | 3，x      | 6，x      | 6，x      | 8,x       |
| 5    | xvuwyt  | 7,v       | 6,v       | 3，x      | 6，x      | 6，x      | 8,x       |
| 6    | xvuwytz | 7,v       | 6,v       | 3，x      | 6，x      | 6，x      | 8,x       |

## Problem 9

 NO, this is because that decreasing link cost won’t cause a loop (caused by the next-hop relation of between two nodes of that link). Connecting two nodes with a link is equivalent to decreasing the link weight from infinite to the finite weight. 

## Problem 10 

At each step, each updating of a node’s distance vectors is based on the Bellman-Ford equation, i.e.. only decreasing those values in its distance vector. There is no increasing in values. If no updating, then no message will be sent out. Thus, D(x) is non-increasing. Since those costs are finite, then eventually distance vectors will be stabilized in finite steps.  

## Problem 12 

Since full AS path information is available from an AS to a destination in BGP, loop detection is simple – if a BGP peer receives a route that contains its own AS number in the AS path, then using that route would result in a loop.