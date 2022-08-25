import pandas, numpy, itables

# from itables import init_notebook_mode


class InteractiveTable:
    ###
    #
    #   CORE
    #
    def __init__(self, dataframe: pandas.DataFrame):
        # init_notebook_mode(connected=True)

        self.__dataframe = dataframe.copy(deep=True)
        self.__dataframe.reset_index(inplace=True)  # Forces the index to be shown by iTables

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

    ###
    #
    #   BASIC USAGE
    #
    def head(self, max_rows: int):
        self.__dataframe = self.__dataframe.head(max_rows)

        return self

    def drop_index(self):
        self.__dataframe.drop(columns=["index"], inplace=True)

        return self

    def create_index(self, start_value: int = 0):
        if "index" in self.__dataframe.columns:
            self.drop_index()

        self.__dataframe.index = numpy.arange(start_value, len(self.__dataframe) + start_value)
        self.__dataframe.reset_index(inplace=True)

        return self

    ###
    #
    #   ORDERING
    #
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

    ###
    #
    #   LAYOUT
    #
    def show_entries_menu(self, entries_list: list[int]):
        self.__entries_list = entries_list

        return self

    def no_paging(self):
        self.__paging = False

        return self
