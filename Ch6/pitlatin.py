# if a word starts with a vowel the word yay is added
# else the consonant is moved at the end followed by ay

print('Enter the English Message')
message = input()
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = []
for word in message.split():
    # separate non-letters at start of this word
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    # separate non-letters at end of this word
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]
    
    # remember if the word was in uppercase or titlecase
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    word = word.lower()

    # separate consonants at start of this word
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # add the piglatin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'
    
    # set the word back to uppercase or title case
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    
    # add the non-letters back to the sart or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# join all the words back together in a single string.
print(' '.join(pigLatin))