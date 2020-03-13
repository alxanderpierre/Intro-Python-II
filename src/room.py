# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        print("---------")
        print(self.name)
        print("")
        print(self.description)
        print(f"{self.get_exists_strings()}")
    def get_exists_strings(self):
        exits = []
        if self.n_to is not None:
            exists.append("n")
        if self.n_to is not None:
            exists.append("s")
        if self.n_to is not None:
            exists.append("e")
        if self.n_to is not None:
            exists.append("w
        return exist
