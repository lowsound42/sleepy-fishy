label threeclass:
    scene day three class
    show classroomgeneric
    show mrpink

    p "Good morning everyone, hope everyone is feeling well-rested, because it\'s time for a POP QUIZ!"
    "There is a collective groan from the room."

    fs "“What the fish! I\'ve only been here for two days, how the fin am I supposed to do this…”"
    
    menu:

        "Steal a look from G\'s test sheet":
            $ gerty_points += 10

        "Do your best to remember everything from the past two days":
            $sally_points += 10

    p "Okay everyone, time\'s up! Hand in your papers. I hope to see that you have all been paying attention! Don\'t forget, today is the last day to buy your Fish Fling tickets. The dance is tomorrow!"
    
    jump threelunch