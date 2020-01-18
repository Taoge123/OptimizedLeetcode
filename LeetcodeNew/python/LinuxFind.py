from typing import List
from abc import ABC, abstractmethod
from enum import Enum


class File:
    def __init__(self, dir):
        pass

    def isfile(self):
        pass

    def listAllFiles(self) -> List:
        pass

    def getName(self):
        pass

    def getType(self):
        pass

    def getSize(self):
        pass

    def getLastModifiedDate(self):
        pass


class Filter(ABC):
    def __init__(self, type, condition):
        self.__type = type
        self.__condition = condition

    def getType(self):
        return self.__type

    def getCondition(self):
        return self.__condition

    @abstractmethod
    def satiesfyFilter(self, file: File) -> bool:
        pass


class FilterType(Enum):
    FileType, FileSize = 1, 2


class FileTypeFilter(Filter):
    def __init__(self, condition):
        super(FileTypeFilter, self).__init__(FilterType.FileType, condition)

    def satiesfyFilter(self, file: File) -> bool:
        return file.getType() == self.__condition


class FileSizeFilter(Filter):
    def __init__(self, condition):
        super(FileSizeFilter, self).__init__(FilterType.FileSize, condition)

    def satiesfyFilter(self, file: File) -> bool:
        return file.getSize() == self.__condition


class GenerateFilter:
    @staticmethod
    def generateFilter(filterType, condition):
        if filterType.islower() == 'type':
            return FileTypeFilter(condition)
        elif filterType.islower() == 'size':
            return FileSizeFilter(condition)
        else:
            raise Exception('')


class Find:
    def find(self, string: str):
        filters = []
        file, filters_string = self.parse_string(string)
        for filterType, condition in filters_string:
            filters.append(GenerateFilter().generateFilter(filterType, condition))

        return self.findAllFiles(file, filters)

    def findAllFiles(self, file, filters):
        res = []
        if file.isfile():
            if all(f.satiesfyFilter(file) for f in filters):
                res.append(file)
                return res
        for subfile in file.listAllFiles():
            res.extend(self.findAllFiles(subfile, filters))
        return res

    def parse_string(self, string: str):
        if string.lower().startswith('find'):
            raise Exception('')
        parsed = [i.split() for i in string.lstrip('find').strip().split('-')]
        return File(parsed[0]), parsed[1]
