import pandas as pd

from agentes.agente_tarefa import AgenteTarefa
from agentes.agente_desempenho import AgenteDesempenho


class AgenteTutor:

    def __init__(self):

        self.base = pd.read_csv("dados/perguntas.csv")

        self.agente_tarefa = AgenteTarefa()
        self.agente_desempenho = AgenteDesempenho()

    def responder(self, pergunta, aluno):

        pergunta = pergunta.lower().strip()

        atividades = self.agente_tarefa.verificar(aluno)
        nota = self.agente_desempenho.analisar(aluno)

        # CONSULTAS TEÓRICAS

        resultado = self.base[
            self.base["pergunta"].str.lower() == pergunta
        ]

        if not resultado.empty:

            resposta = resultado.iloc[0]["resposta"]

            mensagem = f"""
{resposta}

-------------------------

Resumo acadêmico:

Nota atual: {nota}

Atividades pendentes: {atividades['pendentes']}
"""

            return mensagem

        # CONSULTA DE NOTA

        if any(x in pergunta for x in [
            "nota",
            "desempenho",
            "media",
            "média"
        ]):

            if nota >= 7:
                return f"""
Sua nota atual é {nota}.

Seu desempenho está satisfatório.
"""
            else:
                return f"""
Sua nota atual é {nota}.

Recomenda-se reforço nos estudos.
"""

        # CONSULTA DE ATIVIDADES

        if any(x in pergunta for x in [
            "atividade",
            "pendente",
            "trabalho"
        ]):

            texto = "\n".join(
                atividades["lista"]
            )

            return f"""
Situação das atividades:

{texto}

Total pendentes: {atividades['pendentes']}
"""

        return """
Pergunta não encontrada.

Exemplos:

• o que é dijkstra
• o que é bellman ford
• qual minha nota
• tenho atividades pendentes
"""