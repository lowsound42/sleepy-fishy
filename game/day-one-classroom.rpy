label classroom:

    scene bg class entrance
    with dissolve

    show outside school
    image side school = im.FactorScale("school fincenzo.png", 0.25,0.25)

    show mrpink

    p "Everyone give a warm welcome to Finchenzo Wong, he is transferring here from Atlantis. Feel free to take your seat in the back Finchenzo"

    scene bg class internal
    with dissolve
    show classroom

    show gilbert
    b "Where are those flippers from, the dumpster?"
    "school of fish laugh at Fincenzo"

    label bobby_response:
    menu:
        fs "(bobby asked you if your flippers were from the dumpster)"

        "Flip you, you fugly bottom feeder, I got them at your mom\’s house":
            hide classroom
            hide gilbert
            $ gerty_points += 10
            jump gintro
        "Ignore the fish, choose a seat closer to the window":
            hide classroom
            hide gilbert
            $ sally_points += 10
            jump sintro


    label pink_end:
        hide classroomgeneric
        show classroom
        show mrpink
        p "Ok class, settle down, we’re starting now."