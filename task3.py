import requests
def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()  
    else:
        print("Failed to fetch data")
        return []
def search_users(users, keyword):
    keyword = keyword.lower()
    return [
        user for user in users
        if keyword in user["name"].lower()
        or keyword in user["email"].lower()
    ]
def display_users(users):
    if not users:
        print("No matching records found.")
        return

    print("\nMatched Users:")
    print("-" * 50)
    for user in users:
        print(f"Name  : {user['name']}")
        print(f"Email : {user['email']}")
        print(f"City  : {user['address']['city']}")
        print("-" * 50)
def main():
    users = fetch_users()

    if not users:
        return

    keyword = input("Enter name or email to search: ")
    filtered_users = search_users(users, keyword)
    display_users(filtered_users)

if __name__ == "__main__":
    main()
