your_given_word = input('Enter a word that you want to calulate it\'s vowels: ')
vowel = ['a','e','i','o','u']
temp_count = []

for i in your_given_word:
    '''
    func: This function will count how many vowel is there in the given str
    '''
    for j in vowel:
        if i == j:
            temp_count.append(j)
        else:
            pass
print(len(temp_count))