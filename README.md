# Sistema Multiagente para Acompanhamento Acadêmico

Projeto desenvolvido para a disciplina de Inteligência Artificial, com foco na aplicação de **Sistemas Multiagentes (SMA)** no contexto educacional.

## Sobre o Projeto

O sistema tem como objetivo auxiliar alunos no acompanhamento de suas atividades acadêmicas por meio de agentes especializados que atuam de forma colaborativa.

A solução foi inspirada em pesquisas sobre Sistemas Multiagentes aplicados à educação e ambientes virtuais de aprendizagem.

O protótipo permite:

- Responder dúvidas acadêmicas básicas;
- Consultar atividades pendentes;
- Verificar desempenho do aluno;
- Integrar informações através de um Agente Tutor.

---

## Arquitetura do Sistema

O sistema é composto por três agentes principais:

### Agente Tutor

Responsável por:

- Receber perguntas do usuário;
- Consultar os demais agentes;
- Consolidar as informações;
- Gerar respostas contextualizadas.

### Agente de Tarefas

Responsável por:

- Consultar atividades cadastradas;
- Identificar pendências;
- Informar o status das entregas.

### Agente de Desempenho

Responsável por:

- Consultar notas dos alunos;
- Avaliar desempenho acadêmico;
- Gerar recomendações simples.

---

## Fluxo de Funcionamento

```text
Aluno
  │
  ▼
Agente Tutor
  │
  ├──► Agente de Tarefas
  │
  ├──► Agente de Desempenho
  │
  └──► Base de Conhecimento
  │
  ▼
Resposta ao Usuário
```

---

## Tecnologias Utilizadas

- Python 3
- Streamlit
- Pandas
- CSV (armazenamento dos dados)

---

## Estrutura do Projeto

```text
sma-educacional/
│
├── app.py
├── requirements.txt
│
├── agentes/
│   ├── agente_tutor.py
│   ├── agente_tarefa.py
│   └── agente_desempenho.py
│
├── dados/
│   ├── perguntas.csv
│   ├── atividades.csv
│   └── notas.csv
│
└── README.md
```

---

## Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/sma-educacional.git
```

### 2. Acessar a pasta do projeto

```bash
cd sma-educacional
```

### 3. Crie o ambiente virtual:
```bash
python3 -m venv .venv
```

### 4. Ative o ambiente virtual:
```bash
source .venv/bin/activate
```

### 5. Instalar dependências

```bash
pip install -r requirements.txt
```

### 6. Executar a aplicação

```bash
streamlit run app.py
```

---

## Exemplos de Perguntas

O sistema responde perguntas como:

```text
o que é dijkstra
o que é bellman ford
o que é kruskal
o que é prim
qual minha nota
como está meu desempenho
tenho atividades pendentes
```

---

## Funcionalidades

✅ Consulta de conteúdo acadêmico

✅ Consulta de notas

✅ Consulta de atividades

✅ Dashboard com métricas

✅ Visualização de desempenho

✅ Arquitetura baseada em Sistemas Multiagentes

---

## Resultados Esperados

O sistema permite:

- Melhor acompanhamento acadêmico;
- Consulta rápida de informações;
- Apoio ao processo de ensino-aprendizagem;
- Demonstração prática da aplicação de SMA na educação.

---

## Desenvolvedores:
- Beatriz Brito
- Giovanna Monteiro
- Mariana Paiva
- Othon Flávio

Projeto desenvolvido para a disciplina Inteligência Artificial II — IESB · Ciência da Computação · 2026/1

---

