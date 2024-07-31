from app.classes import User


def parse_users(users: list) -> list[User]:
    return [
        User(
            user_id=user["user_id"],
            first_name=user["first_name"],
            last_name=user["last_name"],
            email=user["email"],
            image=user["image"],
            gender=user["gender"],
            allergy=user["allergy"],
            tool=user["tool"],
            number_of_strikes=user["number_of_strikes"]
        )
        for user in users
    ]