class Wordle:
    with open("words.txt") as file:
        words = file.read().splitlines() 
    sure = ["*","*","*","*","*"]
    half_letters = []
    unsure_pos = [[],[],[],[],[]]
    not_letters = []
    possible_words = []
    def Turn(self):
        self.possible_words.clear()
        for word in self.words:
            fits = True
            for i in range(5):
                if self.sure[i] != "*" and self.sure[i] != word[i]:
                    fits = False
                if word[i] in self.unsure_pos[i]:
                    fits = False
            if fits:
                self.possible_words.append(word)

        best_score = 0
        best_word = ""
        for word in self.possible_words:   
            score = 1
            for letter in self.half_letters:
                if word.count(letter) == 1:
                    score += 10
            for letter in word:
                if letter in self.not_letters:
                    score -= 100
            if score > best_score:
                best_score = score
                best_word = word
        print(best_word)
        return best_word
    
    def Play(self):
        print("What word did you play? ")
        word = input()
        while True:
            for i in range(len(word)):
                print(f"What did {word[i]} return? ")
                color = input()
                if color == "C":
                    self.sure[i] = word[i];
                elif color == "Y":
                    self.half_letters.append(word[i])
                    self.unsure_pos[i].append(word[i])
                elif color == "G":
                    self.not_letters.append(word[i])
            word = self.Turn()

wordle = Wordle()
wordle.Play()
