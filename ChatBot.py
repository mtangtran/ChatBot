"""
Initial Chatbot class.

This class will handle the calls from other classes. This is meant to obfuscate the internal logic from the user.

"""
class ChatBot:

    def __init__(self):
        self.name = ""
        pass

    def getHelloMessage(self, name):
        self.name = name
        return "Hello {}! Welcome to Chatbot.py!".format(name)

    def getWelcomeMessage(self):
        return "How may I help you?"

    def getGoodByeMessage(self):
        return "Goodbye {}!".format(self.name)

