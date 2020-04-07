a=0
b=1
c=0

print('FIBONACCI SERIES')
n = int(input('How many numbers do you want to display: '))

i=0
if n<2:
    print("Invalid Input")
else :
    print(0)
    print(1)
    while i < (n - 2):
        c = a + b
        a = b
        b = c
        print(c)
        i = i + 1
    
