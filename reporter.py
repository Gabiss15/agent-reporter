import json
from datetime import datetime


class ReporterAgent:

    def __init__(self, input_file):
        self.input_file = input_file

    def load_data(self):
        with open(self.input_file, "r") as file:
            return json.load(file)

    def validate_data(self, data):

        required_fields = [
            "componentes",
            "entradas",
            "saidas"
        ]

        for field in required_fields:
            if field not in data:
                raise ValueError(
                    f"Campo vazio: {field}"
                )

    def generate_report(self, data):

        report = f"""# Relatório Técnico

Data de geração: {datetime.now().strftime("%d/%m/%Y %H:%M")} 

# Sistema

{data.get("nome_sistema", "Não informado")}

## Componentes

"""

        for component in data["componentes"]:
            report += f"- {component}\n"

        report += "\n# Entradas\n\n"

        for item in data["entradas"]:
            report += f"- {item}\n"

        report += "\n# Saídas\n\n"

        for item in data["saidas"]:
            report += f"- {item}\n"

        report += "\n# Restrições\n\n"

        for item in data.get("restricoes", []):
            report += f"- {item}\n"

        report += "\n# Comportamentos Esperados\n\n"

        for item in data.get("comportamentos", []):
            report += f"- {item}\n"

        return report

    def save_report(self, report):

        with open(
            "relatorio.md",
            "w",
            encoding="utf-8"
        ) as file:
            file.write(report)

        print("Relatório gerado com sucesso.")

    def execute(self):

        data = self.load_data()

        self.validate_data(data)

        report = self.generate_report(data)

        self.save_report(report)


if __name__ == "__main__":

    reporter = ReporterAgent("input.json")

    reporter.execute()