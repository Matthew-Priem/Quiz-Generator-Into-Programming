def palindromes(words):
    result = {"palindrome": [], "non-palindrome": []}
    
    reversed_word = ''
    for word in words:        
        #reverse the word and check if it is the orginal word
        for letter in word:
            reversed_word = letter + reversed_word
            if reversed_word == word:
                result["non-palindrome"].append(word)
            else:
                result["palindrome"].append(word)
    
    return result