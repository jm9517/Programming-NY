n = int(input("Please enter a positive integer:"))

for i in range(1, n+1):
    line = (n-i)*" " + i*"*"
    print(line)