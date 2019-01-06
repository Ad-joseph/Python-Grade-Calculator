#Created by Alexander Dunne

marks = [] #creates an empty list
weights = []
achieved_mark = []
testing = []


def grade_calculation():
    for idx in range(1,8):
        print("Please enter your mark for assignment {}".format(idx))
        print("-----------------------------------------")
        mark = float(input("Mark achieved: "))
        weight = float(input("Total weight for assignment:"))
        marks.append(mark)
        weights.append(weight)
        achieved_mark = (mark/100)*weight
        testing.append(achieved_mark)
        print ("\nMark achieved: ",round(achieved_mark, 2),"%","out of:",weight,"%\n")

def grade_certification():
    if sum(testing) < 40:
        print("You did not pass this module")

    elif sum(testing) >=40 and sum(testing) < 49:
            print("You achieved: 3rd class")

    elif sum(testing) >= 50 and sum(testing) < 59:
            print("You achieved: Lower second class (2.2)")

    elif sum(testing) >= 60 and sum(testing) < 69:
            print("You achieved: Upper second class (2.1)")
    else:
         print("You achieved: First class")


def output():
    overall_mark = achieved_mark
    print ("Total mark for the module: ",sum(testing))

def main():
    grade_calculation()
    output()
    grade_certification()

main()
