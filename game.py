import numpy as np
import pandas as pd
from grid import generate_grid
from display import highlight_cell

def run_game():
    
    array = generate_grid()
    df = pd.DataFrame(array, columns=['C1','C2','C3','C4','C5','C6'], index=['R1','R2','R3','R4','R5','R6'])
    df = df.astype("str")
    
    print("\n menu")
    print("level 1 : easy")
    print("level 2 : medium")
    print("level 3 : hard")
    name = input("enter your name : ")
    level = int(input("enter the level : "))


    match level:
        case 1:
            n = 3
            max_attempts = 10
        case 2:
            n = 4
            max_attempts = 15
        case 3 :
            n = 5
            max_attempts = 20
        case _:
            print("invalid level")
            exit()

    target_row = np.random.choice(df.index,n)
    target_col = np.random.choice(df.columns,n)

    array = np.stack([target_row,target_col],axis=1)
    correct_answer = []
    for row,col in array:
        #print(f" Row : {row} and col : {col}")
        correct_answer.append((row,col,df.loc[row,col]))
        df.loc[row,col] = " "
    print()
    # print("-"*20)

    # print(correct_answer)
    sodu_style = highlight_cell(df)
    # to get the player choice of row and col and check if the answer is correct or not
    print(df.to_string())
    print("-"*20)
    attempts = 0
    while len(correct_answer) > 0 and attempts < max_attempts:
        attempts += 1
        user_row = input("enter the row (R1-R6): ").upper()
        user_col = input("enter the col (C1-C6): ").upper()
        user_guess = int(input("enter the guess: "))
        if (user_row,user_col,str(user_guess)) in correct_answer:
            print(f"correct answer {name} (attempt left : {max_attempts - attempts})")
            correct_answer.remove((user_row,user_col,str(user_guess)))
            df.loc[user_row,user_col] = user_guess
            sodu_style = highlight_cell(df)
            print(df.to_string())
            print("-"*20)
        else:
            print(f"wrong answer {name} (attempt left : {max_attempts - attempts})")
            print(df.to_string())
            print("-"*20)
    print("-"*20)
    if len(correct_answer) == 0:
        print("you have won the game")
    else:
        print("you have lost the game and the correct answer is : ")
        for row, col, value in correct_answer:
            print(f" Row : {row} and col : {col} and the value is : {value}")

if __name__ == "__main__":
    run_game()
