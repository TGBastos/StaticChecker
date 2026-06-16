import file_to_list as fl
def findFile(fileName, fileDir = '.'):
        fileOutput = ''
        if fileName[-4:] != '.261':
             fileName = f'{fileName}.261'
        if fileDir != '.':
             fileName = f'{fileDir}{fileName}'
        try:
            with open(fileName, 'r') as file:
                 fileOutput = file.readlines()
        except FileNotFoundError:
            print('arquivo não encontrado')
        return fileOutput