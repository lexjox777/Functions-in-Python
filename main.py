# def greet():
#     return 'Hello Maria'
   
# print(greet())

#====================

# '''
# Functions with parameters
# '''
#  any functions in a parameter is known as an arguements(name, etc)
# def greet(name):
#   return f"Hello {name}, Good morning"

# print(greet("Felix"))
# print(greet("Maria"))

#=========================
# '''
# Arbitrary parameters
# '''
# def fruits(*names):

# # (*name) means the arguements can accept multiple parameters
# # '''
# # Accepts unknown number of fruit names and prints each of them 
# # *name: list of fruits
# # '''
#   for fruit in names:
#    print(fruit)
# fruits("Orange","Banana")


# ================
# '''
# Keyword parameters
# '''
# def greet(name,msg):

#   return f"Hello {name}, {msg}"
  
# # print(greet("Kingsley","Good morning"))
# # print(greet("Maria","Good morning"))
# print(greet(name="Kingsley",msg="Good morning"))
# print(greet(msg="Good morning",name="Maria"))

# ===================

'''
Arbitrary Keyword parameters
'''
#  ** is used in defining arbitary keywords
# def person(**student):
# #  print(type(student))
# # #  this is  a type of Dict
# #  print(student)
#  for key in student:
#    print(student[key])
# person(fname="Kingsley",lname="Maria")


'''
Default parameter values
'''
# def greet(name='David'):
#   return f"Hello, {name}"
# print(greet())
# print(greet('Maria'))

#==================
'''
pass statement
'''
def greet():
  pass

#==================
'''
Recursion
'''
def factorial_recursive(n):
  '''
  multiply a given number by every number by every number less than it down to 1 in a factorial way
  e.g if n is 5 then calculte 5*4*3*2*1=120
  n: is the highest starting number
  '''
  if n==1:
     return True
  else:
     return n * factorial_recursive(n-1)
print(factorial_recursive(5))