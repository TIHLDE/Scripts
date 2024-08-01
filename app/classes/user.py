

class User:
    def __init__(
        self,
        user_id,
        first_name,
        last_name,
        email,
        image,
        gender,
        allergy,
        tool,
        number_of_strikes,

    ):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.image = image
        self.gender = gender
        self.allergy = allergy
        self.tool = tool
        self.number_of_strikes = number_of_strikes


class EventRegistrationUser:
    def __init__(
        self,
        user_id,
        first_name,
        last_name,
        email,
        allow_photo,
        event_id
    ):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.allow_photo = allow_photo
        self.event_id = event_id


class SimpleCSVUser:
    def __init__(
        self,
        user_id,
        name,
        email
    ):
        self.user_id = user_id
        self.name = name
        self.email = email