class Question:
    def __init__(self, question_text, answer, multiple_choice_options=None, question_counter=None):
        self.question_text = question_text
        self.answer = answer
        self.multiple_choice_options = multiple_choice_options
        self.question_counter = question_counter
    def __repr__(self):
        return "{" + self.question_text +" , "+ self.answer +" , "+str(self.multiple_choice_options) +" , "+str(self.question_counter) +" }"

quiz_questions = [
    Question("Question 1. What is the capital city of Japan?", "Tokyo", ["Tokyo, Seoul, Shanghai or Fuji"], 1),
    Question("Question 2. Finish the phrase. The early bird catches the [blank]", "Worm", ["Spider, Elephant, Mosquito, Worm"], 2),
    Question("Question 3. Which actor plays Captain Jack Sparrow in the Pirates of the Carribean franchise?", "Johnny Depp", ["Orlando Bloom, George Clooney, Mark Whalberg, Johnny Depp"], 3),
    Question("Question 4. Paul McCartney was a member of which band?", "The Beatles", ["The Who, The Beatles, ELO, Metallica"], 4),
    Question("Question 5. What is the tallest mountain in the world?", "Mount Everest", ["Ben Nevis, Snowdonia, K2, Mount Everest"], 5),
    Question("Question 6. Which is the smallest country in the world?", "Vatican City", ["Vatican City, San Marino, Malta, Grenada"], 6),
    Question("Question 7, On average, how many million of miles is the Sun from the Earth", "93", ["101, 93, 86, 1025"], 7),
    Question("Question 8. In what year did Amy Winehouse pass away?", "2011", ["2001, 2005, 2013, 2011"], 8),
    Question("Question 9. What nationality is Avril Lavigne?", "Canadian", ["American, Canadian, British, Australian"], 9),
    Question("Question 10. Which treaty formally conclided the First World War in 1919?", "Treaty of Versailles", ["Treaty of Berlin, Treaty of Dublin, Treaty of Versailles, Treaty of Paris"], 10),
    Question("Question 11. In which year was the nation state of Germany established?", "1871", ["1845, 1789, 1864, 1871"], 11),
    Question("Question 12. Which UK Prime Minister served between 1916 and 1922?", "David Lloyd George", ["Stanley Baldwin, David Lloyd George, Winston Churchill, Bonar Law"], 12),
    Question("Question 13. What was the name of the assissin who killed Archduke Franz Ferdinand and his wife in Sarajevo in 1914?", "Gavrillo Princip", ["Gavrillo Princip, Leon Trotsky, Georgy Lvov, Nikolai Golitsyn"], 13),
    Question("Question 14. In what year were the first Academy Awards held?", "1929", ["1924, 1929, 1927, 1919"], 14),
    Question("Question 15. What are people with Alektorophobia afraid of?", "Chickens", ["Chickens, Geese, Ducks, Turkeys"], 15),
]

