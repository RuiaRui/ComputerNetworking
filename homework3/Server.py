from socket import *
import os

# 创建TCP监听套接字
tcpSocket = socket(AF_INET, SOCK_STREAM)
# 设置绑定的信息
localAddress = ('', 12000)
# 绑定端口
tcpSocket.bind(localAddress)
# 设置最大连接数
tcpSocket.listen(1)
# 设置服务关闭标志位
on = 1

# 开始监听
while True:
    try:
        print("Server is ready")
        connect, clientAddress = tcpSocket.accept()

        while True:
            try:
                # 接收信息
                data = connect.recv(1024).decode()

                if data == "shutdown":  # 收到"shut down"关闭服务器
                    tcpSocket.close()
                    on = 0
                    print("{} : {}    ————    server shutdown".format(clientAddress, data))
                    break

                else:
                    print("{} : {}".format(clientAddress, data))

                # 键入数据
                data = input("sever send ： ")
                connect.send(data.encode())
                print("message sent")

            except:
                connect.close()

        if on == 0:
            break

    except:
        tcpSocket.close()
        break
