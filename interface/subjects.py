
class subjects: 
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
        

        