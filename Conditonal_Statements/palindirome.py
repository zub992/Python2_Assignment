string=input("Enter the String : ")
if string.lower()==string[::-1].lower():
    print("This is the Palindromic Sequence")
else:
    print("This is not palindromic Sequence ")