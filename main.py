
import csv
from csv import writer
import pandas as pd

#read csv file 
df = pd.read_csv('Books.csv')

#The starting function 
def Start():
    start = input("welcome to your book collection. Continue? [Y/N] ")
    if start == 'Y':
        Next()
    else:
        exit()
#function for options
def Next():
    question = input("What would you like to do next? \n View Everything [V] \n Add a Book [A] \n Exit [E] ")
    if question == 'V':
        print(df)
        Next()
    elif question == 'A':
        Add()
    else: 
        exit() 
#function to add a book
def Add():
    
    Name = input("Input Name of Book: ")
    Author = input("Please Enter The Author Name: ")
    Rating = input("Please Enter a Rating On a Scale of 1-10: ")
    with open('Books.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([Name, Author, Rating]) 
    Next()
#main class
class myBook():
    def __init__(self) -> None:
        pass
   
   
    Start()

   
    
