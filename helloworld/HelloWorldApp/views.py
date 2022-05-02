from django.shortcuts import render
# from django.http import HttpResponse
 
from django.http import JsonResponse

def sayHello(request):
    x = "Hello "+str(2+2+2)
    responseData = {
        'Group Leader': "Chathushka Rodrigo",
        'Members': ["Shasvathan, Chamath, Buddhisha, Adhikari"],
        'Projects' : ['CDAP project managment system']
    }
    print(x)
    return JsonResponse(responseData)
# def sayHello(request):
#     return HttpResponse('Hello World')
# # Create your views here.