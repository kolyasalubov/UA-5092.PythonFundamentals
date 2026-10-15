#Task3
#Write a function that calculates the number of characters included ingiven string
#nput: "hello"
#output: {"h":1, "e":1,"l":2,"o":1}

print("Task3")

str = input("Write string:")
result = {}

for i in str:
    b=result.get(i,0) + 1
    result[i] = b
print(result)

