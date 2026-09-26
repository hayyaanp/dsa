def winner(erica, bob):

    erica_score = 0

    for index, value in enumerate(erica):
        if value == "E":
            erica_score += 1
        elif value == "M":
            erica_score += 3
        elif value == "H":
            erica_score += 5

    bob_score = 0

    for index, value in enumerate(bob):
        if value == "E":
            bob_score += 1
        elif value == "M":
            bob_score += 3
        elif value == "H":
            bob_score += 5

    return "Erica" if erica_score > bob_score else "Bob" if erica_score == bob_score else "Tie"