import sys

def findFile():
        if len(sys.argv) < 2:
            print("Erro: Forneça o nome do arquivo fonte como parâmetro.")
            sys.exit(1)

        fileName = sys.argv[1]

        fileOutput = ''
        if fileName[-4:] != '.261':
             fileName = f'{fileName}.261'
        if len(sys.argv) > 2:
             fileName = f'{sys.argv[2]}{fileName}'
        try:
            with open(fileName, 'r') as file:
                 fileOutput = file.read()
        except FileNotFoundError:
            print('arquivo não encontrado')
            sys.exit(1)
        return fileOutput

def definirNomeBase():
    nome_base = sys.argv[1]
    if nome_base[-4:] == '.261':
        nome_base = nome_base[:-4]
    return nome_base