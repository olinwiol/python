def fox():
    init()
    game_loop()
    credit()

def init():
    variables = {
        "difficulty": {
            "easy": "1",
            "medium": "2",
            "hard": "3",
        },
        "ranked": {
            "false": False,
            "true": True,
        },
    }

    print("Difficulty\n")
    while True:
        try:
            user_input = input("Choose difficulty level: ").lower()
            variables["difficulty"] = variables["difficulty"][user_input]
            break
        except KeyError:
            print("Invalid input. Please choose from 'easy', 'medium' or 'hard'.")

    return variables

def game_loop():
    return

def credit():
    return


fox()
