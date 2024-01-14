import requests

# Setting up parameters for the Open Trivia Database API request
parameters = {
    "amount": 10,
    "type": "boolean"
}

# Sending a GET request to the Open Trivia Database API with the specified parameters
response = requests.get("https://opentdb.com/api.php",params=parameters)
# Checking for any HTTP errors in the response
response.raise_for_status()

# Parsing the JSON response to extract question data
data = response.json()
question_data = data["results"]

