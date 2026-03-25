#List containg square number from  1 to 10
list_square=[x*x for x in range(1,11)]
print(list_square)
#checking list containg leap year or not
leap_year=[]
not_leap_year=[]
for year in list_square:
    if((year%4 ==0 and year %100!=0) or(year %400==0)):
        leap_year.append(year)
    else:
        not_leap_year.append(year)
print("Leap years are \n",leap_year)
print("Not leap year \n",not_leap_year)
#funtion to return array that are even
even_array=[]
def even(list_square):
    for i in list_square:
        if i%2==0:
            even_array.append(i)
    return even_array
print("array containig even array is \n",even(list_square))
#print member of 1st array present in second array

member=[x for x in list_square if x in even_array]
print(f"members present in both arrays are:\n",member)

