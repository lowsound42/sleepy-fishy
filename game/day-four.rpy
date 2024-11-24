label day_four:
    scene fishfling
    play music "punk.wav"
    show dance
    "You walk into the gym, it looks beautiful. Mr. Pink is standing on stage, with an acoustic guitar."

    show mrpink
    p "Welcome everyone, to the Fish Fling! Dance your hearts out!"
    hide mrpink
    if sally_points > gerty_points:
        show sally:
            zoom 0.75
            xpos 0.3
        s "Hey Finchenzo - wanna dance with me?"
    else:
        show gertrude:
            zoom 0.75
            xpos 0.3
        g "Hey Finchenzo - wanna dance with me?"

    
    menu:
        ff ""
        "This school isn't so bad after all":
            jump happy
        "I realize I'm a lone fish after all. If I'm going to be a Fishfather one day, I've gotta keep my heart cold and my head clear.”":
            jump fishfather

label fishfather:
    scene fishfather
    show shadow office
    f "I'm ready father"
    jump end

label happy:
    ff "Let's dance!"
    jump end

label end:
    scene black
    centered "story: Jessica"
    centered "art: Lisa"
    centered "music: Ali"
    centered "developers: Henry, Thomas, Omar"
    centered "special mention: Gobi the schnauzer"
    centered "built with Renpy"

    stop music fadeout 1.0