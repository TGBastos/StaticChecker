# === INFORMAÇÕES DA EQUIPE (Edite aqui) ===
CODIGO_EQUIPE = "E01" 
COMPONENTES = [
    "Pedro Henrique Santiago Bastos; pedrohenrique.bastos@ucsal.edu.br; (75) 99250-6686",
    "Anne Feitoza Vasconcelos; anne.vasconcelos@ucsal.edu.br; (74) 99989-9790",
    "Thiago Gomes Bastos Santos; thiagogomes.santos@ucsal.edu.br; (75) 98828-5405",
    "Anna Luíza Morerira de Oliveira; annaluiza.oliveira@ucsal.edu.br; (71) 98181-3136"
]
# =========================================

def gerar_cabecalho():
    cabecalho = f"Código da Equipe: {CODIGO_EQUIPE}\n"
    cabecalho += "Componentes:\n"
    for componente in COMPONENTES:
        cabecalho += f"{componente}\n"
    return cabecalho