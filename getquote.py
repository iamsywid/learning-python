import random


def get_quote():
    listOfQuotes = [
        "You don’t have to turn this into something. It doesn’t have to upset you. - Marcus Aurelius",
        "A wise man once said nothing.",
        "We travel, initially, to lose ourselves; and we travel, next, to find ourselves” – Pico Iyer",
        "I love sleep. My life has the tendency to fall apart when I’m awake, you know?” – Ernest Hemingway",
        "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. — Ralph Waldo Emerson",
        "People don't tend to wander around and suddenly find themselves at the top of Mount Everest. - Zig Ziglar",
        "When you judge another, you do not define them, you define yourself. - Wayne Dyer",
        "You don't lead by pointing and telling people some place to go. You lead by going to that place and making a case. - Ken Kesey"
    ]
    return random.choice(listOfQuotes)

print(get_quote())
