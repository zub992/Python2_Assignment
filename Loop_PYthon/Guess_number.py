correct_num=30
guess_num=None
while(correct_num!=guess_num):
    guess_num=int(input("Enter the number :"))

    if(guess_num>correct_num):
        print("Too High! Try Again")
    elif(guess_num<correct_num):
        print("Too Low! Try Again")

    else:
        print("Congradulation!You Guess the Correct Number")