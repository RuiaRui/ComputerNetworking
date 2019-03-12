## Problem 4

a) The document request was http://gaia.cs.umass.edu/cs453/index.html. The Host （s http://gaia.cs.umass.edu）: field indicates the server's name and /cs453/index.html indicates the file name. 

b) The browser is running HTTP version 1.1, as indicated just before the first <cr><lf> pair. 

c) The browser is requesting a persistent connection, as indicated by the Connection: keep-alive. 

d) This is a trick question. This information is not contained in an HTTP message anywhere. So there is no way to tell this from looking at the exchange of HTTP messages alone. One would need information from the IP datagrams (that carried the TCP segment that carried the HTTP GET request) to answer this question. 

e) Mozilla/5.0.  The browser type information is needed by the server to send different versions of the same object to different types of browsers.

## Problem 5  

a)  The status code of 200 and the phrase OK indicate that the server was able to locate the document successfully. The reply was provided on Tuesday, 07 Mar 2008 12:39:45 Greenwich Mean Time. 

b) The document index.html was last modified on Saturday 10 Dec 2005 18:27:46 GMT. 

c) There are 3874 bytes in the document being returned. 

d) The first five bytes of the returned document are : <!doc. The server agreed to a persistent connection, as indicated by the Connection: Keep-Alive field 





## Problem 7 

The total amount of time to get the IP address is

RTT1+RTT2+......+RTTN



Once the IP address is known, RTT0 elapses to set up the TCP connection and another RTT0 elapses to request and receive the small object. The total response time is 
no 2RTT0+RTT1+RTT2+RTT3+.... RTTn 

## Problem 8  

a)  
RTT1+RTT2+....+RTTn+2RTT0+8 * 2RTTo  =18 RTTo+RTT1+....RTTn

b)  
RTT1+RTT2+....+RTTn+2RTTo+2*2RTTo  =6 RTTo+RTT1+....RTTn
 c) Persistent connection with pipelining. This is the default mode of HTTP. 
RTT1+RTT2+....+RTTn+2RTTo+RTTo  =3RTTo+RTT1+....RTTn

Persistent connection without pipelining, without parallel connections.  
RTT1+RTT2+....+RTTn+2RTTo+8 RTTo  =10RTTo+RTT1+....RTTn

## Problem 14 

SMTP uses a line containing only a period to mark the end of a message body. HTTP uses “Content-Length header field” to indicate the length of a message body.  No, HTTP cannot use the method used by SMTP, because HTTP message could be binary data, whereas in SMTP, the message body must be in 7-bit ASCII format.