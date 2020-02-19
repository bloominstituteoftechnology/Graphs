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


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(ran.randomChoice(l))
print(ran.randomChoice(l))
print(ran.randomChoice(l))
print(ran.randomChoice(l))
print(ran.randomChoice(l))
print(ran.randomChoice(l))
print(ran.randomChoice(l))


d = {"a": 32, "b": 324234, "c": 309}
print(ran.randomChoice(d))
print(ran.randomChoice(d))
print(ran.randomChoice(d))
