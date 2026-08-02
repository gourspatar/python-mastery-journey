class Playlist:
    def __len__(self):
        return 10


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __eq__(self, other):
        return self.score == other.score    # Output Is Always Boolean...


playlist = Playlist()

print(len(playlist))


player1 = Player("Gour", 100)
player2 = Player("Rahul", 100)
player3 = Player("Amit", 50)

print(player1 == player2)
print(player1 == player3)