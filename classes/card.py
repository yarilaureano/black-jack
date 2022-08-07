rank = range(1, 14)
suit = ('clubs', 'diamonds', 'hearts', 'spades')


class Card:

    m_rank = None
    m_suite = None
    m_is_face_up = False

    def get_value(self):
        return None

    def flip(self):
        self.m_is_face_up  = not self.m_is_face_up  