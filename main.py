import random

Triangle_X = [
                       ["X"],
                     ["X","X"],
                   ["X","X","X"],
                 ["X","X","X","X"],
               ["_","_","_","_","_"],
             ["_","_","_","_","_","_"],
           ["_","_","_","_","_","_","_"],
         ["_","_","_","_","_","_","_","_"],
       ["_","_","_","_","_","_","_","_","_"],
         ["_","_","_","_","_","_","_","_"],
           ["_","_","_","_","_","_","_"],
             ["_","_","_","_","_","_"],
                ["_","_","_","_","_"],
                  ["Y","Y","Y","Y"],
                    ["Y","Y","Y"],
                      ["Y","Y"],
                        ["Y"]
]

Turn = ["PC"]

run = True

def Human_Turn():
    Moves = []
    x =int( input("Which row do you want to choose from : "))
    print("Example [0,1,2,3,4] \n so to get '3' it will be row 0 element 3")
    y =int( input("Which element do you want:"))
    row_switcher = 1

    if x>=8 :
        row_switcher = -1




    Z=int(y)+ int(row_switcher)
    x1 = 1 +int(x)
    if Triangle_X[x1][y] == "_":
        Moves.append([x1,y])

    elif Triangle_X[x1][y] != "_":
        if Triangle_X[x1+1][y] == "_":
            Moves.append([(x1+1),y])

    if Triangle_X[x1][Z] == "_":
        Moves.append([x1, Z])

    elif Triangle_X[x1][Z] != "_":
        if row_switcher == 1:
            if Triangle_X[x1+1][Z+1] == "_":
                Moves.append([(x1+1), (Z+1)])
        elif row_switcher == -1:
            if Triangle_X[x1+1][Z-1] == "_":
                Moves.append([(x1+1), (Z-1)])
    print(Moves)
    c = int( input("Which choice do you want start from '0' :"))
    c1 = int(Moves[c][1])
    c2 = int(Moves[c][0])
    Triangle_X[c2][c1] = "X"
    Triangle_X[x][y]= "_"

    Turn[0] = "PC"




def PC_Turn_Easy():
    Valid = False
    Moves = []
    Possible_Rows = []
    Possible_Elements = []
    for i in range(len(Triangle_X)):
        for Y in Triangle_X[i]:
            if Y == "Y":
                Possible_Rows.append(i)
                break




    while Valid != True:


        rand_x =int(random.choice(Possible_Rows))
        #print("rand x is :",rand_x)


        Rand_Y_List = Triangle_X[rand_x]

        for i in range(len(Rand_Y_List)):
            if Rand_Y_List[i] == "Y":
                Possible_Elements.append(i)

        Edge_Possibilty = False

        # print(Possible_Elements)

        rand_y = random.choice(Possible_Elements)
        # print("rand y is :", rand_y)
        row_switcher = 1
        if rand_x <= 8:
            row_switcher = -1

        Z = int(rand_y) + int(row_switcher)
        x1 = int(rand_x) - 1

        if Triangle_X[x1][rand_y] == "_":
            Moves.append([x1, rand_y])

        elif Triangle_X[x1][rand_y] != "_":
            if Triangle_X[x1 - 1][rand_y] == "_":
                Moves.append([(x1 - 1), rand_y])

        if Triangle_X[x1][Z] == "_":
            Moves.append([x1, Z])

        elif Triangle_X[x1][Z] != "_":
            if row_switcher == 1:
                if Triangle_X[x1 - 1][Z + 1] == "_":
                    Moves.append([(x1 - 1), (Z + 1)])
            elif row_switcher == -1:
                if Triangle_X[x1 - 1][Z - 1] == "_":
                    Moves.append([(x1 - 1), (Z - 1)])

        if len(Moves) > 0:
            Valid = True
        else:
            continue

        print("x : ", rand_x, "y : ", rand_y)


        c = int(len(Moves))
        print("Moves len is : ",c)
        print(Moves)
        c1 = int(random.randint(0,c-1))
        print("random : ",c1)
        c2 = int(Moves[c1][1])
        print("c2 is : ",c2)
        choice_1 = int(Moves[c1][0])
        Triangle_X[choice_1][c2] = "Y"
        Triangle_X[rand_x][rand_y] = "_"
        Turn[0] = "Human"






def PC_Turn_Hard():
    Valid = False
    Moves = []
    Possible_Rows = []
    Possible_Elements = []
    R = [0]
    for i in range(len(Triangle_X)):
        for Y in Triangle_X[i]:
            if Y == "Y":
                Possible_Rows.append(i)
                break







    for i in range(len(Possible_Rows)):
        if int(Possible_Rows[i]) < 2:
            Possible_Rows.pop(i)




    while Valid != True:

        rand_x = int(Possible_Rows[R[0]])

        print("Current Row is",rand_x )

        print("Possible Rows :",Possible_Rows)

        Rand_Y_List = Triangle_X[rand_x]

        for i in range(len(Rand_Y_List)):
            if Rand_Y_List[i] == "Y":
                Possible_Elements.append(i)

        Edge_Possibilty = False

       #print(Possible_Elements)


        rand_y = random.choice(Possible_Elements)
       # print("rand y is :", rand_y)
        row_switcher = 1
        if rand_x <= 8:
            row_switcher = -1
            Edge_Possibilty = True

        Z =  int(rand_y) + int(row_switcher)
        x1 = int(rand_x) - 1


        if Edge_Possibilty == False:
            if Triangle_X[x1][rand_y] == "_":
                Moves.append([x1,rand_y])

            elif Triangle_X[x1][rand_y] != "_":
                if Triangle_X[x1-1][rand_y] == "_":
                    Moves.append([(x1-1),rand_y])

        elif Edge_Possibilty == True:
            if rand_y != int(len(Rand_Y_List))- 1:
                if Triangle_X[x1][rand_y] == "_":
                    Moves.append([x1, rand_y])

                elif Triangle_X[x1][rand_y] != "_":
                    if len(Triangle_X[x1-1]) > rand_y:
                        if Triangle_X[x1-1][rand_y] == "_":
                            Moves.append([(x1 - 1), rand_y])

        if Edge_Possibilty == False:
            if Triangle_X[x1][Z] == "_":
                Moves.append([x1,Z])

            elif Triangle_X[x1][Z] != "_":
                if row_switcher == 1:
                    if Triangle_X[x1-1][Z+1] == "_":
                        Moves.append([(x1-1),(Z+1)])
                elif row_switcher == -1:
                    if Triangle_X[x1-1][Z-1] == "_":
                        Moves.append([(x1-1),(Z-1)])


        elif Edge_Possibilty == True:
            if rand_y != 0:
                if Triangle_X[x1][Z] == "_":
                    Moves.append([x1, Z])

                elif Triangle_X[x1][Z] != "_":
                    if row_switcher == 1:
                        if Triangle_X[x1 - 1][Z + 1] == "_":
                            Moves.append([(x1 - 1), (Z + 1)])
                    elif row_switcher == -1:
                        if Triangle_X[x1 - 1][Z - 1] == "_":
                            Moves.append([(x1 - 1), (Z - 1)])




        print("Moves is:",Moves)


        if len(Moves) > 0:
            Valid = True
            print("Validd")
        else:
            R[0] = R[0]+1
            print("Invaliddd")
            print("Ro isss ", R[0])
            continue



        print("x : ", rand_x, "y : ", rand_y)


        c = int(len(Moves))
        print("Moves len is : ",c)
        print(Moves)
        c1 = int(random.randint(0,c-1))
        print("random : ",c1)
        c2 = int(Moves[c1][1])
        print("c2 is : ",c2)
        choice_1 = int(Moves[c1][0])
        Triangle_X[choice_1][c2] = "Y"
        Triangle_X[rand_x][rand_y] = "_"
        Turn[0] = "Human"




def Board_State():
    for i in range(len(Triangle_X)):
        s = len(Triangle_X[i])
        if(i == 4 or i ==13):
            print("   "*4,"-----------------------")
        print(i,"   "*(8-(s-1)),Triangle_X[i])


def main(Level):
    print("Current Board State \n")
    Board_State()

    print("Current turn is :", Turn[0])
    if Turn[0] == "Human":
        Human_Turn()


    elif Turn[0] == "PC":
        if Level == "easy":
            PC_Turn_Easy()

        elif Level == "Hard":
            PC_Turn_Hard()



def User_Win_State():
    WIN = True
    i = 13
    while i < 17:
        for y in Triangle_X[i]:
            if y != "X":
                WIN = False

                break
        i = i+1
    return WIN




def PC_Win_State():
    WIN = True
    i = 0
    while i < 4:
        for y in Triangle_X[i]:
            if y != "Y":
                WIN = False

                break
        i = i+1
    return WIN








level1 = int(input("Choose the game Difficulty level, Press '1' For easy , '2' For Hard"))

if level1 == 1:
    levelo ="easy"

if level1 == 2:
    levelo = "Hard"

while run:
    main(levelo)
    if User_Win_State() == True:
        print("Congrats you won the GAMEE!!!!!")
        run = False

    elif PC_Win_State() == True:
        print("You LOST :(")
        run = False





