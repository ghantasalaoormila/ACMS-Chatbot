from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import logging 
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
trainer.train([
	"hi",
	"hello",
	"hey",
	"heya",
	"hello user" ])

trainer.train([
	"how are you",
	"I'm good! Thank you!",
	"I'm good! How abt you?" ])

trainer.train([
	"What is the Credit Distribution for each semester?",
	"16 credits" ])

trainer.train([
	"What is the duration of each semester?",
	"6 months" ])

trainer.train([
	"What are the areas of specialization for M.Tech (CSE)?",
	"There are four areas of specialization : Theory and Systems(TS)  ,Data Science(DS), Networking & Communication(NC) , Signal Processing and Pattern Recognition(SP)" ])

trainer.train([
	"What are the areas of specialization for M.Tech (ECE)?",
	"There are four areas of specialization : VLSI Systems (VL) ,Networking & Communication(NC) ,Signal Processing and Pattern Recognition(SP)." ])

trainer.train([
	"How many credits are given for thesis?",
	"A student can accumulate 16 credits on successful completion of thesis or Masters Project." ])

trainer.train([
	"How many PE/RE courses are allowed to be opted per semester?",
	"Institute allows only one PE/RE per semester." ])

trainer.train([
	"How many PE/RE can a student opt in the entire programme duration?",
	"Student can opt for only 3 PE/RE in the entire programme." ])

trainer.train([
	"How many electives under a particular specialization have to be completed for specialization degree?",
	"Five electives must be completed to get specialization degree." ])
trainer.train([
	"What is the duration of a Master’s thesis?",
	"Thesis/Masters Project shall be of 24 weeks duration." ])
trainer.train([
	"What are the programs offered?",
	"Institute offers MS,M.Tech and Imtech programs." ])
trainer.train([
	"How many electives under a particular specialization have to be completed for specialization degree?",
	"Five electives must be completed to get specialization degree." ])
trainer.train([
	"What are the available branches?",
	"Computer Science & Engineering,Electronics & Communication Engineering and Digital Society" ])
trainer.train([
	"What is the duration of Mtech/imtech programme?",
	"Mtech programme is of 2 years and imtech program is of 5 years." ])

trainer.train([
	"What is the duration of imtech programme?",
	"imtech program is of 5 years." ])
trainer.train([
	"Is any part time programme available?",
	"No. Institute doesn't offer any part-time programmes." ])
trainer.train([
	"What is the criteria for admission of International Students?",
	"Foreign nationals (FNs) and non-resident Indians (NRIs) are welcome to apply for the M.Tech. programme. Such applicants can apply with valid GRE and TOEFL scores.Only those students whose undergraduate education was in an Anglophone country(i.e. Australia, Canada, New Zealand, Singapore, UK, and the US) are exempt from TOEFL. Shortlisted FNs and NRIs applicants have to go through an online interview." ])
trainer.train([
	"What is the selection criteria for the students?",
	"Students are shortlisted based on their GATE scores." ])



#get response
#response = chatbot.get_response('Hello user')

#print(response)


while True:
    try:
        user_input = input('you:')
        user_input = user_input.lower()
        bot_response = chatbot.get_response(user_input)

        print('chatbot:')
        print(bot_response)
        


    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
