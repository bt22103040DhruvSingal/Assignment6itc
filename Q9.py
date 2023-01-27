class isValid:
    inString = " "###class variable for storing input string
    def assign(self,string):
        self.inString = string
    def Valid(self):
        isValid = True
        for k in range(len(self.inString)):
            if not isValid:
                break
            c = self.inString[k]
            if c in[")","}","]"]:###if an open bracket is placed then check for previous
                if k == 0:###First position then isn't valid
                    isValid = False
                if self.inString[k-1] not in ["(","{","["]:###prev position wasn't brakets
                    isValid = False
            ###if ( or any other at the last of string then also invalid
            if c in ["(","{","["] and k == len(self.inString)-1:
                print("Got here")
                isValid = False
                break
            if c == "(" :
                if self.inString[k+1] != ")":
                         isValid = False
            if c == "{":
                if self.inString[k+1]!= "}":
                    isValid = False
            if c == "[":
                if self.inString[k+1]!= "]":
                    isValid = False
        return isValid
v = isValid()
v.assign(input("Enter the string: "))
print("Validity of parenthesis = ",v.Valid())
