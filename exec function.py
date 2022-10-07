exec("print('so this is my practice work')")
list_str = "[5,6,2,1]"
list_str = exec(list_str)
print(list_str)    # it will give none
exec("list_str2 = [5,6,2,1,1]")  # list can print
print(list_str2)
exec("def test():print('heloo there!!!')")# new function can also be defined in exec
test()
#exec('''
#def test2():
#print('lets see if multi line work....')''')
#test2()

#eval : evaluating expression
#exec : executing statements
print(1+1)   # this is expression
print(1==0)   # this is a expression
a = 1         # this is a statement which is to be executed
eval("print(1+1)")
exec("c=3")
print(c)
eval("print(c+3)")
code ='num1, num2 = 7,8;print(f"{num1}+{num2} = {num1 + num2}")'
# exec(code)


# you can ask the user what to execute
# code = input('what shall we do today?')
# for num in range(2):print(num, num**2,num**3)
# exec(code)

# lets build a dictionary comprehension
# exec("({num:num**3 for num in range(6)})")# Nothing printed!Now, let's try eval()
# eval("({num:num**3 for num in range(6)})")
# solution for the risk
# step1: you can use dir() to check what variables are available to the user restart the shell
# import os
# code = input('what shall we do today?')
# print(os.listdir())
# exec(code)


# exec("x=10\nprint(x)")
# exec("x,y =10,15\nprint(f' sum of x and y is {x+y}')")
# X= ("x,y =10,15\nprint(f' sum of x and y is {x+y}')")
# exec(X)

# input can be taken from user
# exec(input("enter code:"))

# exec(input("enter code:"),{"_builtins_":{"print":print}})# now user can use only print function as it is the only function defined here
# exec(input("enter code:"),{"_builtins_":{"display":print}})#print function can be used by the name of display function

# exec(input("enter code:"),{"_builtins_":None})# now user cannot use any function of builtins


# exec(input("enter code:"),{"_builtins_":None},{"print": print})# now user can use this one function of builtins


# exec can be used in triple quotes also
# exec("""def fun():
#     return "hello world"
# print(fun())
# """)