from __future__ import print_function
from opcode import opname
import tkinter as tk
from tkinter import END, StringVar, filedialog
from tkinter import ttk
from tkinter.font import BOLD
from Subjects import Subject
import Functions as fn
import csv

#funciones
def searchFile():
    file = filedialog.askopenfilename(title="Buscar archivo", filetypes=(("Tipo de archivos", 
    "*.csv"), ("Archivos csv", "*.csv")))
    with open(file) as f:
        reader = csv.reader(f, delimiter=",")
        for data in reader:
            fn.addSubject(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
       
def printValues():  
    longitud = len(Subject.subjects_list)
    for i in range(0, longitud):
        print(Subject.subjects_list[i].code+ "," + Subject.subjects_list[i].name + "," + Subject.subjects_list[i].status + "," + Subject.subjects_list[i].credit)              

def window_openFile():
    windowOpenFile = tk.Toplevel()
    windowOpenFile.geometry("500x200")
    lbl = tk.Label(windowOpenFile, text="Cargar Archivo", font=("Arial", 12, BOLD))
    lbl.place(x = 195, y = 10)
    btn = tk.Button(windowOpenFile, text="Buscar Archivo", command=searchFile, font=("Arial", 10))
    btn.place(x=150, y=80, width=200, height=50)
    btnR = tk.Button(windowOpenFile, text="Regresar", command=windowOpenFile.destroy, font=("Arial", 10))
    btnR.place(x=20, y=10, width=100, height=30)
    
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
    
    for data in Subject.subjects_list:
        table.insert('',0, text=data.code, values=(data.name, data.prerequisites, data.required, 
        data.semester, data.credit, data.status))
     
def window_addSubject():
    windowAddSubject = tk.Toplevel()
    windowAddSubject.geometry("500x450")
    lbl = tk.Label(windowAddSubject, text="Agregar Curso", font=("Arial", 12, BOLD))
    lbl.place(x=200, y=10)
    
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
    
    lbl = tk.Label(windowAddSubject, text="Código", font=("Arial", 10))
    lbl.place(x = 60, y = 80)
    lbl1 = tk.Label(windowAddSubject, text="Nombre", font=("Arial", 10))
    lbl1.place(x = 60, y = 120)
    lbl2 = tk.Label(windowAddSubject, text="Pre-requisitos", font=("Arial", 10))
    lbl2.place(x = 60, y = 160)
    lbl3 = tk.Label(windowAddSubject, text="Obligatorio", font=("Arial", 10))
    lbl3.place(x = 60, y = 200)
    lbl4 = tk.Label(windowAddSubject, text="Semestre", font=("Arial", 10))
    lbl4.place(x = 60, y = 240)
    lbl5 = tk.Label(windowAddSubject, text="Créditos", font=("Arial", 10))
    lbl5.place(x = 60, y = 280)
    lbl6 = tk.Label(windowAddSubject, text="Estado", font=("Arial", 10))
    lbl6.place(x = 60, y = 320)
    
    def addS():
        fn.addSubject(code.get(), name.get(), prerequisite.get(), requested.get(), semester.get(), credi.get(), status.get())
    
    btn = tk.Button(windowAddSubject, text="Agregar Curso", command=addS, font=("Arial", 10))
    btn.place(x=160, y=360, width=200, height=30)
    btn2 = tk.Button(windowAddSubject, text="Regresar", command=windowAddSubject.destroy, font=("Arial", 10))
    btn2.place(x=20, y=10, width=100, height=30) 
    
def window_deleteSubject():
    windowDeleteSubject = tk.Toplevel()
    windowDeleteSubject.geometry("500x250")
    
    code = StringVar()
    entry = tk.Entry(windowDeleteSubject, textvariable=code)
    entry.place(x=50, y=70, width=400, height=60)
    
    def delete():
        fn.deleteSubject(code.get())
    
    btn = tk.Button(windowDeleteSubject, text="Eliminar Curso", command=delete)
    btn.place(x=50, y=150, width=400, height=35)
    btn1 = tk.Button(windowDeleteSubject, text="Regresar", command=windowDeleteSubject.destroy)
    btn1.place(x=20, y=20, width=100, height=30)
    
def window_showSubject():
    windowShowSubject = tk.Toplevel()
    windowShowSubject.geometry("500x500")
    
    codeToSearch = StringVar()
    
    txtM = tk.Entry(windowShowSubject, textvariable=codeToSearch)
    txtM.place(x=160, y=10, width=200, height=30)
    txt = tk.Entry(windowShowSubject)
    txt.place(x=160, y=80, width=200, height=30)
    txt1 = tk.Entry(windowShowSubject)
    txt1.place(x=160, y=120, width=200, height=30)
    txt2 = tk.Entry(windowShowSubject)
    txt2.place(x=160, y=160, width=200, height=30)
    txt3 = tk.Entry(windowShowSubject)
    txt3.place(x=160, y=200, width=200, height=30)
    txt4 = tk.Entry(windowShowSubject)
    txt4.place(x=160, y=240, width=200, height=30)
    txt5 = tk.Entry(windowShowSubject)
    txt5.place(x=160, y=280, width=200, height=30)
    txt6 = tk.Entry(windowShowSubject)
    txt6.place(x=160, y=320, width=200, height=30)
    
    lbl = tk.Label(windowShowSubject, text="Código", font=("Arial", 10))
    lbl.place(x = 60, y = 80)
    lbl1 = tk.Label(windowShowSubject, text="Nombre", font=("Arial", 10))
    lbl1.place(x = 60, y = 120)
    lbl2 = tk.Label(windowShowSubject, text="Pre-requisitos", font=("Arial", 10))
    lbl2.place(x = 60, y = 160)
    lbl3 = tk.Label(windowShowSubject, text="Obligatorio", font=("Arial", 10))
    lbl3.place(x = 60, y = 200)
    lbl4 = tk.Label(windowShowSubject, text="Semestre", font=("Arial", 10))
    lbl4.place(x = 60, y = 240)
    lbl5 = tk.Label(windowShowSubject, text="Créditos", font=("Arial", 10))
    lbl5.place(x = 60, y = 280)
    lbl6 = tk.Label(windowShowSubject, text="Estado", font=("Arial", 10))
    lbl6.place(x = 60, y = 320)
        
    def search():
        result = fn.showSubject(codeToSearch.get())
        
        if  result == True:
            position = fn.searchPosition(codeToSearch.get());
            
            txt.insert(0, Subject.subjects_list[position].code)
            txt1.insert(0, Subject.subjects_list[position].name)
            txt2.insert(0, Subject.subjects_list[position].prerequisites)
            txt3.insert(0, Subject.subjects_list[position].required)
            txt4.insert(0, Subject.subjects_list[position].semester)
            txt5.insert(0, Subject.subjects_list[position].credit)
            txt6.insert(0, Subject.subjects_list[position].status)
            
    def cleanEntry():
        txt.delete(0, 100)
        txt1.delete(0, 100)
        txt2.delete(0, 100)
        txt3.delete(0, 100)
        txt4.delete(0, 100)
        txt5.delete(0, 100)
        txt6.delete(0, 100)
    
    btn1 = tk.Button(windowShowSubject, text="Buscar", command=search, font=("Arial", 10))
    btn1.place(x = 380, y = 10, width=100, height=30)
    btn2 = tk.Button(windowShowSubject, text="Borrar", command=cleanEntry, font=("Arial", 10))
    btn2.place(x=160, y=370, width=200, height=30)
    btn3 =  tk.Button(windowShowSubject, text="Regresar", command=windowShowSubject.destroy, font=("Arial", 10))
    btn3.place(x=20, y=10, width=100, height=30)
    
def window_editSubject():
    windowEditSubject = tk.Toplevel()
    windowEditSubject.geometry("500x450")
    
    code = StringVar()
    name = StringVar()
    prerequisite = StringVar()
    semester = StringVar()
    requested = StringVar()
    credi = StringVar()
    status =StringVar()
    
    codeToSearch = StringVar()
    txtM = tk.Entry(windowEditSubject, textvariable=codeToSearch)
    txtM.place(x=160, y=10, width=200, height=30)
    txt = tk.Entry(windowEditSubject, textvariable=code)
    txt.place(x=160, y=80, width=200, height=30)
    txt1 = tk.Entry(windowEditSubject, textvariable=name)
    txt1.place(x=160, y=120, width=200, height=30)
    txt2 = tk.Entry(windowEditSubject, textvariable=prerequisite)
    txt2.place(x=160, y=160, width=200, height=30)
    txt3 = tk.Entry(windowEditSubject, textvariable=requested)
    txt3.place(x=160, y=200, width=200, height=30)
    txt4 = tk.Entry(windowEditSubject, textvariable=semester)
    txt4.place(x=160, y=240, width=200, height=30)
    txt5 = tk.Entry(windowEditSubject, textvariable=credi)
    txt5.place(x=160, y=280, width=200, height=30)
    txt6 = tk.Entry(windowEditSubject, textvariable=status)
    txt6.place(x=160, y=320, width=200, height=30)
    
    lbl = tk.Label(windowEditSubject, text="Código", font=("Arial", 10))
    lbl.place(x = 60, y = 80)
    lbl1 = tk.Label(windowEditSubject, text="Nombre", font=("Arial", 10))
    lbl1.place(x = 60, y = 120)
    lbl2 = tk.Label(windowEditSubject, text="Pre-requisitos", font=("Arial", 10))
    lbl2.place(x = 60, y = 160)
    lbl3 = tk.Label(windowEditSubject, text="Obligatorio", font=("Arial", 10))
    lbl3.place(x = 60, y = 200)
    lbl4 = tk.Label(windowEditSubject, text="Semestre", font=("Arial", 10))
    lbl4.place(x = 60, y = 240)
    lbl5 = tk.Label(windowEditSubject, text="Créditos", font=("Arial", 10))
    lbl5.place(x = 60, y = 280)
    lbl6 = tk.Label(windowEditSubject, text="Estado", font=("Arial", 10))
    lbl6.place(x = 60, y = 320)
    
    def search():
        result = fn.showSubject(codeToSearch.get())
        
        if  result == True:
            position = fn.searchPosition(codeToSearch.get());
            
            txt.insert(0, Subject.subjects_list[position].code)
            txt1.insert(0, Subject.subjects_list[position].name)
            txt2.insert(0, Subject.subjects_list[position].prerequisites)
            txt3.insert(0, Subject.subjects_list[position].required)
            txt4.insert(0, Subject.subjects_list[position].semester)
            txt5.insert(0, Subject.subjects_list[position].credit)
            txt6.insert(0, Subject.subjects_list[position].status)
            
    def edit():
        position = fn.searchPosition(codeToSearch.get());
        fn.modifySubject(position, code.get(), name.get(), prerequisite.get(), semester.get(), requested.get(),
                    credi.get(), status.get())
    
    
    btn = tk.Button(windowEditSubject, text="Buscar", command=search, font=("Arial", 10))
    btn.place(x = 380, y = 10, width=100, height=30)
    btn1 = tk.Button(windowEditSubject, text="Editar", command=edit, font=("Arial", 10))
    btn1.place(x=160, y=370, width=200, height=30)
    btn2 = tk.Button(windowEditSubject, text="Regresar", command=windowEditSubject.destroy, font=("Arial", 10))
    btn2.place(x=20, y=10, width=100, height=30)
    

def window_manageSubjects():
    windowManageSubjects = tk.Toplevel()
    windowManageSubjects.geometry("500x450")
    lbl = tk.Label(windowManageSubjects, text="Gestionar Cursos", font=("Arial", 12, BOLD))
    lbl.place(x=190, y=10)
    btn = tk.Button(windowManageSubjects, text="Listar Cursos", command=window_viewSubjects, font=("Arial", 10))
    btn.place(x=180, y=80, width=150, height=50)
    btn1 = tk.Button(windowManageSubjects, text="Mostrar Cursos", command=window_showSubject, font=("Arial", 10))
    btn1.place(x=180, y=140, width=150, height=50)
    btn2 = tk.Button(windowManageSubjects, text="Agregar Cursos", command=window_addSubject, font=("Arial", 10))
    btn2.place(x=180, y=200, width=150, height=50)
    btn3 = tk.Button(windowManageSubjects, text="Editar Cursos", command=window_editSubject, font=("Arial", 10))
    btn3.place(x=180, y=260, width=150, height=50)
    btn4 = tk.Button(windowManageSubjects, text="Eliminar Cursos", command=window_deleteSubject, font=("Arial", 10))
    btn4.place(x=180, y=320, width=150, height=50)
    btn5 = tk.Button(windowManageSubjects, text="Regresar", command=windowManageSubjects.destroy, font=("Arial", 10))
    btn5.place(x=20, y=10, width=100, height=30)
    
def window_credits():
    windowCredits = tk.Toplevel()
    windowCredits.geometry("500x450")
    lbl = tk.Label(windowCredits, text="Conteo de Créditos", font=("Arial", 12, BOLD))
    lbl.place(x=180, y=10)
    
    lblApproved_title = tk.Label(windowCredits, text="Créditos Aprobados", font=("Arial", 10))
    lblApproved_title.place(x= 175, y=50)
    approvedCredits = StringVar()
    approvedCredits.set(str(fn.coursesCounter("0")))
    lblApproved = tk.Label(windowCredits, textvariable=approvedCredits, font=("Arial", 10))
    lblApproved.place(x=325, y=50)
    
    lblCursing_title = tk.Label(windowCredits, text="Créditos Cursando", font=("Arial", 10))
    lblCursing_title.place(x= 175, y=80)
    cursingCredits = StringVar()
    cursingCredits.set(str(fn.coursesCounter("1")))
    lblCursing = tk.Label(windowCredits, textvariable=cursingCredits, font=("Arial", 10))
    lblCursing.place(x=325, y=80)

    lblCursingP_title = tk.Label(windowCredits, text="Créditos Pendientes", font=("Arial", 10))
    lblCursingP_title.place(x= 175, y=110)
    cursingPCredits = StringVar()
    cursingPCredits.set(str(fn.coursesPCounter("-1", "1")))
    lblCursingP = tk.Label(windowCredits, textvariable=cursingPCredits, font=("Arial", 10))
    lblCursingP.place(x=325, y=110)
    
    #creditos hasta semestre N
    lbl = tk.Label(windowCredits, text="Créditos Obligatorios hasta Semestre N", font=("Arial", 10, BOLD))
    lbl.place(x= 130, y= 160)
    combo = ttk.Combobox(windowCredits)
    combo['values'] = ('1','2','3','4','5','6','7','8','9','10')
    combo.place(x= 135, y= 185, width=120, height=30)

 
    credP = StringVar()
 
    def creditsUntilSemester():
        credP.set(str(fn.requiredCredits(combo.get())))
        
    bc = tk.Button(windowCredits, text="Contar", command=creditsUntilSemester)
    bc.place(x= 260, y= 185, width=120, height=30)
    lbl2 = tk.Label(windowCredits, text="Resultado:", font=("Arial", 10))
    lbl2.place(x= 210, y= 225)
    lbl3 = tk.Label(windowCredits, textvariable=credP, font=("Arial", 10))
    lbl3.place(x= 280, y= 225)  
      
    #creditos en semestre N
    lbl = tk.Label(windowCredits, text="Créditos del Semestre N", font=("Arial", 10, BOLD))
    lbl.place(x= 180, y= 270)
    combo2 = ttk.Combobox(windowCredits)
    combo2['values'] = ('1','2','3','4','5','6','7','8','9','10')
    combo2.place(x= 135, y= 295, width=120, height=30)
 
    credA = StringVar()
    credC = StringVar()
    credPP = StringVar()
    
    def creditsUntilSemesterN():
        credA.set(str(fn.requiredCreditsNA(combo2.get())))
        credC.set(str(fn.requiredCreditsNC(combo2.get())))
        credPP.set(str(fn.requiredCreditsNP(combo2.get())))
    
    bb = tk.Button(windowCredits, text="Contar", command=creditsUntilSemesterN)
    bb.place(x= 260, y= 295, width=120, height=30)
    
    T1 = tk.Label(windowCredits, text="Resultado créditos aprobados:", font=("Arial", 10))
    T1.place(x= 130, y= 335)
    T2 = tk.Label(windowCredits, text="Resultado créditos asignados:", font=("Arial", 10))
    T2.place(x= 130, y= 358)
    T2 = tk.Label(windowCredits, text="Resultado créditos pendientes:", font=("Arial", 10))
    T2.place(x= 130, y= 380)
    
    lbl7 = tk.Label(windowCredits, textvariable=credA, font=("Arial", 10))
    lbl7.place(x= 320, y= 335)
    lbl8 = tk.Label(windowCredits, textvariable=credC, font=("Arial", 10))
    lbl8.place(x= 320, y= 358)
    lbl9 = tk.Label(windowCredits, textvariable=credPP, font=("Arial", 10))
    lbl9.place(x= 320, y= 380)
    
    b = tk.Button(windowCredits, text="Regresar", command=windowCredits.destroy)
    b.place(x=20, y=10, width=100, height=30)
    
#ventana de menú principal
window = tk.Tk()
window.geometry("500x400")
#window.eval('tk::PlaceWindow . center')
lbl1 = tk.Wm.title(window, "Gestión de Cursos Ingeniería")
lbl2 = tk.Label(window, text="Nombre del Curso: Lab. Lenguajes Formales y de Programación", font=("Arial", 12, BOLD))
lbl2.place(x=5,y=40)
lbl3 = tk.Label(window, text="Nombre del Estudiante: Aldo Saúl Vásquez Moreira", font=("Arial", 12, BOLD))
lbl3.place(x=40,y=60)
lbl4 = tk.Label(window, text="Carné del Estudiante: 202109754", font=("Arial", 12, BOLD))
lbl4.place(x=130, y=80)

#botones de menú principal
b = tk.Button(window, text="Cargar Archivo", command=window_openFile, font=("Arial", 10))
b.place(x=180, y=120, width=150, height=50)
b1 = tk.Button(window, text="Gestionar Cursos", command=window_manageSubjects, font=("Arial", 10))
b1.place(x=180, y=180, width=150, height=50)
b2 = tk.Button(window, text="Conteo de Créditos", command=window_credits, font=("Arial", 10))
b2.place(x=180, y=240, width=150, height=50)
b3 = tk.Button(window, text="Salir", command=window.destroy, font=("Arial", 10))
b3.place(x=180, y=300, width=150, height=50)

window.mainloop()