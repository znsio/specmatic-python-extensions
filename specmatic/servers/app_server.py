from abc import abstractmethod, ABC


class AppServer(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def set_app_config(self, host: str, port: int):
        pass

    @abstractmethod
    def reset_app_config(self):
        pass

    @property
    @abstractmethod
    def host(self):
        pass

    @property
    @abstractmethod
    def port(self):
        pass
