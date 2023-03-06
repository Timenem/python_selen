"""
You're modelling the interaction between a large number of quarks and have decided to create a Quark class so you can generate your own quark objects.

Quarks are fundamental particles and the only fundamental particle to experience all four fundamental forces.
Your task

Your Quark class should allow you to create quarks of any valid color ("red", "blue", and "green") and any valid flavor ('up', 'down', 'strange', 'charm', 'top', and 'bottom').

Every quark has the same baryon_number (BaryonNumber in C#): 1/3.

Every quark should have an .interact() (.Interact() in C#) method that allows any quark to interact with another quark via the strong force. When two quarks interact they exchange colors.
"""
class Quark:
    baryon_number = 0.3333333333333333
    __valid_colors = ['red', 'green', 'blue']
    __valid_positions = ['up', 'down', 'strange', 'charm', 'bottom', 'top']

    def __init__(self, color: str, flavor: str):
        """set valid color and flavor """
        if color not in self.__valid_colors:
            raise Exception("not valid color")
        else:
            self.color = color
        if flavor not in self.__valid_positions:
            raise Exception("not valid flavor")
        else:
            self.flavor = flavor

    def interact(self, other_quark: 'Quark'):
        """changing current color to opposite """
        self.color, other_quark.color = other_quark.color, self.color
