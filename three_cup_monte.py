""" This is a script to play three cup monte"""
from random import shuffle

def generate_three_cups(my_list):
    """ Function to generate shuffled cups"""
    shuffle(my_list)
    return my_list
def create_user_ip():
    """ Function to insert user guess"""
    my_x=''
    while(my_x not in [0,1,2]):
        my_x=int(input("Enter either 0 or 1 or 2"))
    return my_x
def check_equality(data,guess):
    """ Function to check user guess is correct or not"""
    if data[guess]==1:
        print("Wow!You have made a correct guess")
    else:
        print("Sorry, Your answer is not correct. Please try again")
    print(f'Your Guess is at - {guess} index')
    print(f'Ball is in {data}')

if __name__=="__main__":
    my_list_new=[0,0,1]
    data_new=generate_three_cups(my_list_new)
    guess_new=create_user_ip()
    check_equality(data_new,guess_new)
