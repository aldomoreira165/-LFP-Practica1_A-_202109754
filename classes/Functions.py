from tkinter import messagebox
from Subjects import Subject
import tkinter as tk

def addSubject(code, name, prerequisites, required, semester, credit, status):
        newSubject = Subject(code, name, prerequisites,required, semester, credit, status)
        Subject.subjects_list.append(newSubject)
        print(len(Subject.subjects_list))

def deleteSubject(codeParameter):
    answer = False;
    longitude = len(Subject.subjects_list)
    print(longitude)
    for i in range(longitude):
        if Subject.subjects_list[i].code == codeParameter:
            Subject.subjects_list.pop(i)
            answer = True    
            break
    
    if answer == True:
         messagebox.showinfo(message="Curso eliminado correctamente.", title="Operación realizada con éxito")
    else:
        messagebox.showerror(message="Curso no encontrado.", title="Operación no realizada.")
            
            
def modifySubject(position,code, name, prerequisites, required, semester, credit, status):
    Subject.subjects_list[position].code = code
    Subject.subjects_list[position].name = name
    Subject.subjects_list[position].prerequisites = prerequisites
    Subject.subjects_list[position].required = required
    Subject.subjects_list[position].semester = semester
    Subject.subjects_list[position].credit = credit
    Subject.subjects_list[position].status = status
    messagebox.showinfo(message="Curso modificado correctamente.", title="Operación realizada con éxito")
                
def showSubject(codeParameter):
    longitude = len(Subject.subjects_list)
    for i in range(longitude):
        if Subject.subjects_list[i].code == codeParameter:
            var = 1
            break
        else: 
            var = 0
    
    if var == 1:
        messagebox.showinfo(message="Curso encontrado con éxito.", title="Operación realizada con éxito")
        return True
    else:
        messagebox.showerror(message="Curso no encontrado.", title="Operación no realizada") 
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

def requiredCredits(semester):
    counter = 0
    longitude = len(Subject.subjects_list)
    for i in range(longitude):
        if Subject.subjects_list[i].required == "1" and Subject.subjects_list[i].semester <= semester:
            counter += int(Subject.subjects_list[i].credit)
    return counter

def requiredCreditsNA(semester):
    counter = 0
    longitude = len(Subject.subjects_list)
    for i in range(longitude):
        if Subject.subjects_list[i].semester == semester and Subject.subjects_list[i].status == "0":
            counter += int(Subject.subjects_list[i].credit)
    return counter

def requiredCreditsNC(semester):
    counter = 0
    longitude = len(Subject.subjects_list)
    for i in range(longitude):
        if Subject.subjects_list[i].semester == semester and Subject.subjects_list[i].status == "1":
            counter += int(Subject.subjects_list[i].credit)
    return counter

def requiredCreditsNP(semester):
    counter = 0
    longitude = len(Subject.subjects_list)
    for i in range(longitude):
        if Subject.subjects_list[i].semester == semester and Subject.subjects_list[i].status == "-1":
            counter += int(Subject.subjects_list[i].credit)
    return counter