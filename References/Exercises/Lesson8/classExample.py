class Patient (object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.condition = []

    def get_details(self):
        print(f"Patient record: " + self.name , self.age + " years"\
            f"current information: " + self.condition )

    def add_info(self, information):
        self.condition.append(information)

class infant(Patient):

    def __init__(self, name, age):
        self.vaccination = []
        super().__init__(name, age)

    def add_vac(self, vaccine):
        self.vaccination.append(vaccine)

    def get_details(self):
        print(f"Patient record:" + self.name , self.age + "years"
            f"vaccine information: " + self.vaccination +
            f"current information: "+ self.condition )

steve = Patient("Steven Hughes", "40")
Greg = infant("Greg Stephen", "1")