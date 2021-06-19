class NegativeValueException(ValueError):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{0} is negative age'.format(self.value)
