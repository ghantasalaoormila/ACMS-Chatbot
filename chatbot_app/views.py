from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
	context = {}    
	return render(request, 'index.html', context=context)
	
@csrf_exempt
def get_reply(request):
	response = {"reply": "Hi"}
	return JsonResponse(response)
