import pandas, numpy, itables


class InteractiveTable:
    def __init__(self, dataframe: pandas.DataFrame):
        self.__dataframe = dataframe.copy(deep=True)
        self.__dataframe.reset_index(inplace=True, drop=True)

        self.__max_bytes = 0
        self.__paging = True
        self.__entries_list = [10, 25, 50, 100]
        self.__order = None

    @property
    def config(self) -> dict:
        cfg = {
            "maxBytes": self.__max_bytes,
            "lengthMenu": self.__entries_list,
            "paging": self.__paging
        }

        if self.__order is not None:
            cfg["order"] = self.__order

        return cfg

    def show(self):
        itables.show(self.__dataframe, **self.config)

    def limit_rows(self, max_rows: int):
        self.__dataframe = self.__dataframe.head(max_rows)

        return self

    def show_index(self, start_value: int = 0):
        # TODO: check if there is already an index column

        self.__dataframe.index = numpy.arange(start_value, len(self.__dataframe) + start_value)
        self.__dataframe.reset_index(inplace=True)

        return self

    def unordered(self):
        self.__order = []

        return self

    def add_order(self, column_name: str, sort_order: str = "asc"):
        assert column_name in self.__dataframe.columns

        if self.__order is None:
            self.__order = []

        idx = list(self.__dataframe.columns).index(column_name)

        self.__order.append([idx, sort_order])

        return self

    def show_entries_menu(self, entries_list: list[int]):
        self.__entries_list = entries_list

        return self

    def no_paging(self):
        self.__paging = False

        return self
