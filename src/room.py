class Room:
    def __init__(self, name, description, items, n_to={}, s_to={}, w_to={}, e_to={}):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.w_to = w_to
        self.e_to = e_to
        self.items = items

    def add_item(self, newItem):
        self.items.append(newItem)

    def remove_item(self, item):
        self.items.remove(item)

    def __str__(self):
        return f"{self.name} \n\n- Room Description - {self.description} \n"

