from __future__ import print_function
from pyexpat.errors import codes
from re import X
import tkinter as tk
from tkinter import END, Y, Button, IntVar, StringVar, filedialog, Place
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
    windowAddSubject.geometry("500x450")
    lbl = tk.Label(windowAddSubject, text="Agregar Curso")
    lbl.place(x=210, y=20, width=100, height=30)
    
    code = StringVar()
    name = StringVar()
    prerequisite = StringVar()
    semester = StringVar()
    requested = StringVar()
    credi = StringVar()
    status =StringVar()
    
    txt = tk.Entry(windowAddSubject, textvariable=code)
    txt.place(x=160, y=80, width=200, height=30)
    txt1 = tk.Entry(windowAddSubject, textvariable=name)
    txt1.place(x=160, y=120, width=200, height=30)
    txt2 = tk.Entry(windowAddSubject, textvariable=prerequisite)
    txt2.place(x=160, y=160, width=200, height=30)
    txt3 = tk.Entry(windowAddSubject, textvariable=requested)
    txt3.place(x=160, y=200, width=200, height=30)
    txt4 = tk.Entry(windowAddSubject, textvariable=semester)
    txt4.place(x=160, y=240, width=200, height=30)
    txt5 = tk.Entry(windowAddSubject, textvariable=credi)
    txt5.place(x=160, y=280, width=200, height=30)
    txt6 = tk.Entry(windowAddSubject, textvariable=status)
    txt6.place(x=160, y=320, width=200, height=30)
    
    def addS():
        Subjects.addSubject(code.get(), name.get(), prerequisite.get(), requested.get(), semester.get(), credi.get(), status.get())
    
    btn = tk.Button(windowAddSubject, text="Agregar Curso", command=addS)
    btn.place(x=160, y=360, width=200, height=30)
    btn2 = tk.Button(windowAddSubject, text="Regresar", command=windowAddSubject.destroy)
    btn2.place(x=20, y=20, width=100, height=30) 
    
def window_deleteSubject():
    windowDeleteSubject = tk.Toplevel()
    windowDeleteSubject.geometry("500x250")
    
    code = StringVar()
    entry = tk.Entry(windowDeleteSubject, textvariable=code)
    entry.place(x=50, y=70, width=400, height=60)
    
    def delete():
        Subjects.deleteSubject(code.get())
    
    btn = tk.Button(windowDeleteSubject, text="Eliminar Curso", command=delete)
    btn.place(x=50, y=150, width=400, height=35)
    btn1 = tk.Button(windowDeleteSubject, text="Regresar", command=windowDeleteSubject.destroy)
    btn1.place(x=20, y=20, width=100, height=30)
    
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
    windowManageSubjects.geometry("500x450")
    lbl = tk.Label(windowManageSubjects, text="Gestionar Cursos")
    lbl.place(x=205, y=20)
    btn = tk.Button(windowManageSubjects, text="Listar Cursos", command=window_viewSubjects)
    btn.place(x=180, y=80, width=150, height=50)
    btn1 = tk.Button(windowManageSubjects, text="Mostrar Cursos", command=window_showSubject)
    btn1.place(x=180, y=140, width=150, height=50)
    btn2 = tk.Button(windowManageSubjects, text="Agregar Cursos", command=window_addSubject)
    btn2.place(x=180, y=200, width=150, height=50)
    btn3 = tk.Button(windowManageSubjects, text="Editar Cursos")
    btn3.place(x=180, y=260, width=150, height=50)
    btn4 = tk.Button(windowManageSubjects, text="Eliminar Cursos", command=window_deleteSubject)
    btn4.place(x=180, y=320, width=150, height=50)
    btn5 = tk.Button(windowManageSubjects, text="Regresar", command=windowManageSubjects.destroy)
    btn5.place(x=180, y=380, width=150, height=50)
    
#ventana de menú principal
window = tk.Tk()
window.geometry("500x400")
#window.eval('tk::PlaceWindow . center')
lbl1 = tk.Wm.title(window, "Gestión de Cursos Ingeniería")
lbl2 = tk.Label(window, text="Nombre del Curso: Lab. Lenguajes Formales y de Programación")
lbl2.place(x=75,y=40)
lbl3 = tk.Label(window, text="Nombre del Estudiante: Aldo Saúl Vásquez Moreira")
lbl3.place(x=120,y=60)
lbl4 = tk.Label(window, text="Carné del Estudiante: 202109754")
lbl4.place(x=160, y=80)

#botones de menú principal
b = tk.Button(window, text="Cargar Archivo", command=window_openFile)
b.place(x=180, y=120, width=150, height=50)
b1 = tk.Button(window, text="Gestionar Cursos", command=window_manageSubjects)
b1.place(x=180, y=180, width=150, height=50)
b2 = tk.Button(window, text="Conteo de Créditos")
b2.place(x=180, y=240, width=150, height=50)
b3 = tk.Button(window, text="Salir", command=window.destroy)
b3.place(x=180, y=300, width=150, height=50)

window.mainloop()