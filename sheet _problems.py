#Q1
# Create a function that takes an integer as an argument and returns "Even" for even
#numbers or "Odd" for odd numbers.
def type_of_number(x):
    if x%2==0:
        return f"{x}is even"
    elif x%2==1:
       return f"{x} is odd "
x=int(input("enter the number").strip())
result=type_of_number(x)  
print (result)

         
#Q2
# Given a string, you have to return a string in which each character (case-sensitive) is
#repeated once.
def repeated_character(word):
    for i in word:
        print(i)
        print(i)
    return f"{i}"
word=input("enter the word")       
repeated_character(word)     
result=repeated_character
print(result)
#Q3  You get an array of numbers, return the sum of all of the positives ones.
#Example [1,-4,7,12] => 1 + 7 + 12 = 20
#Note: if there is nothing to sum, the sum is default to 0 .
def new_poitive_numbers(numbers):
    #positive_numbers=[]
    numbers=[1,-4,7,12]
    for num in numbers:
      #  if num>=0:
          #  positive_numbers.append(num)
       # elif num<=0:
       #     result=0      
    #result=sum(positive_numbers) 
   # return result
result=new_poitive_numbers([1,-4,7,12])
print(result)
#Q4  In this simple assignment you are given a number and have to make it negative. But
#maybe the number is already negative?
def make_negative(number):
    if number>=0:
        return(number*-1)
    elif number<=0:
       return(number)
number=int(input("enter the number")) 
result=make_negative(number)  
print(result) 
 #Q5 Complete the solution so that it reverses the string passed into it.
#def reverses(any_word):
  #  return any_word[ : :-1]
any_word="mona"
result=reverses(any_word)
print(result)
#Q6
def take_boolean(value):
    if value.capitalize()=="True":
      return "Yes"
    elif value.capitalize()=="False":
       return "No" 
value =input("enter the value")
result=take_boolean(value) 
print(result) 
#name='mona'
#Q7 write function to Remove first char and last char in the word but the word have 2 chars don’t
#remove it
def remove_char(word):
    lenght=len(word) 
    if lenght>2:
        return word[1:-1]
    elif lenght<=2:
        return word[ : : ] 
word=input("enter the word").strip() 
result=remove_char(word)  
print(result)  
list1=[1,2,3,4]
total=sum(list1)
print(total)
#Q9)Complete the square sum function so that it squares each number passed into it and
#then sums the results together.
#For example, for [1, 2, 2] it should return 9 because 1**2+2**2+2**2=9.
def sum_squares(numbers):
    squares_numbers=[]
    numbers=[1,2,2]
    for num in numbers:
        squares=num**2
        squares_numbers.append(squares) 
    total=sum(squares_numbers)
    return total
numbers=[1,2,2]    
result=sum_squares(numbers) 
print(result) 
 #Q10 Return the number (count) of vowels in the given string.
#We will consider a , e , i , o , u as vowels for this Kata (but not y ).
#The input string will only consist of lower case letters and/or spaces.
def count_the_vowel(sentence):    
    new_vowel=[]       
    vowel="aioue"
   # sentence=input("enter the word")
    for i in sentence:
        if i in vowel:
            new_vowel.append(i)
    print(new_vowel)
    answer=len(new_vowel)
    return answer
sentence=input("enter the word")
result=count_the_vowel(sentence)
print(result)
#Q11 Welcome. In this kata, you are asked to square every digit of a number and concatenate
def squared(number):
    answer=''
    #number=int(input("enter the number"))
    for i in str(number):
        square=int(i)**2
        answer+=str(square)
    #print(answer)
    return(answer)
number=int(input("enter the number"))
result=squared(number)
print(result)  
#q8
s_new=''
s1=input("enter s1")
s2=input("enter s2")
for i in s1:
    if i .islower():
        h=i.capitalize()
        s_new+=(h)
    elif i.isupper():
        y=i.lower() 
        s_new+=y
if s_new==s2:
    print(True)
else:
    print(False) 
#q12 For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs
def vowels_removing(sentence):
    sentence="i have two brothers"
    v=["a","i","o","u","e"]
    for h in sentence:
        if h in v:
            new_sentence=sentence.replace(h, "")
        return(new_sentence)
sentence="i have two brothers"
result=vowels_removing(sentence)
print(result)
#Q13  In this little assignment you are given a string of space separated numbers, and have to
#return the highest and lowest number.
def highest_and_lowest(numbers):
  for num in numbers:
      numbers= "1 2 3 4 5"
      new_number=numbers.split()
      high=int(max (new_number))
#print(high)
      low= int(min (new_number))
#print(low)
  print(f"{high} {low}")
numbers= "1 2 3 4 5"  
result=highest_and_lowest(numbers)
print(result)
#q15
word="ahmed"
for i in word:
  lenght=len(word)
  k=int(lenght/2)
if k%2==0:
  print((word[k-1])+(word[k]))
elif k%2==1:
   m=int((k+1)/2)
   print(word[m-1])
   #q16
def string_filter(mona):
  lis=[]
  for i in mona:
      if type(i)==int:
          lis.append(i)
  return(lis)
mona=([1,'a','b',0,15])
result=string_filter(mona)
print(result)
#q17
accum=("abcd")
for i in accum:
  print(i.capitalize())
  #q18
#example=("ooxx")
example=input("enter EX")
print(example.count("o"))
print(example.count("x"))
if example.count("o")==example.count("x"):
  print(True)
else:
  print(False)  
  #q19
example=1,-2,2
for i in example:
  if i >0:
     print(True)
  elif i<=0:
    print(False)  

  
















      
  
     
    



 
    




















