define d = Character('Mafia Dad', color="#5b5655")
define f = Character('Fincenzo', color="#1ea6cd", image="fincenzo")
define fs = Character('Fincenzo', color="#1ea6cd", image="school")
define p = Character('Mister Pink', color="#eb3af3", image="mrpink")
define pl = Character('Pink Lunch', color="#eb3af3", image="lunchpink")
define b = Character('Bobby', color="#5b5655")
define s = Character('Sally', color="#5b5655")
define g = Character('Gertrude', color="#5b5655")
define mrp = Character('Mr. Pink', color="#5b5655")
define npcf = Character('NPC Fish', color="#cf4226")
define ll = Character('"Lunch Lady"', color="#228822")
define sh = Character('Shellby', color="#86dad5")
define gl = Character('Gilbert', color = "#555555")
define r = Character('Ramsea', color = "#555555")
image sally_scaled = im.Scale("sally.png", 800, 1000)
image gerty_scaled = im.Scale("gertrude.png", 800, 1000)


define sally_points = 0
define gerty_points = 0

image side fincenzo = im.FactorScale("fincenzo.png", 0.25,0.25)
image side school = im.FactorScale("school.png", 0.25,0.25)

label start:

    scene bg shadow office
    
    show shadow office

    d "Listen, Finny my boy, we\'ve gotta keep a low profile for now"

    d "The Manta-gues have been on our ass. You\'re gonna be the future Fishhead and I\'ve got to protect you."

    f "{i}Ugh, another day, another school, we have to hide out in this small town. I don\'t even know if I want to be the Fishhead anymore.{/i}"

    jump classroom


