from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time

# Create your views here.
def index(request):
	context = {}    
	return render(request, 'index.html', context=context)
	
@csrf_exempt
def get_reply(request):
	query = request.GET['q']
	response = get_model_response(str(query))
	
	return JsonResponse({"reply": str(response)})
	
	
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import logging 
def get_model_response(user_input):
	time.sleep(2)  #intentionally--- to show loading gif in UI
	logging.basicConfig(filename='example.log',level=logging.DEBUG)
	#logger.setLevel(logging.CRITICAL)
	#chatbot = ChatBot('Amazon')
	chatbot = ChatBot(
	    'Amazon',
	    storage_adapter='chatterbot.storage.SQLStorageAdapter',
	    logic_adapters=[
	        {
	            'import_path': 'chatterbot.logic.BestMatch',
	            'default_response': 'I am sorry, but I do not understand.',
	            'maximum_similarity_threshold': 0.90
	        }
	    ],
	    database_uri='sqlite:///database.sqlite3'
	)
	trainer = ListTrainer(chatbot)
	bot_response = chatbot.get_response(user_input)
	#print('chatbot:')
	return(bot_response)
        
