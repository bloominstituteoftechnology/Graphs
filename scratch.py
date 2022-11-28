d = {
    "cat": "bob",
    "dog": 23,
    19: 18,
    90: "fish"
}


print(d.items())

sum = 0

for key, value in d.items():
    if type(value) == int:
        sum += value
print(sum)
