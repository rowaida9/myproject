
class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        return f"{self.color} {self.value}"

class Deck:
    def __init__(self):
        colors = ['Red', 'Green', 'Blue', 'Yellow']
        values = ['0'] + [str(i) for i in range(1, 10)] * 2 + ['Skip', 'Reverse', 'Draw Two'] * 2
        self.cards = [Card(color, value) for color in colors for value in values]
        random.shuffle(self.cards)

    def draw_card(self):
        if self.cards:
            return self.cards.pop()
        return None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        card = deck.draw_card()
        if card:
            self.hand.append(card)

    def play_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
            return card
        return None

class Game:
    def __init__(self, player_names):
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]
        self.current_player_index = 0
        self.direction = 1  # 1 for clockwise, -1 for counter-clockwise
        self.start_game()

    def start_game(self):
        for player in self.players:
            for _ in range(7):
                player.draw(self.deck)

    def next_turn(self):
        self.current_player_index = (self.current_player_index + self.direction) % len(self.players)

    def play(self):
        # هنا يمكنك إضافة منطق اللعب وإدارة الأدوار وهكذا
        pass

         if __name__ == "__main__":
         player_names = ["Alice", "Bob", "Charlie"]
        game = Game(player_names)

















