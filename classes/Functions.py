from tkinter import messagebox
from Subjects import Subject

#funcion para agregar cursos de forma individual
def addSubjectIndividual(code, name, prerequisites, required, semester, credit, status):
    longitude = len(Subject.subjects_list)
    answer = False
    for i in range(longitude):
        if Subject.subjects_list[i].code == code:
            answer = True
            break
         
    if answer == True:
        messagebox.showerror(message="El curso que desea agregar ya existe.", title="Operación no realizada.")
    elif (required != "0" and required != "1"):
        messagebox.showerror(message="Dato no aceptado en el campo 'Obligatorio'.", title="Operación no realizada.")
    elif (semester != "1" and semester != "2" and semester != "3" and semester != "4" and semester != "5" and semester != "6" and semester != "7" and semester != "8" and semester != "9" and semester != "10"):
        messagebox.showerror(message="Dato no aceptado en el campo 'Semestre'.", title="Operación no realizada.")
    elif (status != "1" and status != "0" and status != "-1"):
        messagebox.showerror(message="Dato no aceptado en el campo 'Estado'.", title="Operación no realizada.")
    else:
        newSubject = Subject(code, name, prerequisites,required, semester, credit, status)
        Subject.subjects_list.append(newSubject)
        messagebox.showinfo(message="Curso agregado correctamente.", title="Operación realizada con éxito")
        print(len(Subject.subjects_list))

#funcion para agregar archivo csv
def addSubjectFile(code, name, prerequisites, required, semester, credit, status):
    added = False
    longitude = len(Subject.subjects_list)
    for i in range(longitude):
        if Subject.subjects_list[i].code == code:
            added = True
            break
     
    if (added == False):    
        newSubject = Subject(code, name, prerequisites, required, semester, credit, status)
        Subject.subjects_list.append(newSubject)
        print(len(Subject.subjects_list))

#funcion para eliminar un curso
def deleteSubject(codeParameter):
    answer = False
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

#funcion para modificar un curso
def modifySubject(position, code, name, prerequisites, required, semester, credit, status):
    longitude = len(Subject.subjects_list)
    answer = False
         
    if (required != "0" and required != "1"):
        messagebox.showerror(message="Dato no aceptado en el campo 'Obligatorio'.", title="Operación no realizada.")
    elif (semester != "1" and semester != "2" and semester != "3" and semester != "4" and semester != "5" and semester != "6" and semester != "7" and semester != "8" and semester != "9" and semester != "10"):
        messagebox.showerror(message="Dato no aceptado en el campo 'Semestre'.", title="Operación no realizada.")
    elif (status != "1" and status != "0" and status != "-1"):
        messagebox.showerror(message="Dato no aceptado en el campo 'Estado'.", title="Operación no realizada.")
    else:
        Subject.subjects_list[position].code = code
        Subject.subjects_list[position].name = name
        Subject.subjects_list[position].prerequisites = prerequisites
        Subject.subjects_list[position].required = required
        Subject.subjects_list[position].semester = semester
        Subject.subjects_list[position].credit = credit
        Subject.subjects_list[position].status = status
        messagebox.showinfo(message="Curso modificado correctamente.", title="Operación realizada con éxito")

#funcion para mostrar un curso
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

#funcion para saber si un curso existe    
def searchPosition(codeParameter):
    longitude = len(Subject.subjects_list)
    for i in range(longitude):
        if Subject.subjects_list[i].code == codeParameter:
            return i

#funcion para contar creditos        
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

#funcion para contar creditos de cursos obligatorios
def requiredCredits(semester):
    counter = 0
    longitude = len(Subject.subjects_list)
    for i in range(longitude):
        if Subject.subjects_list[i].required == "1" and not Subject.subjects_list[i].semester > semester:
            counter += int(Subject.subjects_list[i].credit)
    return counter

#funcion para contar creditos acumulados hasta semestre N de cursos aprobados
def requiredCreditsNA(semester):
    counter = 0
    longitude = len(Subject.subjects_list)
    for i in range(longitude):
        if Subject.subjects_list[i].semester == semester and Subject.subjects_list[i].status == "0":
            counter += int(Subject.subjects_list[i].credit)
    return counter

#funcion para contar creditos acumulados hasta semestre N de cursos asignados
def requiredCreditsNC(semester):
    counter = 0
    longitude = len(Subject.subjects_list)
    for i in range(longitude):
        if Subject.subjects_list[i].semester == semester and Subject.subjects_list[i].status == "1":
            counter += int(Subject.subjects_list[i].credit)
    return counter

#funcion para contar creditos acumulados hasta semestre N de cursos pendientes
def requiredCreditsNP(semester):
    counter = 0
    longitude = len(Subject.subjects_list)
    for i in range(longitude):
        if Subject.subjects_list[i].semester == semester and Subject.subjects_list[i].status == "-1":
            counter += int(Subject.subjects_list[i].credit)
    return counter