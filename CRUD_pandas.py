import pandas as pd
import os


class CSVPANDAS:
    def __init__(self, path, columns):
        self.path = path
        self.columns = columns
        self.df = pd.DataFrame(columns=self.columns)

    def crud_csv(self, function, rows={}, edit_index=0, edit_indexes=[]):
        if function == "read":
            self.__load_csv()
        if function == "read_csv":
            self.__read_csv()
        if function == "add_rows":
            self.__add_rows(rows)
        if function == "update_row":
            self.__update_row(edit_index, rows)
        if function == "delete_row":
            self.__delete_row(edit_index)
        if function == "delete_rows":
            self.__delete_rows(edit_indexes)
        if function == "delete_all":
            self.__delete_all()

    def __read_csv(self):
        data = pd.read_csv(self.path)
        # print(data)
        return data

    def __add_rows(self, rows):
        new_rows = pd.DataFrame(rows, columns=self.columns)
        new_dataset = pd.concat([self.df, new_rows])
        new_dataset = new_dataset.to_csv(self.path, mode="a", index=False,
                                         header=not os.path.isfile(self.path))

    def __update_row(self, edit_index, rows):
        data = self.__read_csv()
        if (data.shape[0] > edit_index):
            data.loc[edit_index] = rows
            data.to_csv(self.path, index=False)
        else:
            print("No se puede editar una fila inexistente")

    def __delete_row(self, edit_index):
        data = self.__read_csv()
        if (data.shape[0] > edit_index):
            data = data.drop(edit_index)
            data.to_csv(self.path, index=False)
        else:
            print("No existe la fila que quiere eliminar")

    def __delete_rows(self, edit_indexes):
        data = self.__read_csv()
        if (data.shape[0] > max(edit_indexes)):
            for i in edit_indexes:
                data = data.drop(i)
            data.to_csv(self.path, index=False)
        else:
            print("No se puede eliminar alguna columna por su inexistencia")

    def __delete_all(self):
        data = pd.DataFrame(columns=self.columns)
        data = data.to_csv(self.path, mode='w', index=False)


if __name__ == '__main__':
    manager = CSVPANDAS("algo.csv", ["name", "last_name", "age"])
    manager.crud_csv("delete_all")
    manager.crud_csv("add_rows", {"name": ["Pedro", "Miguel", "Juan", "Adrian", "Manuel"],
                                  "last_name": ["Pedrales", "Pedraza", "Fernandez", "Apaza", "Delgadillo", ], "age": [25, 20, 56, 45, 15]})
    manager.crud_csv("update_row", rows={"name": "Luis",
                                         "last_name": "Afif", "age": 20}, edit_index=1)
    manager.crud_csv("delete_row", edit_index=0)
    manager.crud_csv("delete_rows", edit_indexes=[0, 1])
