import sys

from ChatBot import ChatBot
def print_hi(obj, name):
    print(obj.getHelloMessage(name))
# Press the green button in the gutter to run the script.



if __name__ == '__main__':
    flag = False
    try:
        name = sys.argv[1]
    except:

        name = input("Hello! May you please tell me your name? ")

    obj = ChatBot()
    print_hi(obj, name)
    print(obj.getWelcomeMessage())
    while not flag:

        inp = input("Please enter a phrase:")
        if inp == "" or inp=="stop":
            flag = True

    print(obj.getGoodByeMessage())
