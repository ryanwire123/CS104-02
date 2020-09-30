numberOfScores = 0
score = 0
total = 0
average = 0.0
scoreCount = 0

numberOfScores =  int(input ("Please enter the number of scores you want to average: "))

#add a loop to make code repeast until scoreCount == numberOfScores
score = int(input ("Please enter a score: "))
total = total + score
scoreCount = scoreCount + 1


average = total / numberOfScores
print (average)

