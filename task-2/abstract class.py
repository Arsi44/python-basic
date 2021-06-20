from abc import ABCMeta, abstractmethod

# Создаем абстрактный класс
class FileManagerABC(metaclass=ABCMeta):

    @abstractmethod
    def read_file(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def write_file(self, text: str) -> int:
        raise NotImplementedError

    @abstractmethod
    def close_file(self) -> None:
        raise NotImplementedError

# Создаем наследуемы от абстрактного класс
class FileManage(FileManagerABC):
    def __init__(self, filename: str):
        self.f = filename

    def read_file(self) -> str:
        with open(self.f, 'r') as file:
            text = file.read()
        return text

    def write_file(self, text: str) -> int:
        with open(self.f, 'a') as file:
            count = file.write(text)
        print('count:', count)
        return count

    def close_file(self):
        print('Closing', self.f)
        self.f.close()

# Создаем экземпляр класса
file_manager = FileManage('file.txt')


# Проводим операции с экземпляром класса
file_manager.read_file()
file_manager.write_file('\nhello again')

