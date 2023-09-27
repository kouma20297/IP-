def ip_convert(ip):
    ip_l = [int(s) for s in ip.split(".")]
    return (ip_l[0] << 24) + (ip_l[1] << 16) + (ip_l[2] << 8) + (ip_l[3] << 0)


def decToDot(num):
    ret = (
        str((num >> 24) & 0xFF)
        + "."
        + str((num >> 16) & 0xFF)
        + "."
        + str((num >> 8) & 0xFF)
        + "."
        + str((num >> 0) & 0xFF)
    )
    return ret


ip1 = ip_convert(input("サーバーのIPアドレスを入力"))
sub1 = ip_convert(input("サーバーのサブネットマスクを入力"))
ip2 = ip_convert(input("クライアントのIPアドレスを入力"))
sub2 = ip_convert(input("クライアントのサブネットマスクを入力"))

# ネットワークアドレスの定義
server_networkaddress1 = ip1 & sub1
client_networkaddress1 = ip2 & sub2
server_networkaddress2 = ip2 & sub1
client_networkaddress2 = ip1 & sub2


# 接続判定
if server_networkaddress1 == server_networkaddress2 and client_networkaddress1 == client_networkaddress2:
    print("接続")
else:
    print("接続できない")
