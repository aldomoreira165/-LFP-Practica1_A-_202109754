from __future__ import print_function
import code
from pyexpat.errors import codes
import tkinter as tk
from tkinter import END, Button, IntVar, StringVar, filedialog
from tkinter import ttk
from tkinter.font import names
from unicodedata import name
from urllib import request
from Subjects import Subjects

global codeX
code = 0
global nameS
nameS = ""
global prerequisiteS
prerequisiteS = 0
global semesterS
semesterS = 0
global requestedS
requestedS = 0
global crediS
crediS = 0
global statusS
statusS = 0

#funciones

def saludo():
    print('Hola')

def imprimir():
        print('HOLIS')

def searchFile():
   file = filedialog.askopenfilename(title="Buscar archivo", filetypes=(("Tipo de archivos", 
    "*.csv"), ("Archivos csv", "*.csv")))
   
   fileToRead = open(file, "r")
   
   for i in fileToRead.readlines():
       data = i.split(",")
       sub = Subjects(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
       Subjects.subjects_list.append(sub)

def printValues():
    longitud = len(Subjects.subjects_list)
    for i in range(0, longitud):
        print(Subjects.subjects_list[i].code+ "," + Subjects.subjects_list[i].name)              

def window_openFile():
    windowOpenFile = tk.Toplevel()
    windowOpenFile.geometry("300x300")
    tk.Label(windowOpenFile, text="Cargar Archivo").pack()
    tk.Button(windowOpenFile, text="Buscar Archivo", command=searchFile).pack()
    tk.Button(windowOpenFile, text="Print", command=printValues).pack()
    tk.Button(windowOpenFile, text="Regresar", command=windowOpenFile.destroy).pack()
    
def window_viewSubjects():
    windowViewSubjects = tk.Toplevel()
    windowViewSubjects.geometry("500x500")
    table = ttk.Treeview(windowViewSubjects, columns=("#0","#1","#2","#3","#4","#5"))
    table.grid(row=1, column=0, columnspan=2)
    table.heading("#0", text="Código")
    table.heading("#1", text="Nombre")
    table.heading("#2", text="Pre")
    table.heading("#3", text="Obligatorio")
    table.heading("#4", text="Semestre")
    table.heading("#5", text="Créditos")
    table.heading("#6", text="Estado")
    
    for data in Subjects.subjects_list:
        table.insert('',0, text=data.code, values=(data.name, data.prerequisites, data.required, 
        data.semester, data.credit, data.status))
        
def addS():
    Subjects.subjects_list.append(codeX, nameS, prerequisiteS, semesterS, requestedS, crediS, statusS) 

def window_addSubject():
    windowAddSubject = tk.Toplevel()
    windowAddSubject.geometry("300x300")
    tk.Label(windowAddSubject, text="Agregar Curso").pack()
    codeX = IntVar()
    nameS = StringVar()
    prerequisiteS = IntVar()
    semesterS = IntVar()
    requestedS = IntVar()
    crediS = IntVar()
    statusS = IntVar()
    
    tk.Entry(windowAddSubject, textvariable=codeX).pack()
    tk.Entry(windowAddSubject, textvariable=nameS).pack()
    tk.Entry(windowAddSubject, textvariable=prerequisiteS).pack()
    tk.Entry(windowAddSubject, textvariable=semesterS).pack()
    tk.Entry(windowAddSubject, textvariable=requestedS).pack()
    tk.Entry(windowAddSubject, textvariable=crediS).pack()
    tk.Entry(windowAddSubject, textvariable=statusS).pack()
    
    tk.Button(windowAddSubject, text="Agregar Curso", command=addS).pack()
    tk.Button(windowAddSubject, text="Regresar", command=windowAddSubject.destroy).pack()   

def window_manageSubjects():
    windowManageSubjects = tk.Toplevel()
    windowManageSubjects.geometry("300x300")
    tk.Label(windowManageSubjects, text="Gestionar Cursos").pack()
    tk.Button(windowManageSubjects, text="Listar Cursos", command=window_viewSubjects).pack()
    tk.Button(windowManageSubjects, text="Agregar Cursos", command=window_addSubject).pack()
    tk.Button(windowManageSubjects, text="Editar Cursos").pack()
    tk.Button(windowManageSubjects, text="Eliminar Cursos").pack()
    tk.Button(windowManageSubjects, text="Regresar", command=windowManageSubjects.destroy).pack()
    
#ventana de menú principal
window = tk.Tk()
window.geometry("500x500")
tk.Wm.title(window, "Gestión de Cursos Ingeniería")
tk.Label(window, text="Nombre del Curso: Lab. Lenguajes Formales y de Programación").pack()
tk.Label(window, text="Nombre del Estudiante: Aldo Saúl Vásquez Moreira").pack()
tk.Label(window, text="Carné del Estudiante: 202109754").pack()

#botones de menú principal
tk.Button(window, text="Cargar Archivo", command=window_openFile).pack()
tk.Button(window, text="Gestionar Cursos", command=window_manageSubjects).pack()
tk.Button(window, text="Conteo de Créditos").pack()
tk.Button(window, text="Salir", command=window.destroy).pack()

window.mainloop()