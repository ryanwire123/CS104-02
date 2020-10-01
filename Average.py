numberOfScores = 0
score = 0
total = 0
average = 0.0
scoreCount = 0

numberOfScores =  int(input ("Please enter the number of scores you want to average: "))

#add a loop to make code repeast until scoreCount == numberOfScores use a while loop
while (scoreCount < numberOfScores):
    score = int(input ("Please enter a score: "))
    total = total + score
    scoreCount = scoreCount + 1

#can not concatenate string and float in same line so average was needed to be cast as a string
average = total / numberOfScores
print ("The average of the test scores is: " + str(average))

