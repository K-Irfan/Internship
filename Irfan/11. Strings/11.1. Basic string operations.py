x='Irfan'
print(x[3],"\n")

for i in x:
    print(i)
print(f"\n{len(x)}")

txt='Anusha is an Idiot'
print("\n"+txt)
print('Idiot' in txt)
if 'Idiot' in txt:
    print("Yes, Idiot is present in the text\n")

print("f-strings")
age=22
Str=f"My name is Irfan and my age is {age}"
print("String Operations")
print(Str.upper())
print(Str.lower())
print(x.capitalize())
print(x.casefold())
print(x.center(20))