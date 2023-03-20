import json
import re
import random_responses


# Load JSON data
def load_json(file):
    with open(file, encoding='utf-8') as intents_file:
        print(f"Loaded '{file}' successfully!")
        return json.load(intents_file)


# Store JSON data
intents_data = load_json("intents.json")


def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    # Check all the intents
    for intent in intents_data["intents"]:
        response_score = 0
        required_score = 0
        required_words = intent["required_words"]

        # Check if there are any required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        # Amount of required words should match the required score
        if required_score == len(required_words):
            # print(required_score == len(required_words))
            # Check each word the user has typed
            for word in split_message:
                # If the word is in the intent, add to the score
                if word in intent["user_input"]:
                    response_score += 1

        # Add score to list
        score_list.append(response_score)
        # Debugging: Find the best phrase
        # print(response_score, intent["user_input"])

    # Find the best response and return it if they're not all 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # Check if input is empty
    if input_string == "":
        return "Tafadhali andika kitu ili tuweze kuongea :("

    # If there is no good response, return a random one.
    if best_response != 0:
        return random.choice(intents_data["intents"][response_index]["bot_response"])

    return random_responses.random_string()


while True:
    user_input = input("Wewe: ")
    print("Boti:", get_response(user_input))

