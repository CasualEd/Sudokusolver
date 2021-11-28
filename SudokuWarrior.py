#list of 81 
Agnya=[]#Agnya is the log and represents the gradual filling of the grid the first part is the position the second is about the second guesses available and the third is the guess that has been done.

def sudokusolver(sud):
    #bannedpossibilities=[[] for i in range(81)]
    empty=[]
    Imp=[[] for i in range(27)]
    time=0           #1-9 for ligns 10-18 for colonns 19-27 for the squares
    def emptycheck():#checked should work
        empty=[]     #emptycheck first lists down all of the impossibilities for each empty sudoku case
        for i in range(9):#lign, column and square
            u=[]
            for j in range(9*i,9*(i+1)):
                if sud[j]!=0 and sud[j] not in u:
                    u.append(sud[j])
            Imp[i]=u
            u=[]
            for j in range(9):
                if sud[i+9*j]!=0 and sud[i+9*j] not in u:
                    u.append(sud[i+9*j])
            Imp[9+i]=u
            u=[]
            a=i%3
            for k in range(3):
                for j in range(27*(i//3)+a*3+9*k,27*(i//3)+a*3+9*k+3):#order for the square
                    if sud[j]!=0 and sud[j] not in u:#left to right up to down
                        u.append(sud[j])
            Imp[18+i]=u
        for i in range(81):#checking for the zeros check should function
            if sud[i]==0:
                imp=[]
                for j in Imp[i//9]:
                    if j not in imp and j!=0:
                        imp.append(j)
                        #print(1,i,j)
                for j in Imp[9+i%9] :
                    if j not in imp and j!=0:
                        imp.append(j)
                        #print(2,i,j)
                for j in Imp[18+(i//27)*3+(i%9)//3] :
                    if j not in imp and j!=0:
                        imp.append(j)
                        #print(3,i,j)
                empty.append([i,imp])#1 is position 2 is impossibilities
        return empty
    def guessin():#The fonction is used to guess if there is no other moves to be done
        a=0
        g=0
        for i in range(len(empty)): #Trying to find the square with the least possibilities
            if len(empty[i][1])>a:
                a=len(empty[i][1])
                g=i
        gwess=0
        while gwess in empty[g][1] and gwess<10: #Determining one of the possibilities for a square
            gwess+=1
        if len(empty[g][1])!=0:
            empty[g][1].pop()
        Agnya.append([empty[g][0],empty[g][1],gwess])
        sud[empty[g][0]]=gwess
    def Solver():#The function is used to fix up the sudoku by eliminating a preexisting guess and proceeds to the next one
        a=len(Agnya)-1
        while len(Agnya)!=0 and Agnya[a][1]==[]:
            sud[Agnya[a][0]]=0
            Agnya.pop()
            a=a-1
        if Agnya!=[]:
            gwess=Agnya[a][1].pop() 
            Agnya[a][2]=gwess
            sud[Agnya[a][0]]=gwess
    def Egnimatic():#This function tries to see if one particular case is the only that can have a certain value for a column,square and line
        tru=0
        l=len(Agnya)
        for i in range(9):
            Line=[]
            Squa=[]
            Cool=[]
            for j in range(len(empty)):
                if 9*i<=empty[j][0] and empty[j][0]<9*(i+1): #This puts all the empty squares on the same line in a same list
                    Line.append(empty[j])
                if empty[j][0]%9==i:#This puts all the empty squares on the same column in a same list
                    Cool.append(empty[j])
                if (empty[j][0]//27)*3+(empty[j][0]%9)//3==i: #This puts all the empty squares on the same square in a same list
                    Squa.append(empty[j])
            for j in range(len(Line)):
                Coos=[] #Coos represents for an element j all the impossibilities that all the other empty square on the same line have
                for k in range(1,10):
                    a=0
                    for c in range(len(Line)):
                        if c!=j and k not in Line[c][1]:
                            a=1
                            break
                    if a==0:
                        Coos.append(k)
                for k in range(1,10):
                    if k in Coos and k not in Line[j][1]: 
                        sud[Line[j][0]]=k
                        Agnya.append([Line[j][0],[],k])
            for j in range(len(Cool)):
                Coos=[]
                for k in range(1,10):
                    a=0
                    for c in range(len(Cool)):
                        if c!=j and k not in Cool[c][1]:
                            a=1
                            break
                    if a==0:
                        Coos.append(k)
                for k in range(1,10):
                    if k in Coos and k not in Cool[j][1]:
                        sud[Cool[j][0]]=k
                        Agnya.append([Cool[j][0],[],k])
            for j in range(len(Squa)):
                Coos=[]
                for k in range(1,10):
                    a=0
                    for c in range(len(Squa)):
                        if c!=j and k not in Squa[c][1]:
                            a=1
                            break
                    if a==0:
                        Coos.append(k)
                for k in range(1,10):
                    if k in Coos and k not in Squa[j][1]:
                        sud[Squa[j][0]]=k
                        Agnya.append([Squa[j][0],[],k])     
        # printer(sud)
        # f=input("Check ")
        if l==len(Agnya):
            tru=0
        else:
            tru=1
        return tru
                
    empty=emptycheck()             
    while len(empty)!=0: #Program doesn't stop until the sudoku is filled
        Error=0    #Error is a variable used to indicate when the guess was wrong
        t=0
        Arrangements=[]
        for i in range(len(empty)):#Checking all the squares to see who has only one possibility
            if len(empty[i][1])==8:
                Arrangements.append(i)
                t=1
        for j in range(1,len(Arrangements)):
            while j>0 and Arrangements[j-1]<Arrangements[j]:
                (Arrangements[j-1],Arrangements[j])=(Arrangements[j],Arrangements[j-1])
        for i in Arrangements:
            gwess=1
            if i<len(empty):
                while gwess in empty[i][1] and gwess<10:
                    gwess+=1
                Agnya.append([empty[i][0],[],gwess])
                sud[empty[i][0]]=gwess #Updating the sudoku 
        
        empty=emptycheck()
        a=Egnimatic()  #Tries to see if one particular case is the only that can have a certain value for a column,square and line
        empty=emptycheck()
        print(a)
        if a==0 and len(empty)!=0:#If nothing happened the algorithm starts testing out all the possibilities with guessin
            time+=1
            guessin()
            empty=emptycheck()
            print(time)
            
        for i in range(len(empty)): #Check if there is any incoherences in the sudoku
            if len(empty[i][1])==9:
                Error=1
        if Error==1:
            Solver()
    for i in range(9):
        # print('C'est terminé')
        print("[ ",sud[9*i]," ",sud[9*i+1]," ",sud[9*i+2]," ] [ ",sud[9*i+3]," ",sud[9*i+4]," ",sud[9*i+5]," ] [ ",sud[9*i+6]," ",sud[9*i+7]," ",sud[9*i+8]," ]")
        
            
                
        
#if bannedpossibilities[i]!=[] and bannedpossibilities[i][0]<len(Agnya) and j in bannedpossibilities[i][1]:
#To implement in line 35 if bannedpossibilities are used 
ezlife=[1,0,0,0,6,0,8,0,9,0,6,3,0,2,0,0,5,0,0,8,0,0,0,0,0,0,1,0,0,0,4,0,0,5,0,8,0,0,7,8,0,1,2,4,0,0,2,0,0,0,0,0,0,0,0,0,2,3,0,0,0,0,4,8,4,9,0,1,6,0,3,0,0,3,0,9,4,0,0,8,0]

e=[1,7,4,5,6,3,8,2,9,9,6,3,1,2,0,4,5,7,2,8,5,7,0,0,3,6,1,6,0,1,4,3,2,5,0,8,3,0,7,8,0,1,2,4,6,4,2,8,6,0,0,0,0,3,0,0,2,3,0,0,6,0,4,8,4,9,2,1,6,7,3,5,0,3,6,9,4,0,0,8,2]
r=[2,8,0,6,4,1,3,9,5,1,6,9,5,7,3,8,2,4,3,4,5,8,0,9,6,7,1,9,2,6,1,5,4,7,3,8,7,1,3,9,8,2,5,4,6,4,5,8,7,3,6,9,1,2,5,7,1,2,9,8,4,6,3,8,3,2,4,6,7,1,5,9,6,9,4,3,0,5,2,8,7]
ens=[0,0,6,0,0,0,0,0,0,0,0,2,4,0,0,0,0,0,0,0,0,0,6,7,0,9,0,0,6,4,0,0,0,0,0,0,8,0,0,3,0,0,4,0,1,0,5,0,0,0,2,9,3,0,1,0,0,0,0,0,0,6,0,0,0,0,2,0,8,7,1,0,0,0,8,0,0,0,0,0,0]
impossible=[0 for i in range(81)]


def printer(sud):
    for i in range(9):
        print("[ ",sud[9*i]," ",sud[9*i+1]," ",sud[9*i+2]," ] [ ",sud[9*i+3]," ",sud[9*i+4]," ",sud[9*i+5]," ] [ ",sud[9*i+6]," ",sud[9*i+7]," ",sud[9*i+8]," ]")
