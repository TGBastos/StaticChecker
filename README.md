#  Static Checker — Linguagem Pava2026-1

Projeto da disciplina **Compiladores** do curso de **Bacharelado em Engenharia de Software — UCSAL**.

**Professor:** Osvaldo Requião Melo
**Semestre:** 2026.1
**Equipe:** E01

---

##  Integrantes

| Nome                           | E-mail                                                                        | Telefone        |
| ------------------------------ | ----------------------------------------------------------------------------- | --------------- |
| Pedro Henrique Santiago Bastos | [pedrohenrique.bastos@ucsal.edu.br](mailto:pedrohenrique.bastos@ucsal.edu.br) | (75) 99250-6686 |
| Anne Feitoza Vasconcelos       | [anne.vasconcelos@ucsal.edu.br](mailto:anne.vasconcelos@ucsal.edu.br)         | (74) 99989-9790 |
| Thiago Gomes Bastos Santos     | [thiagogomes.santos@ucsal.edu.br](mailto:thiagogomes.santos@ucsal.edu.br)     | (75) 98828-5405 |
| Anna Luíza Moreira de Oliveira | [annaluiza.oliveira@ucsal.edu.br](mailto:annaluiza.oliveira@ucsal.edu.br)     | (71) 98181-3136 |

---

#  Sobre o Projeto

Este projeto implementa um **Static Checker** para a linguagem **Pava2026-1**.

Nesta etapa (**Etapa 7 — LEX**), foram desenvolvidos:

* Analisador Léxico;
* Tabela de Símbolos;
* Geração automática dos relatórios `.LEX` e `.TAB`;
* Tratamento de comentários, constantes e identificadores.



#  Estrutura do Projeto

| Arquivo              | Responsabilidade                                        |
| -------------------- | ------------------------------------------------------- |
| `main.py`            | Programa principal responsável pela execução do sistema |
| `file_reader.py`     | Leitura do arquivo fonte e resolução do nome base       |
| `lexico.py`          | Implementação do analisador léxico                      |
| `estruturas.py`      | Tabela de símbolos e estruturas auxiliares              |
| `gerar_cabecalho.py` | Geração do cabeçalho dos relatórios                     |
| `gerar_LEX.py`       | Geração do relatório de análise léxica                  |
| `gerar_TAB.py`       | Geração do relatório da tabela de símbolos              |

Todos os arquivos devem permanecer no mesmo diretório para que os imports funcionem corretamente.

---

#  Requisitos

* Python 3.x
* Bibliotecas padrão utilizadas:

  * `sys`
  * `string`

Não há dependências externas.

---

# Como Executar

Dentro da pasta do projeto:

```bash
python main.py NomeDoArquivo
```

## Exemplos

```bash
python main.py Teste
```

ou

```bash
python main.py Teste.261
```

### Regras de entrada

* A extensão `.261` é adicionada automaticamente quando omitida.
* Caso o arquivo não exista, o programa exibe:

```text
arquivo não encontrado
```

* Caso nenhum parâmetro seja informado:

```text
Erro: Forneça o nome do arquivo fonte como parâmetro.
```

---

#  Arquivos Gerados

A execução produz dois arquivos:

```text
NomeDoArquivo.LEX
NomeDoArquivo.TAB
```

---

##  Relatório `.LEX`

Contém todos os átomos identificados durante a análise léxica.

Para cada átomo são apresentados:

* Lexeme
* Código do átomo
* Índice na tabela de símbolos
* Linha de ocorrência

### Exemplo

```text
Lexeme: PROGRAM,
Código: A19, indiceTabSimb: -,
Linha: 4.

Lexeme: TESTEFINAL,
Código: C03, indiceTabSimb: 1,
Linha: 4.
```

---

##  Relatório `.TAB`

Contém a tabela de símbolos consolidada ao final da análise.

Para cada entrada são apresentados:

* Número da entrada
* Código
* Lexeme
* Quantidade de caracteres antes e depois da truncagem
* Tipo do símbolo
* Linhas de ocorrência

### Exemplo

```text
Entrada: 1, Código: C03, Lexeme: TESTEFINAL,
QtdCharsAntesTrunc: 10, QtdCharDepoisTrunc: 10,
TipoSimb: , Linhas: (4).

Entrada: 2, Código: C01, Lexeme: CONTADOR,
QtdCharsAntesTrunc: 8, QtdCharDepoisTrunc: 8,
TipoSimb: , Linhas: (6, 12).
```

---

#  Exemplo de Uso

## Arquivo `Teste.261`

```java
/* TESTE MESTRE PAVA2026-1
   Equipe E01 - Validacao Final */

program TesteFinal

    integer contador := 0 ;
    real taxaJuros := 12.5e-2 ;
    string nomeDaVariavelComMaisDeTrintaCaracteres := "Muito Grande" ;
    character opcao := 'S' ;

    if ( contador <= 10 ) {
        print taxaJuros ;
    } else {
        break ;
    }

    return ;
```

### Execução

```bash
python main.py Teste
```

---

# Recursos Implementados

### Tratamento de caracteres

* Filtro de caracteres inválidos;
* Conversão automática para caixa alta;
* Linguagem case-insensitive.

### Comentários

* Comentários de bloco:

```java
/* comentário */
```

* Comentários de linha:

```java
// comentário
```

### Constantes reconhecidas

* `intConst`
* `realConst`
* `realConst` com notação exponencial
* `stringConst`
* `charConst`

Exemplos:

```java
123
12.5e-2
"Texto"
'A'
```

### Operadores reconhecidos

Operadores compostos:

```java
:=
<=
>=
==
!=
```

Operadores simples de um caractere também são reconhecidos.

### Identificadores

* Truncamento automático em 30 caracteres válidos;
* Reaproveitamento de entradas já existentes na tabela de símbolos;
* Registro de até cinco linhas de ocorrência.

### Classificação por contexto

| Contexto         | Código |
| ---------------- | ------ |
| Nome de programa | `C03`  |
| Nome de função   | `C02`  |
| Variável         | `C01`  |

---

#  Limitações 

### Análise Sintática

Ainda não implementada.






