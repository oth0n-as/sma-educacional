import streamlit as st
import pandas as pd

from agentes.agente_tutor import AgenteTutor
from agentes.agente_tarefa import AgenteTarefa
from agentes.agente_desempenho import AgenteDesempenho

# ==================================
# AGENTES
# ==================================

tutor = AgenteTutor()
tarefa = AgenteTarefa()
desempenho = AgenteDesempenho()

# ==================================
# DADOS
# ==================================

notas_df = pd.read_csv("dados/notas.csv")
atividades_df = pd.read_csv("dados/atividades.csv")

# ==================================
# TÍTULO
# ==================================

st.title("Sistema Multiagente Educacional")

# ==================================
# SIDEBAR
# ==================================

st.sidebar.title("Métricas")

total_alunos = notas_df["aluno"].nunique()

media_notas = round(
    notas_df["nota"].mean(),
    2
)

atividades_pendentes = (
    atividades_df["status"]
    .str.lower()
    .eq("pendente")
    .sum()
)

st.sidebar.metric(
    "Total de alunos",
    total_alunos
)

st.sidebar.metric(
    "Média Geral",
    media_notas
)

st.sidebar.metric(
    "Pendências",
    atividades_pendentes
)

# ==================================
# GRÁFICO DE NOTAS
# ==================================

st.sidebar.subheader("Notas por Aluno")

st.sidebar.bar_chart(
    notas_df.set_index("aluno")["nota"]
)

# ==================================
# GRÁFICO DE ATIVIDADES
# ==================================

status = atividades_df["status"].value_counts()

st.sidebar.subheader("Status das Atividades")

st.sidebar.bar_chart(status)

# ==================================
# FORMULÁRIO
# ==================================

aluno = st.text_input(
    "Nome do aluno"
)

pergunta = st.text_input(
    "Digite sua dúvida"
)

st.info("""
Perguntas disponíveis:

• o que é dijkstra
• o que é bellman ford
• o que é kruskal
• o que é prim
• qual minha nota
• como está meu desempenho
• tenho atividades pendentes
""")

# ==================================
# CONSULTA
# ==================================

if st.button("Consultar"):

    st.subheader("Resposta do Agente Tutor")

    st.write(
        tutor.responder(
            pergunta,
            aluno
        )
    )

    # ---------------------

    st.subheader("Atividades")

    atividades = tarefa.verificar(aluno)

    if atividades["lista"]:

        for atividade in atividades["lista"]:
            st.write(atividade)

        st.write(
            f"Total de pendências: {atividades['pendentes']}"
        )

    else:

        st.warning(
            "Nenhuma atividade encontrada."
        )

    # ---------------------

    st.subheader("Desempenho")

    nota = desempenho.analisar(aluno)

    if nota is not None:

        if nota >= 7:

            st.success(
                f"Nota: {nota} - Desempenho satisfatório."
            )

        else:

            st.warning(
                f"Nota: {nota} - Recomenda-se reforço nos estudos."
            )

    else:

        st.error(
            "Aluno não encontrado."
        )