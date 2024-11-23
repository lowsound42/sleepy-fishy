label day_two_afterschool_concert:
    scene concert
    "The secret concert takes place after hours at school. You sneak in at 7PM to the cafeteria, and it is packed with fish."

    show sally_scaled
    s "Hey Finchenzo! So glad you made it. I hope you have a great time!"

    hide sally_scaled
    "You move through the crowd, and as the music starts flowing, the fish start grooving. The music picks up and it\’s time for a MOSH PIT!"

    show mrpinkrock
    p "WE ARE FISH FINGER 11. LET\’S GET READY TO ROCK!"

    menu:
        "How do you want to mosh?"
        "Dance extra hard, with reckless abandon, punching and kicking all over the place":
            s "Wow!! I saw you out there! You really know how to rock!"
            $ sally_points += 10

        "Bob your head. Fishfathers don\’t dance.":
            s "You okay? Next mosh I\’m sure you\’ll be better!"
    
    #insert jump here.


label day_two_afterschool_market:
    scene cafeteria
    "You stay behind after the school bell rings and meet in the cafeteria where Gertrude told you to wait."

    show gertrude_scaled
    g "Ok, everyone, the market is open. You can bid or sell, let\’s see what you\’ve got!"

    menu:
        "You look around the tables, your Jellyfish baby is definitely the most valuable one here."
        "You drop off your limited edition Jellyfish baby at the auction table. Where\’s the fun if you don\’t participate?":
            g "Wow, Jellyboo is so rare! I\’m so glad you came."
            $ gerty_points += 10

        "You keep your Jellyfish baby in your bag, you\’d only put it out if there was something valuable to trade for.":
            g "Hmmm, hope you have something to bring next time."

    #insert jump here.
