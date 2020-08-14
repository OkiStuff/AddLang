from sys import *

tokens = []

def ErrorMsg(Errno):
    print("ay homie.. error i think. like how do you get a error when all you do is add numbers?? whatever here is the error\nERRNO: " + str(Errno))
    exit()

def open_file(filename):
    try:
        data = open(filename, "r").read()
        return data
    except Exception:
        print(f"Errno 0: No such file '{filename}'")
        exit()

def lex(filecontents):
    tok = ""
    state = 0
    string = ""
    filecontents = list(filecontents)
    for char in filecontents:
        tok += char
        if tok == " ":
            if state == 0:
                tok = ""
            else:
                tok = " "
        elif tok == "\n":
            tok = ""
        elif tok == "add":
            tokens.append("ADD")
            tok = ""
        elif tok == "cancel task":
            tokens.append("CANCELTASK")
            tok = ""
        elif tok == "\"":
            if state == 0:
                state = 1
            elif state == 1:
                tokens.append("STRING: " + string + "\"")
                string = ""
                state = 0
                tok = ""
        elif state == 1:
            string += tok
            tok = ""
    return tokens
    #print(tokens)

def parse(toks):
    i = 0
    a = 0
    b = 0
    nums = []
    while(i < len(toks)):
        
        if toks[i] + " " + toks[i+1] [0:6] == "ADD STRING":

            if (b == 0):
                try:
                    b = int(toks[i+1] [7:].replace('"', ''))
                except Exception as err:
                    ErrorMsg(err)
            elif (a == 0):
                try:
                    a = int(toks[i+1] [7:].replace('"', ''))
                except Exception as err:
                    ErrorMsg(err)

            if (b > 0 and a > 0):
                print(str(b + a))
                b = 0
                a = 0
            i += 2
def run():
    try:
        data = open_file(argv[1])
    except Exception:
        print("mate.. give me a file..")
        exit()
    toks = lex(data)
    parse(toks)

run()