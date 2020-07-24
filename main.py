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