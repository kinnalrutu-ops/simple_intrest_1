import sys
print("Simple and Compound Interest Calculator")
if len(sys.argv) == 5:
    p = float(sys.argv[1])
    r = float(sys.argv[2])
    t = float(sys.argv[3])
    n = int(sys.argv[4])
else:
   p=5000
   r=5
   t=10
   n=4
r = r / 100
simple_interest = p * r * t
print("Simple Interest:", round(simple_interest, 2))
