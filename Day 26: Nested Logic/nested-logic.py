# Enter your code here. Read input from STDIN. Print output to STDOUT

rd,rm,ry = map(int,input().strip().split())
dd,dm,dy = map(int,input().strip().split())

if (rm,ry)==(dm,dy):
    print(15*(rd-dd))
elif ry==dy and rm>dm:
    print(500*(rm-dm))
elif ry>dy:
    print(10000)
else:
    print(0)

