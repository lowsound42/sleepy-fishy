label classroom:

    scene newschool
    show outside school
    image side school = im.FactorScale("school fincenzo.png", 0.25,0.25)
    
    show school:
        zoom 0.65
        xpos 0.3
    "You arrive at Fish High for your first day"
    hide school
    scene bg class internal
    show classroom
    show mrpink with Dissolve(1.0)
    p "Everyone give a warm welcome to Fincenzo Wong, he is transferring here from Atlantis. Feel free to take your seat in the back Fincenzo"
    hide mrpink

    show gilbert
    b "Where are those flippers from, the dumpster?"
    "You notice the school of fish laugh and jeer"

    label bobby_response:
    menu:
        fs "(Gillbert asked you if your flippers were from the dumpster)"

        "Flip you, you fugly bottom feeder, I got them at your mom\'s house":
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
        p "Ok class, settle down, we're starting now."
        jump day_one_lunch


