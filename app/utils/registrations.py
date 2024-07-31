from app.classes import EventRegistrationUser


def parse_registrations(registrations: list, event_id: str) -> list[EventRegistrationUser]:
    """
    Parse a list of registrations to a list of EventRegistrationUser objects. 
    """
    return [
        EventRegistrationUser(
            user_id=registration["user_info"]["user_id"],
            first_name=registration["user_info"]["first_name"],
            last_name=registration["user_info"]["last_name"],
            email=registration["user_info"]["email"],
            allow_photo=registration["allow_photo"],
            event_id=event_id
        )
        for registration in registrations
    ]


