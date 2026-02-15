"""
Name : Mburu Martin
Adm No : BSCIT-05-0167/2024
Function to sort list of words by length
"""

word_list = []
while True:
    wordList = input("Enter a string (or leave blank to finish) : ")
    if not wordList:
        break
    word_list.append(wordList)

#Function Definition
def sort_words_by_length(word_list):
    return sorted(word_list, key = len)

#Function Call
print(sort_words_by_length(word_list))
