label day_three_afterschool:
    scene daythreeafterschool
    show outside school
    "You see a school of parent fish milling around. You were looking for very specific fish after school"

    menu:
        "Look for Sally":
            $ sally_points += 10
            jump find_sally

        "Look for Gertrude":
            $ gerty_points += 10
            jump find_gerty


label find_sally:
    "Sally is standing by her mother Mrs. Saltwater"

    show mrssaltwater:
        xpos 0.1
        zoom 0.75

    show sallysad:
        xpos 0.2
        zoom 0.75
    sm "Salmantha, you left the house looking like that today? What are you wearing!"

    "Sally looks timid, and her eyes are downcast."

    menu:
        "Hey Sally, nice sweater. It looks really good on you.":
            hide sallysad
            show sally:
                xpos 0.2
                zoom 0.75
            $ sally_points += 10
            sm "Why, Sally, who is this floppy ruffian?"
            sside "Let's just go mom"

        "Hey lady, what the flip is up with your fugly ass dress?":
            hide sallysad
            show sally:
                xpos 0.2
                zoom 0.75
            $ sally_points += 20
            sm "Young fish, how dare you?! Salmantha we are going home right this minute!"
            sside "You know what mom, I'm walking home today. I don't want a ride. C'mon let's go Fincenzo!"

    jump internal_monologue

label find_gerty:
    "G is standing by her father Mr. Gillyweed"

    show mrgillyweed:
        xpos 0.1
        zoom 0.75

    show gertrude:
        xpos 0.4
        zoom 0.75
    gd "Gertie sweetie! How was your day? How are your friends? Tell me all about it!"
    
    "(He reaches out and pinches her cheek)"

    "G looks embarrassed and brushes away his hand"
    gside "Don't call me that dad! I told you to call me G!"

    menu:
        "What's swimming, Mr. G *puts arm around G's shoulder” I'm Fincenzo.":
            hide gertrude
            show gertyhappy:
                xpos 0.4
                zoom 0.75
            $ gerty_points += 10
            gd "Oh, my, hello young fish! Well, Gertie, I think we've got to get going home now…"
            gside "Right…See you later Finny"

        "Hey G and Mr. G - we actually have a school project to do together. Is it okay if G stays a bit later after school today?":
            hide gertrude
            show gertyhappy:
                xpos 0.4
                zoom 0.75
            $ gerty_points += 20
            gd "Oh, of course! Gertie, I'll come back to pick you up in an hour? I love you my little flipper."
            
            gside "Okay, see you later dad!"
            
            hide mrgillyweed
            g "Quick thinking Fin!"
    jump internal_monologue

label internal_monologue:
    fs "man, I think a fish is falling in love"
    jump transition_three