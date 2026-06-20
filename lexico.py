class AnalisadorLexico:
    def __init__(self, texto_fonte):
        self.texto = texto_fonte
        self.posicao = 0
        self.tamanho = len(texto_fonte)
        self.linha_atual = 1

    def avancar(self):
        """Avança o ponteiro de leitura e conta as linhas."""
        if self.posicao < self.tamanho:
            if self.texto[self.posicao] == '\n':
                self.linha_atual += 1
            self.posicao += 1

    def caractere_atual(self):
        """Retorna o caractere atual ou None se chegou ao fim."""
        if self.posicao >= self.tamanho:
            return None
        return self.texto[self.posicao]

    def pular_espacos_e_comentarios(self):
        """Filtro de Primeiro Nível: Ignora espaços, tabulações e comentários."""
        while self.posicao < self.tamanho:
            char = self.caractere_atual()

            # Pula espaços em branco, quebras de linha e tabs
            if char in (' ', '\n', '\t', '\r'):
                self.avancar()
                continue

            # Verifica comentários
            if char == '/':
                proximo_char = self.texto[self.posicao + 1] if self.posicao + 1 < self.tamanho else None

                # Comentário de Linha: //
                if proximo_char == '/':
                    self.avancar() # consome o primeiro /
                    self.avancar() # consome o segundo /
                    while self.caractere_atual() is not None and self.caractere_atual() != '\n':
                        self.avancar()
                    continue # Volta para o início do while para limpar espaços da nova linha

                # Comentário de Bloco: /* ... */
                elif proximo_char == '*':
                    self.avancar() # consome o /
                    self.avancar() # consome o *
                    while self.posicao < self.tamanho:
                        if self.caractere_atual() == '*' and (self.posicao + 1 < self.tamanho and self.texto[self.posicao + 1] == '/'):
                            self.avancar() # consome o *
                            self.avancar() # consome o /
                            break
                        self.avancar()
                    continue # Volta para o início do while para continuar limpando

            # Se não é espaço nem comentário, para o loop (encontramos um caractere útil!)
            break

    def proximo_token(self):
        """Extrai o próximo átomo (palavra ou símbolo) do texto."""
        self.pular_espacos_e_comentarios()

        char = self.caractere_atual()
        if char is None:
            return None  # Fim do arquivo!

        linha_inicio = self.linha_atual
        lexeme = ""

        # Regra 1: Identificadores ou Palavras Reservadas 
        if char.isalpha() or char == '_':
            while self.caractere_atual() is not None and (self.caractere_atual().isalnum() or self.caractere_atual() == '_'):
                lexeme += self.caractere_atual()
                self.avancar()
            return lexeme.upper(), linha_inicio # Tudo convertido para maiúsculo [cite: 265]

        # Regra 2: Strings (stringConst) - inicia e termina com aspas duplas 
        if char == '"':
            lexeme += char
            self.avancar()
            while self.caractere_atual() is not None and self.caractere_atual() != '"':
                lexeme += self.caractere_atual()
                self.avancar()
            if self.caractere_atual() == '"':
                lexeme += '"' # Adiciona a aspa de fechamento
                self.avancar()
            return lexeme, linha_inicio

        # Regra 3: Caracteres (charConst) - inicia e termina com aspas simples 
        if char == "'":
            lexeme += char
            self.avancar()
            while self.caractere_atual() is not None and self.caractere_atual() != "'":
                lexeme += self.caractere_atual()
                self.avancar()
            if self.caractere_atual() == "'":
                lexeme += "'" # Adiciona a aspa de fechamento
                self.avancar()
            return lexeme, linha_inicio

        # Regra 4: Números (intConst e realConst) 
        if char.isdigit():
            # Lê a primeira parte (inteira)
            while self.caractere_atual() is not None and self.caractere_atual().isdigit():
                lexeme += self.caractere_atual()
                self.avancar()
                
            # Verifica se é um número real (se tem ponto seguido de número)
            if self.caractere_atual() == '.':
                proximo = self.texto[self.posicao + 1] if self.posicao + 1 < self.tamanho else ""
                if proximo.isdigit():
                    lexeme += self.caractere_atual() # Adiciona o ponto
                    self.avancar()
                    # Lê as casas decimais
                    while self.caractere_atual() is not None and self.caractere_atual().isdigit():
                        lexeme += self.caractere_atual()
                        self.avancar()
                        
                    # Verifica se tem a parte exponencial (e ou E)
                    if self.caractere_atual() in ('e', 'E'):
                        char_e = self.caractere_atual()
                        proximo_pos = self.posicao + 1
                        char_seguinte = self.texto[proximo_pos] if proximo_pos < self.tamanho else ""
                        
                        # A parte exponencial pode ter um sinal (+ ou -) antes dos dígitos 
                        if char_seguinte in ('+', '-') or char_seguinte.isdigit():
                            lexeme += char_e
                            self.avancar()
                            if self.caractere_atual() in ('+', '-'): # Pega o sinal se houver
                                lexeme += self.caractere_atual()
                                self.avancar()
                            while self.caractere_atual() is not None and self.caractere_atual().isdigit(): # Pega os dígitos do expoente
                                lexeme += self.caractere_atual()
                                self.avancar()
                                
            return lexeme, linha_inicio

        # Regra 5: Símbolos duplos (como :=, <=, >=, ==, !=) [cite: 385]
        proximo = self.texto[self.posicao + 1] if self.posicao + 1 < self.tamanho else ""
        simbolo_duplo = char + proximo

        if simbolo_duplo in (':=', '<=', '>=', '==', '!='):
            self.avancar() # consome o primeiro (ex: :)
            self.avancar() # consome o segundo (ex: =)
            return simbolo_duplo, linha_inicio

        # Regra 6: Símbolos simples (de apenas 1 caractere)
        lexeme = char
        self.avancar()
        return lexeme, linha_inicio