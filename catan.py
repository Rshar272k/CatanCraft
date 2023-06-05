import pyscript
import random
from js import document


def generate_board():
    
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

    return board_resources, board_numbers


def generate_row(row_num, board_resources, board_numbers):

    print(f"Numbers: {board_numbers}")
    row_cards_html = ""
    for i in range(len(board_resources)):
        resource = board_resources[i]
        number = board_numbers[i]
        if resource == '-1':
            continue
        row_cards_html += f'<img class="tile" src="{resource}.png" alt="{resource} Tile">\n'
        row_cards_html += f'<div class="text-overlay"><p class="text-overlay-text">{number}</p></div>'
    
    
    print("---")
    print(row_cards_html)
    if row_num % 2 == 0:
        # Even row
        return f"""
        <div class="row">
                {row_cards_html}
        </div>
        """
    else:
        # Odd row
        return f"""
        <div class="row odd-row">
            {row_cards_html}
        </div>
        """

def generate():
    """Generates a random board"""
    print("Generating board 123...")

    output_div = document.querySelector("#output")

    board_resources, board_numbers = generate_board()
    new_board = ""
    row = 0
    for row in range(7):
        row_resources = []
        row_numbers = []

        for x in board_resources:
            row_resources.append(x[row])
        
        for x in board_numbers:
            row_numbers.append(x[row])
        
        print(f"Row resources: {row_numbers}")
        new_board += generate_row(
            row_num=row,
            board_resources=row_resources,
            board_numbers=row_numbers
        )
        row+=1
    
    output_div.innerHTML = new_board

    # pyscript.write("output", "you clicked the button")
    return "Board generated"