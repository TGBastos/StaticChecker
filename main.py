from file_reader import findFile
from file_to_list import fileToList

# fr.findFile('x, y'):
# 1º parametro deve ser o nome do arquivo
# o 2º é, opcionalmente, o diretorio em que deseja buscar
file = findFile('Teste')
eachLineInFileList = fileToList(file)

#print(eachLineInFileList)