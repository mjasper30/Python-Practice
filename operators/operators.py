# Arithmethic Operators
print(2+2)
print(2-5)
print(2*3)
print(2/4)
print(2 % 4)
print(2**3)
print(10//5)

# Assignment Operators
x = 4
x += 4  # x = x + ?
x -= 4
x *= 4
x /= 4
x %= 4
x **= 4
x //= 4
# x &= 4.1
# x |= 4
# x ^= 4
# x >>= 4
# x <<= 4

# Comparison Operator
print(1 == 1)
print(5 > 5)
print(5 < 1)
print(5 >= 1)
print(5 <= 1)
print(5 != 1)

# Logical Operators
print(True and True)
print(True or False)
print(not (True and False))

# Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have the same content

print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

# Membership Operators

a = ["apple", "banana"]

print("banana" in a)
print("orange" not in a)

# Precedence Operator

"""
Operator	                                    Description	
()	                                            Parentheses	
**	                                            Exponentiation	
+x  -x  ~x	                                    Unary plus, unary minus, and bitwise NOT	
* /  //  %	                                    Multiplication, division, floor division, and modulus	
+  -	                                        Addition and subtraction	
<<  >>	                                        Bitwise left and right shifts	
&	                                            Bitwise AND	
^	                                            Bitwise XOR	
|	                                            Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	                                            Logical NOT	
and	                                            AND	
or	                                            OR

Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right:

Example:
print(5 + 4 - 7 + 3)
Answer: 5
"""

print(5 + 4 - 7 + 3)
