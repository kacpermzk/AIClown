# AI Comedian Bot

The AI Comedian Bot is a Python program that tells jokes and allows users to rate them. It's a fun and interactive way to enjoy some humor and provide feedback on the jokes.

## Features

- **Tell a Joke:** The bot can tell a random joke from its database or a list of custom jokes.
- **Rate a Joke:** Users can rate the jokes on a scale of 1 to 10, with 1 being very disappointed and 10 being extremely happy.
- **Engage with the User:** The bot engages with the user, asking if they'd like to hear a joke and providing responses based on user interactions.
- **Custom Jokes:** You can provide your own list of jokes to make the bot more personal and tailored to your preferences.
- **Adaptability:** The bot can adapt its responses based on user reactions, trying another joke if the user is not satisfied.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone this repository to your local machine.
2. Navigate to the `bots` directory.
3. Create a new directory with your username or bot's name (e.g., `johndoe`).
4. Place the `joke_bot.py` and `test_bot.py` files into your directory.

### Usage

1. Run the `joke_bot.py` script to start the AI Comedian Bot.
2. Choose an option from the menu:
   - Tell a joke
   - Rate a joke
   - Goodbye (to exit)

### Custom Jokes

You can add your own jokes to the bot by providing a list of jokes when initializing the `Bot` class. Here's how:

```python
custom_jokes = [
    "Your custom joke 1",
    "Your custom joke 2",
    # Add more jokes here
]
bot = Bot(custom_jokes)
