import requests

# API endpoint URL 
url = "https://jsonplaceholder.typicode.com/users"

try:
    # Get Request to API
    response = requests.get(url)

    # Check request was successful
    if response.status_code == 200:
        users = response.json()

        if len(users) == 0:
            print("No Users Available")
        else:
            # Loop through each user and display users details
            for index, user in enumerate(users, start=1):
                name = user["name"]
                username = user["username"]
                email = user["email"]
                city = user["address"]["city"]

                print(f"User {index}")
                print(f"Name {name}")
                print(f"Username {username}")
                print(f"Email {email}")
                print(f"City {city}")

            
            ## Print Only Users Whose City starts with 'S'
            print("\n Users From Cities Starting With 'S' ")
            for user in users:
                city = user["address"]["city"]
                if city.startswith("S"):
                    print(f"{user['name']} - {city}")
        
    else:
        print(f"Failed to Fetch Details: {response.status_code}")


except requests.exceptions.RequestException as e:
    print("Error Occured while Fetching data", e)
