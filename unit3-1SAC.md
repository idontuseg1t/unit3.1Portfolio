A shipping company needs a program to calculate the shipping cost of a package based on its weight. Packages that weigh less than or equal to 5kg cost $5 to ship, packages that weigh between 5kg and 10kg cost $10 to ship, and packages that weigh more than 10kg cost $15 to ship. Write a Python program that asks the user for the weight of the package and calculates the shipping cost based on the weight entered. The program should then display the shipping cost to the user.

- input: weight
- less than or equal to 5kg = $5
- between 5kg and 10kg = 10$
- more than 10kg = 15$

```python
BEGIN
    INPUT weight
    
    IF weight > 10 then:
        RETURN $15
    else if weight > 5 and weight <= 10 then:
        RETURN $10
    else:
        RETURN $5
    ENDIF

END
```


```python
def calcCost(weight):
    if weight > 10: # if weight is more than 10 NOT INCLUDING 10
        return "$15"
    elif weight > 5 and weight <= 10: # if weight is more tha 5kg NOT INCLUDING 5 and less than 10 INCLUDING 10
        return "$10"
    else: # returns 5$ if the weight is less than or equal to 5
        return "$5"

w = float(input('What is the weight of your package in kilograms?: '))
if w <= 0: # checking for invalid weights
    print("That is an invalid weight")
else:
    print(f"The shipping cost for a package weighing {w} kg is {calcCost(w)}")
```

    What is the weight of your package in kilograms?:  18


    The shipping cost for a package weighing 18.0 kg is $15

The shipping company needs to determine a bulk rate of 8 packages. If the average is less than or equal to 5kg they get a discount rate of $4.50 to ship, average that weigh between 5kg and 10kg they get a discount rate of $9  to ship, and packages that weigh more than 10kg they get a discount rate of $14 to ship. Write a Python program that asks the user for a list of package weights, calculates the average of the list and displays the discounted cost to the user.

BEGIN
    DEFINE function calcCost(weight):
        if weight > 10 then: 
            return 15
        else if weight > 5 and weight <= 10 then: 
            return 10
        else: 
            return 5
        ENDIF
        
    DEFINE function calcAverage(weights):
        total <-- 0
    for the number of items in weights:
        total <-- total + item-no
    ENDFOR
    average <-- total/8
    return average
    

    DEFINE function avgCost(avg):
        if avg <= 5 then:
            return 4.50
        else if avg > 5 and avg <= 10 then:
            return 9
        else:
            return 14
        ENDIF

END

```python
def calcCost(weight): # function for calculating costs of weights
    if weight > 10: 
        return 15
    elif weight > 5 and weight <= 10: 
        return 10
    else: 
        return 5

def calcAverage(weights): # function for calculating average of weights
    total = 0
    for x in weights:
        total += x
    average = float(total)/8
    return average

def avgCost(avg): # function for calculating the discount
    
    if avg <= 5:
        return 4.50
    elif avg > 5 and avg <= 10:
        return 9
    else:
        return 14
weightlist = []
totalcost = 0
for i in range(8):
    w = float(input(f'Weight of package {i + 1}: '))
    weightlist.append(w)
    totalcost += float(calcCost(w))
    i += 1
    

print(f"The average weight of the 8 packages is {calcAverage(weightlist)}kg.")
print(f"You get a discount of ${str(avgCost(calcAverage(weightlist)))}.")
print(f"Cost without discount: ${totalcost}")
print(f"Cost with discount: ${totalcost - float(avgCost(calcAverage(weightlist)))}")

```

    Weight of package 1:  2
    Weight of package 2:  3
    Weight of package 3:  2
    Weight of package 4:  2
    Weight of package 5:  2
    Weight of package 6:  3
    Weight of package 7:  2
    Weight of package 8:  3


    The average weight of the 8 packages is 2.375kg.
    You get a discount of $4.5.
    Cost without discount: $40.0
    Cost with discount: $35.5

Sect 3: The shipping company got a suggestion from their delivery drivers, Jessie & Ollie. They noticed the package deliveries overlapped. The point is Jessie’s delivery route is shorter. Ollie wants to know which deliveries to hand off to Jessie.

NOTE: The numbers are location IDs
Use this data to check your solution
Jessie = [2,5,8,11,14,17,20,23,26,29]
Ollie  = [1,3,5, 7, 9,11,13,15,17,19,21,24,26]

Jessie = [1, 7, 8, 11, 12, 13, 14, 24, 26, 29]
Ollie  = [2, 4, 7,  9, 10, 12, 14, 18, 19, 21, 24, 25, 29]
BEGIN

for each item in Ollie:
    if that item is in Jessie then:
        Return True
    ENDIF
ENDFOR
        
END

```python
Jessie = [1, 7, 8, 11, 12, 13, 14, 24, 26, 29]
Ollie  = [2, 4, 7,  9, 10, 12, 14, 18, 19, 21, 24, 25, 29]


for num in Ollie:
    if num in Jessie:
        print(f"Jessie can deliver the package at location {num}")
```

    Jessie can deliver the package at location 7
    Jessie can deliver the package at location 12
    Jessie can deliver the package at location 14
    Jessie can deliver the package at location 24
    Jessie can deliver the package at location 29



```python

```
