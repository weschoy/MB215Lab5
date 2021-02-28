from EmployeeClass import Employee

dictName={47899:"Susan Meyers",39119:"Mark Jones",81774:"Joy Rogers"}
dictDepartment={47899:"Accounting",39119:"IT",81774:"Manufacturing"}
dictJob={47899:"Vice President",39119:"Programmer",81774:"Engineer"}

nloop=0

while nloop==0:
    try:
        print("Enter 1 to look up an employee in the dictionary")
        print("Enter 2 to add a new employeee to the dictionary")
        print("Enter 3 to change an existing employee's name, department, and job title in the dictionary")
        print("Enter 4 to delete an employee from the dictionary")
        print("Enter any other number to quit the program")
        nInput=int(input())
        if nInput==1:
            try:
                nID=int(input("Enter the ID number of the employee you're looking for: "))
                User=Employee(dictName.get(nID),nID,dictDepartment.get(nID),dictJob.get(nID))
                print("\n",User,"\n")
            except:
                print("Employee not found \n")
        elif nInput==2:
            sName=input("Please enter the new employee's name: ")
            nID=int(input("Please enter the new employee's ID number: "))
            sDepartment=input("Please enter the new employee's department: ")
            sJob=input("Please enter the new employee's job title: ")
            dictName[nID]=sName
            dictDepartment[nID]=sDepartment
            dictJob[nID]=sJob
            User=Employee(dictName.get(nID),nID,dictDepartment.get(nID),dictJob.get(nID))
            print("Employee added!")
            print("\n",User,"\n")
        elif nInput==3:
            print("Insert the the employee's changed information below, if there are any changes. If not, enter the original information")
            sName=input("Please enter the employee's name: ")
            nID=int(input("Please enter the employee's ID number: "))
            sDepartment=input("Please enter the employee's department: ")
            sJob=input("Please enter the employee's job title: ")
            dictName[nID]=sName
            dictDepartment[nID]=sDepartment
            dictJob[nID]=sJob
            User=Employee(dictName.get(nID),nID,dictDepartment.get(nID),dictJob.get(nID))
            print("Employee's information changed!")
            print("\n",User,"\n")
        elif nInput==4:
            try:
                nID=int(input("Please enter the employee's ID number to delete them from the system: "))
                del dictName[nID]
                del dictDepartment[nID]
                del dictJob[nID]
                print("Employee's information deleted")
            except:
                print("Employee not found. Please try again")
        else: 
            nloop=1
    except:
        print("Please enter a valid option \n")


print("Bye! See you next time!")
