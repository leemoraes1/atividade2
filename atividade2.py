class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.cursos_lecionados = []

    def ministrar_curso(self, curso):
        if curso not in self.cursos_lecionados:
            self.cursos_lecionados.append(curso)
            curso.add_prof(self)

    def __str__(self):
        return self.nome

class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.professor = None

    def add_prof(self, professor):
        self.professor = professor

    def __str__(self):
        if self.professor:
            return f"Curso: {self.nome}, Professor: {self.professor.nome}"
        else:
            return f"Curso: {self.nome}, Professor: Não atribuído"

professor1 = Professor("Dieimes")
professor2 = Professor("Paulo")
curso1 = Curso("Redes")
curso2 = Curso("Programação")
professor1.ministrar_curso(curso2)
professor2.ministrar_curso(curso1)

print(curso1)
print(curso2)
print(f"Cursos lecionados por {professor1}: {[curso.nome for curso in professor1.cursos_lecionados]}")
print(f"Cursos lecionados por {professor2}: {[curso.nome for curso in professor2.cursos_lecionados]}")