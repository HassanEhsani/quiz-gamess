print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()
    
print("okay! Let's play :)")
socre = 0

answer = input("what does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
    socre += 1
else:
    print("Incorrect!")
answer = input("what is the first number? ")
if answer == "one":
    print("Correct!")
    socre += 1
else:
    print("Incorrect!")
answer = input("what is 1 + 1? ")
if answer == "two":
    print("Correct!")
    socre += 1
else:
    print("Incorrect!")

print("you got " + str(socre) + " question correct")
print("you got " + str((socre / 3) * 100) + "%.")
