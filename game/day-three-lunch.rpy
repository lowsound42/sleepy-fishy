label threelunch:
    scene day three lunch
    
    show lunchroom
    
    "Time for lunch! You are hungry after that pop quiz."

    show npcfish

    npcf "Fish Fling tickets on sale! Get your Fish Fling tickets here!"

    hide npcfish
    show gilbert
    b "Hey new kid! Why would you even bother buying tickets? No one wants to go with the new fish anyway."
    
    menu:
        fs "(Gilbert insulted you)"
        "Try to step around him":
            hide gilbert
            $ sally_points += 10
            jump sally_invite
        "Punch him":
            hide gilbert
            $ gerty_points += 10
            jump gerty_invite


    label sally_invite:


        show sally:
            xpos 0.3
            zoom 0.7

        "Sally intervenes."

        s "Ugh, go away Gillbert. Hey Fincenzo, lots of us are going! You should definitely come."

    jump day_three_afterschool
    
    label gerty_invite:
        

        show gertrude:
            xpos 0.3
            zoom 0.7

        "You land a good one right in his gill. Gill stumbles and is about to fight back until G intervenes"

        s "Flip off Gill, don\'t hate on him since you don\'t have a date. You should come, Finny, it\'s gonna be a good time."
        
    jump day_three_afterschool