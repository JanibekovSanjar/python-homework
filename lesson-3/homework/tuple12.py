tuple1 = ('lemon','banana',"mountain",'eagle',"rock",'stone')
a = sorted(list(tuple1))
print(a[-2] if len(tuple1)>3 else None)