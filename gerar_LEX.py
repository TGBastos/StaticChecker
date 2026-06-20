import sys
import os
import file_reader as fr
from gerar_cabecalho import gerar_cabecalho
from estruturas import TabelaSimbolos, obter_codigo_reservado
from lexico import AnalisadorLexico

def gerar_LEX(nome_base, nome_arquivo, lexico, tabela_simbolos):    
# Prepara a criação do arquivo .LEX
    arquivo_lex_nome = f"{nome_base}.LEX"
    
    with open(arquivo_lex_nome, 'w', encoding='utf-8') as arq_lex:
        # Escreve o cabeçalho no .LEX [cite: 77]
        arq_lex.write(gerar_cabecalho())
        arq_lex.write(f"\nRELATÓRIO DA ANÁLISE LÉXICA.\nTexto fonte analisado: {nome_arquivo}\n\n")

        print(f"Analisando arquivo '{nome_arquivo}'...")
        
        token_anterior = None  # Guarda o último token reservado visto

        while True:
            resultado = lexico.proximo_token()
            
            if resultado is None:
                break
                
            lexeme, linha = resultado
            codigo = obter_codigo_reservado(lexeme)
            
            if codigo is not None:
                # É reservado: índice não se aplica [cite: 78]
                arq_lex.write(f"Lexeme: {lexeme},\nCódigo: {codigo}, indiceTabSimb: -,\nLinha: {linha}.\n")
                token_anterior = lexeme  # Atualiza o contexto
            else:
                # É identificador/constante: salva na Tabela e pega o índice [cite: 78, 326]
                codigo_identificador = "C01"  # Por padrão

                # Classificação por contexto: token anterior define se é programName ou functionName
                if token_anterior == "PROGRAM":
                    codigo_identificador = "C03"
                elif token_anterior == "FUNCTYPE":
                    codigo_identificador = "C02"
                # Constantes literais: C04 a C07
                elif lexeme.startswith('"'):
                    codigo_identificador = "C04"
                elif lexeme.startswith("'"):
                    codigo_identificador = "C05"
                elif lexeme.isdigit():
                    codigo_identificador = "C06"
                elif lexeme[0].isdigit() and ("." in lexeme or "E" in lexeme):
                    codigo_identificador = "C07"

                token_anterior = None  # Reseta após consumir o contexto
                
                entrada = tabela_simbolos.registrar_identificador(lexeme, codigo_identificador, linha)
                arq_lex.write(f"Lexeme: {entrada.lexeme},\nCódigo: {codigo_identificador}, indiceTabSimb: {entrada.entrada},\nLinha: {linha}.\n")
    return arquivo_lex_nome