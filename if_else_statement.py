# Condition Operators :
"""
 Greater Than : >
 Less Than : <
 Greater Than Or Equal To : >=
 Less Than Or Equal To : <=
 Not Equal To : !=
 Equal To : ==
"""

a = 35
b = 283
c = 100
if a > b:
    print("A is Greater Than B")
elif a == b:
    print("A is Equal To B")
else:
    print("A is Less Than B")

# and Operator Use For Multiple Condition Check and Execute Function if All Condition are True
if a > b and c > a:
    print("A")
else:
    print("B")

# or Operator Use For Multiple Condition Check and Execute Function if Any Of One Condition are True
if a > b or c > a:
    print("A")
else:
    print("B")
