from tkinter import *
import csv
import random


y_car = []
def random_car():
    with open('cars.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            x_car = ({'mark':row['Марка'], 'model':row['Модель'], 's_year':row['Год от'], 'e_year':row['Год до']}) 
            y_car.extend([x_car])
    return 0

random_car()
model_c = random.choice(y_car)
print(model_c)
model_g = model_c.get('mark')
print(model_g)
root = Tk()

root.title("Рандомайзер авто")
root.geometry("600x480")

label = Label(text=model_g)
label.pack()

root.mainloop()