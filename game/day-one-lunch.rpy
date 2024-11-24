define sally_fight = True
define fight_status = True

label day_one_lunch:

    scene bg lunch room line
    show lunchroom

    "You arrive in the lunchroom, and notice the line is very long and you are very hungry."
    
    menu: 
        "You decide to:"

        "Pretend to know someone in the line and cut in":

            $ gerty_points += 1
            jump cut_line

        "Stand at the back of the line":

            $ sally_points += 1
            jump bully_lunch

label cut_line:
    show npcfish

    f "Hey my fishman - long time no see. It\'s been ages eh! Haven\'t seen you since Mussel Camp"

    pl "Oh, uh, haha, yeah! How\'s it going"

    f "Oh good, y\'know, swimming around. Ok see you later!"
    hide npcfish
    show fincenzo:
        xpos 0.2
        zoom 0.75

    show lunchpink:
        xpos 0.5

    show npcfish at left:
        zoom 0.80

    ll "Hey there new fish on the block, have some extra worms, on the house!"
    jump bully_lunch


label bully_lunch:
    scene bg lunch room line
    show lunchroom
    show npcfish:
        xpos 0.4
        ypos 0.3
        zoom 0.25

    "You notice a small guppy fish, Shellby, getting their lunch money stolen. He stands sad and small and dejected in the back."

    menu:
        "You decide to:"

        "You go over to him quietly, and offer your extra worms. Shellby is grateful":
            sh "Thanks so much!"

            hide npcfish

            show sally_scaled

            s "Hey - Finchenzo right? I saw what you did. That was really nice. Want to sit with me?"

            show sally_scaled at left

            show gilbert at right

            gl "Yo Sally, come sit with me and leave this loser behind"

            gl "{i}He pulls her fin{/i}"

            s "Let go of me, Gillbert!"
            
            $ sally_points += 1

            jump fish_fight
        
        "You go over to the fish bully, stick out your fin to make him trip.":

            $ sally_fight = False
            
            hide npcfish

            show gilbert

            "Gilbert falls into his food"

            gl "Who the flip do you think you are my guy?"

            $ gerty_points += 1

            jump fish_fight


label fish_fight:
    scene bg lunch room line
    show fightscene

    call fight_start

    if fight_status:
        show finwin:
            pos(0.05, 0.60)
            zoom 0.25

        if sally_fight:
            
            show sally_scaled

            s "Wow, thanks Finchenzo! Are you okay? Where\'d you learn to fight like that?"
            
            menu: 
                "Oh that was nothing. My dad taught me how to fight":
                    $ sally_points += 1
                    jump day_one_afterschool

                "I just got lucky. I don\'t usually do things like that":
                    jump day_one_afterschool
        else:

            show gerty_scaled
            
            gs "Smooth moves there, Finny boy. That guy\'s major chum scum. Where\'d you learn to fight like that?"

            menu: 
                "Oh that was nothing. My dad taught me how to fight":
                    $ gerty_points += 1
                    jump day_one_afterschool

                "That fish has two left fins, he didn\'t stand a chance anyway.":
                    jump day_one_afterschool
    else:
        if sally_fight:
            
            show sally_scaled:
                xpos 0.4
                zoom 0.75

            show gillbertwin:
                xpos 0.1
                zoom 0.75

            s "You okay, Finchenzo? Thanks for trying to help, that guy\'s a total blowhole."

            fs "Thanks, I\'m okay"

            fs "{i}Ugh, my dad would be so disappointed{/i}"

            jump day_one_afterschool
        else:

            show gerty_scaled:
                xpos 0.4
                zoom 0.75
            
            show gillbertwin:
                xpos 0.1
                zoom 0.75

            gs "Need some help there, Finny boy? That guy\'s major chum scum."

            fs "Thanks, I\'m okay"

            fs "{i}Ugh, my dad would be so disappointed{/i}"
            jump day_one_afterschool
