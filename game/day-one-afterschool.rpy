label day_one_afterschool:
    scene outside school

    fs "{i}What a day{/i}"

    menu:
        "You walk out the front steps and notice the fish in front of you drop his wallet"

        "Money has been tight since your family had to go into hiding. You take the wallet, each fish for his own, like any Fishfather would.":
            show gerty_scaled
            g "Looks like you\’ve got some extra cash to spend. Want to get a seaweed shake?"   

        "You pick up the wallet, and return it to your fellow fish. A good Fishfather knows when to take and when to give.":
            show sally_scaled
            s "Hey, want to walk home with me?"

    jump transition_one    