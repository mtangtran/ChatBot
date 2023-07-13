class LogManager:

    def __init__(self):
        self.log = "ChatBotLog.txt"
        self.numEntries = 0
    def writeLog(self, entry):
        file = open(self.log, "a")
        file.write(entry)
        file.close()
        self.numEntries += 1
    def readLog(self):
        with open(self.log) as f:
            print(f.readlines())

    def getEntries(self):
        return self.numEntries

