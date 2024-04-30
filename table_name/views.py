from django.shortcuts import render

# Create your views here.
from table_name.models import *
from django.http import HttpResponse

def insert_topic(request):
    tn=input('Enter a topic_name : ')
    e=input('Enter a email : ')
    to=Topic.objects.get_or_create(topic_name=tn,email=e)[0]
    
    to.save()
    d={'QLTO':Topic.objects.all()}
    return render(request,'display_topic.html',d)




def insert_webpage(request):
     tn=input('Enter a topic_name : ')

     ''''to=Topic.objects.get(topic_name=tn) 
     by usin get method it will check whether given condition is there or not if it bis there it will add the data on the table other wise it will throw the error'''



     to=Topic.objects.filter(topic_name=tn)
     if to:
         

         n=input('Enter a name : ')
         u=input('Enter a url : ')
         t=input('enter a team : ')
         ob=Webpage.objects.get_or_create(topic_name=to[0],name=n,url=u,team=t)[0]
         ob.save()
         d={'QLWO':Webpage.objects.all()}
         return render(request,'display_webpage.html',d)  


     else:
          return HttpResponse('your given data is not there in your table'
                              
                              
                              ) 
def insert_accessrecords(request):
     '''tn=input('Enter a topic_name : ')
     to=Topic.objects.get_or_create(topic_name=tn)[0]
     to.save()
     n=input('Enter a name : ')
     u=input('Enter a url : ')
     t=input('enter a team : ')
     ob=Webpage.objects.get_or_create(topic_name=to,name=n,url=u,team=t)[0]
     ob.save()'''
    

     d = input('Enter a id :')
     
     ob=Webpage.objects.filter(id = d)
     if ob:
     
        d=input('Enter a date : ')
        a=input('Enter a author : ')

        ob2=AccessRecord.objects.get_or_create(name=ob[0],date=d,author=a)[0]
        ob2.save()
        d={'QLAO':AccessRecord.objects.all()}
        return render(request,'display_accessrecord.html',d)
     else:
        return HttpResponse('invalid data')
     

def display_topic(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}

    return render(request,'display_topic.html',d)

def display_webpage(request):
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)


def display_accessrecord(request):
    QLAO=AccessRecord.objects.all()
    d={'QLAO':QLAO}
    return render(request,'display_accessrecord.html',d)

     