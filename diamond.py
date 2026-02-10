#diamond
#    *
#   ***
#  *****
#   ***
#    * 
diamond = 3
for i in range (diamond):
    print(" "*(diamond-i-1)+ "*" *(2*i+1))

for i in range (diamond-2,-1,-1):
    print(" "*(diamond-i-1)+"*"*(2*i+1))
    