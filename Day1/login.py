import getpass
_username = 'alex'
_password = 'abc123'
user = input("请输入用户名：")
password = input("请输入密码：")
if user == _username and password == _password:
    print("Welcome user %s login"% user)
else:
    print("Wrong username or password")