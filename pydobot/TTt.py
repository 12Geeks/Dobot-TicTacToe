import time
from random import *
from glob import glob

from dobot import *

# Varables
Groundlevel = -36
current_player = 1
p1_sq = set()
p2_sq = set()
COM_sq = set()
win_sequence = set()
Avaliable = [1,2,3,4,5,6,7,8,9]
drawn_sq = 0
end = False

win_sequence = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {7, 5, 3}]

# Connecting to dobot
available_ports = glob('/dev/cu*usb*')  # mask for OSX Dobot port
if len(available_ports) == 0:
    print('no port found for Dobot Magician')
    exit(1)

device = Dobot(port=available_ports[0])


def return_home():
    device.jump(200, 10 , Groundlevel+30)

# init function
def init_draw():
    print("Game initialising...\nPlease Wait...")
    device.jump(225.0, 0.0, Groundlevel)
    device.go(225.0, 75, Groundlevel)
    device.jump(250.0, 0.0, Groundlevel)
    device.go(250.0, 75, Groundlevel)
    device.jump(200.0, 25, Groundlevel)
    device.go(275, 25, Groundlevel)
    device.jump(200, 50, Groundlevel)
    device.go(275, 50, Groundlevel)
    device.jump(200, 0 , Groundlevel+30)
    print("Game Loaded. \nPlease select 1 - 9. \nP1 Gets circle shape and P2 gets a cross.")

# Draw function
def Draw_shape(sq_num, shape):
    x, y = None, None
    # go to square postion
    if sq_num == 1:
        device.jump(205, 5, Groundlevel)
        x, y = 205, 5
    elif sq_num == 2:
        device.jump(230, 5, Groundlevel)
        x, y = 230, 5
    elif sq_num == 3:
        device.jump(255, 5, Groundlevel)
        x, y = 255, 5
    elif sq_num == 4:
        device.jump(205, 30, Groundlevel)
        x, y = 205, 30
    elif sq_num == 5:
        device.jump(230, 30, Groundlevel)
        x, y = 230, 30
    elif sq_num == 6:
        device.jump(255, 30, Groundlevel)
        x, y = 255, 30
    elif sq_num == 7:
        device.jump(205, 55, Groundlevel)
        x, y = 205, 55
    elif sq_num == 8:
        device.jump(230, 55, Groundlevel)
        x, y = 230, 55
    elif sq_num == 9:
        device.jump(255, 55, Groundlevel)
        x, y = 255, 55

    # Draw the shape
    if shape == "circle":
        y += 5
        device.jump(x, y, Groundlevel)
        device.go(x, y+2.5, Groundlevel)
        device.go(x+5.303, y+2.5+5.303, Groundlevel)
        device.go(x+5.303+5, y+2.5+5.303, Groundlevel)
        device.go(x+5.303+5+5.303, y+2.5, Groundlevel)
        device.go(x+5.303+5+5.303, y-2.5, Groundlevel)
        device.go(x+5.303+5, y-2.5-5.303, Groundlevel)
        device.go(x+5.303, y-2.5-5.303, Groundlevel)
        device.go(x, y-2.5, Groundlevel)
        device.go(x, y+1, Groundlevel)

    elif shape == "cross":
        device.go(x+15, y+15, Groundlevel)
        device.jump(x, y+15, Groundlevel)
        device.go(x+15, y, Groundlevel)

def Computer_AI():
    # Check computer win moves
    COM_sq_testing = COM_sq.copy()
    for i in range(1,10):
        if i in Avaliable:
            COM_sq_testing.add(i)
            print(COM_sq_testing)
            if move_check(COM_sq_testing) == True:
                return i
            else:
                COM_sq_testing.remove(i)
                
    # Check Player win moves
    p1_sq_testing = p1_sq.copy()
    for i in range(1,10):
        if i in Avaliable:
            p1_sq_testing.add(i)
            print(p1_sq_testing)
            if move_check(p1_sq_testing) == True:
                return i
            else:
                p1_sq_testing.remove(i)

     # Play center
    if 5 in Avaliable:
        return 5
    
    # Play a corner
    corner = [1, 3, 7, 9]
    shuffle(corner)
    for i in corner:
        if i in Avaliable:
            return i

    #Play a side
    side = [2, 4, 6, 8]
    shuffle(side)
    for i in side:
        if i in Avaliable:
            return i

def move_check(squares):
    winning = False
    for sequence in win_sequence:
        for num in sequence:
            if num not in squares:
                winning = False
                break
            else:
                winning = True
        if winning == True:
            return winning

def end_game(squares, name):
    isEnd = False
    # For draw
    if Avaliable == []:
        isEnd = True
        print("draw")
        return(end)

    # For winning
    for sequence in win_sequence:
        for num in sequence:
            if num not in squares:
                isEnd = False
                break
            else:
                isEnd = True
        if isEnd == True:
            # Draw the winning line
            if sequence == win_sequence[0]:
                device.jump(200, 12.5, Groundlevel)
                device.go(275, 12.5, Groundlevel)
                print("Done 1")
            if sequence == win_sequence[1]:
                device.jump(200, 37.5, Groundlevel)
                device.go(275, 37.5, Groundlevel)
                print("Done 2")
            if sequence == win_sequence[2]:
                device.jump(200, 62.5, Groundlevel)
                print("Done 3")
                device.go(275, 62.5, Groundlevel)
            if sequence == win_sequence[3]:
                device.jump(212.5, 0, Groundlevel)
                device.go(212.5, 75, Groundlevel)
                print("Done 4")
            if sequence == win_sequence[4]:
                device.jump(237.5, 0, Groundlevel)
                device.go(237.5, 75, Groundlevel)
                print("Done 5")
            if sequence == win_sequence[5]:
                device.jump(262.5, 0, Groundlevel)
                device.go(262.5, 75, Groundlevel)
                print("Done 6")
            if sequence == win_sequence[6]:
                device.jump(275, 75, Groundlevel)
                device.go(200, 0, Groundlevel)
                print("Done 7")
            if sequence == win_sequence[7]:
                device.jump(200, 0, Groundlevel)
                device.go(275.5, 75, Groundlevel)
                print("Done 8")

            return_home()
            print(name + " Won. ")

            break

    return(isEnd)

# Main code
init_draw()
return_home()
vs = input("Computer(1)/Human(2): ")
while end != True:
    # player 1
    if current_player == 1 and Avaliable != []:
        shape = input("player 1: ")
        try:
            shape = int(shape)
            if shape in Avaliable:
                p1_sq.add(Avaliable.pop(Avaliable.index(shape)))

                if vs == "1":
                    current_player = 3
                else:
                    current_player = 2

                Draw_shape(shape, "circle")
                return_home()
                drawn_sq += 1
                print(p1_sq)
                print(COM_sq)
                end = end_game(p1_sq, "Player 1 ")
                print(Avaliable)
                print(end)

                if end == True:
                    print("ended")
                    break

            else:
                print("Area Occupied...")
        except:
            print("Input Not A Number...")

    # player 2
    elif current_player == 2 and Avaliable != []:
        shape = input("player 2: ")
        try:
            shape = int(shape)
            if shape in Avaliable:
                p2_sq.add(Avaliable.pop(Avaliable.index(shape)))
                current_player = 1
                Draw_shape(shape, "cross")
                return_home()
                drawn_sq += 1

                end = end_game(p2_sq, "Player 2 ")
                if end == True:
                    print("ended")
                    break
            else:
                print("Area Occupied...")
        except:
            print("Input Not A Number...")

    # Computer 3
    elif current_player == 3 and Avaliable != []:
        shape = Computer_AI()
        print(shape)
        COM_sq.add(Avaliable.pop(Avaliable.index(shape)))
        current_player = 1
        Draw_shape(shape, "cross")
        return_home()
        drawn_sq += 1
        print(COM_sq)
        print(p1_sq)
        print(Avaliable)
        
        end = end_game(COM_sq, "Computer ")
        print(end)
        if end == True:
            print("ended")
            break

    else:
        print("Draw.\nended")
        break
    
