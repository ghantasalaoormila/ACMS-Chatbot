from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from googletrans import Translator
import nltk
from nltk.corpus import stopwords
import pandas as pd
import pickle
from nltk.tokenize import word_tokenize 
from nltk import pos_tag

import numpy as np
import re
import logging

import gensim
from gensim import corpora, models, similarities
from sklearn.metrics.pairwise import cosine_similarity

import os
import json
import string
import random
logging.basicConfig()
logger = logging.getLogger('logger')
#logging.basicConfig(filename='example.log',level=logging.DEBUG)
translator = Translator()
# Create your views here.
def index(request):
	context = {}    
	return render(request, 'index.html', context=context)
	
@csrf_exempt
def get_reply(request):
	#response = {"reply": "Hi"}
	#return JsonResponse(response)
	query = request.GET['q']
	print(str(query))
	language = detectlang(str(query))
	print(language)
	inputbyuser = translatedata(str(query),'en')

	#print(translatedata(str(query),'ko'))
	"""response = {"reply": query}
	if(str(query)=="Hi"):
		return JsonResponse(response)
	else: return JsonResponse({"reply":"Failed!"})"""
	response = get_reply_chatbot(inputbyuser)
	#response = get_reply_dataset("chatbot_app/static/chatbot.txt",data)
	print(response)
	result = translatedata(str(response),language)
	print("result is " + result)
	return JsonResponse({"reply": str(result)})
	
	
def detectlang(input):
	language = translator.detect(input)
	return language.lang

def translatedata(input,lang):
	result = translator.translate(input,dest = lang)
	return result.text

def pre_process(questions):
    stop_words = stopwords.words("english")
   
    
    # Tokenlization
    questions_tokens = [nltk.word_tokenize(t) for t in questions]
    # Removing Stop Words
    questions_stop = [[t for t in tokens if (t not in stop_words) and (3 < len(t.strip()) < 15)]
                      for tokens in questions_tokens]
    
    questions_stop = pd.Series(questions_stop)
    return questions_stop

def train_model(data):
    """Function trains and creates Word2vec Model using parsed
    data and returns trained model"""
    model = gensim.models.Word2Vec(data,min_count=1)
    return model

def Talk_To_Javris(data, model,sentence):
    print("inside jarvis")
    # Preprocessing of user input
    sentence_pp = pre_process(pd.Series(sentence)) 
    print(sentence_pp)
    cosines = []
    try:
        # Get vectors and average pooling
        question_vectors = []
        for token in sentence_pp:
            try:
                vector = model[token]
                question_vectors.append(vector)
            except:
                continue
        question_ap = list(pd.DataFrame(question_vectors[0]).mean())
        print("question_ap")
        print(question_ap)

        # Calculate cosine similarity
        for t in data['Average_Pooling']:
            if t is not None and len(t) == len(question_ap):
                val = cosine_similarity([question_ap], [t])
                cosines.append(val[0][0])
            else:
                cosines.append(0)
    except:
        print("in except")
        pass
            
    # If not in the topic trained
    if len(cosines) == 0:
        not_understood = "Apology, I do not understand. Can you rephrase?"
        return not_understood, 999
    
    else: 
        # Sort similarity
        index_s =[]
        score_s = []
        for i in range(len(cosines)):
            x = cosines[i]
            if x >= 0.6:
                index_s.append(i)
                score_s.append(cosines[i])
            """else:
                index_s.append("0000")
                score_s.append("-0.000")"""
                

        reply_indexes = pd.DataFrame({'index': index_s, 'score': score_s})
        reply_indexes = reply_indexes.sort_values(by="score" , ascending=False)
       # print(reply_indexes['score'].iloc[0])
       # print(reply_indexes['index'].iloc[0])
        reply_indexes.head()
        
        # Find Top Questions and Score
        
        r_index = int(reply_indexes['index'].iloc[0])
        r_score = float(reply_indexes['score'].iloc[0])

        reply = str(data.iloc[:,2][r_index])
        print('reply is' + reply)
        return reply, r_score

# Greeting function
def greeting(sentence):
	GREETING_INPUTS = ("hello", "hi", "greetings", "hello i need help", "good day","hey","i need help", "greetings")
	GREETING_RESPONSES = ["Good day, How may i of help?", "Hello, How can i help?", "hello", "I am glad! You are talking to me."]
	for word in sentence.split():
		if word.lower() in GREETING_INPUTS:
			return random.choice(GREETING_RESPONSES)


def get_reply_chatbot(sentence):

    path = '/home/bksahitya/Documents/ACMS/'
    data = pd.read_csv(path+'chatbotdataset.csv')
    data['Question'] = data['Question'].apply(lambda x: " ".join(x.lower() for x in x.split()))


    
    # Initial preprocessing training data
    questions = data['Question']
    questions_pp = pre_process(questions)
    length = data['Question'].apply(len)

    train_data = pd.DataFrame({'Question': list(data['Question']),
                                'Question_Tokens': questions_pp,
                                'Answer': list(data['Answer']),
                               'Length':length
                               })

    questions_data = list(train_data['Question_Tokens'])

    model = train_model(questions_data)
    model.save('word2vec')

    # Save Word2Vec model
    word2vec_pickle_path = path + 'chatbot.bin'
    f = open(word2vec_pickle_path, 'wb')
    pickle.dump(model, f) 
    f.close()

    model = gensim.models.KeyedVectors.load(word2vec_pickle_path)

    train_data['Question_Vectors'] = None
    train_data['Average_Pooling'] = None
    for i in range(len(train_data)):
        question_tokens = train_data['Question_Tokens'][i]
        question_vectors=[]

        for token in question_tokens:
            vector =model[token]
            question_vectors.append(vector)
        train_data['Question_Vectors'][i]= question_vectors
        train_data['Average_Pooling'][i] = list(pd.DataFrame(question_vectors).mean())

    train_data['Question_Tokens'] = [" ".join(l) for l in train_data['Question_Tokens']]
    length = train_data['Question_Tokens'].apply(len)
    train_data = train_data.assign(Question_Length=length)
    data_json = json.loads(train_data.to_json(orient='records'))
    chatbot_path = path + 'chatbot.json'
    with open(chatbot_path, 'w') as outfile:
        json.dump(data_json, outfile)
    with open(chatbot_path) as file:
        reader = json.load(file)
        questions = []
        questions_tokens = []
        answers = []
        question_lengths = []
        question_vectors = []
        average_pooling = []
        for row in reader:
            questions.append(row['Question'])
            questions_tokens.append(row['Question_Tokens'].split())
            answers.append(row['Answer'])
            question_lengths.append(row['Length'])
            question_vectors.append(row['Question_Vectors'])
            average_pooling.append(row['Average_Pooling'])

        train_data = pd.DataFrame({
                                    'Question': questions,
                                    'Question_Tokens': questions_tokens,
                                    'Answer': answers,
                                    'Length': question_lengths,
                                    'Question_Vectors': question_vectors,
                                    'Average_Pooling': average_pooling})


    flag_query = True
    # Read word2vec model
    word2vec_pickle_path = path + 'chatbot.bin'
    model = gensim.models.KeyedVectors.load(word2vec_pickle_path)

    #while(flag_query == True):
    print('sentence is'+sentence)
    sentence = sentence.lower()
    if(sentence != 'bye'):
        if(greeting(sentence) != None):
            reply = greeting(sentence.lower())
            #print(reply)
        else:
            reply, score = Talk_To_Javris(train_data, model,sentence)
            #print('reply is'+reply)

            #For Tracing, comment to remove from print 
            #print("")
            #print("SCORE: " + str(score))
    else:
        flag_query = False
    return reply
    #print('Bye! Hope that i am of help.') 
