def variable_length_args_demo(*args, **kwargs):
    """
    Demonstrates the use of variable-length arguments.

    :param *args: Any number of positional arguments.
    :param **kwargs: Any number of keyword arguments.
    """
    # Processing positional arguments
    print("Positional arguments:")
    for arg in args:
        print(f" - {arg}")
    
    # Processing keyword arguments
    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f" - {key}: {value}")

# Example usage
variable_length_args_demo(1, 2, 3, name="Salman", age=58, city="Mumbai")
