from random import randint


def wining_ticket_generator():
    return tuple([randint(1, 49) for _ in range(6)])


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
    return sorted(player_ticket)


print(player_ticket_generator())
