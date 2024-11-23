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

        "Stand at the back of the line":

            $ sally_points += 1

    jump cut_line


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
    show shellby

    "You notice a small guppy fish, Shellby, getting their lunch money stolen. He stands sad and small and dejected in the back."

    menu:
        "You decide to:"

        "You go over to him quietly, and offer your extra worms. Shellby is grateful":
            sh "Thanks so much!"

            hide shellby

            show sally

            s "Hey - Finchenzo right? I saw what you did. That was really nice. Want to sit with me?"

            show sally at left

            show gilbert at right

            gl "Yo Sally, come sit with me and leave this loser behind"

            gl "{i}He pulls her fin{/i}"

            s "Let go of me, Gillbert!"
            
            $ sally_points += 1

            jump fish_fight
        
        "You go over to the fish bully, stick out your fin to make him trip.":

            $ sally_fight = False
            
            hide shellby

            show gilbert

            "Gilbert falls into his food"

            gl "Who the flip do you think you are my guy?"

            $ gerty_points += 1

            jump fish_fight


label fish_fight:
    scene bg lunch room line
    show lunchroom

    "FIGHT moment, this should be a MINIGAME!!!"

        if fight_status:

            if sally_fight:
                
                show sally

                s "Wow, thanks Finchenzo! Are you okay? Where\'d you learn to fight like that?"

                menu: 
                    "Oh that was nothing. My dad taught me how to fight":

                        $ sally_points += 1

                        jump twoclass

                    "I just got lucky. I don\'t usually do things like that":

                        jump twoclass
            else:

                show gertrude
                
                g "Smooth moves there, Finny boy. That guy\'s major chum scum. Where\'d you learn to fight like that?"

                menu: 
                    "Oh that was nothing. My dad taught me how to fight":

                        $ gerty_points += 1
                        jump twoclass

                    "That fish has two left fins, he didn\'t stand a chance anyway.":
                        jump twoclass

        else:
            if sally_fight:
                
                show sally

                s "You okay, Finchenzo? Thanks for trying to help, that guy\'s a total blowhole."

                f "Thanks, I\'m okay"

                f "{i}Ugh, my dad would be so disappointed{/i}"

                jump twoclass
            else:

                show gertrude
                
                g "Need some help there, Finny boy? That guy\'s major chum scum."

                f "Thanks, I\'m okay"

                f "{i}Ugh, my dad would be so disappointed{/i}"
                jump twoclass