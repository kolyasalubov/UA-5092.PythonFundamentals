class NegativeAgeError(ValueError):
    """Raised when a negative age is provided."""


class OutOfBoundsException(BaseException):
    """Raised when a number is outside the allowed range."""
    def __init__(self, data):
        self.data = f"{data} number is out of allowed range."

    def __str__(self):
        return repr(self.data)
