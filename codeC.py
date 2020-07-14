
dictionary = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}

sum = 0
for v in dictionary.values():
    if type(v) == int:
        sum = sum + v
print(sum) 