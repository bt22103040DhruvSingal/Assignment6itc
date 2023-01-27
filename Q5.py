###Create a list for the words
words = []
string = input("Enter string:")
string = string.lower()###Convert lower case for sorting
words = string.split("-")
words = sorted(words)
for j in range(len(words)):
    if j == len(words)-1:
        ###End of string encountered
        ###do not put Hyphen in print
        print(words[j])
    else:
        print(words[j],end = '-')
    
