import pandas as pd


class AgenteTarefa:

    def __init__(self):
        self.dados = pd.read_csv("dados/atividades.csv")

    def verificar(self, aluno):

        atividades = self.dados[
            self.dados["aluno"].str.lower() == aluno.lower()
        ]

        if atividades.empty:
            return {
                "lista": [],
                "pendentes": 0
            }

        lista = []
        pendentes = 0

        for _, linha in atividades.iterrows():

            lista.append(
                f"{linha['atividade']} - {linha['status']}"
            )

            if linha["status"].lower() == "pendente":
                pendentes += 1

        return {
            "lista": lista,
            "pendentes": pendentes
        }