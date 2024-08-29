dictionary={"monday":[],"tuesday":[],"wed":[],"thurs":[],"friday":[]}

def mark_present(name,day):
    if name in dictionary[day]:
        return
    else:
        dictionary[day].append(name)

def mark_absent(name,day):
    if name not in dictionary[day]:
        return 
    else:
        dictionary[day].remove(name)

def is_present(name,day):
    if name in dictionary[day]:
        return True
    else:
        return False

def display(day):
   print(dictionary[day])

day=input("day")
n=input("no. of students:")
names=[]
for i in range(0,int(n)):
    name=input("name of student")
    names.append(name)
    mark_present(name,day)

mark_present("mihir","monday")
mark_present("sanvi","monday")
print(is_present("sanvi","monday"),is_present("ishika","monday"))
mark_absent("mihir","monday")
display("monday")

