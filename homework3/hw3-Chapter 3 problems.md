## Problem 3

01010011+01100110+01110100=00101110

So, the one's complement = 1 1 0 1 0 0 0 1. 

To detect errors, the receiver adds the four words (the three original words and the checksum). If the sum contains a zero, the receiver knows there has been an error. All one-bit errors will be detected, but two-bit errors can be undetected For example., if the last digit of the first word is converted to a 0 and the last digit of the second word is converted to a 1. 







##  Problem 5

No, the receiver cannot be absolutely certain that no bit errors have occurred. This is for the reason that the manner in which the checksum for the packet is calculated. If the corresponding bits of two 16-bit words in the packet were 0 and 1 then even if these get flipped to 1 and 0 respectively, the sum still remains the same. 

Hence, the 1s complement the receiver calculates will also be the same. This means the checksum will verify even if there was transmission error. 





## Problem 6 

Suppose the sender is in state “Wait for call 1 from above” and the receiver is in state “Wait for 1 from below.”  The sender sends a packet with sequence number 1, and transitions to “Wait for ACK or NAK 1,” waiting for an ACK or NAK.  Suppose now the receiver receives the packet with sequence number 1 correctly, sends an ACK, and transitions to state “Wait for 0 from below,” waiting for a data packet with sequence number 0. 

However, the ACK is corrupted.  When the rdt2.1 sender gets the corrupted ACK, it resends the packet with sequence number 1.  

However, the receiver is waiting for a packet with sequence number 0 and (as shown in the home work problem) always sends a NAK when it doesn't get a packet with sequence number 0. Hence the sender will always be sending a packet with sequence number 1, and the receiver will always have the state "NAK" that packet.  Neither will progress forward from that state.



## Problem 12

 The protocol would still work, since a retransmission would be what would happen if the packet received with errors has actually been lost. And from the receiver standpoint, it never knows which of these events, if either, will occur.   

## Problem 15 

1500*8/10^9=12 microseconds. 

In order for the sender to be busy 98% of the time, we must have

98%=0.012n/30.012  n approximately equals to 2451 packets

So, It takes 12 microseconds (or 0.012 milliseconds) to send a packet.