import file_reader as fr
import gerar_LEX as gl
import gerar_TAB as gt
from estruturas import TabelaSimbolos, obter_codigo_reservado
from lexico import AnalisadorLexico

def main():
    texto_fonte = fr.findFile()
    nome_base = fr.definirNomeBase()
    nome_arquivo = f"{nome_base}.261"

    tabela_simbolos = TabelaSimbolos()
    lexico = AnalisadorLexico(texto_fonte)

    arquivo_lex_nome = gl.gerar_LEX(nome_base, nome_arquivo, lexico, tabela_simbolos)

    arquivo_tab_nome = gt.gerar_TAB(nome_base, nome_arquivo, lexico, tabela_simbolos)

    print(f"Análise concluída com sucesso!")
    print(f"Relatórios gerados: {arquivo_lex_nome} e {arquivo_tab_nome}")

if __name__ == "__main__":
    main()