
class Subjects: 
    code = 0
    name = ""
    prerequisites = 0
    required = 0
    semester = 0
    credit = 0
    status = 0
    subjects_list = []
    
    def __init__(self, code, name, prerequisites, required, semester, credit, status):
        self.code = code
        self.name = name
        self.prerequisites = prerequisites
        self.required = required
        self.semester = semester
        self.credit = credit
        self.status = status
        
    def addSubject(code, name, prerequisites, required, semester, credit, status):
        newSubject = Subjects(code, name, prerequisites, required, semester, credit, status)
        Subjects.subjects_list.append(newSubject)
        
    def deleteSubject(codeParameter):
        longitude = len(Subjects.subjects_list)
        for i in range(0, longitude-1):
            if Subjects.subjects_list[i].code == codeParameter:
                del Subjects.subjects_list[i]
                
    def showSubject(codeParameter):
        longitude = len(Subjects.subjects_list)
        for i in range(0, longitude-1):
            if Subjects.subjects_list[i].code == codeParameter:
                print(Subjects.subjects_list[i])
            else:
                print("No se ha encontrado el registro.")
        
            
    