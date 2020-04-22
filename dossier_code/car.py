class Car:
    """
    A class used to represent a Car

    Attributes
    ----------
    color : str
        color of car

    Methods
    -------
    get_color()
        Return current car color
    compare_color(color)
        Compare current car color value with provided color value
    """
    def __init__(self, color):
        self.color = color

    def get_color(self):
        """
        Returning a string that describes the car color
        """
        return f"La voiture est de color {self.color}"

    def compare_color(self, color_to_compare):
        """
        Returning True if color_to_compare is equals to the current car color

        Parameters
        ----------
        color_to_compare : str
        The color to compare with
        """
        return color_to_compare == self.color
