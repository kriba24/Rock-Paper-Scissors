import random
humanInput = 0
botInput = 0
humanScore = 0
botScore = 0
while humanScore < 3 and botScore < 3:
    print('Your score: ' + str(humanScore))
    print('Bot score: ' + str(botScore))
    try:
        humanInput = int(input('Enter 1 for rock, 2 for scissors, and 3 for paper: '))
    except ValueError:
        print('That\'s not valid input! Try again')
    botInput = random.randint(1, 3)
    if humanInput < 1 or humanInput > 3:
        print('Try again! That\'s not valid input!')
        continue
    elif humanInput == 1:
        if botInput == 1:
            print('Tie!')
            continue
        elif botInput == 2:
            print('You win!')
            humanScore += 1
            continue
        else:
            print('You lose!')
            botScore += 1
            continue
    elif humanInput == 2:
        if botInput == 1:
            print('You lose!')
            botScore += 1
            continue
        elif botInput == 2:
            print('Tie!')
            continue
        else:
            print('You win!')
            humanScore += 1
            continue
    else:
        if botInput == 1:
            print('You win!')
            humanScore += 1
            continue
        elif botInput == 2:
            print('You lose!')
            botScore += 1
            continue
        else:
            print('Tie!')
            continue
print('Your score: ' + str(humanScore))
print('Bot\'s score: ' + str(botScore))
