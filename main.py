
import csv
from csv import writer
import pandas as pd

#read csv file 
df = pd.read_csv('Books.csv')

#The starting function 
def start_input():

    start = input("welcome to your book collection. Continue? [Y/N] ")
    if start == 'Y':
        next_input()
    else:
        exit()

#function for options

def next_input():

    question = input("What would you like to do next? \n View Everything [V] \n Add a Book [A] \n Exit [E] ")
    if question == 'V':
        print(df)
        next_input()
    elif question == 'A':
        add_input()
    else: 
        exit() 

#function to add a book

def add_input():

    Name = input("Input Name of Book: ")
    Author = input("Please Enter The Author Name: ")
    Rating = input("Please Enter a Rating On a Scale of 1-10: ")
    with open('Books.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([Name, Author, Rating]) 
    next_input()

#main class
class myBook():
    def __init__(self) -> None:
        pass
   
   
    start_input()

   
    
