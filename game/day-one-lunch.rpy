define sally_fight = True

label day_one_lunch:

    scene bg lunch room line

    "You arrive in the lunchroom, and notice the line is very long and you are very hungry."
    
    menu: 
        "You decide to:"

        "Decide to cut at the beginning of the line":

            jump cut_line

            $ gerty_points += 1

        "Stand at the back of the line":

            $ sally_points += 1


label cut_line:
    show npc fish lunch
    f "Hey my fishman - long time no see. It\’s been ages eh! Haven\’t seen you since Mussel Camp"

    npcf "Oh, uh, haha, yeah! How\’s it going"

    f "Oh good, y\’know, swimming around. Ok see you later!"

    show fincenzo:
        xpos 0.1
        zoom 0.75

    show lunch lady:
        xpos 0.5

    show npc fish lunch at left

    ll "Hey there new fish on the block, have some extra worms, on the house!"
    jump bully_lunch


label bully_lunch:
    scene bg lunch room line
    show shellby

    "You notice a small guppy fish, Shellby, getting their lunch money stolen. He stands sad and small and dejected in the back."

    menu:
        "You decide to:"

        "You go over to him quietly, and offer your extra worms. Shellby is grateful":
            sh "Thanks so much!"

            hide shellby

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
            
            hide shellby

            show gilbert

            "Gilbert falls into his food"

            gl "Who the flip do you think you are my guy?"

            $ gerty_points += 1

            jump fish_fight


label fish_fight:
    scene bg lunch room line

    "FIGHT moment, this should be a MINIGAME!!!"
    
    menu: 
        "Win":
            if sally_fight:
                
                show sally_scaled

                s "Wow, thanks Finchenzo! Are you okay? Where\’d you learn to fight like that?"

                menu: 
                    "Oh that was nothing. My dad taught me how to fight":

                        $ sally_points += 1
                        pass

                    "I just got lucky. I don\’t usually do things like that":
                        
                        pass

            else:

                show gertrude_scaled
                
                g "Smooth moves there, Finny boy. That guy\’s major chum scum. Where\’d you learn to fight like that?"

                menu: 
                    "Oh that was nothing. My dad taught me how to fight":

                        $ gerty_points += 1
                        pass

                    "That fish has two left fins, he didn\’t stand a chance anyway.":

                        pass
        "Lose":
            if sally_fight:
                
                show sally_scaled

                s "You okay, Finchenzo? Thanks for trying to help, that guy\’s a total blowhole."

                f "Thanks, I\’m okay"

                f "{i}Ugh, my dad would be so disappointed{/i}"
            else:

                show gertrude_scaled
                
                g "Need some help there, Finny boy? That guy\’s major chum scum."

                f "Thanks, I\’m okay"

                f "{i}Ugh, my dad would be so disappointed{/i}"

    jump day_one_afterschool