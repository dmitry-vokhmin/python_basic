class Warehouse:
    def __init__(self, name):
        self.name = name
        self.__box = []

    def get_item(self, *args):
        self.__box.extend(args)

    def __getitem__(self, item):
        try:
            return self.__box[item]
        except TypeError:
            for tech in self.__box:
                if item == tech.name:
                    return tech

class Technics:
    def __init__(self, *args):
        self.args = args


class Printer(Technics):
    def __init__(self, model, year, name="printer", *args):
        super().__init__(*args)
        self.model = model
        self.year = year
        self.name = name

class Scanner(Technics):
    def __init__(self, model, year, name="scanner", *args):
        super().__init__(*args)
        self.model = model
        self.year = year
        self.name = name

class Xerox(Technics):
    def __init__(self, model, year, name="xerox", *args):
        super().__init__(*args)
        self.model = model
        self.year = year
        self.name = name

a = Printer("sda", 2014)
b = Scanner("wqewqe", 2015)
c = Xerox("5weq1", 2016)
warehouse = Warehouse("home")
warehouse.get_item(a, b, c)
print(warehouse["printer"])