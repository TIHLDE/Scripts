from app.enums import FunctionName


def list_functions():
    """
    List all available functions.
    """
    functions = FunctionName.all()
    functions = "\n- ".join(functions)
    print(f"Mulige funksjoner du kan bruke:\n\n- {functions}\n")


if __name__ == "__main__":
    list_functions()