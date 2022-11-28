d = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}

def numbers():
  sum = 0
  for k, v in d.items():
    if isinstance(v, int):
      sum = sum + v
      print(sum)