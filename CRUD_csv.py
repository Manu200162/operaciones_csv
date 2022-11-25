import csv


class CRUDCSV:
    def __init__(self, path):
        self.path = path

    def crud_csv(self, function,  rows=[], row=0, new_path='', headers=[]):
        if function == "read":
            self.__load_csv()

        if function == "add_row":
            self.__add_row(rows)
        if function == "add_rows":
            self.__add_rows(rows)
        if function == "update_row":
            self.__update_row(row, rows)
        if function == "delete_row":
            self.__delete_row(row)
        if function == "delete_rows":
            self.__delete_rows(rows)
        if function == "delete_all":
            self.__delete_all()
        if function == "change_csv":
            self.__change_file(new_path)
        if function == "add_headers":
            self.__add_headers(headers)

    def __load_csv(self):
        with open(self.path, 'a+')as file:
            file.seek(0)
            reader = csv.reader(file)
            data = []
            for row in reader:
                data.append(row)
            file.close()
        return data

    def __add_row(self, row: list):
        with open(self.path, 'a', newline='') as file:
            write_row = csv.writer(file)
            write_row.writerow(row)
            file.close()

    def __add_rows(self, rows):
        try:
            with open(self.path, 'a', newline='') as file:
                write_row = csv.writer(file)
                write_row.writerows(rows)
                file.close()
        except:
            print("Se esta tratando de meter un solo elemento, porfavor usar add_row o \n" +
                  "poner como lista de listas [[]]")

    def __update_row(self, row, update):
        data = self.__load_csv()
        if (len(data) > row):
            with open(self.path, 'w', newline='') as result:
                writer = csv.writer(result)
                data[row] = update
                writer.writerows(data)
                result.close()

    def __delete_row(self, row):
        data = self.__load_csv()
        if (len(data) > row):
            with open(self.path, 'w', newline='')as result:
                writer = csv.writer(result)
                data.pop(row)
                writer.writerows(data)
                result.close()
        else:
            print("No se puede eliminiar un elemento inexistente")

    def __delete_rows(self, rows):
        data = self.__load_csv()
        with open(self.path, 'w', newline='')as result:
            writer = csv.writer(result)
            for i, r in enumerate(data):
                if i not in rows:
                    writer.writerow(r)
            result.close()

    def __delete_all(self):
        data = self.__load_csv()
        with open(self.path, 'w') as file:
            file.close()

    def __change_file(self, path):
        self.path = path

    def __add_headers(self, headers):
        with open(self.path, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            file.close()


if __name__ == "__main__":

    csv_manager = CRUDCSV("prueba.csv")
    csv_manager.crud_csv("delete_all")
    csv_manager.crud_csv("add_row", [1, "Estoy Haciendo la prueba", "Si"])
    csv_manager.crud_csv("add_row", [2, "Estoy Haciendo la prueba", "Jaja"])
    csv_manager.crud_csv("add_row", [3, "Estoy Haciendo la prueba", "PuedSer"])
    csv_manager.crud_csv("add_row", [4, "Estoy Haciendo la prueba", "Ya"])
    csv_manager.crud_csv("add_row", [5, "Estoy Haciendo la prueba", "No"])

    csv_manager.crud_csv("update_row", rows=[
                         3, "Hago el update del pex", "Nos"], row=2)
    csv_manager.crud_csv("delete_row", row=1)
    new_rows = [[6, "Ya meto varios pexes", "Jiji"], [7, "SIIIUUUU", "Nel"]]
    csv_manager.crud_csv("add_rows", new_rows)
    csv_manager.crud_csv("delete_rows", rows=[1, 2])
