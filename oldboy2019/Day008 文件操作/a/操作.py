import requests #网络请求
rs = requests.get("https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1571850057085&di=d971bc793ebe82b7550e8a5707aba4a3&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201801%2F27%2F20180127090906_JhTB4.jpeg")
f = open("baiqi.jpg",mode="wb")
f.write(rs.content)
f.flush()
f.close()