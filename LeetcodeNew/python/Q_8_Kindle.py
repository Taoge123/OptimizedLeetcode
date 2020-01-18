from enum import Enum
from abc import ABC, abstractmethod


class Format(Enum):
    PDF, TXT = 1, 2


class Book:
    def __init__(self, format_: Format, content: str):
        self.__format = format_
        self.__content = content

    def getFormat(self):
        return self.__format

    def getContent(self):
        return self.__content


class EReader(ABC):
    @abstractmethod
    def readBook(self, book):
        pass

    @abstractmethod
    def EReaderType(self):
        pass


class PDFEReader(EReader):
    def readBook(self, book):
        book.getContent()

    @abstractmethod
    def EReaderType(self):
        return 'PDF'


class TXTEReader(EReader):
    def readBook(self, book):
        book.getContent()

    @abstractmethod
    def EReaderType(self):
        return 'TXT'


class EReaderFactory:
    def creatReader(self, book):
        if book.getFormat() == Format.PDF:
            return PDFEReader()
        elif book.getFormat() == Format.TXT:
            return TXTEReader()
        else:
            raise Exception('')


class Kindle:
    def __init__(self):
        self.__books = []
        self.__readerFactory = EReaderFactory()


    def readBook(self, book):
        reader = self.__readerFactory.creatReader(book)
        return reader.readBook(book)

    def download(self, book):
        pass

    def remove(self, book):
        pass