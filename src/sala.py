from dataclasses import dataclass
from src.aluno import Aluno


@dataclass
class Sala:
    numero: int
    capacidade: int
    alunos: list[Aluno]

    def __str__(self) -> str:
        return f"Sala(numero={self.numero}, capacidade={self.capacidade}, alunos={self.alunos})"

    def __repr__(self) -> str:
        return self.__str__()

    def adicionar_aluno(self, aluno: Aluno) -> None:
        if len(self.alunos) < self.capacidade:
            self.alunos.append(aluno)
        else:
            raise ValueError("Sala cheia, não é possível adicionar mais alunos.")

    def remover_aluno(self, aluno: Aluno) -> None:
        if aluno in self.alunos:
            self.alunos.remove(aluno)
        else:
            raise ValueError("Aluno não encontrado na sala.")

    def listar_alunos(self) -> list[Aluno]:
        return self.alunos.copy()
