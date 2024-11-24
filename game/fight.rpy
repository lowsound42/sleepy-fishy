label fight_start:

    scene classroomgeneric

    $ cont = 0 #continue variable
    $ counter = 0
    $ arr_keys = ["K_LEFT", "K_RIGHT", "K_UP", "K_DOWN"] #list of keyboard inputs to be selected from. See https://www.pygame.org/docs/ref/key.html for more keys

    call qte_setup(0.5, 0.5, 0.01, renpy.random.choice(arr_keys), 0.5, 0.5)
    # call qte_setup(0.5, 0.5, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
    # "Function Call" - see label qte_setup for detail on "function"
    # in the above, I randomly select a key from a previously defined set of keys (arr_keys), and randomise the location

    while cont == 1 and counter < 10:
        call qte_setup(0.5, 0.5, 0.01, renpy.random.choice(arr_keys), 0.5, 0.5)
        # call qte_setup(0.5, 0.5, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
        $ counter = counter + 1
        # to repeat the qte events until it is missed

    if counter == 10: #if we reached 10 rounds without missing
        #"Success!"
        $ fight_status = True
        
    else:
        #play sound "sounds/miss.mp3"
        #"{b}GAME OVER{/b}"
        $ fight_status = False

    # basic game over sound + message

    return
    
'''
"Function"/pseudo-function
calls the qte screen
parameters are:
    - amount of time given
    - total amount of time (is usually the same as above)
    - timer decreasing interval
    - the key/keyboard input to hit in the quick time event
    - the x alignment of the bar/box
    - the y alignment of the bar/box
'''
label qte_setup(time_start, time_max, interval, trigger_key, x_align, y_align):

    $ time_start = time_start
    $ time_max = time_max
    $ interval = interval
    $ trigger_key = trigger_key

    hide right
    hide left
    hide up
    hide down

    if trigger_key == "K_RIGHT":
        show right:
            xalign 0.5
            yalign 0.4

    elif trigger_key == "K_LEFT":
        show left:
            xalign 0.5
            yalign 0.4

    elif trigger_key == "K_UP":
        show up:
            xalign 0.5
            yalign 0.4

    elif trigger_key == "K_DOWN":
        show down:
            xalign 0.5
            yalign 0.4

    call screen qte_simple
    # can change to call screen qte_button to switch to button mode
    

    $ cont = _return
    # 1 if key was hit in time, 0 if key not

    return

screen qte_simple:
    #key input qte

    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_simple')])
    # timer, using variables from label qte_setup
    # false is the condition if the timer runs out - and this will be reached if the user doesn't get hit the key on time

    key trigger_key action ( Return(1) )
    # the "key detector" (ends qte_event by returning 1)

    # vbox:
    #     xalign x_align
    #     yalign y_align
    #     spacing 25
    #     # vbox arrangement

    #     text trigger_key:
    #         xalign 0.5
    #         color "#e30606"
    #         size 36

    bar:
        value time_start
        range time_max
        xalign 0.5
        yalign 0.6
        xmaximum 300
        if time_start < (time_max * 0.25):
            left_bar "#f00"
            # this is the part that changes the colour to red if the time reaches less than 25%
