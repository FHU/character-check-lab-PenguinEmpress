#Remove pass and complete the code
def check_character(word, index):
   i = word[index]
   if i.isalpha() == True:
      return "letter"
   elif i.isdigit() == True:
      return "digit"
   elif i.isspace() == True:
      return "white space"
   else:
      return "unknown"

if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))