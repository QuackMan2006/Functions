def starts_with_A(word):
    if (word[0] == "A"):
        return True
    else:
        return False


#Main routine
word_to_check = input("Enter the word: ").upper()
print(starts_with_A(word_to_check))
