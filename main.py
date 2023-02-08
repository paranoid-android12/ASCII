def parse(length):
    for x in range(0, 7):
        for i in range(length):
            coord = dict_test[lett[i]][0]
            print(temp[coord + x], end="", flush=True)
        print("")
    print("")

while 1:
    temp = open('ASCII/SHIT.txt','r').read().split('\n')
    lett = input("ENTER A MAXIMUM OF 7 LETTERS: \n")
    lett = lett.lower()

    if len(lett) > 7:
        print("bitch i said maximum of 7\n\n")
        continue
    tro = lett.isnumeric()
    
    if tro == True:
        print("no habla numero")
        continue
    
    dict_test = {
        'a' : [0,6],
        'b' : [7,13],
        'c' : [14,20],
        'd' : [21,27],
        'e' : [28,34],
        'f' : [35,41],
        'g' : [42,48],
        'h' : [49,55],
        'i' : [56,62],
        'j' : [63,69],
        'k' : [70,76],
        'l' : [77,83],
        'm' : [84,90],
        'n' : [91,97],
        'o' : [98,104],
        'p' : [105,111],
        'q' : [112,118],
        'r' : [119,125],
        's' : [126,132],
        't' : [133,139],
        'u' : [140,146],
        'v' : [147,153],
        'w' : [154,160],
        'x' : [161,167],
        'y' : [168,174],
        'z' : [175,181],
    }

    if tro == True:
        print("no habla numero")
        continue
    parse(len(lett))
    



