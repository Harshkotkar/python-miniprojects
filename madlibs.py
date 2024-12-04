import random

def madlib_():
    print("Welcome to Madlib Game_____:)\n")
    print("Create a funny and meaningful story by filling in the blanks. Let's begin! 😄\n")

    madlibs = [
        {
            "template": """
            Once upon a time, in a {adjective} village named {place}, lived a {adjective2} {animal}. 
            Every morning, it would {verb} around the {object}, hoping to find {food}. 
            One day, a {adjective3} wizard appeared and offered the {animal} a magical {object2}.
            The {animal} used it to {verb2} {plural_noun}, which made the villagers {emotion}. 
            They declared the {animal} their {title}, and the village became the happiest place ever.
            """,
            "prompts": [
                "adjective", "place", "adjective2", "animal", "verb", "object",
                "food", "adjective3", "object2", "verb2", "plural_noun", "emotion", "title"
            ]
        },
        {
            "template": """
            In the land of {place}, a {adjective} {character} named {name} was known for their 
            ability to {verb}. One day, {name} was challenged by a {adjective2} {villain} to a duel 
            of {plural_noun}. With the help of their loyal {animal}, {name} {verb2} and won the duel. 
            The {villain} admitted defeat and decided to become {name}'s apprentice.
            """,
            "prompts": [
                "place", "adjective", "character", "name", "verb", "adjective2",
                "villain", "plural_noun", "animal", "verb2"
            ]
        },
        {
            "template": """
            Deep in the heart of {place}, there was a {adjective} inventor named {name}. 
            {name} created a {object} that could {verb} anything into {plural_noun}. 
            When the {villain} tried to steal the invention, {name} and their {animal} 
            outsmarted them by {verb2}. The villagers celebrated by feasting on {food} 
            and declared {name} a {title} forever.
            """,
            "prompts": [
                "place", "adjective", "name", "object", "verb", "plural_noun",
                "villain", "animal", "verb2", "food", "title"
            ]
        }
    ]

    # Select a random story
    selected_madlib = random.choice(madlibs)

    # Collect user inputs
    inputs = {}
    for prompt in selected_madlib["prompts"]:
        inputs[prompt] = input(f"Enter a {prompt.replace('_', ' ')}: ")

    # Generate the story
    story = selected_madlib["template"].format(**inputs)

    # Display the final story
    print("\nHere's your story! 🌟")
    print(story)

# Run the game
madlib_()
