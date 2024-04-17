import sys
import os

from utils import get_users


def main():
    if len(sys.argv) > 1:
        X_CSRF_TOKEN = sys.argv[1]
    else:
        print("Du må oppgi din X-CSRF-TOKEN.")
        return
    
    if os.path.exists("results.txt"):
        os.remove("results.txt")
    
    page = 1
    
    response = get_users(X_CSRF_TOKEN, page)

    users = response["results"]
    has_next_page = response["next"]

    while has_next_page:
        page += 1
        response = get_users(X_CSRF_TOKEN, page)
        users += response["results"]
        has_next_page = response["next"]
    
    for user in users:
        with open("results.txt", "a") as f:
            f.write(f"{user['first_name']} {user['last_name']} - {user['email']} - {user['study']['group']['name']}\n")


if __name__ == "__main__":
    main()