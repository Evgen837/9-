 # -*- coding: utf-8 -*-
# # сделать генератор текста на основе статсистики
# # Идея проста: подсчитаем какие буквы наиболее часто стоят рядом
# # Точнее, подсчитаем как часто за буквой Х идет буква У, на основе романа Война и мир
# # После этого начнем с произвольной буквы и каждую следующую будем выбирать в зависимости от
# # частоты ее появления в статистике.
# # Для этого нужно открыть файл, подготовить статсистику и затем генерить текст
#
# # !Запомнить! привести к нужному виду во всех ОС: os.path.normpath(path)
# # Пример: path = 'C:/Windows/help'
# # path_normalized = os.path.normpath(path)
# # print(path_normalized)
# # получить время создания файла: print(os.path.getctime(file))
#
# import zipfile
#
# # zip_file_name = 'robinson.zip'
# # zfile = zipfile.ZipFile(zip_file_name, 'r')
# # for filename in zfile.namelist():
# #     zfile.extract(filename)
#
# # посчитаем статистику
# from pprint import pprint
# from random import randint
#
# file_name = 'voina.txt'
# stat = {}
# sequence = '   '
# with open(file_name, 'r', encoding='ANSI') as file:
#     for line in file:
#         # print(line)
#         for char in line:
#             if sequence in stat:
#                 if char in stat[sequence]:
#                     stat[sequence][char] += 1
#                 else:
#                     stat[sequence][char] = 1
#             else:
#                 stat[sequence] = {char: 1}
#             sequence = sequence[1:] + char
#
# # pprint(stat)
# # pprint(len(stat))
# totals = {}
# stat_for_generate = {}
# for sequence, char_stat in stat.items():
#     totals[sequence] = 0
#     stat_for_generate[sequence] = []
#     for char, count in char_stat.items():
#         totals[sequence] += count
#         stat_for_generate[sequence].append([count, char])
#     stat_for_generate[sequence].sort(reverse=True)
# # pprint(totals)
# # pprint(stat_for_generate)
#
# # теперь генерация
# N = 1000
# printed = 0
# sequence = '   '
# while printed < N:
#     char_stat = stat_for_generate[sequence]
#     total = totals[sequence]
#     dice = randint(1, total)
#     pos = 0
#     for count, char in char_stat:
#         pos += count
#         if dice <= pos:
#             break
#     print(char, end='')
#     printed += 1
#     sequence = sequence[1:] + char






# # написать скрипт для упрорядочивания фотографий
# # скприпт должен разложить файлы из одной папки по годам и месяцам в другую
# #
# import os
# import shutil
# import zipfile
# from abc import ABCMeta, abstractmethod
#
# class FilesSorter(metaclass=ABCMeta):
#
#     def __init__(self, zip_archive, target_folder):
#         self.zip_archive = zip_archive
#         self.target_folder = target_folder
#         self.zip_file = None
#         self.file_name = None
#
#     def sorting_files(self):
#         self._create_target_folder()
#         with zipfile.ZipFile(file=self.zip_archive) as self.zip_file:
#             for self.file_name in self.zip_file.namelist():
#                 self._replace_from_archive_to_sub_folder()
#
#     def _create_target_folder(self):
#         if not os.path.isdir(self.target_folder):
#             os.makedirs(self.target_folder)
#
#     @abstractmethod
#     def _create_sub_folder(self):
#         pass
#
#     def _replace_from_archive_to_sub_folder(self):
#         if (self.zip_file.getinfo(name=self.file_name)).file_size > 0:
#             new_folder = self._create_sub_folder()
#             if not os.path.isdir(new_folder):
#                 os.makedirs(new_folder)
#             with self.zip_file.open(name=self.file_name, mode='r') as src:
#                 with open(file=os.path.join(new_folder, os.path.basename(self.file_name)), mode='wb') as dst:
#                     shutil.copyfileobj(fsrc=src, fdst=dst)
#
# class SortByMonths(FilesSorter):
#     def _create_sub_folder(self):
#         file_info = (self.zip_file.getinfo(name=self.file_name)).date_time
#         return os.path.normpath(os.path.join(self.target_folder, str(file_info[0]), str(file_info[1])))
#
# target_folder = os.path.normpath(os.path.join(os.path.dirname(__file__), 'icons_by_year'))
# zip_archive = 'icons.zip'
# sort_by_months = SortByMonths(zip_archive=zip_archive, target_folder=target_folder)
# sort_by_months.sorting_files()


