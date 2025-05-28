from dataclasses import dataclass


@dataclass
class Aluno:
    nome: str
    idade: int
    matricula: str

    def __str__(self):
        return (
            f"Aluno(nome={self.nome}, idade={self.idade}, matricula={self.matricula})"
        )

    def __repr__(self):
        return self.__str__()
