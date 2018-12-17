from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import json,datetime
from panel.settings import OPTIONS
from database.mysql_manager import MysqlManager
from libs import public

# Create your views here.
@login_required
def index(request):
    setting = json.loads(public.readfile('data/setting.json'))
    user = {
        'name': request.user,
        'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return render(request, "database.html", {"setting": setting, 'user': user})

@login_required
def AddDatabase(request):
    dbManager = MysqlManager("mysql", 'root', eval(OPTIONS['dbrootpwd']))
    result = dbManager.query("show databases;")
    print(result)
    if result:
         content = { 'flag': 'Success' }
    else:
         content = { 'Error': 'test'}
    return JsonResponse(content)
def CreateDatabase(request):
    if request.method == 'POST':
        try:
            post = json.loads(request.body)

            #User.objects.create_superuser(name=post['name'], user=post['user'], password=post['password'], host=post['host'], comment=post['comment'])
            #context = {'flag': 'Success'}
            message = 'this data is %r' % request.POST.get('name')
            #context = 
        except Exception as e:
            message = {'flag': 'Error', 'context': str(e)}
            #print(context)
            #print(locals())
        return HttpResponse(message)


def Delatabase(request):
    dbManager = MysqlManager("mysql", 'root', eval(OPTIONS['dbrootpwd']))
