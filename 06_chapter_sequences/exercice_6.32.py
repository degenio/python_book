team = []

def enter_player():
    name = input('Enter the player name: ')
    code = input('Enter the player code: ')
    goals = int(input('Enter the number of goals: '))
    assists = int(input('Enter the number of assists: '))
    team.append({'name': name, 'code': code, 'goals': goals, 'assists': assists})

def display_statistics():
    # Average goals
    goals = [x['goals'] for x in team]
    average_goals = sum(goals) / len(goals)
    print('Average goals: {:7.2f}'.format(average_goals))
    # Average assists
    assists = [x['assists'] for x in team]
    average_assists = sum(assists) / len(assists)
    print('Average assists: {:7.2f}'.format(average_assists))
    # Number of players with goals less than the average
    goals_below_average = len([x for x in team if x['goals'] < average_goals])
    print('Number of players with goals below the average: {}'.format(goals_below_average))
    # Number of players with assists greater than or equal to the average
    assists_above_average = len([x for x in team if x['assists'] >= average_assists])
    print('Number of players with assists above or equal to the average: {}'.format(assists_above_average))
    return goals, assists

def calculate_efficiency(goals, assists):
    for player in team:
        # Calculate efficiency
        player['efficiency'] = (0.6 * player['goals'] / sum(goals)) + (0.4 * player['assists'] / sum(assists))

def select_players(threshold):
    for player in team:
        if player['efficiency'] > threshold:
            print('Player {} with code {} will be kept!'.format(player['name'], player['code']))
        else:
            print('Player {} with code {} will not be kept!'.format(player['name'], player['code']))


def main():
    player_count = int(input('Enter the number of players: '))
    i = 0
    while i < player_count:
        enter_player()
        i += 1
    # Display statistics
    goals, assists = display_statistics()
    threshold = float(input('Enter the threshold for keeping players: '))
    calculate_efficiency(goals, assists)
    select_players(threshold)

if __name__ == '__main__':
    main()
