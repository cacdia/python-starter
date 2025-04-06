# Python Starter

## 📋 Conteúdo

- [Pré-requisitos](#pré-requisitos)
- [Primeiros Passos](#primeiros-passos)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Desenvolvimento](#desenvolvimento)
- [Solução de Problemas no Windows](#solução-de-problemas-no-windows)

## 🔧 Pré-requisitos

Certifique-se de instalar os seguintes programas antes de começar:

- **Python 3.13 ou superior**
  [Download Python](https://www.python.org/downloads/)

- **Visual Studio Code**
  [Download VSCode](https://code.visualstudio.com/)

- **Git**
  [Download Git](https://git-scm.com/downloads)

- **uv (recomendado)**

  Instale utilizando o comando adequado ao seu sistema operacional:

  ```bash
  # Windows (PowerShell)
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

  # macOS/Linux
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

## 🚀 Primeiros Passos

Siga os passos abaixo para configurar rapidamente o projeto:

### 1. Clone o repositório

```bash
git clone https://github.com/thiag0bezerra/python-starter.git
cd python-starter
```

### 2. Configure o ambiente virtual

Crie o ambiente virtual e instale automaticamente todas as dependências:

```bash
uv sync
```

### 3. Configure o VSCode

Abra o projeto no Visual Studio Code:

```bash
code .
```

#### Instale as extensões recomendadas

Ao abrir o projeto pela primeira vez:

- Uma notificação aparecerá sugerindo a instalação das extensões recomendadas.
- Clique em **Install All** ou em **Show Recommendations**.
- Alternativamente, pressione `Ctrl+Shift+X` (ou `Cmd+Shift+X` no macOS) e digite `@recommended` na barra de pesquisa.

#### Selecione o interpretador Python correto

1. Pressione `Ctrl+Shift+P` (ou `Cmd+Shift+P` no macOS).
2. Digite **Python: Select Interpreter**.
3. Escolha o interpretador Python referente ao ambiente virtual criado (`.venv`), geralmente exibido como:
   `"Python 3.13.x ('.venv':venv)"`.

### 4. Execute o projeto

```bash
uv run main.py
```

## 📁 Estrutura do Projeto

```
python-starter/
├── main.py              # Ponto de entrada do programa
├── pyproject.toml       # Metadados e dependências do projeto
├── .python-version      # Versão recomendada do Python
└── .vscode/             # Configurações otimizadas para VSCode
    ├── extensions.json  # Extensões recomendadas
    └── settings.json    # Configurações específicas do projeto
```

## 💻 Desenvolvimento

### Comandos essenciais

Use os comandos abaixo para facilitar o desenvolvimento do projeto:

```bash
# Executar o código
uv run main.py        # recomendado

# Formatar código com Ruff
ruff format .

# Adicionar uma nova dependência
uv add nome-do-pacote

# Sincronizar dependências após alterações no pyproject.toml
uv sync
```

## 🪟 Solução de Problemas no Windows

Caso enfrente problemas relacionados a permissões no PowerShell, execute:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
