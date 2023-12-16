table = {
    "CU"    :	"see you",
    ":-)"   :	"I’m happy",
    ":-("	:   "I’m unhappy",
    ";-)"	:   "wink",
    ":-P"	:   "stick out my tongue",
    "(~.~)"	:   "sleepy",
    "TA"	:   "totally awesome",
    "CCC"	:   "Canadian Computing Competition",
    "CUZ"	:   "because",
    "TY"    :   "thank-you",
    "YW"    :   "you’re welcome",
    "TTYL"	:   "talk to you later",
}

while True:
    cmd = input()
    if cmd not in table:
        print(cmd)
    else:
        print(table[cmd])
    if cmd == "TTYL":
        break