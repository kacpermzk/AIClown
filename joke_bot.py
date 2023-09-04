import random

class Bot:
    def __init__(self, custom_jokes=None):
        if custom_jokes is None:
            self.jokes = self.load_jokes_from_file("jokes.txt")
        else:
            self.jokes = custom_jokes
        self.ratings = {}

    def load_jokes_from_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                jokes = file.read().split('\n\n')  # Assuming jokes are separated by double line breaks
                return [joke.strip() for joke in jokes if joke.strip()]
        except FileNotFoundError:
            print(f"File '{file_path}' not found. Make sure the file is in the same directory as your script.")
            return []

    def tell_joke(self):
        if self.jokes:
            return random.choice(self.jokes)
        else:
            return "I've run out of jokes for now. Please add more jokes to the database."

    def rate_joke(self, joke, rating):
        self.ratings[joke] = rating
        response = "Thank you for rating!"
        
        if rating == 1:
            response += " I'm very disappointed. Can I have another go?"
        elif rating == 10:
            response += " I'm thrilled you enjoyed it so much!"

        return response

    def get_average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings.values()) / len(self.ratings)

    def personalize_joke(self, user_preferences):
        category = user_preferences.get("category")
        return self.tell_joke(category)

    def adapt_joke(self, reaction):
        if reaction.lower() == "boo":
            return "I'm sorry to hear that. Let me try another one: " + self.tell_joke()
        else:
            return self.tell_joke()

    def engage_user(self):
        return "Would you like to hear a joke? You can also specify a category."

    def check_appropriateness(self, joke):
        # In a more advanced version, you can implement a content filter.
        return True
    
if __name__ == "__main__":
    bot = Bot()
    print("AI Comedian Bot")
    print("================")
    while True:
        print("1. Tell a joke")
        print("2. Goodbye")
        choice = input("Choose an option (1/2): ")

        if choice == "1":
            joke = bot.tell_joke()
            print(joke)
            try:
                rating = int(input("Rate the joke (1-10): "))
                if 1 <= rating <= 10:
                    response = bot.rate_joke(joke, rating)
                    print(response)
                else:
                    print("Invalid rating. Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a valid integer rating (1-10).")
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
