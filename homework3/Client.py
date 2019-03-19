from socket import *


# 创建套接字
tcpSocket = socket(AF_INET, SOCK_STREAM)

# 设置目标服务器地址信息
aimAddress = ('localhost', 12000)

# 绑定本地端口
tcpSocket.connect(aimAddress)
print("——ready to connect——")

while True:
    try:
        # 键入数据
        data = input("sending : ")
        # 发送数据
        tcpSocket.send(data.encode())
        print("message sent")
        # 接收数据
        data = tcpSocket.recv(1024).decode()
        print(data)

        if not data:
            tcpSocket.close()
            print("client shutdown")
            break

    except:
        tcpSocket.close()
        print("error")
        break
