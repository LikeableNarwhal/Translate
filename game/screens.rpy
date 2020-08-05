init -3 python:
    # config.game_menu.insert(1,( "text_history", u"Text History", ui.jumps("text_history_screen"), 'not main_menu'))

    # styles
    style.readback_window.xsize = 580
    style.readback_window.ysize = 720
    style.readback_window.align = (.05, .5)
    style.readback_window.background = Transform("#000", alpha=persistent.window_opacity)


    style.readback_frame.background = None
    style.readback_frame.xpadding = 10
    style.readback_frame.xmargin = 15
    style.readback_frame.ymargin = 15

    #style.readback_text.color = "#"

    style.create("readback_button", "readback_text")
    style.readback_button.background = None

    style.create("readback_button_text", "readback_text")

    #style.readback_label_text.bold = True
    style.readback_label_text.font = "GUI/Fonts/NotoSansCJKjp-DemiLight.otf"
    style.readback_label_text.color = "#fefbee"

    # starts adding new config variables
    config.locked = False

    # Configuration Variable for Text History
    config.readback_buffer_length = 100 # number of lines stored
    config.readback_full = True # True = completely replaces rollback, False = readback accessible from game menu only (dev mode)
    config.readback_disallowed_tags = ["size"] # a list of tags that will be removed in the text history
    config.readback_choice_prefix = ">> "   # this is prefixed to the choices the user makes in readback

    # ends adding new config variables
    config.locked = True

init -2 python:

    # Two custom characters that store what they said
    class ReadbackADVCharacter(ADVCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            store.current_voice = ''
            return

    class ReadbackNVLCharacter(NVLCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            store.current_voice = ''
            return

    # this enables us to show the current line in readback without having to bother the buffer with raw shows
    def say_wrapper(who, what, **kwargs):
        store_current_line(who, what)
        return renpy.show_display_say(who, what, **kwargs)

    config.nvl_show_display_say = say_wrapper

    adv = ReadbackADVCharacter(show_function=say_wrapper)
    nvl = ReadbackNVLCharacter()
    NVLCharacter = ReadbackNVLCharacter

    # rewriting voice function to replay voice files when you clicked dialogues in text history screen
    def voice(file, **kwargs):
        if not config.has_voice:
            return

        _voice.play = file

        store.current_voice = file

    # overwriting standard menu handler
    # Overwriting menu functions makes Text History log choice which users choose.
    def menu(items, **add_input):

        newitems = []
        for label, val in items:
            if val == None:
                narrator(label, interact=False)
            else:
                newitems.append((label, val))

        rv = renpy.display_menu(newitems, **add_input)

        # logging menu choice label.
        for label, val in items:
            if rv == val:
                store.current_voice = ''
                store_say(None, config.readback_choice_prefix + label)
        return rv

    def nvl_screen_dialogue():
        """
         Returns widget_properties and dialogue for the current NVL
         mode screen.
         """

        widget_properties = { }
        dialogue = [ ]

        for i, entry in enumerate(nvl_list):
            if not entry:
                continue

            who, what, kwargs = entry

            if i == len(nvl_list) - 1:
                who_id = "who"
                what_id = "what"
                window_id = "window"

            else:
                who_id = "who%d" % i
                what_id = "what%d" % i
                window_id = "window%d" % i

            widget_properties[who_id] = kwargs["who_args"]
            widget_properties[what_id] = kwargs["what_args"]
            widget_properties[window_id] = kwargs["window_args"]

            dialogue.append((who, what, who_id, what_id, window_id))

        return widget_properties, dialogue

    # Overwriting nvl menu function
    def nvl_menu(items):

        renpy.mode('nvl_menu')

        if nvl_list is None:
            store.nvl_list = [ ]

        screen = None

        if renpy.has_screen("nvl_choice"):
            screen = "nvl_choice"
        elif renpy.has_screen("nvl"):
            screen = "nvl"

        if screen is not None:

            widget_properties, dialogue = nvl_screen_dialogue()

            rv = renpy.display_menu(
                items,
                widget_properties=widget_properties,
                screen=screen,
                scope={ "dialogue" : dialogue },
                window_style=style.nvl_menu_window,
                choice_style=style.nvl_menu_choice,
                choice_chosen_style=style.nvl_menu_choice_chosen,
                choice_button_style=style.nvl_menu_choice_button,
                choice_chosen_button_style=style.nvl_menu_choice_chosen_button,
                type="nvl",
                )

            for label, val in items:
                if rv == val:
                    store.current_voice = ''
                    store_say(None, config.readback_choice_prefix + label)
            return rv

        # Traditional version.
        ui.layer("transient")
        ui.clear()
        ui.close()

        ui.window(style=__s(style.nvl_window))
        ui.vbox(style=__s(style.nvl_vbox))

        for i in nvl_list:
            if not i:
                continue

            who, what, kw = i
            rv = renpy.show_display_say(who, what, **kw)

        renpy.display_menu(items, interact=False,
                           window_style=__s(style.nvl_menu_window),
                           choice_style=__s(style.nvl_menu_choice),
                           choice_chosen_style=__s(style.nvl_menu_choice_chosen),
                           choice_button_style=__s(style.nvl_menu_choice_button),
                           choice_chosen_button_style=__s(style.nvl_menu_choice_chosen_button),
                           )

        ui.close()

        roll_forward = renpy.roll_forward_info()

        rv = ui.interact(roll_forward=roll_forward)
        renpy.checkpoint(rv)

        for label, val in items:
            if rv == val:
                store.current_voice = ''
                store_say(None, config.readback_choice_prefix + label)
        return rv

    ## readback
    readback_buffer = []
    current_line = None
    current_voice = None

    def store_say(who, what):
        global readback_buffer, current_voice
        if preparse_say_for_store(what):
            new_line = (preparse_say_for_store(who), preparse_say_for_store(what), current_voice)
            readback_buffer = readback_buffer + [new_line]
            readback_prune()

    def store_current_line(who, what):
        global current_line, current_voice
        current_line = (preparse_say_for_store(who), preparse_say_for_store(what), current_voice)

    # remove text tags from dialogue lines
    disallowed_tags_regexp = ""
    for tag in config.readback_disallowed_tags:
        if disallowed_tags_regexp != "":
            disallowed_tags_regexp += "|"
        disallowed_tags_regexp += "{"+tag+"=.*?}|{"+tag+"}|{/"+tag+"}"

    import re
    remove_tags_expr = re.compile(disallowed_tags_regexp) # remove tags undesirable in readback
    def preparse_say_for_store(input):
        global remove_tags_expr
        if input:
            return re.sub(remove_tags_expr, "", input)

    def readback_prune():
        global readback_buffer
        while len(readback_buffer) > config.readback_buffer_length:
            del readback_buffer[0]

    # keymap overriding to show text_history.
    def readback_catcher():
        ui.add(renpy.Keymap(rollback=(SetVariable("yvalue", 1.0), ShowMenu("text_history"))))
        ui.add(renpy.Keymap(rollforward=ui.returns(None)))

    if config.readback_full:
        config.rollback_enabled = False
        config.overlay_functions.append(readback_catcher)

init python:
    yvalue = 1.0
    class NewAdj(renpy.display.behavior.Adjustment):
        def change(self,value):

            if value > self._range and self._value == self._range:
                return Return()
            else:
                return renpy.display.behavior.Adjustment.change(self, value)

    def store_yvalue(y):
        global yvalue
        yvalue = int(y)

screen text_history:

    #use navigation
    tag menu

    if not current_line and len(readback_buffer) == 0:
        $ lines_to_show = []

    elif current_line and len(readback_buffer) == 0:
        $ lines_to_show = [current_line]

    elif current_line and not ( ( len(readback_buffer) == 3 and current_line == readback_buffer[-2]) or current_line == readback_buffer[-1]):
        $ lines_to_show = readback_buffer + [current_line]

    else:
        $ lines_to_show = readback_buffer


    $ adj = NewAdj(changed = store_yvalue, step = 300)

    window:
        style_group "readback"

        side "c r":

            frame:

                has viewport:
                    mousewheel True
                    draggable True
                    yinitial yvalue
                    yadjustment adj

                vbox:
                    null height 10

                    for line in lines_to_show:

                        if line[0] and line[0] != " ":
                            label line[0] # name

                        # if there's no voice just log a dialogue
                        if not line[2]:
                            text line[1]

                        # else, dialogue will be saved as a button of which plays voice when clicked
                        else:
                            textbutton line[1] action Play("voice", line[2] )

                        null height 10

            bar adjustment adj style 'vscrollbar'
        textbutton _("Return") text_size 20 activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" align (.97, 1.0) action Return() at buttonfade


# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"
            background Transform(Frame("GUI/textbox.png",0,0), alpha=persistent.window_opacity)

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu

init -4:

    if persistent.window_opacity == None:
        $persistent.window_opacity = 0.8


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    #add "GUI/yesno.png"
    window:
        style "menu_window"
        xalign 0.5
        yalign 0.4

        vbox:
            style "menu"
            spacing 15

            for caption, action, chosen in items:

                if action:

                    button:
                        action action at barfade
                        style "menu_choice_button"

                        text caption style "menu_choice" xalign 0.5

                else:
                    text caption style "menu_caption" xalign 0.5


init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear
        idle_color "#c3c1b7"
        insensitive_color "#c3c1b7"
        hover_color "#fefbee"
        size 25
        font "GUI/Fonts/NotoSansCJKjp-Light.otf"

    style menu_choice_button is button:
        background "GUI/choice.png"
        hover_background "GUI/choice_hover.png"
        top_padding 25
        bottom_padding 50
        xpadding 100
        xmaximum 654
        xminimum 654
        yminimum 94
        xalign 0.5


image ctc_glow:
    "GUI/ctc_glow.png"
    subpixel True
    block:
        alpha 0.2
        linear 1.5 alpha 1.5
        linear 1.5 alpha 0.2
        repeat

image ctc_stone:
    "GUI/ctc.png"
    subpixel True
    block:
        alpha 0.8
        linear 1.5 alpha 1.2
        linear 1.5 alpha 0.8
        repeat

image ctc:
    xpos 1040
    ypos 650
    LiveComposite(
    (34, 34),
    (0, 0), "ctc_glow",
    (0, 0), "ctc_stone")

image clouds:
    contains:
        "GUI/clouds_.png"
        subpixel True
        block:
            xpos -2277
            linear 60 xpos -4554
            repeat

    contains:
        "GUI/clouds_.png"
        subpixel True
        block:
            xpos 0
            linear 60 xpos -2277
            repeat

    contains:
        "GUI/clouds_.png"
        subpixel True
        block:
            xpos 2277
            linear 60 xpos 0
            repeat

image splash = "GUI/SoftColors_black.png"
image black = Solid("#000000")

label splashscreen:
    scene black
    with Pause(0.3)

#    show splash with dissolve
#    with Pause(1)

    $ renpy.show("splash")
    $ renpy.transition(Dissolve(1.))
    $ renpy.pause(2., hard=True)

    scene black with dissolve
    with Pause(0.3)
    return



##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"
        background Transform(Frame("GUI/base.png",0,0), alpha=persistent.window_opacity)

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    on "show" action Stop("sound")

    # This ensures that any other menu screen is replaced.
    tag menu
    add "clouds"
    add "GUI/main_menu.png"
    add "GUI/logo.png"
#    window:
#        background Transform(Frame("GUI/mm.png",0,0), alpha=persistent.window_opacity)
    # The background of the main menu.

### To remove the "Demo Version" line just comment / delete the next block
    hbox:
        xpos 820
        ypos 245

        label _("Demo Version")

##############

        # The main menu buttons.
    hbox:
        style_group "mm"
        xalign 0.51
        yalign 0.92
        spacing 25
        textbutton _("LOAD") text_size 20 text_outlines [ (absolute(1), "#4682B4", absolute(-1), absolute(1)) ] activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("load") at slide
        textbutton _("SETTINGS") text_size 20 text_outlines [ (absolute(1), "#4682B4", absolute(-1), absolute(1)) ] activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3"  action ShowMenu("preferences") at slide
        textbutton _("START") text_size 20 text_outlines [ (absolute(1), "#4682B4", absolute(-1), absolute(1)) ] activate_sound "sound/AQD_CONFIRM.mp3" hover_sound "sound/AQD_HOVER.mp3" background "GUI/start.png" action Start() at slide
        textbutton _("GALLERY") text_size 20 text_outlines [ (absolute(1), "#4682B4", absolute(-1), absolute(1)) ] activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3"  action ShowMenu("gallery") at slide
        textbutton _("QUIT") text_size 20 text_outlines [ (absolute(1), "#4682B4", absolute(-1), absolute(1)) ] activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action Quit(confirm=False) at slide


    if persistent.anya_cleared:
        if persistent.diana_cleared:
            if persistent.cameron_cleared:
                if persistent.elisabeth_cleared:
                    hbox:
                        style_group "mm"
                        xalign 0.511
                        yalign 0.97
                        spacing 25
                        textbutton _("MEMORIES") text_size 20 activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action at slide

init -100:

    # Make all the main menu buttons be the same size.


    style mm_button:

        background None

    style mm_button_text:
        font "GUI/Fonts/NotoSansCJKjp-DemiLight.otf"
        hover_color "ffffff"
        insensitive_color "#565656"
        selected_color "ffffff"


    if persistent.anya_cleared == None:
        $persistent.anya_cleared = False

    if persistent.diana_cleared == None:
        $persistent.diana_cleared = False

    if persistent.cameron_cleared == None:
        $persistent.cameron_cleared = False

    if persistent.elisabeth_cleared == None:
        $persistent.elisabeth_cleared = False

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen load_save_slot:
    #tag menu
    #modal True
    $ file_text = "%2s. %s\n  %s" % (
                        FileSlotName(number, 4),
                        FileTime(number, empty=_("Empty Slot")),
                        FileSaveName(number))

    add FileScreenshot(number) xpos 0 ypos 0
    text file_text xalign .0 yalign 1.9 size 20 font "GUI/Fonts/goodvibes.otf" color "#474646"

screen save:

    # This ensures that any other menu screen is replaced.
    tag menu
    window:
        at slidemenu
        background Transform(Frame("GUI/base.png",0,0), alpha=persistent.window_opacity)

        add "GUI/book.png"

        vbox:
            xpos 765
            ypos 15
            imagebutton idle "return_idle" hover "return_hover" activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action [Hide("save"), Return()]  at returnfade


        imagemap:
            alpha False
            ground "GUI/slots.png"
            idle "GUI/idle.png"
            hover "GUI/slots_hover.png"
            insensitive "GUI/idle.png"

            hotspot (600, 62, 282, 95) at slotfade clicked FileAction(1):
                use load_save_slot(number=1)
            hotspot (600, 206, 162, 95) at slotfade clicked FileAction(2):
                use load_save_slot(number=2)
            hotspot (600, 350, 162, 95) at slotfade clicked FileAction(3):
                use load_save_slot(number=3)
            hotspot (600, 494, 162, 95) at slotfade clicked FileAction(4):
                use load_save_slot(number=4)

        add "GUI/slot_frames.png"

        vbox:
            xpos 746
            ypos 69
            imagebutton idle "GUI/delete.png" insensitive "GUI/delete_s.png" action FileDelete(1) at buttonfade

        vbox:
            xpos 746
            ypos 213
            imagebutton idle "GUI/delete.png" insensitive "GUI/delete_s.png" action FileDelete(2) at buttonfade

        vbox:
            xpos 746
            ypos 357
            imagebutton idle "GUI/delete.png" insensitive "GUI/delete_s.png" action FileDelete(3) at buttonfade

        vbox:
            xpos 746
            ypos 501
            imagebutton idle "GUI/delete.png" insensitive "GUI/delete_s.png" action FileDelete(4) at buttonfade


        hbox:
            xpos 175
            ypos 67
            style_group "stitle"

            label _("Save")

        vbox:
            xpos 115
            ypos 470
            style_group "navigation"

            textbutton _("     Load") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("load") at slotfade
            textbutton _("     Settings") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("preferences") at slotfade
            textbutton _("     Main Menu") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action MainMenu() at slotfade
            textbutton _("     Quit") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action Quit() at slotfade

        hbox:
            xpos 160
            ypos 127
            style_group "page"
            textbutton _("Auto") action FilePage("auto") at slotfade
            textbutton _("1") action FilePage("1") at slotfade
            textbutton _("2") action FilePage("2") at slotfade
            textbutton _("3") action FilePage("3") at slotfade
            textbutton _("4") action FilePage("4") at slotfade
            textbutton _("5") action FilePage("5") at slotfade
            textbutton _("6") action FilePage("6") at slotfade
            textbutton _("7") action FilePage("7") at slotfade
            textbutton _("8") action FilePage("8") at slotfade
            textbutton _("9") action FilePage("9") at slotfade
            textbutton _("10") action FilePage("10") at slotfade


screen load():

    # This ensures that any other menu screen is replaced.
    tag menu
    if main_menu:
        add "GUI/clouds.png"
    window:
        at slidemenu
        background Transform(Frame("GUI/base.png",0,0), alpha=persistent.window_opacity)

        add "GUI/book.png"

#        imagemap:
#            alpha False
#            ground "GUI/slots.png"
#            idle "GUI/idle.png"
#            hover "GUI/slots_hover.png"
#            insensitive "GUI/idle.png"

#            hotspot (600, 62, 162, 95) activate_sound "sound/AQD_CONFIRM.mp3" at slotfade clicked FileAction(1):
#                use load_save_slot(number=1)
#            hotspot (600, 206, 162, 95) activate_sound "sound/AQD_CONFIRM.mp3" at slotfade clicked FileAction(2):
#                use load_save_slot(number=2)
#            hotspot (600, 350, 162, 95) activate_sound "sound/AQD_CONFIRM.mp3" at slotfade clicked FileAction(3):
#                use load_save_slot(number=3)
#            hotspot (600, 494, 162, 95) activate_sound "sound/AQD_CONFIRM.mp3" at slotfade clicked FileAction(4):
#                use load_save_slot(number=4)


        imagemap:
            alpha False
            ground "GUI/slots.png"
            idle "GUI/idle.png"
            hover "GUI/slots_hover.png"
            insensitive "GUI/idle.png"

            hotspot (600, 62, 162, 95) at slotfade clicked FileAction(1):
                use load_save_slot(number=1)
            hotspot (600, 206, 162, 95) at slotfade clicked FileAction(2):
                use load_save_slot(number=2)
            hotspot (600, 350, 162, 95) at slotfade clicked FileAction(3):
                use load_save_slot(number=3)
            hotspot (600, 494, 162, 95) at slotfade clicked FileAction(4):
                use load_save_slot(number=4)


        add "GUI/slot_frames.png"

        vbox:
            xpos 746
            ypos 69
            imagebutton idle "GUI/delete.png" insensitive "GUI/delete_s.png" action FileDelete(1) at buttonfade

        vbox:
            xpos 746
            ypos 213
            imagebutton idle "GUI/delete.png" insensitive "GUI/delete_s.png" action FileDelete(2) at buttonfade

        vbox:
            xpos 746
            ypos 357
            imagebutton idle "GUI/delete.png" insensitive "GUI/delete_s.png" action FileDelete(3) at buttonfade

        vbox:
            xpos 746
            ypos 501
            imagebutton idle "GUI/delete.png" insensitive "GUI/delete_s.png" action FileDelete(4) at buttonfade
        hbox:
            xpos 175
            ypos 67
            style_group "stitle"

            label _("Load")

        vbox:
            xpos 115
            ypos 470
            style_group "navigation"

            textbutton _("     Save") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("save") at slotfade
            textbutton _("     Settings") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("preferences") at slotfade
            if main_menu:
                textbutton _("     Main Menu") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action Return() at slotfade
            else:
                textbutton _("     Main Menu") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action MainMenu() at slotfade
            textbutton _("     Quit") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action Quit() at slotfade

        vbox:
            xpos 765
            ypos 15
            imagebutton idle "return_idle" hover "return_hover" activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action [Hide("load"), Return()]  at returnfade

        hbox:
            xpos 160
            ypos 127
            style_group "page"
            textbutton _("Auto") action FilePage("auto") at slotfade
            textbutton _("1") action FilePage("1") at slotfade
            textbutton _("2") action FilePage("2") at slotfade
            textbutton _("3") action FilePage("3") at slotfade
            textbutton _("4") action FilePage("4") at slotfade
            textbutton _("5") action FilePage("5") at slotfade
            textbutton _("6") action FilePage("6") at slotfade
            textbutton _("7") action FilePage("7") at slotfade
            textbutton _("8") action FilePage("8") at slotfade
            textbutton _("9") action FilePage("9") at slotfade
            textbutton _("10") action FilePage("10") at slotfade

init -2 python:
    config.thumbnail_width = 162
    config.thumbnail_height = 95
    config.quit_action = Quit(confirm=False)

init -2:
    style stitle_label_text:
        size 43
        font "GUI/Fonts/goodvibes.otf"
        color "#333333"

    style page_button:
        ypadding 3
        background None
        xpadding 2

    style page_button_text:
        size 22
        font "GUI/Fonts/goodvibes.otf"
        idle_color "#474646"
        hover_color "#000000"
        selected_hover_color "#000000"
        selected_idle_color "#000000"

    style navigation_button:
        ypadding 4
        idle_background "GUI/button.png"
        hover_background "GUI/button_hover.png"
        insensitive_background "GUI/button.png"


    style navigation_button_text:
        size 31
        font "GUI/Fonts/goodvibes.otf"
        idle_color "#333333"
        insensitive_color "#333333"
        hover_color "#000000"



##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():
    tag menu
    if main_menu:
        add "GUI/clouds.png"
    window:
        at slidemenu
        background Transform(Frame("GUI/base.png",0,0), alpha=persistent.window_opacity)
        add "GUI/book.png"

        hbox:
            xpos 230
            ypos 127
            style_group "page"
            textbutton _(" 1 ") action ShowMenu("preferences") at slotfade
            textbutton _(" 2 ") action ShowMenu("preferences_text") at slotfade

        vbox:
            xpos 115
            ypos 433
            style_group "navigation"

            textbutton _("     Encyclopedia") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("encyclopedia") at slotfade
            textbutton _("     Save") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("save") at slotfade
            textbutton _("     Load") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("load") at slotfade
            if main_menu:
                textbutton _("     Main Menu") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action Return() at slotfade
            else:
                textbutton _("     Main Menu") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action MainMenu() at slotfade
            textbutton _("     Quit") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action Quit() at slotfade

        vbox:
            xpos 765
            ypos 15
            imagebutton idle "return_idle" hover "return_hover" activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action [Hide("preferences"), Return()]  at returnfade

        hbox:
            xpos 175
            ypos 67
            style_group "stitle"

            label _("Settings")

        hbox:
            xpos 490
            ypos 70
            style_group "preftitle"
            label _("Display")

        vbox:
            xpos 570
            ypos 100

            style_group "prefbutton"
            textbutton _("    Window") action Preference("display", "window") at buttonfade
            textbutton _("    Fullscreen") action Preference("display", "fullscreen") at buttonfade

        hbox:
            xpos 490
            ypos 180
            style_group "preftitle"
            label _("Transitions")

        vbox:
            style_group "prefbutton"
            xpos 570
            ypos 210
            textbutton _("    All") action Preference("transitions", "all") at buttonfade
            textbutton _("    None") action Preference("transitions", "none") at buttonfade

        hbox:
            xpos 490
            ypos 310
            style_group "preftitle"
            label _("Music volume") text_size 24

        vbox:
            xpos 500
            ypos 350
            style_group "pref"
            bar value Preference("music volume") at barfade


        hbox:
            xpos 490
            ypos 410
            style_group "preftitle"
            label _("Sound Effect volume") text_size 24

        vbox:
            xpos 500
            ypos 450
            style_group "pref"
            bar value Preference("sound volume") at barfade


        hbox:
            xpos 490
            ypos 510
            style_group "preftitle"
            label _("Voice volume") text_size 24

        vbox:
            xpos 500
            ypos 550
            style_group "pref"
            bar value Preference("voice volume") at barfade



screen preferences_text():

    tag menu
    if main_menu:
        add "GUI/clouds.png"
    window:
        at slidemenu
        background Transform(Frame("GUI/base.png",0,0), alpha=persistent.window_opacity)
        add "GUI/book.png"

        hbox:
            xpos 230
            ypos 127
            style_group "page"
            textbutton _(" 1 ") action ShowMenu("preferences") at slotfade
            textbutton _(" 2 ") action ShowMenu("preferences_text") at slotfade

        vbox:
            xpos 115
            ypos 433
            style_group "navigation"

            textbutton _("     Encyclopedia") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("encyclopedia") at slotfade

            textbutton _("     Save") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("save") at slotfade
            textbutton _("     Load") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("load") at slotfade
            if main_menu:
                textbutton _("     Main Menu") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action Return() at slotfade
            else:
                textbutton _("     Main Menu") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action MainMenu() at slotfade
            textbutton _("     Quit") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action Quit() at slotfade

        vbox:
            xpos 765
            ypos 15
            imagebutton idle "return_idle" hover "return_hover" activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action [Hide("preferences_text"), Return()]   at returnfade

        hbox:
            xpos 175
            ypos 67
            style_group "stitle"

            label _("Settings")

        hbox:
            xpos 490
            ypos 70
            style_group "preftitle"
            label _("Skip")

        vbox:
            xpos 540
            ypos 100
            style_group "prefbutton"
            textbutton _("   Seen messages") action Preference("skip", "seen") at buttonfade
            textbutton _("   All messages") action Preference("skip", "all") at buttonfade

        hbox:
            xpos 490
            ypos 180
            style_group "preftitle"
            label _("After choices")

        vbox:
            style_group "prefbutton"
            xpos 540
            ypos 210
            textbutton _("   Stop skipping") action Preference("after choices", "stop") at buttonfade
            textbutton _("   Keep skipping") action Preference("after choices", "skip") at buttonfade

        hbox:
            xpos 490
            ypos 310
            style_group "preftitle"
            label _("Textbox opacity") text_size 24

        vbox:
            xpos 500
            ypos 350
            style_group "pref"
            bar value FieldValue(persistent, "window_opacity", range=1.0, style="slider") at barfade


        hbox:
            xpos 490
            ypos 410
            style_group "preftitle"
            label _("Text speed") text_size 24

        vbox:
            xpos 500
            ypos 450
            style_group "pref"
            bar value Preference("text speed") at barfade


        hbox:
            xpos 490
            ypos 510
            style_group "preftitle"
            label _("Auto-forward time") text_size 24

        vbox:
            xpos 500
            ypos 550
            style_group "pref"
            bar value Preference("auto-forward time") at barfade




init -2:
    style pref_frame:
        xfill False
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True



    style prefbutton_button:
        xalign 0.0
        selected_background "GUI/pref_hover.png"
        selected_hover_background "GUI/pref_hover.png"
        idle_background "GUI/pref.png"
        hover_background "GUI/pref.png"
        insensitive_background "GUI/pref.png"


    style prefbutton_button_text:
        idle_color "#333333"
        insensitive_color "#565656"
        hover_color "#000000"
        text_align 0.0
        font "GUI/Fonts/NotoSansCJKjp-Light.otf"

    style soundtest_button:
        xalign 1.0

    style pref_slider:
        left_bar "GUI/bar.png"
        right_bar "GUI/bar.png"
        ymaximum 32
        xmaximum 250
        thumb "GUI/slider.png"
        left_gutter 10
        right_gutter 15

    style preftitle_label_text:
        size 31
        font "GUI/Fonts/goodvibes.otf"
        color "#333333"


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):
    modal True
    add "GUI/yesno.png" xpos 40

    vbox:
        style_group "yesno"
        xalign .5
        yalign .3
        spacing 30

        label _(message):
            xalign 0.5
            left_padding 450
            right_padding 400


    hbox:
        xalign 0.52
        yalign 0.45
        spacing 10
        style_group "yesno"

        textbutton _("  Yes") action yes_action
        textbutton _("  No") action no_action
    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"
        hover_background "GUI/pref_hover_.png"
        idle_background "GUI/pref.png"


    style yesno_label_text:
        text_align 0.5
        color "#000000"
        size 20

    style yesno_button_text:
        idle_color "#333333"
        insensitive_color "#565656"
        hover_color "#000000"
        font "GUI/Fonts/goodvibes.otf"
        size 31

##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():
    showif quick_menu:
        hbox:
            style_group "mm"

            xalign 0.5
            yalign 1.0
            textbutton _("MENU") text_size 18 background "GUI/menu.png" action SetVariable("quick_menu", False)

        hbox:
            at slide
            style_group "mm"

            xalign 0.33
            yalign 1.0
            textbutton _("BACK") text_size 15 action ShowMenu("text_history")
            textbutton _("AUTO") text_size 15 action Preference("auto-forward", "toggle")
            textbutton _("SKIP") text_size 15 action Skip()
            textbutton _("HIDE") text_size 15 action HideInterface()

        hbox:
            at slide
            style_group "mm"

            xalign 0.7
            yalign 1.0
            textbutton _("SAVE") text_size 15 action ShowMenu('save')
            textbutton _("LOAD") text_size 15 action ShowMenu('load')
            textbutton _("SETTINGS") text_size 15 action ShowMenu('preferences')
            textbutton _("QUIT") text_size 15 action Quit()


    else:
        hbox:
            yalign 1.0
            xalign 0.5
            style_group "mm"
            textbutton _("MENU") text_size 18 background "GUI/menu.png" action SetVariable("quick_menu", True)






init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

init -2 python:
    quick_menu=False
