letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


#Build your Point Dictionary

letter_to_points = {a:b for a, b in zip(letters, points)}
#print(letter_to_points)

letter_to_points[" "] = 0

#Score a Word

def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
    return point_total

#brownie_points = score_word("BROWNIE")
#print(brownie_points)

#Score a Game

def player_to_words(game_history):
    player_to_points = {}
    for player, words in game_history.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points

    return player_to_points

game1_history = {"player1" : ['BLUE', 'TENNIS', 'EXIT'], "wordNerd" : ['EARTH', 'EYES', 'MACHINE'], "Lexi Con" : ['ERASER', 'BELLY', 'HUSKY'], "Prof Reader" : ['ZAP', 'COMA', 'PERIOD']}
#print(player_to_words(game1_history))


#play_word()

def play_word(player, word, game_history):
    game_history[player].append(word)
    print(player_to_words(game_history))

play_word("player1", "LEONARD", game1_history)