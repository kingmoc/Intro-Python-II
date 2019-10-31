class Items:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        return print(f"You have picked up a/n {self.name} (use it wisely)\n")

    def on_drop(self):
        return print(f"You have dropped the {self.name}\n")

    def __str__(self):
        return f"You picked up a/n {self.name} \n Description: {self.description}"

    def __repr__(self):
        return f"Items({repr(self.name), repr(self.description)})"