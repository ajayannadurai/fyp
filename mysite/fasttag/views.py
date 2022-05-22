from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from django.views import generic
from .models import users
import json
from django.http import StreamingHttpResponse

def index(request):
    return render(request,'fasttag/index.html')



class transfer(generic.DetailView):
    model = users
    template_name = 'fasttag/payment.html' 

def sucess(request):
    return render(request,'fasttag/sucess.html')
   
    
def pay(request,fastid):    
    fromid=get_object_or_404(users, fastid=fastid)
    cash=request.POST['fund']
    if(len(cash)!=0):
        cash=int(cash)
    else:
        cash=0
    if(cash>0):
        fromid.fine=fromid.fine-cash
        fromid.save()
    else:
        if(fromid.accbal>fromid.fine):
            fromid.accbal=fromid.accbal-fromid.fine
            fromid.fine=0
            fromid.save()
        else:
            print("error")
    return HttpResponseRedirect(reverse('fasttag:sucess'))

def finecalc(speed,limit):
    if speed>limit+10:
        return 300
    else:
        return 350


def fine(request):
    if request.method=='POST':
            data = json.loads(request.body.decode("utf-8"))
            
            id=int(data['data'][0]['fasttrackid'])
            speed=int(data['data'][1]['speed'])
            speedlimit=int(data['data'][2]['speedlimit'])
            print("fasttagid :",id,"speed :",speed,"speedlimit ",speedlimit)
            fine=finecalc(speed,speedlimit)
            fromid=get_object_or_404(users, fastid=id)
            fromid.fine+=fine
            fromid.save()
            print("username :",fromid.username,"updated fine amount :",fromid.fine)

            return StreamingHttpResponse('overspeed data sent '+str(data))
    return StreamingHttpResponse('it was GET request')
