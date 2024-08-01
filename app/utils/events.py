

def get_event_id(
    message: str = "Skriv inn id til arrangement: "
) -> int:
    """
    Get event id.
    """
    try:
        return int(input(message))
    except ValueError:
        print("\nEvent id må være et tall.\n")
        return get_event_id(message)