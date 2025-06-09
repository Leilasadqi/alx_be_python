def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations on two numbers.
    
    Args:
        num1: First number (float)
        num2: Second number (float)
        operation: String specifying the operation ('add', 'subtract', 'multiply', 'divide')
        
    Returns:
        Result of the operation as float, or error message string for division by zero
    """
    operation = operation.lower()
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
