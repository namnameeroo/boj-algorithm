input = input()
input = str(input)
left = sum([int(x) for x in input[0:len(input)//2]])
right = sum([int(x) for x in input[len(input)//2:]])
result = "LUCKY" if left==right else "READY"
print(result)