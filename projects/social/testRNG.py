from MyRNG import MyRandom

ran = MyRandom()



total = 0
iterations = 100
expectedAvg = 50

counts = {}
for i in range(iterations):
    randVal = ran.randomNumber(expectedAvg * 2)
    total += randVal
    counts[randVal] = counts.get(randVal, 0) + 1

average = total / iterations
print(average, len(counts))
