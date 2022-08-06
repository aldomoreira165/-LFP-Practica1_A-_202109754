from __future__ import print_function
from pyexpat.errors import codes
import tkinter as tk
from tkinter import END, Button, IntVar, StringVar, filedialog
from tkinter import ttk
from tokenize import String
from types import CodeType
from Subjects import Subjects

#funciones
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
     
def window_addSubject():
    windowAddSubject = tk.Toplevel()
    windowAddSubject.geometry("300x300")
    tk.Label(windowAddSubject, text="Agregar Curso").pack()
    
    code = StringVar()
    name = StringVar()
    prerequisite = StringVar()
    semester = StringVar()
    requested = StringVar()
    credi = StringVar()
    status =StringVar()
    
    tk.Entry(windowAddSubject, textvariable=code).pack()
    tk.Entry(windowAddSubject, textvariable=name).pack()
    tk.Entry(windowAddSubject, textvariable=prerequisite).pack()
    tk.Entry(windowAddSubject, textvariable=requested).pack()
    tk.Entry(windowAddSubject, textvariable=semester).pack()
    tk.Entry(windowAddSubject, textvariable=credi).pack()
    tk.Entry(windowAddSubject, textvariable=status).pack()
    
    def addS():
        Subjects.addSubject(code.get(), name.get(), prerequisite.get(), requested.get(), semester.get(), credi.get(), status.get())
    
    tk.Button(windowAddSubject, text="Agregar Curso", command=addS).pack()
    tk.Button(windowAddSubject, text="Regresar", command=windowAddSubject.destroy).pack()  
    
def window_deleteSubject():
    windowDeleteSubject = tk.Toplevel()
    windowDeleteSubject.geometry("300x300")
    
    code = StringVar()
    tk.Entry(windowDeleteSubject, textvariable=code).pack()
    
    def delete():
        Subjects.deleteSubject(code.get())
    
    tk.Button(windowDeleteSubject, text="Eliminar Curso", command=delete).pack()
    tk.Button(windowDeleteSubject, text="Regresar", command=windowDeleteSubject.destroy).pack()
    
def window_showSubject():
    windowShowSubject = tk.Toplevel()
    windowShowSubject.geometry("300x300")
    codeToLookFor = StringVar()
    tk.Entry(windowShowSubject, textvariable=codeToLookFor).pack()
    
    def lookinFor():
        Subjects.showSubject(codeToLookFor)
    
    tk.Button(windowShowSubject, text="Verificar", command=lookinFor).pack()
    tk.Button(windowShowSubject, text="Regresar", command=windowShowSubject.destroy).pack()

def window_manageSubjects():
    windowManageSubjects = tk.Toplevel()
    windowManageSubjects.geometry("300x300")
    tk.Label(windowManageSubjects, text="Gestionar Cursos").pack()
    tk.Button(windowManageSubjects, text="Listar Cursos", command=window_viewSubjects).pack()
    tk.Button(windowManageSubjects, text="Mostrar Cursos", command=window_showSubject).pack()
    tk.Button(windowManageSubjects, text="Agregar Cursos", command=window_addSubject).pack()
    tk.Button(windowManageSubjects, text="Editar Cursos").pack()
    tk.Button(windowManageSubjects, text="Eliminar Cursos", command=window_deleteSubject).pack()
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