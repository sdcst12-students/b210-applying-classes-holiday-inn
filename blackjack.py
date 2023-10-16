class game:
    def createDeck(self):
        ranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
        suits = ['C','D','H','S']
        deck = []
        for rank in ranks:
            for suit in suits:deck.append(rank+suit)
        self.deck = deck
        #print(deck)
        #print(self.deck)
    
    def value(self,hand):
        val1 = 0
        val2 = 0
        namecards = ['A', 'K', 'Q', 'J', 'T']
        for i in range(0,len(hand)):
            if hand[i][0] not in namecards:
                val1 = val1 + int(hand[i][0])
                val2 = val2 + int(hand[i][0])


            elif hand[i][0] == 'A':
                val1 +=1
                val2 += 11


            elif hand[i][0] == 'Q' or hand[i][0] == 'K' or hand[i][0] == 'T' or hand[i][0] == 'J':
                val1 += 10
                val2 += 10
            return val1 if val1 ==val2 else [val1,val2]

    def bust(self,value):
        return True if value > 21 else False
    def dealer(self):
        dealer = []
        score = 0
        while True:
            dealer.append(self.deck[0])


            try:
                self.deck.pop(0)
                if (self.value(dealer)) > 16:
                    score = self.value(dealer)
                    break
           
            except:
                if self.value(dealer)[0] > 16:
                    score = self.value(dealer)[0]
                    break


                elif self.value(dealer)[1] > 16:
                    score = self.value(dealer)[1]
                    break


        return [ dealer , score , self.deck ]

    def main(self):
        import random
        unshuf = self.createDeck()
        deck = random.shuffle(unshuf)
        outputs = self.dealer(deck)
    def __init__(self):
        self.createDeck()
        print(self.dealer())
        pass
    


        

g=game()
