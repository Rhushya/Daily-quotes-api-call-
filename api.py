import requests

# List of categories
categories = [
    "age",
    "alone",
    "amazing",
    "anger",
    "architecture",
    "art",
    "attitude",
    "beauty",
    "best",
    "birthday",
    "business",
    "car",
    "change",
    "communication",
    "computers",
    "cool",
    "courage",
    "dad",
    "dating",
    "death",
    "design",
    "dreams",
    "education",
    "environmental",
    "equality",
    "experience",
    "failure",
    "faith",
    "family",
    "famous",
    "fear",
    "fitness",
    "food",
    "forgiveness",
    "freedom",
    "friendship",
    "funny",
    "future",
    "god",
    "good",
    "government",
    "graduation",
    "great",
    "happiness",
    "health",
    "history",
    "home",
    "hope",
    "humor",
    "imagination",
    "inspirational",
    "intelligence",
    "jealousy",
    "knowledge",
    "leadership",
    "learning",
    "legal",
    "life",
    "love",
    "marriage",
    "medical",
    "men",
    "mom",
    "money",
    "morning",
    "movies",
    "success",
]

# Print the categories
print("Available categories:")
for category in categories:
    print("-", category)

# Prompt the user to enter the category of quotes
category = input("Enter the category of  from the above : ")

# Construct the API URL with the user-provided category
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)

# Replace 'YOUR_API_KEY' with your actual API key
response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})

# Check if the request was successful
if response.status_code == requests.codes.ok:
    print(response.text)  # Print the response (quote)
else:
    print("Error:", response.status_code, response.text)  # Print error message
