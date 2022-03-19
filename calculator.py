import math
def end():
    print("*"*60)
    print("Thanks for using my program. Hope you enjoyed it.\nPlease give me your valuable feedback.\nIt helps me to improve my program. :)")
    print("*"*60)
    print("Made with Python by Akash")
    print("*"*60)
    exit()
def calculate():
    o1=int(input("Which operation do you want:\n Type 1 for numarical\n Type 2 for Trigonometrical \n Type 3 for algebraic\n Type 4 to exit\n\t:"))
    if o1==1:
        operation=int(input("Which operation do you want\n Type 1 to addition\n Type 2 for substraction\n Type 3 for multiplication\n Type 4 for division\n Type 5 for average\n\t:"))  
        num1=int(input("Input the 1st number here:"))
        num2=int(input("Input the 2nd number here:"))
        if operation==1:
            def addition(num1,num2):
                return num1+num2
            print("Answer:{}".format(addition(num1,num2)))
        elif operation==2:
            def substraction(num1,num2):
                return num1-num2
            print("Answer:{}".format(substraction(num1,num2)))
        elif operation==3:
            def multiplication(num1,num2):
                return num1*num2
            print("Answer:{}".format(multiplication(num1,num2)))
        elif operation==4:
            def division(num1,num2):
                return num1/num2
            print("Answer:{}".format(division(num1,num2)))
        elif operation==5:
            def average(num1,num2):
                return (num1+num2)/2
            print("Answer:{}".format(average(num1,num2)))
        else:
            print("Your input is wrong , please check it out and try again")
    elif o1==2:
        ratio=str(input("Input the ratio here[sin/cos/tan/cosec/sec/cot]:"))
        angle=int(input("Input the value of angle here:"))
        if ratio=="Sin" or ratio=="SIN" or ratio=="sin":
            print("Answer:{}".format(math.sin(angle)))
        elif ratio=="Cos" or ratio=="cos" or ratio=="COS":
            print("Answer:{}".format(math.cos(angle)))
        elif ratio=="tan" or ratio=="Tan" or ratio=="TAN":
            print("Answer:{}".format(math.tan(angle)))
        elif ratio=="cosec" or ratio=="Cosec" or ratio=="COSEC":
            print("Answer:{}".format(math.pow(math.sin(angle),-1)))
        elif ratio=="sec" or ratio=="Sec" or ratio=="SEC":
            print("Answer:{}".format(math.pow(math.cos(angle),-1)))
        elif ratio=="cot" or ratio=="Cot" or ratio=="COT":
            print("Answer:{}".format(math.pow(math.tan(angle),-1)))
        else:
            print("Your input is wrong , please check it out and try again.")
    elif o1==3:
        operat=int(input("Which operation do you want:\n 1 for (a+b)^n\n 2 for (a-b)^n\n 3 for (a^n+b^n)\n 4 for (a^n-b^n)\n 5 for x^n\n 6 for x^1/2\n\t: "))
        if operat==1:
            a=int(input("Input the value of a here:"))
            b=int(input("Input the value of b here:"))
            n=int(input("Input the value of n here:"))
            print("Answer:{}".format(math.pow((a+b),n)))
        elif operat==2:
            a=int(input("Input the value of a here:"))
            b=int(input("Input the value of b here:"))
            n=int(input("Input the value of n here:"))
            print("Answer:{}".format(math.pow((a-b),n)))
        elif operat==3:
            a=int(input("Input the value of a here:"))
            b=int(input("Input the value of b here:"))
            n=int(input("Input the value of n here:"))
            print("Answer:{}".format((math.pow(a,n))+(math.pow(b,n))))
        elif operat==4:
            a=int(input("Input the value of a here:"))
            b=int(input("Input the value of b here:"))
            n=int(input("Input the value of n here:"))
            print("Answer:{}".format((math.pow(a,n))-(math.pow(b,n))))
        elif operat==5:
            x=int(input("Input the value of x here:"))
            n=int(input("Input the value of n here:"))
            print("Answer:{}".format(math.pow(x,n)))
        elif operat==6:
            x=int(input("Input the value of x here:"))
            if x==-1:
                print("Answer:{}".format("i"))
            else:
                print("Answer:{}".format(math.sqrt(x)))
        else:
            print("Your input is wrong , please check it out and try again.")
    elif o1==4:
       end()
    else:
        print("Your input is wrong , please check it out and try again.")
    print("-"*60)
calculate()
def again():
    last=int(input("Do you want to carry on your calculation or exit:\n Type 1 to calculate\n Type 2 to exit\n\t:"))
    if last==1:
        calculate()
        again()
    elif last==2:
      end()
    else:
        again()
again()