from gerar_cabecalho import gerar_cabecalho

def gerar_TAB(nome_base, nome_arquivo, lexico, tabela_simbolos):

# Gera o arquivo .TAB após a análise terminar
    arquivo_tab_nome = f"{nome_base}.TAB"
    with open(arquivo_tab_nome, 'w', encoding='utf-8') as arq_tab:
        # Escreve o cabeçalho no .TAB [cite: 176, 179]
        arq_tab.write(gerar_cabecalho())
        arq_tab.write(f"\nRELATÓRIO DA TABELA DE SÍMBOLOS.\nTexto fonte analisado: {nome_arquivo}\n\n")
        
        for chave, entrada in tabela_simbolos.tabela.items():
            linhas_str = ", ".join(map(str, entrada.linhas))
            arq_tab.write(f"Entrada: {entrada.entrada}, Código: {entrada.codigo}, Lexeme: {entrada.lexeme},\n")
            arq_tab.write(f"QtdCharsAntesTrunc: {entrada.qtd_chars_antes_trunc}, QtdCharDepoisTrunc: {entrada.qtd_char_depois_trunc},\n")
            arq_tab.write(f"TipoSimb: {entrada.tipo_simb}, Linhas: ({linhas_str}).\n\n")
    return arquivo_tab_nome 