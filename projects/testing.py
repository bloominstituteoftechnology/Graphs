# Add up and print the sum of the all of the minimum elements of each inner array:
# [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175

the_problem = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

sum_arr = []

for a in the_problem:
    low_num = a[0]
    for j in a:
            
        if low_num > j:
            the_problem.pop(j)
        else:
            low_num = j
            

# while x not in checked 
    # for each inner arr
        # set low_num to the first number in the inner arr
        # if first number is < the next number then move on to the next number
        # if the number is not smaller than the next number replace low_num with that next number and move on
        # at the end of the inner arr append the low_num to the sum_arr and go to the next inner array

    
