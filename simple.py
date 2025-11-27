import sys
print("Simple Interest Calculator")
if len(sys.argv) == 3:
    p = float(sys.argv[1])
    r = float(sys.argv[2])
    t = float(sys.argv[3])
else:
   p=5000
   r=5
   t=10
simple_interest = p * r * t/100
print("Simple Interest:", round(simple_interest, 2))
