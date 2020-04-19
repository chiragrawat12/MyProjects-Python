#***********************************************Tic Tac Toe Game**************************************************
ticTac=[1,2,3,4,5,6,7,8,9]
while True:
    playGame=int(input("Do you Want to play game or want to quit::\n(1):Play New Game\n(2):Quit Game\n(Press 1 or 2):"))

    if playGame==1:
        print("Rules for Game:\n1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9 \nYou have to enter 0 or X space and then number according to this position diagram \nSo,lets play ;)")
        print()
        print("{} | {} | {}\n{} | {} | {}\n{} | {} | {}".format(ticTac[0],ticTac[1],ticTac[2],ticTac[3],ticTac[4],ticTac[5],ticTac[6],ticTac[7],ticTac[8]))
        
        
        while True:
            print("Play your chance: ")
            xrz=input()
            pos=int(input())

            if ticTac[pos-1] !='0' and (ticTac[pos-1]!='x' or ticTac[pos-1]!='X'):
                                         ticTac[pos-1]=xrz
            else:
                print("You have already added Number Before please try another position by watching diagram!")
                continue
            
            if ticTac[0]==ticTac[1] and ticTac[1]==ticTac[2] and ticTac[0]==ticTac[2]:
                print(ticTac[0] ,"Won the match")
                break
            elif ticTac[3]==ticTac[4] and ticTac[4]==ticTac[5] and ticTac[3]==ticTac[5]:
                print(ticTac[3],"Won the Match")
                break
            elif ticTac[6]==ticTac[7] and ticTac[7]==ticTac[8] and ticTac[6]==ticTac[8]:
                print(ticTac[6],"Won the match")
                break            
            elif ticTac[0]==ticTac[3] and ticTac[3]==ticTac[6] and ticTac[0]==ticTac[6]:
                print(ticTac[0],"Won the match")
                break
            elif ticTac[1]==ticTac[4] and ticTac[4]==ticTac[7] and ticTac[1]==ticTac[7]:
                print(ticTac[1],"Won the match")
                break
            elif ticTac[2]==ticTac[5] and ticTac[5]==ticTac[8] and ticTac[2]==ticTac[8]:
                print(ticTac[2],"Won the match")
                break
            elif ticTac[2]==ticTac[4] and ticTac[4]==ticTac[6] and ticTac[2]==ticTac[6]:
                print(ticTac[1],"Won the match")
                break
            elif ticTac[0]==ticTac[4] and ticTac[4]==ticTac[8] and ticTac[0]==ticTac[8]:
                print(ticTac[2],"Won the match")
                break            
            else:
                print("{} | {} | {}\n{} | {} | {}\n{} | {} | {}".format(ticTac[0],ticTac[1],ticTac[2],ticTac[3],ticTac[4],ticTac[5],ticTac[6],ticTac[7],ticTac[8]))
                continue
            
        print("{} | {} | {}\n{} | {} | {}\n{} | {} | {}".format(ticTac[0],ticTac[1],ticTac[2],ticTac[3],ticTac[4],ticTac[5],ticTac[6],ticTac[7],ticTac[8]))

    elif playGame==2:
        print("Thankyou for being here :)")
        break
    else:
        print("Invalid Input! Enter Again!")

