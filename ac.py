list =['1 + 855', '3801 - 2', '45 + 43', '123 + 49']
def arithmetic_arranger(problems, boolean = False):
    dashes = []
    firstNum = []
    secondNum= []
    operand = []
    answers = []
    longerNum = []
    length = []

    firstLine = ''
    secondLine = ''
    thirdLine = ''
    fourthLine = ''

    #setting the contraints.
    if len(problems) > 5:
        return "Too many problems."
    for index in range(len(problems)):
        for i in problems[index]:
            if i == "*" or i== "/":
                return "Error: Operator must be '+' or '-'."
        value = problems[index].split() 
        if value[0].isdecimal() == False or value[2].isdecimal() == False:
            return("Error: Numbers must only contain digits.")
        if len(value[0]) > 4 or len(value[2]) > 4:
            return("Error: Numbers cannot be more than four digits.")
    # return ("Error: Numbers\n cannot be more than four digits.")

    #doing the arithmetic
    for index in range(len(problems)):
            value = problems[index].split()
            firstNum.append((value[0]))
            secondNum.append((value[2]))
            operand.append((value[1]))
            if len(value[0]) > len(value[2]):
                    longerNum.append((value[0]))
            else:
                longerNum.append((value[2]))

            if value[1] == "+":
                answer = int(value[0]) + int(value[2])
                answers.append(answer)
            
            else:
                answer = int(value[0]) - int(value[2])
                answers.append(answer)

    
    for i in range(len(problems)):
        numOfDashes = len(longerNum[i]) + 2 
        dashes.append("-" * numOfDashes)
        length.append(numOfDashes)


    for i in range(len(problems)):

        numOfSpace1 = length[i] - len(firstNum[i])
        firstLine += " " * numOfSpace1 + firstNum[i] + "    "
        secondLine += operand[i] + " " * (length[i] - 1 - len(secondNum[i])) + secondNum[i] +'    '
        thirdLine += dashes[i] + "    "
        fourthLine +=" " * (len(dashes[i]) - len(str(answers[i]))) + str(answers[i]) + "    "
        if (boolean == False):
            fourthLine = ""


    if boolean == False:
        arranged_problems= firstLine.rstrip() + "\n" + secondLine.rstrip() + '\n' + thirdLine.rstrip()
    else:
        arranged_problems= firstLine.rstrip() + "\n" + secondLine.rstrip() + '\n' + thirdLine.rstrip() + '\n' + fourthLine.rstrip()

    return(arranged_problems)




print(arithmetic_arranger(["3 + 855", "3801 + 3802", "45 + 43", "123 + 49"]))