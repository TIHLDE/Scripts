from app.exceptions import ScriptError
from app.handler import handle_function_call
from app.utils.setup import setup


def main():
    try:
        setup()
        handle_function_call()
    except Exception as e:
        if isinstance(e, ScriptError):
            print(f"\n{e}\n")
            return
        
        print(f"\nEn ukjent feil oppstod, med følgende beskjed: \n\n{e}\n\nVennligst prøv igjen. Hvis problemet vedvarer, kontakt Index.")


if __name__ == "__main__":
    main()