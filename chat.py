import chatterbot
from chatterbot import ChatBot
from Chatterbot.trainers import ListTrainer
from Chatterbot.trainers import ChatterBotCorpusTrainer

class Chat_T:
    chatbot: None

    def __init__(self):
        self.chatbot = ChatBot("ChatBot")
    # Training with Personal Ques & Ans
        conversation = [
            "Hello",
            "Hi there!",
            "How are you doing?",
            "I'm doing great.",
            "You're welcome.",
            "who Developed you",
            "NLP class",
            "This is a chatbot to answer your query",
            "I'm supervisedly trained"
        ]
        trainer = ListTrainer(self.chatbot)
        trainer.train(conversation)

    def chat(self, t1):
        response = self.chatbot.get_response(t1)
        return response