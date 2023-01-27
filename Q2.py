def isPalindrome(word):
    i = 0
    j = len(string)-1
    while i < j:
       if string[i] != string[j]:
        return False
       i += 1
       j -= 1
    ###If the compiler reaches here
    return True
string = input("Enter string:")
string = string.replace(" ","")
string = string.lower()
if isPalindrome(string):
    print("Is a palindrome")
else:
    print("Is not a palindrome")
     
