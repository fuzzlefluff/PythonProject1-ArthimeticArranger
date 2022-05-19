

def arithmetic_arranger(problems,showAwns = False):
    resultString = ""
    problemCollection = []

    #check if we have too many problems
    if(len(problems) > 5):
        resultString = "Error: Too many problems."
        return resultString
    
    for token in problems:
        splitToken = token.split()
        
        #check our digit counts and return an error if they are too big
        if(len(splitToken[0]) > 4):
            resultString = "Error: Numbers cannot be more than four digits."
            return resultString
        if(len(splitToken[2]) > 4):
            resultString = "Error: Numbers cannot be more than four digits."
            return resultString

        #check to see if we have valid digit only operands
        if not (splitToken[0].isdigit()):
            resultString = "Error: Numbers must only contain digits."
            return resultString
        if not (splitToken[2].isdigit()):
            resultString = "Error: Numbers must only contain digits."
            return resultString
        
        #calculate the result of our current problem, if we got an error reuturn that
        resStr = sumString(token)
        if("Error" in resStr):
            return resStr

       
        #store our valid values
        firstline = splitToken[0]
        secondline = splitToken[2]
        fourthline = resStr

         #add the operator with the proper amount of spaces depending on which number has a larger digit count
        if(len(splitToken[0]) > len(splitToken[2])):
            diff = len(splitToken[0]) - len(splitToken[2])
            secondline = splitToken[1] + spaceAdder(secondline,diff+1)

        elif(len(splitToken[0]) <= len(splitToken[2])):
            firstline = spaceAdder(firstline,1)
            secondline = splitToken[1] + spaceAdder(secondline,1)
            fourthline = spaceAdder(fourthline,1)

        #align all our numbers to the right with each other
        rightAlign = rightAlign3Strings(firstline,secondline,fourthline)
        firstline = rightAlign[0]
        secondline = rightAlign[1]
        fourthline = rightAlign[2]

        #create a third line with the proper amount of dashes
        thirdline = ""
        for i in range(len(secondline)):
            thirdline = thirdline + "-"
      
        problem = [firstline,secondline,thirdline,fourthline]
        problemCollection.append(problem)

    #clear our lines and build our final string
    firstline = ""
    secondline = ""
    thirdline = ""
    fourthline = ""
    for p in problemCollection:
        firstline += p[0] + "    "
        secondline += p[1] + "    "
        thirdline += p[2] + "    "
        fourthline += p[3] + "    "
    
    #rstrip clears trailing whitespace while leaving leading whitespace
    firstline = firstline.rstrip()
    secondline = secondline.rstrip()
    thirdline = thirdline.rstrip()
    fourthline = fourthline.rstrip()

    resultString += firstline + "\n"
    resultString += secondline + "\n"
    
    
    if(showAwns):
        resultString += thirdline + "\n"
        resultString += fourthline
    else:
        resultString += thirdline
    
    return resultString

#takes a single string and returns the result
def sumString(problem):
    resultString = "Error: Operator must be '+' or '-'."
    workString = problem.split()
    if("+" in problem):
        resultString = str(int(workString[0]) + int(workString[2]))
        return resultString
    elif("-" in problem):
         resultString = str(int(workString[0]) - int(workString[2]))
         return resultString
    return resultString

#takes 3 string and right aligns them to the largest string
def rightAlign3Strings(str1,str2,str3):
    resultList = ["error","error","error"]
    str1len = len(str1)
    str2len = len(str2)
    str3len = len(str3)
 
    #figure out and store how big the largest number everything needs to be aligned to
    largestStrLen = str1len
    if(str2len > largestStrLen):
        largestStrLen = str2len
    if(str3len > largestStrLen):
        largestStrLen = str3len
        
    #add spaces to numbers that need them added
    if(largestStrLen != str1len):
        diff = largestStrLen - str1len
        str1 = spaceAdder(str1,diff)
    if(largestStrLen != str2len):
        diff = largestStrLen - str2len
        str2 = spaceAdder(str2,diff)
    if(largestStrLen != str3len):
        diff = largestStrLen - str3len
        str3 = spaceAdder(str3,diff)
    
    resultList = [str1,str2,str3]
    return resultList

#adds spaces in front of a string
def spaceAdder(inpStr,amount):
    
    for i in range(amount):
        inpStr = " " + inpStr
    return inpStr