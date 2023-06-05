
import random

def generate():
    
    ores = ['ore'] * 5
    woods = ['wood'] * 6
    bricks = ['brick'] * 5
    sheeps = ['sheep'] * 6
    hays = ['hay'] * 6
    deserts = ['desert'] * 2

    resources = ores + woods + bricks + hays + deserts + sheeps

    random.shuffle(resources)


    board_resources = [
        ['-1', '-1', '-1', ' ', '-1', '-1', '-1'],
        ['-1', '-1', ' ', ' ', ' ', '-1', '-1'],
        ['-1', ' ', ' ', ' ', ' ', ' ', '-1'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],    
    ]

    for row in range(6):
        for column in range(7):
            if board_resources[row][column] != '-1':
                board_resources[row][column] = resources.pop()


    print("Resources:")
    for row in range(6):
        print(board_resources[row])
        

    board_tokens=[2,3,4,5,6,8,9,10,11,12,2,3,4,5,6,8,9,10,11,12]
    additional_tokens =[2,3,4,5,6,8,9,10,11,12]
    random.shuffle(additional_tokens)

    while len(board_tokens) < 28:
        board_tokens.append(additional_tokens.pop())



    board_numbers = [
        ['-1', '-1', '-1', '', '-1', '-1', '-1'],
        ['-1', '-1', ' ', ' ', ' ', '-1', '-1'],
        ['-1', ' ', ' ', ' ', ' ', ' ', '-1'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    ]


    for row in range(6):
        for column in range(7):
            if board_numbers[row][column] != '-1':
                if board_resources[row][column] != 'desert':
                    # print(f"Len: {len(board_tokens)} at {row} {column}")
                    board_numbers[row][column] = board_tokens.pop()

    print("----")
    print("Tokens:")
    for row in range(6):
        print(board_numbers[row])


generate()