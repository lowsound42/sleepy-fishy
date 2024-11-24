define sally_secret = True
define gerty_secret = True

label twolunch:
    scene day two lunch
    
    show lunchroom
    
    show ramsea:
        xpos 0.1
        zoom 0.75

    show npcfish:
        xpos 0.4
        ypos 0.3
        zoom 0.25

    "You\'re sitting and eating your lunch. Ramsea comes up to you, little Shellby in tow."

    r "Hey Finchenzo, I saw what you did yesterday for little Shellby. He\'s my little brother."

    sh "Thanks so much man! That guy\'s real chum scum"

    r "Can we sit with you?"

    jump ramsea_response

    label ramsea_response:
    menu:
        fs "(Ramsea asked to sit with you)"

        "Yeah man, feel free":
            $ sally_points += 10
        "It\'s a free fish country, do what you want":
            $ gerty_points += 10
    
    r "Listen, you did something for him, and I wanna do something for you. This school deals in secrets and I know all of them. Normally I charge for information, but I\'ll give you one on the house. What do you want to know?"

    menu:
        fs "(Ramsea will tell you a secret)"

        "Learn a secret about the school":
            $ sally_points += 10
            jump faculty_secret
        "Learn gossip about another student":
            $ gerty_points += 10
            jump student_secret


    label faculty_secret:
        r "Mr Pink is part of an anti-establishment rock band, he\'s playing a show tonight. If you\'re interested, you should talk to Spunk"

        fs "Who\'s spunk?"

        r "Oh right - it\'s Sally. That'\s her stage name."

        hide ramsea
        hide npcfish

        show sally:
            xpos 0.3
            zoom 0.7

        "You find Sally in the lunchroom."

        s "Hey Fincenzo, what\'s up?"

    menu:

        "Hey Spunk - heard there\'s a show tonight, can I score tickets?":
            $ sally_points += 10
            s "Haha, of course! I\'ll send you the details."

        "Wow Sally, you\'re in a band with our teacher? What\'s up with that?":
            s "Hey, you\'ve never heard a fish play! You should come check us out tonight, we\'re gonna blow you away!"

    jump day_two_afterschool_concert
    
    label student_secret:
        r "There is an underground market that sells fishy babies™. If you\'re looking to make some extra cash, you should talk to Gertrude"

        fs "Who\'s Gertrude?"

        r "Oh fish! You didn\'t hear that from me, I meant “G.” But don\'t call her that, she hates it"

        hide ramsea
        hide npcfish

        show gertrude:
            xpos 0.3
            zoom 0.7

        "You find G in the lunchroom."

    menu:

        "Hey G, I heard you\'re in on the Fishy Beanie game - I want in":
            s "Meet me after school at 4PM, bring your stash."

        "Hey Gertrude, I\'ve got Fishy Beanies at home I\'m trying to move - I want in":
            $ gerty_points += 10
            s "Whoa Finboy! Keep your voice down. Meet me after school at 4PM, bring your stash."

    jump day_two_afterschool_market