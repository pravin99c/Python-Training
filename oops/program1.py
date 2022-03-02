# 1. Take the word and its meaning as input from the user.
# Create a class named flashcard, use the __init__() function to assign values for Word and Meaning.
# -> Now use the __str__() function to return a string that contains the word and meaning.
# -> Store the returned strings in a list named flash.
# -> Use a while loop to print all the stored flashcards.
# -> Add proper error handling
# 		-> Result image is attached in thread


import string



class flashcard():
    def __init__(self, word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return str(self.word)+','+str(self.meaning)
while True:
    try:
        print("Welcome to flashcard application ")
        string_list=[]
        val=0
        while val==0:
            try:
        
                name_word=flashcard(str(input("Enter tha name you want to add to flashcard : ")),str(input("Enter the meaning of the word : ")))
                string_list.append(name_word)
            except:
                raise
            else:
                val=int(input("Enter 0 add another flashcard and 1 to exit : "))
                if val==1:
                    i=0
                    while len(string_list)!=0:
                        print(string_list[i])
                        i +=1
                elif val>1:
                    break
    except Exception as e:
        print(e)
        break
    
