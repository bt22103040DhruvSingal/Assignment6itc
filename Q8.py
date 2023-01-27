class SumZero:
    Numlist = []
    def assign(self,n):
        self.Numlist = n
    def printList(self):
        listOfThreenum = []###A list to store all the lists of 3 integers summing to zero
        l = len(Numlist)
        ###Set 3 position indexes one with lower, middle and highest indexes
        for i in range(l-2):
          for j in range(i+1,l-1):
            for k in range(j+1,l):
             sumofNum = Numlist[i]+Numlist[j]+Numlist[k]
             if sumofNum == 0:
                listOfThreenum +=[(Numlist[i],Numlist[j],Numlist[k])]
        ###print all original lists
        origList = []
        for n in listOfThreenum:
            if n in origList:
                continue
            else:
                origList.append(n)
        ###Print them
        print(origList)
print("Enter numbers of the list seprated by spaces:")
num = input()
num = num.split(" ")
Numlist = []###A list to store all the integers entered
for k in num:
    Numlist.append(int(k))
S = SumZero()
S.assign(Numlist)
S.printList()
