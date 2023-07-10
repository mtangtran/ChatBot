"""
Initial Chatbot class.

This class will handle the calls from other classes. This is meant to obfuscate the internal logic from the user.

This class will use other classes to execute the internal logic.
"""
from LogManager import LogManager
from DBmanager  import DBManager
class ChatBot:

    def __init__(self):
        self.name = ""
        self.logManager = LogManager()
        pass

    def getHelloMessage(self, name):
        self.name = name

        message = "Hello {}! Welcome to Chatbot.py!".format(name)
        self.logManager.writeLog(message)
        return message
    def getWelcomeMessage(self):

        message= "How may I help you?"
        self.logManager.writeLog(message)
        return message
    def getGoodByeMessage(self):

        message= "Goodbye {}!".format(self.name)
        self.logManager.writeLog(message)
        return message
