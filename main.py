#Characters: 247
#Functionality: read file from drive, create practice list, shuffle list, repeat practicing untill all answers are right

[globals().update({"r":[k.strip() for k in open(input("")+".txt",'r').readlines()]}),globals().update({"v":[i for i in range(int(len(r)/2))]}),__import__('random').shuffle(v),[0 if input(r[i*2+1])==r[i*2]else[print(r[i*2]),v.append(i)]for i in v]]

#"Readable" version with comments:
[
    globals().update({"r":                                                            #Add variable called r to globals
                      [k.strip() for k in open(input("")+".txt",'r').readlines()]     #Split text from file to list with: [question1, answer1, q2, a2, q3, a3, ...]
    }),
    globals().update({"v":                                                            #Add variable called v to globals
                      [i for i in range(int(len(r)/2))]                               #List with numbers in range(0-(amount_of_questions)) (used as indices in main loop)
    }),
    __import__('random').shuffle(v),                                                  #Shuffle the list with indices so the user doesn't develop muscle memory, but really learns the words
    [
        0 if input(r[i*2+1])==r[i*2]                                                  #Don't do anything when the answer is right
        else[
          print(r[i*2]),                                                              #When the answer is wrong: show the right answer and add the question back into the list
          v.append(i)
        ]for i in v
    ]
]
