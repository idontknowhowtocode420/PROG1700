#gather Information
import datetime #import global function date/time


userdate, usermonth = input('What year and month were you born?(Please format as YYYY MONTH in values)').split() #take input define it as two ints
if input() == str:
    print('invalid')

if userdate.isalpha(): #decided to use is alpha bool for detecting letter input in either input in month or year
    print('Please do not enter letters for your Year of Birth')
    exit

if usermonth.isalpha():
    print('Please do not enter letters for your Month of Birth')
    exit    
#userdate = int #input now always = int
#usermonth = int


#Value = int(13)
#Value2 = int(2024)

yr = datetime.datetime.now().year #global date and time in varibles, cant define as int until if statements are yet, how am i going to detect future years/invalid months?
mon = datetime.datetime.now().month

if userdate.isdigit():
    yh = int(userdate)

    
    print('You are')
    print(yr - yh)
else: 
    print('Please enter a valid year')
    exit

if usermonth.isdigit():
    mo = int(usermonth)
    print('And')
    op = mo - mon
    print(abs(op))
    print('Months Old')
else:
    print('Please enter a valid Month')
    exit













#while usermonth == Value: #trash code
    #print('Please enter a valid month!')
    #exit


#while userdate < yr:
    #print('Please enter a valid year!')
    #exit
    