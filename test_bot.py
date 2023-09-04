from joke_bot import Bot

def test_tell_joke_with_custom_jokes():
    # Initialize the bot with your jokes
    custom_jokes = [
        "You ever notice how grown-up life is just a bunch of questions you're too embarrassed to ask? Like, 'Do I need to own a salad spinner?'",
        "I used to think adulthood was about having it all together, but now I realize it's more about trying not to fall apart in public.",
        # Add more jokes here
    ]
    bot = Bot(custom_jokes)

    # Test if the bot tells a joke from your list
    joke = bot.tell_joke()
    assert joke in custom_jokes

def test_rate_joke_with_custom_jokes():
    # Initialize the bot with your jokes
    custom_jokes = [
        "You ever notice how grown-up life is just a bunch of questions you're too embarrassed to ask? Like, 'Do I need to own a salad spinner?'",
        "I used to think adulthood was about having it all together, but now I realize it's more about trying not to fall apart in public.",
        # Add more jokes here
    ]
    bot = Bot(custom_jokes)

    # Rate a joke from your list
    joke_to_rate = "You ever notice how grown-up life is just a bunch of questions you're too embarrassed to ask? Like, 'Do I need to own a salad spinner?'"
    rating = 8
    bot.rate_joke(joke_to_rate, rating)

    # Check if the rating was recorded correctly
    assert bot.ratings[joke_to_rate] == rating
