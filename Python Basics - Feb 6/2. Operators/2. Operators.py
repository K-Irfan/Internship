operators=['Arithmetic operator','Assignment operator','Comparison operator','Logical operator','Identity operator','Membership operator','Bitwise operator']
def op():
    for i,no in enumerate(operators, start=1):
        print(f"{i}. {no}")
print(f"There are {len(operators)} operators in Python")
op()

print("\nThe operators have certain precedence.")