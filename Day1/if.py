import getpass
#让密码密文，python标准库，直接import有的库，不用安装
_username='alex'
_password='abc-123'
username = input("username:")
#password = getpass.getpass("password:")
password = input("password:")

if _username == username  and _password == password:
    print("Welcome user {name} login ..".format(name=username))
else:
    print("Invalid username")
