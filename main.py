from random import randint


# function generates 6 wining numbers from range 1 to 49
def wining_ticket_generator():
    win_ticket = [randint(1, 49) for _ in range(6)]
    print(win_ticket)
    return win_ticket


# functions asks user for 6 numbers
def player_ticket_generator():
    player_ticket = []
    while len(player_ticket) < 6:
        try:
            player_number = int(input('Player number: '))
        except ValueError:
            print('your must be an integer.')
            continue
        if player_number < 1 or player_number > 49:
            print('Player number must be between 1 and 49.')
            continue
        if player_number in player_ticket:
            print('this number is already in ticket.')
            continue
        player_ticket.append(player_number)
    player_ticket.sort()
    print(player_ticket)
    return player_ticket


# function uses funtcions: player_ticket_generator and wining_ticket_geerator and makes diff on both sets
def game():
    player_ticket = set(player_ticket_generator())
    win_ticket = set(wining_ticket_generator())
    print(f'you guessed {len(player_ticket & win_ticket)} numbers')


game()
