import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han (JS edition)

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

NEW RULES FOR THIS ASSIGNMENT:
- The house takes a 12% fee on winnings.
- BONUS: If the total of the dice is 2 or 7, you immediately gain +10 mon!
''')

purse = 5000

while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('js: ').strip()
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break  # valid bet

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('js: ').strip().upper()
        if bet not in ('CHO', 'HAN'):
            print('Please enter either "CHO" or "HAN".')
            continue
        break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # BONUS: total equals 2 or 7
    if total in (2, 7):
        print(f'BONUS! The total was {total}. You gain +10 mon.')
        purse += 10

    # Determine if the player won:
    rollIsEven = (total % 2 == 0)
    correctBet = 'CHO' if rollIsEven else 'HAN'
    playerWon = (bet == correctBet)

    # Display the bet results:
    if playerWon:
        print(f'You won! You take {pot} mon.')
        purse += pot
        fee = (pot * 12) // 100  # 12% house fee (integer math)
        print(f'The house collects a {fee} mon fee (12%).')
        purse -= fee
    else:
        purse -= pot
        print('You lost!')

    # Check if the player has run out of money:
    if purse <= 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
