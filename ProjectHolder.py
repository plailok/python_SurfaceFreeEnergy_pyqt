#!/usr/bin/env python
# coding:utf-8
import configparser


class ProjectHolder:

    def __init__(self, config='config', result='result_data'):
        self.config = config
        self.result_data = result
        conf = configparser.RawConfigParser()
        conf.read(self.config)
        self.index_zisman = conf.getint('project', 'zisman_index')
        self.index_owens = conf.getint('project', 'owens_index')
        self.index_total = conf.getint('project', 'total_index')
        print(self.index_total, self.index_owens, self.index_zisman)

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
