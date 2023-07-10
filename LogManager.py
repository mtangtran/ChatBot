class LogManager:

    def __init__(self):
        self.log = "ChatBotLog.txt"

    def writeLog(self, entry):
        file = open(self.log, "a")
        file.write(entry)
        file.close()

    def readLog(self):
        with open(self.log) as f:
            print(f.readlines())

