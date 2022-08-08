from os import stat
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
        
def editSubject(code, name, prerequisites, required, semester, credit, status):
    longitude = len(Subject.subjects_list)
    for i in range(longitude):
        if Subject.subjects_list[i].code == codeParameter:
            Subject.subjects_list[i].code = code
            Subject.subjects_list[i].name = name
            Subject.subjects_list[i].prerequisite = prerequisites
            Subject.subjects_list[i].required = required
            Subject.subjects_list[i].semester = semester
            Subject.subjects_list[i].credit = credit
            Subject.subjects_list[i].status = status
            break
                
def showSubject(codeParameter):
    longitude = len(Subject.subjects_list)
    for i in range(longitude):
        if Subject.subjects_list[i].code == codeParameter:
            print("Hola mundo")
            