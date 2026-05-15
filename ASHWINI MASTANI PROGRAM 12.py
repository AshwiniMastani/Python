#python program to check whether a string is palindrome or not

string=input("enter a string")
reverse_string=string[::-1]

if string== reverse_string:
    print("the string is a palindrome.")
else:
    print("the string is not palindrome.")
    
