# unit3.1Portfolio
Here is the start of this file
```python
print("Hello world!")

```

my fizzbuzz program

```python
num = int(input("type an integer: "))
count = 1
for i in range(num):
    if count % 5 != 0 and count % 3 == 0:
        print("Fizz") # multiples of 3
        
    elif count % 5 == 0 and count % 3 != 0:
        print("Buzz") # multiples of 5
        
    elif count % 5 == 0 and count % 3 == 0:
        print("FizzBuzz") # multiples of both 3 and 5
        
    else:
        print(count)
    
    
    count +=1
    i +=1

```

rabbit counter from grok

```python
init = int(input("Initial population: "))
final = int(input("Final population: "))
pop = float(init)
yearcount = 0
while pop < final:
  pop = pop * 1.37
  yearcount += 1
  
print(f"It would take {yearcount} years for there to be {final} rabbits.")
  
```
