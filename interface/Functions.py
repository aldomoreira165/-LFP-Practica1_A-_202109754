from ast import Sub
from time import process_time_ns
from Subjects import Subject

def addSubject(code, name, prerequisites, required, semester, credit, status):
        newSubject = Subject(code, name, prerequisites,required, semester, credit, status)
        Subject.subjects_list.append(newSubject)
        print(len(Subject.subjects_list))

def deleteSubject(codeParameter):
    longitude = len(Subject.subjects_list)
    print(longitude)
    for i in range(longitude):
        if Subject.subjects_list[i].code == codeParameter:
            Subject.subjects_list.pop(i)
            break
        
def modifySubject(position,code, name, prerequisites, required, semester, credit, status):
    Subject.subjects_list[position].code = code
    Subject.subjects_list[position].name = name
    Subject.subjects_list[position].prerequisites = prerequisites
    Subject.subjects_list[position].required = required
    Subject.subjects_list[position].semester = semester
    Subject.subjects_list[position].credit = credit
    Subject.subjects_list[position].status = status
                
def showSubject(codeParameter):
    longitude = len(Subject.subjects_list)
    for i in range(longitude):
        if Subject.subjects_list[i].code == codeParameter:
            var = 1
            break
        else: 
            var = 0
    
    if var == 1:
        return True
    else: 
        return False
    
def searchPosition(codeParameter):
    longitude = len(Subject.subjects_list)
    for i in range(longitude):
        if Subject.subjects_list[i].code == codeParameter:
            return i
        
def coursesCounter(status):
    counter = 0
    longitude = len(Subject.subjects_list)
    for i in range(longitude):
        if Subject.subjects_list[i].status == status:
            counter += int(Subject.subjects_list[i].credit)
    return counter  

def coursesPCounter(status, required):
    counter = 0
    longitude = len(Subject.subjects_list)
    for i in range(longitude):
        if Subject.subjects_list[i].status == status and Subject.subjects_list[i].required == required:
            counter += int(Subject.subjects_list[i].credit)
    return counter    
            