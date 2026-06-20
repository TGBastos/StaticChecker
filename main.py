<<<<<<< HEAD
from file_reader import findFile
from file_to_list import fileToList

# fr.findFile('x, y'):
# 1º parametro deve ser o nome do arquivo
# o 2º é, opcionalmente, o diretorio em que deseja buscar
file = findFile('Teste')
eachLineInFileList = fileToList(file)

#print(eachLineInFileList)
=======
import sys
import os
from estruturas import TabelaSimbolos, obter_codigo_reservado
from lexico import AnalisadorLexico

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

def main():
    if len(sys.argv) < 2:
        print("Erro: Forneça o nome do arquivo fonte como parâmetro.")
        sys.exit(1)

    nome_parametro = sys.argv[1]
    
    if not nome_parametro.endswith(".261"):
        nome_arquivo = nome_parametro + ".261"
    else:
        nome_arquivo = nome_parametro

    nome_base = nome_arquivo.replace(".261", "")

    if not os.path.exists(nome_arquivo):
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado no diretório atual.")
        sys.exit(1)

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            texto_fonte = arquivo.read()
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        sys.exit(1)

    tabela_simbolos = TabelaSimbolos()
    lexico = AnalisadorLexico(texto_fonte)

    # Prepara a criação do arquivo .LEX
    arquivo_lex_nome = f"{nome_base}.LEX"
    
    with open(arquivo_lex_nome, 'w', encoding='utf-8') as arq_lex:
        # Escreve o cabeçalho no .LEX [cite: 77]
        arq_lex.write(gerar_cabecalho())
        arq_lex.write(f"\nRELATÓRIO DA ANÁLISE LÉXICA.\nTexto fonte analisado: {nome_arquivo}\n\n")

        print(f"Analisando arquivo '{nome_arquivo}'...")
        
        while True:
            resultado = lexico.proximo_token()
            
            if resultado is None:
                break
                
            lexeme, linha = resultado
            codigo = obter_codigo_reservado(lexeme)
            
            if codigo is not None:
                # É reservado: índice não se aplica [cite: 78]
                arq_lex.write(f"Lexeme: {lexeme},\nCódigo: {codigo}, indiceTabSimb: ,\nLinha: {linha}.\n")
            else:
                # É identificador/constante: salva na Tabela e pega o índice [cite: 78, 326]
                codigo_identificador = "C01" # Por padrão
                
                # Se for número inteiro, real, string ou char, usa códigos C04 a C07 do Apêndice A [cite: 369]
                if lexeme.startswith('"'): codigo_identificador = "C04"
                elif lexeme.startswith("'"): codigo_identificador = "C05"
                elif lexeme.isdigit(): codigo_identificador = "C06"
                elif lexeme[0].isdigit() and ("." in lexeme or "E" in lexeme): codigo_identificador = "C07"
                
                entrada = tabela_simbolos.registrar_identificador(lexeme, codigo_identificador, linha)
                arq_lex.write(f"Lexeme: {entrada.lexeme},\nCódigo: {codigo_identificador}, indiceTabSimb: {entrada.entrada},\nLinha: {linha}.\n")

    # Gera o arquivo .TAB após a análise terminar
    arquivo_tab_nome = f"{nome_base}.TAB"
    with open(arquivo_tab_nome, 'w', encoding='utf-8') as arq_tab:
        # Escreve o cabeçalho no .TAB [cite: 176, 179]
        arq_tab.write(gerar_cabecalho())
        arq_tab.write(f"\nRELATÓRIO DA TABELA DE SÍMBOLOS.\nTexto fonte analisado: {nome_arquivo}\n\n")
        
        # Escreve cada entrada da tabela de símbolos [cite: 165, 181]
        for chave, entrada in tabela_simbolos.tabela.items():
            linhas_str = ", ".join(map(str, entrada.linhas))
            arq_tab.write(f"Entrada: {entrada.entrada}, Código: {entrada.codigo}, Lexeme: {entrada.lexeme},\n")
            arq_tab.write(f"QtdCharsAntesTrunc: {entrada.qtd_chars_antes_trunc}, QtdCharDepoisTrunc: {entrada.qtd_char_depois_trunc},\n")
            arq_tab.write(f"TipoSimb: {entrada.tipo_simb}, Linhas: ({linhas_str}).\n\n")

    print(f"Análise concluída com sucesso!")
    print(f"Relatórios gerados: {arquivo_lex_nome} e {arquivo_tab_nome}")

if __name__ == "__main__":
    main()
>>>>>>> c63a474 (Static Checker)
