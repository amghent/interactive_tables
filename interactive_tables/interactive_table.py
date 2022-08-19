import pandas
import itables


class InteractiveTable:
    def __init__(self, dataframe: pandas.DataFrame):
        self.__dataframe = dataframe
        self.__maxBytes = 0

    @property
    def config(self) -> dict:
        cfg = {
            "maxBytes": self.__maxBytes
        }

        return cfg

    def show(self):
        itables.show(self.__dataframe, **self.config)
