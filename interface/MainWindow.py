from fileinput import filename
from pickletools import long1
import tkinter as tk
from tkinter import END, filedialog
from tkinter import ttk
from subjects import subjects

#funciones

def closeWindow():
    window.destroy()
    
def searchFile():
   file = filedialog.askopenfilename(title="Buscar archivo", filetypes=(("Tipo de archivos", 
    "*.csv"), ("Archivos csv", "*.csv")))
   
   fileToRead = open(file, "r")
   
   for i in fileToRead.readlines():
       data = i.split(",")
       sub = subjects(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
       subjects.subjects_list.append(sub)

def printValues():
    longitud = len(subjects.subjects_list)
    for i in range(0, longitud):
        print(subjects.subjects_list[i].code+ "," + subjects.subjects_list[i].name)              

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
    table = ttk.Treeview(windowViewSubjects, columns=("#0","#1","#2","#3","#4","#5","#6"))
    table.grid(row=1, column=0, columnspan=1)
    table.heading("#0", text="Código")
    table.heading("#1", text="Nombre")
    table.heading("#2", text="Pre")
    table.heading("#3", text="Obligatorio")
    table.heading("#4", text="Semestre")
    table.heading("#5", text="Créditos")
    table.heading("#6", text="Estado")
    
    for data in subjects.subjects_list:
        table.insert("",END, values=data)
    
    
    
def window_manageSubjects():
    windowManageSubjects = tk.Toplevel()
    windowManageSubjects.geometry("300x300")
    tk.Label(windowManageSubjects, text="Gestionar Cursos").pack()
    tk.Button(windowManageSubjects, text="Listar Cursos", command=window_viewSubjects).pack()
    tk.Button(windowManageSubjects, text="Agregar Cursos").pack()
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
tk.Button(window, text="Salir").pack()

window.mainloop()