# MB215Lab5

1) Car Class
Write a class named Car that has the following data attributes:

__year_model (for the car’s year model)
__make (for the make of the car)
__speed (for the car’s current speed)
The Car class should have an __init__ method that accept the car’s year model and make as arguments. These values should be assigned to the object’s __year_model and __make data attributes. It should also assign 0 to the __speed data attribute.

The class should also have the following methods:

accelerate
The accelerate method should add 5 to the speed data attribute each time it is called.
brake
The brake method should subtract 5 from the speed data attribute each time it is called.
get_speed
The get_speed method should return the current speed.
Next, design a program that creates a Car object, and then calls the accelerate method five times. After each call to the accelerate method, get the current speed of the car and display it. Then call the brake method five times. After each call to the brake method, get the current speed of the car and display it.

2) Employee Class
Write a class named Employee that holds the following data about an employee in attributes:
name, ID number, department, and job title.
Once you have written the class, write a program that creates three Employee objects to hold the following data:

Name	ID Number	Department	Job Title
Susan Meyers	47899	Accounting	Vice President
Mark Jones	39119	IT	Programmer
Joy Rogers	81774	Manufacturing	Engineer
The program should store this data in the three objects and then display the data for each employee on the screen.

3) Employee Management System
This exercise assumes that you have created the Employee class for Programming Exercise 2.
Create a program that stores Employee objects in a dictionary. Use the employee ID number as the key. The program should present a menu that lets the user perform the following actions:

Look up an employee in the dictionary
Add a new employee to the dictionary
Change an existing employee’s name, department, and job title in the dictionary
Delete an employee from the dictionary
Quit the program