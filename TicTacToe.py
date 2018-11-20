coord = {'A1': ' ', 'A2': ' ', 'A3': ' ', 'B1': ' ', 'B2': ' ', 'B3': ' ', 'C1': ' ', 'C2': ' ', 'C3': ' '}
#ans=['B2','C3','C1','C5','A3','B3','B1','44','A2','C2','+2','A1']
state=1 #to check whether player put proper position 
#count=0
t=0 # count turn
p="O"

Game=0 
"""
game state. 
Running =0 | Win=1 | Draw=-1 
"""

def print_board() :
    print("  │A │B │C │")
    print("─┼─┼─┼─┤")
    print("1 │" + coord['A1'] + " │" + coord['B1'] + " │" + coord['C1'] + " │")
    print("─┼─┼─┼─┤")
    print("2 │" + coord['A2'] + " │" + coord['B2'] + " │" + coord['C2'] + " │")
    print("─┼─┼─┼─┤")
    print("3 │" + coord['A3'] + " │" + coord['B3'] + " │" + coord['C3'] + " │")
    print("─┴─┴─┴─┘")

print_board()

def Move(state,input_coor):
    global t
    #print("Move state : %s" %state)
    if state==1:
        for val in coord.keys():
            if input_coor in val:
                if t%2==0:
                    coord[input_coor] = "O"
                    
                else:
                    coord[input_coor] = "X"
                    
    else:
        t=t-1
        
def check_win():
    global Game
    if(coord['A1'] == coord['B1'] and coord['B1'] == coord['C1'] and coord['A1']!=" "):
        Game=1
    elif(coord['A2'] == coord['B2'] and coord['B2'] == coord['C2'] and coord['A2']!=" "):
        Game=1
    elif(coord['A3'] == coord['B3'] and coord['B3'] == coord['C3'] and coord['A3']!=" "):
        Game=1
    elif(coord['A1'] == coord['A2'] and coord['A2'] == coord['A3'] and coord['A1']!=" "):
        Game=1
    elif(coord['B1'] == coord['B2'] and coord['B2'] == coord['B3'] and coord['B1']!=" "):
        Game=1
    elif(coord['C1'] == coord['C2'] and coord['C2'] == coord['C3'] and coord['C1']!=" "):
        Game=1
    elif(coord['A1'] == coord['B2'] and coord['B2'] == coord['C3'] and coord['A1']!=" "):
        Game=1
    elif(coord['A3'] == coord['B2'] and coord['B2'] == coord['C1'] and coord['A3']!=" "):
        Game=1
    elif(coord['A1']!=" " and coord['A2']!=" " and coord['A3']!=" " and coord['B1']!=" " and coord['B2']!=" " and coord['B3']!=" " and coord['C1']!=" " and coord['C2']!=" " and coord['C3']!=" "):
        Game=-1
    else:
        Game=0
"""        
def Check_Empty(input_coor):
    if(coord[input_coor]==' '):
        return True
    else:
        print("")
        return False
"""

def Condition(input_coor):
    global state
    
    x=input_coor[0]
    y=input_coor[1]
    
    if not x.isalpha():
        print("You input wrong value. You must input a alphabet for X.")
        state=0
    elif x not in 'ABC':
        print("You input wrong value. Your input value for X must between A to C.")
        state=0
    elif not y.isdigit():
        print("You input wrong value. You must input a numeric value for Y.")
        state=0
    elif int(y) not in range(1, 4):
        print("You input wrong value. Your input value for Y must between 1 to 3.")
        state=0
    elif coord[input_coor]!=" ":
        print("You input already taken. Choose another Empty space")
        state=0 
    else: 
        state=1
    #print("Cond state : %s" %state)
    return state

while(Game==0):
    
    if(t%2==0):
        print("It's O's turn!")
        p="O"
    else:
        print("It's X's turn!")
        p="X"
        
    input_coor=input("Input coordinate for new marker: ")
    #input must be have value of x axis A~C and y axis 1~3
    """ 
    for x in ans:
        input_coor=x
    """  
    Condition(input_coor)
    Move(state,input_coor)
    print_board()
    #print(input_coor)
    t=t+1
    check_win()
    
    #print(t)
    
    if(Game==-1):
        print("Draw!")
    elif(Game==1):
        if(p=="O"):    
            print("O is win!")    
        else:    
            print("X is win!") 
    """
    else:
        print("N")
    """        
    #print("Game : %d "%Game)
