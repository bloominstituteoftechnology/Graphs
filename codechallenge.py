# Given an object/dictionary with keys and values that consist of both strings and integers, design an algorithm to calculate and return the sum of all of the numeric values.
# For example, given the following object/dictionary as input:
# {
#   "cat": "bob",
#   "dog": 23,
#   19: 18,
#   90: "fish"
# }
# Your algorithm should return 41, the sum of the values 23 and 18.
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.


# dictionary with keys
# string and ints
# find sum of all NUMERIC values

# just adding value pairs

# 
d = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}

# ht = {}
# print(sum(d.values))

def value_sum(dict):
    sum = 0
    for i in d.keys():
        # print(i)
        if(type(dict[i])==int):
            # print(dict[i])
            sum +=dict[i]
    return sum
print(value_sum(d))


# new_values = re.findall('\d+', dict.values)
#     i = new_values
#     sum = 0
#     # print(i)
#     # new_values = re.findall('\d+', dict.values)
#     for i in d:
#         sum += int(i)
#     print(sum)

# value_sum(d)