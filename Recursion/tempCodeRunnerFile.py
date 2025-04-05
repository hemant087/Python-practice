str = input()
if len(str)%2==0:
    action(str)
else:
    str= str+"."
    action(str)