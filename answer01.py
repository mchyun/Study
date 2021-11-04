"""Ask the user to enter a roman numeral
Validate the number to make sure it follows all the rules.
If the roman numeral is valid then you should convert it to its Arabic equivalent.
Print out the roman numeral and its Arabic equivalent.
by using a dictionary to map each single character roman numeral to the correct Arabic number."""

def solution(c):
    x=['I','V','X','L','C','D','M']
    rule = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    y=list(c)
    count=0
    for n in y:
        if(n not in x and n!=' '):
            count+=1
    if(count==0):
        number = 0
        for m in range(len(c)):
            if m > 0 and rule[c[m]] > rule[c[m - 1]]:
                number += rule[c[m]] - 2 * rule[c[m - 1]]
            else:
                number += rule[c[m]]
    else:
        number=-1
    return number
c=input("Enter Roman values : ")
z=solution(c)
if(z==-1):
    print("The Roman value is incorrect.");
else:
    print("Arabic value corresponding to Roman number "+c+" is "+str(z))
