# bitwise operator -- Bitwise operator works on bits(0 and 1) and performs bit by bit operation
#author-vinay
#tool-- PyCharm

# &(AND) operator-->

"""The AND operator compares two bits and generates
a result of 1 if both bits are otherwise it returns 0"""

print( 2 & 0 )  #perform & operation between binary values of 2 and 0 ans--> 0
print(2 & 3)    #2 binary->10 3 binary->11 so (10 and 11)=10 which is 2

# |(OR) operator

"""The  bitwise OR operator compares two bits and returns 1 if either or both of the 
bits are 1 and it gives 0 if both bits are 0."""
a=2
print(a | 3)    #perform OR operartion between binary value of a i.e 2 and 3 ans-> 3
                # (10 or 11)=11 which is 3

# ^(XOR) operator

"""XOR is a bitwise operator, and it stands for "exclusive or."
 It performs logical operation. If input bits are the same,
 then the output will be false(0) else true(1)"""

print(2 ^ 3)  # 10 xor 11 = 11 which is 1

# ~(bitwise NOT) operator

"""Returns one’s compliement of the number"""
print (~10)       #a = 10 = 1010 (Binary)    ~a = ~1010 = -(1010 + 1) = -(1011) = -11

# << Binary Right Shift operator
"""The right shift operator ( >> ) shifts the first operand the specified number of 
bits to the right. Excess bits(after the decimal(.)) shifted off to the right are discarded.
 Copies of the leftmost bit are shifted in from the left."""

print(12>>4)  # 12 is 1100 in binary so shift 4 bits toward right 0000.1100 and we  get 0000=0

# >> Binary Left operator

"""The left shift operator ( << ) shifts the first operand the specified number of 
bits to the left. Excess bits shifted off to the left are discarded. 
Zero bits are shifted in from the righ"""

print(12<<4) # 12 binary--> 1100(00001100) so shift 4 bits towards left ie 11000000 means 192

