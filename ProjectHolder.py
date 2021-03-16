#!/usr/bin/env python
# coding:utf-8
import configparser


class ProjectHolder:

    def __init__(self, folder_name='.', resultfile_name='result_data', config='config'):
        conf = configparser.RawConfigParser()
        conf.read(config)
        index_z = int(conf.get('project', 'Zisman_index'))
        print(type(conf.get('result', 'liquids1')))
        conf.set('project', 'Zisman_index', str(index_z + 1))
        with open(config, 'w') as c:
            conf.write(c)

        # self.result = []
        # self.folder = folder_name
        # self.resultfile = resultfile_name
        # self.indexes = []
        # self.__init_config(config, folder_name)
        # self.__init_resultfile(resultfile_name)
        # print(f'Liquids => {self.liquids}, Data => {self.result}')
        # print(
        #     f'Name => {self.project_name}, Total => {self.indexes[-1]}, Owens => {self.indexes[0]}, '
        #     f'Zisman => {self.indexes[1]}')
        #
        # self.load()

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
                    self.indexes.append(info[2])

    def save(self):
        with open(f'{self.folder}/config') as config:
            for line in config.readlines():
                print(line)

    def load(self):
        to_write = [str(int(index) + 1) for index in self.indexes]
        print(to_write)
        with open(f'{self.folder}/config') as config:
            _ = 0
            for line in config.readlines():
                print(line[0:3])
                if line[0:3] == '## ':
                    to_correct = line.split(' ')
                    to_correct[-1] = to_write[_]
                    _ += 1

                    config.write(str(to_correct))

        pass

    @staticmethod
    def __get_project_name(line):
        return line[1]


ProjectHolder()
