class Hand:
    m_cards = []

    def add(self, card):
        self.m_cards.append(card)

    def clear(self):
        self.m_cards = []

    def get_total(self):
        return None         