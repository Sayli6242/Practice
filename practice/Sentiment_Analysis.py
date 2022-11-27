"""
- Analyse user review for movie and provide users sentiment
- Create a dictionary of reaction words
- Each word has a sentiment score
- bag_of_words = {"happy":1, "laugh":1, "recommend":1, "great" :2, "love":2,
                "wonderful":2, "not":-1, "shocking":-1, "sad":-2, "crash":-2,
                 "pathetic":-2, "waste":-3 }

- Take user input (**1 complete sentence**), ex as below
- This movie is complete waste of time, would not recommend
- **Split the string by space** to get the words and check if word exists in dictionary.
- If word **present** in dictionary **add the sentiment score** to a variable. if word is not present in dict do nothing
- After analysing all (**loop complete**) the words print overall sentiment score
- if sentiment score is negative value print “Bad movie”
- if sentiment score is positive value print “Good movie”

 # ex This movie is complete waste of time, would not recommend
 # This above sentence has 3 words from dictionary
 # **waste**, **not**, **recommend** 
 # scores for these words are -3, -1 and 1.
 # adding these 3 we get -3 
 - Output should be `Bad moview`

 1) take user input as string.
 2) split string and store in a list.
 3) compare split words in list with key in dict.
 4) If split word is present increse count of word.(maintain sentiment score)
 5) after analysing all words calculate all count.
 7) If score is negetive print 'Bad Movie'.
 8) If score is positive print 'Good Movie'.

"""
def sentiment_analysis(bag_of_words):
    sentiment_score = 0
    # take sentence as input
    input_sentence = input('Enter feedback of movie: ')
    spliting_text = input_sentence.split()
    # print(spliting_text)
    # iterate list to get each word
    for word in spliting_text:
        # print(word)
        # check word present in dictionary
        if word in bag_of_words.keys():
            # sentiment_score = bag_of_words[word] 
            # increse count of word
            sentiment_score = sentiment_score + bag_of_words[word]
    if sentiment_score >= 0:
        print('Good Movie')
    else: 
        print('Bad Movie')
        
        
            

def main():
    bag_of_words = {"happy":1, "laugh":1, "recommend":1, "great" :2, "love":2,
                "wonderful":2, "not":-1, "shocking":-1, "sad":-2, "crash":-2,
                 "pathetic":-2, "waste":-3 }
    
    score = sentiment_analysis(bag_of_words)
main()