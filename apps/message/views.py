from django.shortcuts import render

import MySQLdb
# Create your views here.

from .models import UserMessage

# def getform(request):
#     all_messages = UserMessage.objects.all()
#     # UserMessages默认数据管理器是 objecs
#     # 方法all() 是将所有的数据返回成一个querset类型（djangi的内置类型）
#
#     for message in all_messages:
#         # 每个message实际就是一个UserMessage对象 （可以用对象的相关方法）
#         print(message.name )
#     return render(request, 'form.html')


#手写sql语句来链接数据库
# 使用原生sql获取书的列表
# def book_list(request):
#     # 创建到数据库的连接: 指明用户名，数据库，密码
#     db = MySQLdb.connect(user = 'me', db='mydb', passwd='secret', host='localhost')
#     # 创建一个游标对象执行器
#     cursor = db.cursor()
#     # 书写我们需要的sql语句
#     cursor.execute('SELECT name FROM books ORDER BY name')
#     # 对于fetchall()的结果做遍历，将遍历回来的结果当做数组，取第0个值name。
#     names = [row[0] for row in cursor.fetchall()]
#     db.close()



def getform(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        message = request.POST.get("message")

        user_message = UserMessage()
        user_message.name = name
        user_message.email = email
        user_message.address = address
        user_message.message = message

        user_message.save()
    return render(request, 'form.html')