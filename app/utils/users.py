from app.classes import (
    User,
    SimpleCSVUser
)


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


def parse_csv_users(users: list) -> list[SimpleCSVUser]:
    users: list[SimpleCSVUser] = []

    for user in users:
        if len(user) != 3:
            print("Feil antall kolonner i CSV-filen. CSV-filen må inneholde tre kolonner: 'user_id', 'name', 'email'. Hopper over bruker.")
            continue
            
        user_id, name, email = user
        users.append(
            SimpleCSVUser(
                user_id,
                name,
                email
            )
        )
    
    return users