class CustomException(Exception):
    """Custom exception for your project."""
    def __init__(self, message):
        super().__init__(message)

# Example usage of custom exception
def raise_custom_exception():
    raise CustomException("This is a custom exception message.")

# Exception handling function
def handle_exception(exception):
    try:
        raise exception
    except CustomException as e:
        # Handle the custom exception here (e.g., log it)
        import logger  # Import your logger module
        logger.log_error(f"Custom Exception: {str(e)}")
    except Exception as e:
        # Handle other exceptions here
        import logger  # Import your logger module
        logger.log_error(f"An error occurred: {str(e)}")
