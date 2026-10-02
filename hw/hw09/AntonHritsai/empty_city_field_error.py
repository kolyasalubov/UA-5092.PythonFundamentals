class EmptyCityFieldError(Exception):
    """Exception raised when the city input field is empty."""
    def __init__(self, message: str):
        super().__init__(message)