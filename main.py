from src.aluno import Aluno
from src.sala import Sala


def main() -> None:
    # Cria alguns alunos
    aluno1 = Aluno(nome="Ana", idade=20, matricula="2025001")
    aluno2 = Aluno(nome="Bruno", idade=21, matricula="2025002")
    aluno3 = Aluno(nome="Carla", idade=19, matricula="2025003")

    # Cria uma sala com capacidade para 2 alunos
    sala = Sala(numero=101, capacidade=2, alunos=[])

    # Adiciona alunos à sala
    print("Adicionando alunos à sala...")
    print(f"Adicionando {aluno1.nome}")
    sala.adicionar_aluno(aluno1)
    print(f"Adicionando {aluno2.nome}")
    sala.adicionar_aluno(aluno2)

    # Tenta adicionar um terceiro aluno (deve lançar exceção)
    print(f"Tentando adicionar {aluno3.nome}...")
    try:
        sala.adicionar_aluno(aluno3)
    except ValueError as e:
        print(f"Erro ao adicionar aluno: {e}")

    # Lista os alunos presentes na sala
    print("Alunos na sala:")
    print(sala.listar_alunos())

    # Remove um aluno e mostra a lista novamente
    sala.remover_aluno(aluno1)
    print("\nApós remover Ana:")
    print(sala.listar_alunos())


if __name__ == "__main__":
    main()
