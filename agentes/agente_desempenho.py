import pandas as pd


class AgenteDesempenho:

    def __init__(self):
        self.dados = pd.read_csv("dados/notas.csv")

    def analisar(self, aluno):

        resultado = self.dados[
            self.dados["aluno"].str.lower() == aluno.lower()
        ]

        if resultado.empty:
            return None

        nota = resultado.iloc[0]["nota"]

        return nota