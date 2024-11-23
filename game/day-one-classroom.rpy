label classroom:

    scene bg class entrance
    with dissolve
    
    show mister pink

    p "Everyone give a warm welcome to Finchenzo Wong, he is transferring here from Atlantis. Feel free to take your seat in the back Finchenzo"

    scene bg class internal
    with dissolve

    show bobby
    b "Where are those flippers from, the dumpster?"
    "school of fish laugh at Fincenzo"

    label bobby_response:
    menu:
        "Flip you, you fugly bottom feeder, I got them at your mom\’s house":
            $ gerty_points += 10
            jump gintro
        "Ignore the fish, choose a seat closer to the window":
            $ sally_points += 10
            jump sintro


