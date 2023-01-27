###Remove characters from the string alphabets... if all characters are removed from alphabets
###Then string is pangram
def isPangram(string):
   alphabets = "ABCDEFIGHKLMNOPQRSTUVWXYZ"
   for k in string:
      if k in alphabets:
        alphabets = alphabets.replace(k,"")
   if len(alphabets) == 0:
      return True
   else:
      return False
string = input("Enter string: ")
string = string.upper()###Capital 
string = string.replace(" ","")###Remove all spaces
if isPangram(string):
    print("String is a pangram")
else:
    print("String is not a pangram")
