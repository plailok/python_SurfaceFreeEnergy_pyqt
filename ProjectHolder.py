class ProjectHolder:

    def __init__(self, folder_name=None, resultfile_name='result_data', config='config'):
        self.result = []
        self.folder = folder_name
        self.resultfile = resultfile_name
        self.__init_config(config, folder_name)
        self.__init_resultfile(resultfile_name)
        print(f'Liquids => {self.liquids}, Data => {self.result}')
        print(
            f'Name => {self.project_name}, Total => {self.index}, Owens => {self.index_owens}, '
            f'Zisman => {self.index_zisman}')

    def __init_resultfile(self, resultfile_name):
        with open(resultfile_name, 'r+') as f:
            data = f.readlines()
            for line in data:
                if line.split(',')[0] == 'LIQUIDS':
                    self.liquids = line.split(',')[1:-1]
                    print('No digits', line[:-1])
                else:
                    self.result.append(line.split(',')[:-1])
                    print('Digits', line[:-1])

    def __init_config(self, config, folder_name):
        with open(config, 'r+') as f:
            data = f.readlines()
            for line in data:
                info = line[:-1].split(' ')
                if len(info) == 2:
                    self.project_name = folder_name if folder_name is not None else self.__get_project_name(info)
                elif len(info) == 3:
                    if info[1][0] == 'O':
                        self.index_owens = info[2]
                    elif info[1][0] == 'Z':
                        self.index_zisman = info[2]
                    else:
                        self.index = info[2]

    def save(self):
        with open(f'{self.folder}/config') as config:
            for line in config.readlines():
                print(line)

    def load(self):
        pass

    @staticmethod
    def __get_project_name(line):
        return line[1]


ProjectHolder()
