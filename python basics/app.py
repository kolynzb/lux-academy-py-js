''''name = input('enter the age')
age = input('enter the age')
print(f'{name}  you are  {int(age)}') #interpolation 
print('your name is ' , name) # concantenation'''

#numeric literals
yof = 1222
#ghg= 3 + 4i 

# recursion
def tri_recursion(k):
    if (k>0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

tri_recursion = 4