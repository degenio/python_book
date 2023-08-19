###### Solution 1 ###### 
###### Solution 1 ###### 
#Input
a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))
max_val = a
min_val = b

if b > a:
    max_val = b
    min_val = a

#Find min and max 
if max_val < c:
    max_val = c
elif min_val > c:
    min_val = c

print("Minimum:", min_val, "Maximum:", max_val)



###### Solution 2 ###### 
#Input
a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))
max_val, min_val = a, b

if b > a:
    max_val, min_val = b, a

#Find min and max 
if max_val < c:
    max_val = c
elif min_val > c:
    min_val = c

print("Minimum:", min_val, "Maximum:", max_val)