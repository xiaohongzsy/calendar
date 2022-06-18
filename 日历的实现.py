def printMonth(year,month):#定义 打印月份（年，月） A：

    #函数体 操作动作
    printMonthTitle(year,month)#打印 月份 标题（年，月）A1
    printMonthBody(year,month)#打印 月份 主体（年，月）A2
    #内 局部变量

def printMonthTitle(year,month):#定义 打印月份标题（年，月） ------打印月份标题----A1.1
    #函数体 操作动作
    #新变量1个：获得月份名称（月）getMonthName（month）
    print("    ",getMonthName(month)," ",year)
    print("-"*30)
    print(" sun  mon  tue  wed  thu  fri  sat")

def printMonthBody(year,month):#月份主体
    startDay=getStartDay(year,month)#开始日期=输入获得的开始日期
    numberOfDaysInMonth=getNumberOfDaysInMonth(year,month)#每月天的数量=获得的月份
    i=0
    for i in range(0,startDay):#历遍0--开始日期
        print(" ",end=" ")#打印空格
    for i in range(1,numberOfDaysInMonth+1):#历遍1---获得日期数+1
        print(format(i,"4d"),end=" ")
        if (i+startDay)%7==0:
            print()

def getMonthName(month):#------A1.1.1
    if month==1:
        monthName="JANUARY"
    elif month==2:
        monthName="February"
    elif month==3:
        monthName="March"
    elif month==4:
        monthName="April"
    elif month==5:
        monthName="May"
    elif month==6:
        monthName="June"
    elif month==7:
        monthName="July"
    elif month==8:
        monthName="August"
    elif month==9:
        monthName="September"
    elif month==10:
        monthName="October"
    elif month==11:
        monthName="November"
    else :
        monthName="December"

    return monthName#------需要的返回值！

def getStartDay(year,month):#-----A1.2.1
    START_DAY_FOR_JAN_1_1800=3 #开始日期从1800年1月1日=3
    totalNumberOfDays=getTotalNumberOfDays(year,month)
    return(totalNumberOfDays+START_DAY_FOR_JAN_1_1800)%7
def getTotalNumberOfDays(year,month):
    total=0
    for i in range(1800,year):
        if isLeapYear(i):
            total=total+366
        else:
            total=total+365
    for i in range(1,month):
        total=total+getTotalNumberOfDays(year,i)
    return total
def getNumberOfDaysInMonth(year,month):
    if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
        return 31
    if month==4 or month==6 or month==9 or month==11:
        return 30
    if month==2:
        return 29 if isLeapYear(year)else 28
    return 0
def isLeapYear(year):
    return year%400==0 or (year%4==0 and year%100!=0)

def main():
    year=eval(input("Enter full year(e.g.,2001):"))
    month=eval(input("Enter month as nunber between 1 and 12:"))
    printMonth(year,month)
main()




















