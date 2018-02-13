import time
def ran():
                if x==['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']:
                    print(asm2 + ' winner')
                    time.sleep(5)
                    quit()
                    
                else:
                    print(asm1+' turn')
                                                                            #hina ana ba carete al player we al instraction bta3t player 1 
                    while True:   #while (b) #this while to make the user choose 1 or 2
                        if x==['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']:
                            break
                            
                        
                        print('how many number will you take 1 or 2 ?')
                        while True: #this while if the user was bad and think to put letter or word when i ask about number
                            a=str(input())
                            if a=='1' or a=='2':
                                break
                            print('Please Enter 1 or 2 only')
                   #here when the user enter 1                     
                        if a=='1':                
                            print(x)
                            print('choose the number from the list :')
                            while True : #we will called this while (R)     #this while  to make the user choose from the list not from his mind
                                i=int(input())
                                if i in x :
                                    break
                                print("please choose the number from the list ")
                            while x[i]=='.': #this while to not repeat the same num while playing         #we called this while (a)
                                print('please choose another number this number was taken')
                                i=int(input())
                                if x[i]!='.':
                                    x[i]='.'
                                    print(x)
                                    break     #the end of  wihle (a)
                            if x[i]=='.':
                                break        #the end of while (b)
                            x[i]='.'
                            print(x)
                            san()
                            break
                        #here when the user choose 2
                        elif a=='2':
                            print(x)
                            print('choose The First number : ')
                            while True : #This is while (R)    
                                i=int(input())
                                if i in x:
                                    break
                                print("Please Enter another Number (your choice was taken) ; ")
                            while True:
                                    h=int(input("Enter the secound number : "))
                                    if h in x:
                                        break
                                    print("Please Enter another Number (your choice was taken) :")
                            while True:
                                while (x[i]-x[h])==1 or (x[i]-x[h])==-1 or (x[h]-x[i])==1 or (x[h]-x[i])==-1:
                                        x[i]='.'
                                        x[h]='.'
                                        print(x)
                                        break
                                if x[i]=='.':
                                    
                                         san()
                                         break
                                print('this 2 number isn\'t adjcent number please enter new 2 number ')
                                print(x)
                                while True: #This is while (R)
                                        if x==['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']:
                                            break
                                        print('Do you want to change the number which you choose 1-yes 2-no')
                                        while True:
                                            i=str(input())
                                            if i=='1' or i=='2':
                                                break
                                            print("please choose 1 or 2 only")
                                        if i=='1':
                                            print(x)
                                            print('choose the number from the list :')
                                            while True : #we will called this while (R)     #this while  to make the user choose from the list not from his mind
                                                i=int(input())
                                                if i in x :
                                                    break
                                                print("please choose the number from the list ")
                                            while x[i]=='.': #this while to not repeat the same num while playing         #we called this while (a)
                                                print('please choose another number this number was taken')
                                                i=int(input())
                                                if x[i]!='.':
                                                    x[i]='.'
                                                    print(x)
                                                    break     #the end of  wihle (a)
                                            if x[i]=='.':
                                                break        #the end of while (b)
                                            x[i]='.'
                                            print(x)
                                            san()
                                        if i=='2':
                                            while True:
                                                i=int(input("Enter the first number : "))
                                                if i in x:
                                                    break
                                            while True:
                                                h=int(input("Enter the secound number : "))
                                                if h in x:
                                                    break
                                            while (x[i]-x[h])==1 or (x[i]-x[h])==-1 or (x[h]-x[i])==1 or (x[h]-x[i])==-1:
                                                x[i]='.'
                                                x[h]='.'
                                                print(x)
                                                break
                                            if x[i]=='.':
                                                break    
                                san()
                                break
def san():
                if x==['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']:   #hina nafs al instraction bta3t player 2 
                        print(asm1 +' winner')
                        time.sleep(5)
                        quit()
                else:    
                    print(asm2+' turn')
                    while True:   #while (b)
                        print('how many number will you take 1 or 2 ?')
                        while True: #this while if the user was bad and think to put letter or word when i ask about number
                            a=str(input())
                            if a=='1' or a=='2':
                                break
                            print('Please Enter 1 or 2 only')
                        if a=='1':
                            print(x)
                            print('choose the number from the list :')
                            while True : #while(R)
                                i=int(input())
                                if i in x :
                                    break
                                print("please choose the number from the list ")
                            while x[i]=='.':        #while (a)
                                print('please choose another number this number was taken')
                                i=int(input())
                                if x[i]!='.':
                                    x[i]='.'
                                    print(x)
                                    break     #the end of  wihle (a)
                            if x[i]=='.':
                                break        #the end of while (b)
                            x[i]='.'
                            print(x)
                            ran()
                            break
                        #here when the user choose 2
                        elif a=='2':
                            print(x)
                            print('choose The First number : ')
                            while True : #This is while (R)    
                                i=int(input())
                                if i in x:
                                    break
                                print("Please Enter another Number (your choice was taken) ; ")
                            while True:  
                                    h=int(input("Enter the secound number : "))
                                    if h in x:
                                        break
                                    print("Please Enter another Number (your choice was taken) :")
                            while True:
                                while (x[i]-x[h])==1 or (x[i]-x[h])==-1 or (x[h]-x[i])==1 or (x[h]-x[i])==-1:
                                        x[i]='.'
                                        x[h]='.'
                                        print(x)
                                        break
                                if x[i]=='.':
                                         ran()
                                         break
                                print('this 2 number isn\'t adjcent number please enter new 2 number ')
                                print(x)
                                while True: #This is while (R)
                                        if x==['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']:
                                            break
                                        print('Do you want to change the number which you choose 1-yes 2-no')
                                        while True:
                                            i=str(input())
                                            if i=='1' or i=='2':
                                                break
                                            print("please choose 1 or 2 only")
                                        if i=='1':
                                            print(x)
                                            print('choose the number from the list :')
                                            while True : #we will called this while (R)     #this while  to make the user choose from the list not from his mind
                                                i=int(input())
                                                if i in x :
                                                    break
                                                print("please choose the number from the list ")
                                            while x[i]=='.': #this while to not repeat the same num while playing         #we called this while (a)
                                                print('please choose another number this number was taken')
                                                i=int(input())
                                                if x[i]!='.':
                                                    x[i]='.'
                                                    print(x)
                                                    break     #the end of  wihle (a)
                                            if x[i]=='.':
                                                break        #the end of while (b)
                                            x[i]='.'
                                            print(x)
                                            san()
                                        if i=='2':
                                            while True:
                                                i=int(input("Enter the first number : "))
                                                if i in x:
                                                    break
                                            while True:
                                                h=int(input("Enter the secound number : "))
                                                if h in x:
                                                    break
                                            while (x[i]-x[h])==1 or (x[i]-x[h])==-1 or (x[h]-x[i])==1 or (x[h]-x[i])==-1:
                                                x[i]='.'
                                                x[h]='.'
                                                print(x)
                                                break
                                            if x[i]=='.':
                                                break    
                                ran()
                                break
x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]  #the program will start  from here  
print(x,'\n')
print("this game is very easy every player take one or two num but the num which taken will be like this '.' and who takes the final one or two num will win \n")
asm1=str(input('Enter the player 1 name : '))
asm2=str(input('Enter the player 2 name : '))
while x!=['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']: #this loop must be true  until all num finsh
        print('who will start 1- '+asm1,' or 2- '+asm2)
        while True:
            player=str(input('choose (1,2)  '))
            if player=='1' or player=='2' :
                break
            print('please Enter only 1 or 2 ')
  
        if player=='1':
            ran()
            
        elif player=='2':
            san()

            #enddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

