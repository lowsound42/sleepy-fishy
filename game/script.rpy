define d = Character('Mafia Dad', color="#5b5655")
define f = Character('Fincenzo', color="#1ea6cd", image="fincenzo")
define p = Character('Mister Pink', color="#eb3af3", image="pink")
define b = Character('Bobby', color="#5b5655")
define sally_points = 0
define gerty_points = 0

image side fincenzo = im.FactorScale("fincenzo.png", 0.25,0.25)

label start:

    scene bg shadow office
    
    show shadow dad

    d "Listen, Finny my boy, we\’ve gotta keep a low profile for now"

    d "The Manta-gues have been on our ass. You\’re gonna be the future Fishhead and I\’ve got to protect you."

    f "{i}Ugh, another day, another school, we have to hide out in this small town. I don\’t even know if I want to be the Fishhead anymore.{/i}"

    jump classroom

