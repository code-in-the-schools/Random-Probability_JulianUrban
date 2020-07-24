import random

#list 1
#create a list and initialize variables
list1 = []
uno = 0
dos = 0
tres = 0
cuatro = 0
cinco = 0
seis = 0

#for loop to generate numbers and count values
for i in range(9):
  n = random.randint(1,6)
  list1.append(n)
  if n == 1:
    uno += 1
  elif n == 2:
    dos += 1 
  elif n == 3:
    tres += 1 
  elif n == 4:
    cuatro += 1 
  elif n == 5:
    cinco += 1   
  elif n == 6:
    seis += 1 

#calculating percentages
uno = uno / 10
dos = dos / 10
tres = tres / 10
cuatro = cuatro / 10
cinco = cinco / 10
seis = seis / 10

#printing percentages
print("Number of iterations: 10")
print("1: " + "{:.0%}".format(uno))
print("2: " + "{:.0%}".format(dos))
print("3: " + "{:.0%}".format(tres))
print("4: " + "{:.0%}".format(cuatro))
print("5: " + "{:.0%}".format(cinco))
print("6: " + "{:.0%}".format(seis))



#list 2
#create a list and initialize variables
list2 = []
uno = 0
dos = 0
tres = 0
cuatro = 0
cinco = 0
seis = 0

#for loop to generate numbers and count values
for i in range(99):
  n = random.randint(1,6)
  list2.append(n)
  if n == 1:
    uno += 1
  elif n == 2:
    dos += 1 
  elif n == 3:
    tres += 1 
  elif n == 4:
    cuatro += 1 
  elif n == 5:
    cinco += 1   
  elif n == 6:
    seis += 1 

#calculating percentages
uno = uno / 100
dos = dos / 100
tres = tres / 100
cuatro = cuatro / 100
cinco = cinco / 100
seis = seis / 100

#printing percentages
print("Number of iterations: 100")
print("1: " + "{:.0%}".format(uno))
print("2: " + "{:.0%}".format(dos))
print("3: " + "{:.0%}".format(tres))
print("4: " + "{:.0%}".format(cuatro))
print("5: " + "{:.0%}".format(cinco))
print("6: " + "{:.0%}".format(seis))



#list 3
#create a list and initialize variables
list3 = []
uno = 0
dos = 0
tres = 0
cuatro = 0
cinco = 0
seis = 0

#for loop to generate numbers and count values
for i in range(99999):
  n = random.randint(1,6)
  list3.append(n)
  if n == 1:
    uno += 1
  elif n == 2:
    dos += 1 
  elif n == 3:
    tres += 1 
  elif n == 4:
    cuatro += 1 
  elif n == 5:
    cinco += 1   
  elif n == 6:
    seis += 1 

#calculating percentages
uno = uno / 100000
dos = dos / 100000
tres = tres / 100000
cuatro = cuatro / 100000
cinco = cinco / 100000
seis = seis / 100000

#printing percentages
print("Number of iterations: 100000")
print("1: " + "{:.0%}".format(uno))
print("2: " + "{:.0%}".format(dos))
print("3: " + "{:.0%}".format(tres))
print("4: " + "{:.0%}".format(cuatro))
print("5: " + "{:.0%}".format(cinco))
print("6: " + "{:.0%}".format(seis))



#contract part 2
#get user input
userInput = input("Enter a sequence of numbers using digits 0-9: ")
list4 = userInput

#initialize variables for original rates
ozero = 0
oone = 0
otwo = 0
othree = 0
ofour = 0
ofive = 0
osix = 0
oseven = 0
oeight = 0
onine = 0
count = 0

#count occurances for numbers
for i in list4:
  if i == 0:
    ozero += 1
    count += 1
  elif i == 1:
    oone += 1
    count += 1
  elif i == 2:
    otwo += 1
    count += 1
  elif i == 3:
    othree += 1
    count += 1
  elif i == 4:
    ofour += 1
    count += 1
  elif i == 5:
    ofive += 1
    count += 1
  elif i == 6:
    osix += 1
    count += 1
  elif i == 7:
    oseven += 1
    count += 1
  elif i == 8:
    oeight += 1
    count += 1
  elif i == 9:
    onine += 1
    count += 1

#calculating percentages
if ozero != 0 :
  ozero = ozero / count
if oone != 0 :
  oone = oone / count
if otwo != 0 :
  otwo = otwo / count
if othree != 0 :
  othree = othree / count
if ofour != 0 :
  ofour = ofour / count
if ofive != 0 :
  ofive = ofive / count
if osix != 0 :
  osix = osix / count
if oseven != 0 :
  oseven = oseven / count
if oeight != 0 :
  oeight = oeight / count
if onine != 0 :
  onine = onine / count

#printing original rates
print("Original results")
print("0: " + "{:.0%}".format(ozero))
print("1: " + "{:.0%}".format(oone))
print("2: " + "{:.0%}".format(otwo))
print("3: " + "{:.0%}".format(othree))
print("4: " + "{:.0%}".format(ofour))
print("5: " + "{:.0%}".format(ofive))
print("6: " + "{:.0%}".format(osix))
print("7: " + "{:.0%}".format(oseven))
print("8: " + "{:.0%}".format(oeight))
print("9: " + "{:.0%}".format(onine))



#creating random lists using user inputted numbers
#list 1
#create a list and initialize variables
list4 = []
nzero = 0
none = 0
ntwo = 0
nthree = 0
nfour = 0
nfive = 0
nsix = 0
nseven = 0
neight = 0
nnine = 0

#for loop to generate and count values
for i in range(9):
  j = random.choice(userInput)
  list4.append(j)
  if j == 0:
    nzero += 1
  elif j == 1:
    none += 1
  elif j == 2:
    ntwo += 1
  elif j == 3:
    nthree += 1
  elif j == 4:
    nfour += 1
  elif j == 5:
    nfive += 1
  elif j == 6:
    nsix += 1
  elif j == 7:
    nseven += 1
  elif j == 8:
    neight += 1
  elif j == 9:
    nnine += 1

#calculating percentages
if ozero != 0 :
  ozero = ozero / 10
if oone != 0 :
  oone = oone / 10
if otwo != 0 :
  otwo = otwo / 10
if othree != 0 :
  othree = othree / 10
if ofour != 0 :
  ofour = ofour / 10
if ofive != 0 :
  ofive = ofive / 10
if osix != 0 :
  osix = osix / 10
if oseven != 0 :
  oseven = oseven / 10
if oeight != 0 :
  oeight = oeight / 10
if onine != 0 :
  onine = onine / 10

#printing the results
print("Number of iterations: 10")
print("0: " + "{:.0%}".format(nzero))
print("1: " + "{:.0%}".format(none))
print("2: " + "{:.0%}".format(ntwo))
print("3: " + "{:.0%}".format(nthree))
print("4: " + "{:.0%}".format(nfour))
print("5: " + "{:.0%}".format(nfive))
print("6: " + "{:.0%}".format(nsix))
print("7: " + "{:.0%}".format(nseven))
print("8: " + "{:.0%}".format(neight))
print("9: " + "{:.0%}".format(nnine))



#list 2
#create a list and initialize variables
list5 = []
nzero = 0
none = 0
ntwo = 0
nthree = 0
nfour = 0
nfive = 0
nsix = 0
nseven = 0
neight = 0
nnine = 0

#for loop to generate and count values
for i in range(99):
  j = random.choice(userInput)
  list5.append(j)
  if j == 0:
    nzero += 1
  elif j == 1:
    none += 1
  elif j == 2:
    ntwo += 1
  elif j == 3:
    nthree += 1
  elif j == 4:
    nfour += 1
  elif j == 5:
    nfive += 1
  elif j == 6:
    nsix += 1
  elif j == 7:
    nseven += 1
  elif j == 8:
    neight += 1
  elif j == 9:
    nnine += 1

#calculating percentages
if ozero != 0 :
  ozero = ozero / 100
if oone != 0 :
  oone = oone / 100
if otwo != 0 :
  otwo = otwo / 100
if othree != 0 :
  othree = othree / 100
if ofour != 0 :
  ofour = ofour / 100
if ofive != 0 :
  ofive = ofive / 100
if osix != 0 :
  osix = osix / 100
if oseven != 0 :
  oseven = oseven / 100
if oeight != 0 :
  oeight = oeight / 100
if onine != 0 :
  onine = onine / 100

#printing the results
print("Number of iterations: 100")
print("0: " + "{:.0%}".format(nzero))
print("1: " + "{:.0%}".format(none))
print("2: " + "{:.0%}".format(ntwo))
print("3: " + "{:.0%}".format(nthree))
print("4: " + "{:.0%}".format(nfour))
print("5: " + "{:.0%}".format(nfive))
print("6: " + "{:.0%}".format(nsix))
print("7: " + "{:.0%}".format(nseven))
print("8: " + "{:.0%}".format(neight))
print("9: " + "{:.0%}".format(nnine))



#list 3
#create a list and initialize variables
list6 = []
nzero = 0
none = 0
ntwo = 0
nthree = 0
nfour = 0
nfive = 0
nsix = 0
nseven = 0
neight = 0
nnine = 0

#for loop to generate and count values
for i in range(99999):
  j = random.choice(userInput)
  list6.append(j)
  if j == 0:
    nzero += 1
  elif j == 1:
    none += 1
  elif j == 2:
    ntwo += 1
  elif j == 3:
    nthree += 1
  elif j == 4:
    nfour += 1
  elif j == 5:
    nfive += 1
  elif j == 6:
    nsix += 1
  elif j == 7:
    nseven += 1
  elif j == 8:
    neight += 1
  elif j == 9:
    nnine += 1

#calculating percentages
if ozero != 0 :
  ozero = ozero / 100000
if oone != 0 :
  oone = oone / 100000
if otwo != 0 :
  otwo = otwo / 100000
if othree != 0 :
  othree = othree / 100000
if ofour != 0 :
  ofour = ofour / 100000
if ofive != 0 :
  ofive = ofive / 100000
if osix != 0 :
  osix = osix / 100000
if oseven != 0 :
  oseven = oseven / 100000
if oeight != 0 :
  oeight = oeight / 100000
if onine != 0 :
  onine = onine / 100000

#printing the results
print("Number of iterations: 100")
print("0: " + "{:.0%}".format(nzero))
print("1: " + "{:.0%}".format(none))
print("2: " + "{:.0%}".format(ntwo))
print("3: " + "{:.0%}".format(nthree))
print("4: " + "{:.0%}".format(nfour))
print("5: " + "{:.0%}".format(nfive))
print("6: " + "{:.0%}".format(nsix))
print("7: " + "{:.0%}".format(nseven))
print("8: " + "{:.0%}".format(neight))
print("9: " + "{:.0%}".format(nnine))