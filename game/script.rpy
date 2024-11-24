define d = Character('Mafia Dad', color="#5b5655")
define f = Character('Fincenzo', color="#1ea6cd", image="fincenzo")
define fs = Character('Fincenzo', color="#1ea6cd", image="school")
define ff = Character('Fincenzo', color="#1ea6cd", image="formal")
define fw = Character('Fincenzo', color="#1ea6cd", image="finwin")
define p = Character('Mister Pink', color="#eb3af3", image="mrpink")
define pl = Character('Pink Lunch', color="#eb3af3", image="lunchpink")
define gd = Character('Mr. Gillyweed', color="#228822", image="mrgillyweed")
define sm = Character('Mrs. Saltwater', color="#228822", image="mrssaltwater")
define b = Character('Gillbert', color="#28a510")
define s = Character('Sally', color="#f27df8")
define sside = Character('Sally', color="#f27df8", image="sally")
define gs = Character('G', color="#cfa853")
define g = Character('Gertrude', color="#e63c1a")
define gside = Character('Gertrude', color="#e63c1a", image="gertrude")
define mrp = Character('Mr. Pink', color="#eb3af3")
define npcf = Character('NPC Fish', color="#cf4226")
define ll = Character('"Lunch Lady"', color="#eb3af3")
define sh = Character('Shellby', color="#86dad5", image="shellby")
define gl = Character('Gillbert', color = "#048f04")
define r = Character('Ramsea', color = "#1d6bd1", image="ramsea")
image sally_scaled = im.Scale("sally.png", 800, 1000)
image gerty_scaled = im.Scale("gertrude.png", 800, 1000)


define sally_points = 0
define gerty_points = 0

image side fincenzo = im.FactorScale("fincenzo.png", 0.25,0.25)
image side school = im.FactorScale("school.png", 0.25,0.25)
image side formal = im.FactorScale("formal.png", 0.25,0.25)
image side finwin = im.FactorScale("finwin.png", 0.25,0.25)
image side ramsea = im.FactorScale("ramsea.png", 0.25,0.25)
image side shellby = im.FactorScale("shellby.png", 0.25,0.25)
image side mrgillyweed = im.FactorScale("mrgillyweed.png", 0.25,0.25)
image side mrssaltwater = im.FactorScale("mrssaltwater.png", 0.15,0.15)
image side gertrude = im.FactorScale("gertrude.png", 0.25,0.25)
image side sally = im.FactorScale("sally.png", 0.25,0.25)

label start:

    scene bg shadow office
    
    show shadow office

    d "Listen, Finny my boy, we\'ve gotta keep a low profile for now"

    d "The Manta-gues have been on our ass. You\'re gonna be the future Fishfather and I\'ve got to protect you."

    f "{i}Ugh, another day, another school, we have to hide out in this small town. I don\'t even know if I want to be the Fishfather anymore.{/i}"

    jump transition


