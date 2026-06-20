# estruturas.py

class Token:
    def __init__(self, lexeme, codigo, indice_tab_simb, linha):
        self.lexeme = lexeme
        self.codigo = codigo
        self.indice_tab_simb = indice_tab_simb
        self.linha = linha

class EntradaTabelaSimbolos:
    def __init__(self, entrada, codigo, lexeme, qtd_chars_antes_trunc, qtd_char_depois_trunc):
        self.entrada = entrada
        self.codigo = codigo
        self.lexeme = lexeme.upper() 
        self.qtd_chars_antes_trunc = qtd_chars_antes_trunc
        self.qtd_char_depois_trunc = qtd_char_depois_trunc
        self.tipo_simb = ""
        self.linhas = []

    def adicionar_linha(self, linha):
        if len(self.linhas) < 5: 
            self.linhas.append(linha)

class TabelaSimbolos:
    def __init__(self):
        self.tabela = {}
        self.contador_entradas = 1

    def registrar_identificador(self, lexeme_original, codigo_atomo, linha):
        lexeme_chave = lexeme_original.upper()
        lexeme_truncado = lexeme_chave[:30]

        if lexeme_truncado in self.tabela:
            entrada_existente = self.tabela[lexeme_truncado]
            entrada_existente.adicionar_linha(linha)
            return entrada_existente
        else:
            tamanho_total = len(lexeme_original)
            antes_trunc = min(tamanho_total, 30)
            nova_entrada = EntradaTabelaSimbolos(
                self.contador_entradas, codigo_atomo, lexeme_truncado, antes_trunc, tamanho_total
            )
            nova_entrada.adicionar_linha(linha)
            self.tabela[lexeme_truncado] = nova_entrada
            self.contador_entradas += 1
            return nova_entrada

PALAVRAS_RESERVADAS = {
    "BOOLEAN": "A01", "BREAK": "A02", "CHARACTER": "A03",
    "DECLARATIONS": "A04", "ELSE": "A05", "ENDDECLARATIONS": "A06",
    "ENDFUNCTION": "A07", "ENDFUNCTIONS": "A08", "ENDIF": "A09",
    "ENDPROGRAM": "A10", "ENDWHILE": "A11", "FALSE": "A12",
    "FUNCTIONS": "A13", "FUNCTYPE": "A14", "IF": "A15",
    "INTEGER": "A16", "PARAMTYPE": "A17", "PRINT": "A18",
    "PROGRAM": "A19", "REAL": "A20", "RETURN": "A21",
    "STRING": "A22", "TRUE": "A23", "VARTYPE": "A24",
    "VOID": "A25", "WHILE": "A26"
}

SIMBOLOS_RESERVADOS = {
    ";": "B01", ",": "B02", ":": "B03", "=": "B04", ":=": "B04", 
    "?": "B05", "(": "B06", ")": "807", "[": "B08", "]": "B09", 
    "{": "B10", "}": "B11", "+": "812", "-": "B13", "*": "B14", 
    "/": "B15", "%": "B16", "==": "B17", "!=": "818", "#": "B18", 
    "<": "819", "<=": "820", ">": "B21", ">=": "B22"
}

def obter_codigo_reservado(lexeme):
    chave = lexeme.upper()
    if chave in PALAVRAS_RESERVADAS:
        return PALAVRAS_RESERVADAS[chave]
    if chave in SIMBOLOS_RESERVADOS:
        return SIMBOLOS_RESERVADOS[chave]
    return None