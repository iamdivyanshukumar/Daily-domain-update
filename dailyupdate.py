# 1.class to manage daily update of domain

class Domainupdate:
    def addupdate(self):
        with open('latest update.txt', 'a') as file:  # to open a file in append mode to and new update
            data_input = input("Please enter latest update-")  # to get latest update from user
            file.write(data_input + '\n')  # for append data input in file
        print("Latest update is added")

    def view_update(self):
        with open('latest update.txt', 'r') as file:  # to open a file in reading mode to view update
            task = file.read()
        print(task)


# 2. class to manage other tech experience

class other_tech_exp:
    def add_other_tech_exp(self):
        with open('other_tech_exp.txt', 'a') as file:  # to open a file in append mode
            data_input = input("Please enter your experience-")
            file.write(data_input + '\n')
        print("Your experience is added")

    def view_other_tech_exp(self):
        with open('other_tech_exp.txt', 'r') as file:  # to open a file in reading mode
            task = file.read()
        print(task)


# 3. class to manage discussion

class Discussion:
    def add_dis(self):
        with open('add_dis.txt', 'a') as file:  # to open a file in append mode
            data_input = input("Please enter latest update- ")
            file.write(data_input + '\n')

    def view_dis(self):
        with open('add_dis.txt', 'r') as file:  # to open a file in reading mode
            task = file.read()
        print(task)



# 4. class to manage achievements

class Achievement:
    def add_aceive(self):
        with open('achievement.txt', 'a') as file:
            data_input = input("Enter your achievement- ")
            file.write(data_input + '\n')
        print("Achievement is added")

    def view_aceive(self):
        with open('achievement.txt', 'r') as file:
            aceive = file.read()
        print(aceive)

#class to manage tasks for team1
class Team1():
    def add_task_1(self):
        with open('task1.txt', 'a') as file:
            data_input = input("Enter task:- ")
            file.write(data_input + '\n')
        print("Task is added")

    def view_task_1(self):
        with open('taskA.txt', 'r') as file:
            tasks = file.read()
        print(tasks)

#class to manage tasks for team1
class Team2():
    def add_task_2(self):
        with open('task2.txt', 'a') as file:
            data_input = input("Enter task:- ")
            file.write(data_input + '\n')
        print("Task is added")

    def view_task_2(self):
        with open('task2.txt', 'r') as file:
            tasks = file.read()
        print(tasks)

#display team and team member
def team_menu():
    print("1.(Divyanshu,Prince)")
    print("2.(Udit,Kunal)")

#display task menu
def task_menu():
    print("1.To Add Task")
    print("2.To View Tasks")
    print("3.For Exit")

def exp_menu():
    print("1.Add experience")
    print("2.View experience")
    print("3.For Exit")

def achive_menu():
    print("1.Add achievements")
    print("2.View achievements")
    print("3.For Exit")
#handle domain updates

def domain():
    task_menu()
    task_no = input("Enter task no.: ")
    while True:
        if task_no == "1":
            b = Domainupdate()
            b.addupdate()
        elif task_no == "2":
            b = Domainupdate()
            b.view_update()
        elif task_no == "3":
            print("You terminate the program!!")
            break
        else:
            print("Wrong input")
        break

#handle task for Team1
def task1():
    task_menu()
    task_no = input("Enter task no.: ")
    while True:
        if task_no == "2":
            a = Team1()
            a.add_task_1()
        elif task_no == "2":
            a = Team1()
            a.view_task_1()
        elif task_no == "3":
            print("You terminate the program!!")
            break
        else:
            print("Invalid input")
        break

#handle task for Team2
def task2():
    task_menu()
    task_no = input("Enter task no.: ")
    while True:
        if task_no == "1":
            a = Team2()
            a.add_task_2()
        elif task_no == "2":
            a = Team2()
            a.view_task_2()
        elif task_no == "3":
            print("You terminate the program!!")
            break
        else:
            print("Invalid input")
        break

#handle other tech experience
def other_tech():
    exp_menu()
    task_no = input("Choose one of the above: ")
    while True:
        if task_no == "1":
            c = other_tech_exp()
            c.add_other_tech_exp()
        elif task_no == "2":
            c = other_tech_exp
            c.view_other_tech_exp()
        elif task_no == "3":
            print("You terminate the program!!")
            break
        else:
            print("Invalid input")
        break

#handle achivements
def achive():
    achive_menu()
    task_no = input("Choose one of the above: ")
    while True:
        if task_no == "1":
            d = Achievement()
            d.add_aceive()
        elif task_no == "2":
            d = Achievement()
            d.view_aceive()
        elif task_no == "3":
            print("You terminate the program!!")
            break
        else:
            print("Invalid input")
        break

#display of main menu
def main_menu():
    print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
    print("---------------------------------------------------------------------------")
    print("                            DAILY UPDATE OF DOMAIN                         ")
    print("---------------------------------------------------------------------------")
    print("~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
    input("Please Enter your name TO IDENTIFY YOU - ")
    input("enter your UserID- ")

    print("""\n
    Press_1: For Domain Update
    Press_2: For Task Updates
    Press_3: For Discussion
    Press_4: For Other tech exp
    Press_5: For Achievements
    Press_6: For Exit""")

# main function to run the program
def main():
    main_menu()
    press = int(input("Enter any of above no.: "))
    while True:
        if press == 1:
            domain()
            break
        elif press == 2:
            team_menu()
            team_no = input("Enter your team: ")
            if team_no == "1":
                task1()
                break
            elif team_no == "2":
                task2()
                break
            else:
                print("Invalid Team no.")
                break

        elif press == 3:
            while True:
                e = Discussion()
                e.add_dis()
                e.view_dis()
                break

        elif press == 4:
            other_tech()
            break

        elif press == 5:
            achive()
            break

        elif press == 6:
            print("You terminate the program!!")
            break

        else:
            print("Invalid Input")
            break

#execute main funtion
main()