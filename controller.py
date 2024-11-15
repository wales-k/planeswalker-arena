pOnePool = 20
pTwoPool = 20

pOneTox = 0
pTwoTox = 0

def p1_mod_health(add_to=False, sub_to=False):
    global pOnePool

    # Modify health pool values based on parameters
    if add_to:
        pOnePool += 1
        print(f"pOnePool GLOBAL has increased to ", pOnePool)
    elif sub_to:
        pOnePool -= 1

    # Check for a win condition
    winner = win_check()
    if winner:
        print(f"{winner} wins!")
        return pOnePool, winner  # Return pool values and winner for debugging

    return pOnePool
def p2_mod_health(add_to=False, sub_to=False):
    global pTwoPool

    # Modify health pool values based on parameters
    if add_to:
        pTwoPool += 1
        print(f"pTwoPool GLOBAL has increased to ", pTwoPool)
    elif sub_to:
        pTwoPool -= 1

    # Check for a win condition
    winner = win_check()
    if winner:
        print(f"{winner} wins!")
        return pTwoPool, winner  # Return pool values and winner for debugging

    return pTwoPool

def p1_mod_tox(add_to_p1=False, sub_to_p1=False):
    global pOneTox

    # Modify toxicity pool values based on parameters
    if add_to_p1:
        pOneTox += 1
        print(f"pOneTox GLOBAL has increased to ", pOneTox)

    elif sub_to_p1:
        pOneTox -= 1

    # Check for a win condition based on toxicity
    winner = win_check()
    if winner:
        print(f"{winner} wins!")
        return pOneTox, winner  # Return toxicity values and winner for debugging

    return pOneTox # Return both toxicity values if no winner

def p2_mod_tox(add_to_p2=False, sub_to_p2=False):
    global pTwoTox

    # Modify toxicity pool values based on parameters
    if add_to_p2:
        pTwoTox += 1
        print(f"pTwoTox GLOBAL has increased to ", pTwoTox)
    elif sub_to_p2:
        pTwoTox -= 1

    # Check for a win condition based on toxicity
    winner = win_check()
    if winner:
        print(f"{winner} wins!")
        return pOneTox, winner  # Return toxicity values and winner for debugging

    return pTwoTox # Return both toxicity values if no winner

def win_check():
    # Check health pools for win condition
    if pOnePool <= 0:
        return "Player Two"
    elif pTwoPool <= 0:
        return "Player One"
    
    # Check toxicity levels for win condition
    if pOneTox >= 10:
        return "Player Two"
    elif pTwoTox >= 10:
        return "Player One"
    
    return None  # No winner yet

def reset_values(reset=False):
    global pOnePool, pTwoPool, pOneTox, pTwoTox

    print("before", pOnePool, pTwoPool, pOneTox, pTwoTox)
    pOnePool = 20
    pTwoPool = 20
    pOneTox = 0
    pTwoTox = 0
    print("after", pOnePool, pTwoPool, pOneTox, pTwoTox)