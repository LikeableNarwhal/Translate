#### Here the Cgs are defined.

#init:
#    image cg_1 = "cg_levios.png"
#    image cg_1 var = "cg_levios.png"

init:
    image cg_1 = "CG/cg_levios.png"
#    image cg_1 var = "cg_levios.png"
#    image cg_1 var2 = "cg_levios.png"
    image cg_2 = "CG/cg_anya_mermaid.png"
    image cg_3 = "CG/picnic_cg_1.png"
    image cg_4 = "CG/cg_violetta.png"
    image cg_5 = "CG/cg_acqua_alta.png"
    image cg_6 = "CG/cg_photo_normal.png"
    image cg_6 var = "CG/cg_photo_silly.png"
    image cg_7 = "CG/cg_transform1.png"
    image cg_7 var = "CG/cg_transform2.png"
    image cg_7 var2 = "CG/cg_transform3.png"
    image cg_8 = "bg.png"
    image cg_9 = "CG/cg_mute.png"
    image cg_10 = "CG/cg_anya_room.png"
    image cg_11 = "CG/cg_underwater.png"
    image cg_12 = "CG/cg_urus.png"
    image cg_13 = "bg.png"
    image cg_14 = "CG/cg_mermaid_kiss1.png"
    image cg_14 var = "CG/cg_mermaid_kiss2.png"
    image cg_15 = "CG/cg_diana_alley1.png"
    image cg_15 var = "CG/cg_diana_alley1.png"
    image cg_16 = "CG/cg_diana_gondolier2.png"
    image cg_16 var = "CG/cg_diana_gondolier3.png"
    image cg_16 var2 = "CG/cg_diana_gondolier1.png"
    image cg_17 = "bg.png"
    image cg_18 = "bg.png"
    image cg_19 = "bg.png"
    image cg_20 = "bg.png"
    image cg_21 = "bg.png"
    image cg_22 = "bg.png"
    image cg_23 = "bg.png"
    image cg_24 = "bg.png"
    image cg_25 = "bg.png"
    image cg_26 = "bg.png"
    image cg_27 = "bg.png"
    image cg_28 = "bg.png"
    image cg_29 = "bg.png"
    image cg_30 = "bg.png"
    image cg_31 = "bg.png"
    image cg_32 = "bg.png"
    image cg_33 = "bg.png"
    image cg_34 = "bg.png"
    image cg_35 = "bg.png"
    image cg_36 = "bg.png"
    image cg_37 = "bg.png"
    image cg_38 = "bg.png"
    image cg_39 = "bg.png"
    image cg_40 = "bg.png"
    image cg_41 = "bg.png"
    image cg_42 = "bg.png"
    image cg_43 = "bg.png"
    image cg_44 = "bg.png"
    image cg_45 = "bg.png"
    image cg_46 = "bg.png"
    image cg_47 = "bg.png"
    image cg_48 = "bg.png"

########## These are movie preview images
image movie_1:
    LiveComposite(
    (175, 109),
    (3, 3), im.Scale("Movies/movie_1.png", thumbnail_x, thumbnail_y),
    (0, 0), "GUI/frame_hover.png")

image movie_2:
    LiveComposite(
    (175, 109),
    (3, 3), im.Scale("Movies/movie_2.png", thumbnail_x, thumbnail_y),
    (0, 0), "GUI/frame_hover.png")

image movie_3:
    LiveComposite(
    (175, 109),
    (3, 3), im.Scale("Movies/movie_3.png", thumbnail_x, thumbnail_y),
    (0, 0), "GUI/frame_hover.png")

image movie_4:
    LiveComposite(
    (175, 109),
    (3, 3), im.Scale("Movies/movie_4.png", thumbnail_x, thumbnail_y),
    (0, 0), "GUI/frame_hover.png")

image movie_5:
    LiveComposite(
    (175, 109),
    (3, 3), im.Scale("Movies/movie_5.png", thumbnail_x, thumbnail_y),
    (0, 0), "GUI/frame_hover.png")

image movie_6:
    LiveComposite(
    (175, 109),
    (3, 3), im.Scale("Movies/movie_6.png", thumbnail_x, thumbnail_y),
    (0, 0), "GUI/frame_hover.png")


screen gallery():

    # This ensures that any other menu screen is replaced.
    tag menu
    add "GUI/clouds.png"
    window:
        at slidemenu
        background Transform(Frame("GUI/base.png",0,0), alpha=persistent.window_opacity)

        add "GUI/book.png"

        hbox:
            xpos 190
            ypos 127
            style_group "page"
            if cg_page == 0:
                textbutton _("1") action [SetVariable('cg_page', 0), ShowMenu("gallery")] at slotfade
            else:
                textbutton _("1") text_selected_idle_color "#474646" text_selected_hover_color "#000000" action [SetVariable('cg_page', 0), ShowMenu("gallery")] at slotfade

            if cg_page == 1:
                textbutton _("2") action [SetVariable('cg_page', 1), ShowMenu("gallery")] at slotfade
            else:
                textbutton _("2") text_selected_idle_color "#474646" text_selected_hover_color "#000000" action [SetVariable('cg_page', 1), ShowMenu("gallery")] at slotfade

            if cg_page == 2:
                textbutton _("3") action [SetVariable('cg_page', 2), ShowMenu("gallery")] at slotfade
            else:
                textbutton _("3") text_selected_idle_color "#474646" text_selected_hover_color "#000000" action [SetVariable('cg_page', 2), ShowMenu("gallery")] at slotfade

            if cg_page == 3:
                textbutton _("4") action [SetVariable('cg_page', 3), ShowMenu("gallery")] at slotfade
            else:
                textbutton _("4") text_selected_idle_color "#474646" text_selected_hover_color "#000000" action [SetVariable('cg_page', 3), ShowMenu("gallery")] at slotfade

            if cg_page == 4:
                textbutton _("5") action [SetVariable('cg_page', 4), ShowMenu("gallery")] at slotfade
            else:
                textbutton _("5") text_selected_idle_color "#474646" text_selected_hover_color "#000000" action [SetVariable('cg_page', 4), ShowMenu("gallery")] at slotfade

            if cg_page == 5:
                textbutton _("6") action [SetVariable('cg_page', 5), ShowMenu("gallery")] at slotfade
            else:
                textbutton _("6") text_selected_idle_color "#474646" text_selected_hover_color "#000000" action [SetVariable('cg_page', 5), ShowMenu("gallery")] at slotfade

            if cg_page == 6:
                textbutton _("7") action [SetVariable('cg_page', 6), ShowMenu("gallery")] at slotfade
            else:
                textbutton _("7") text_selected_idle_color "#474646" text_selected_hover_color "#000000" action [SetVariable('cg_page', 6), ShowMenu("gallery")] at slotfade

            if cg_page == 7:
                textbutton _("8") action [SetVariable('cg_page', 7), ShowMenu("gallery")] at slotfade
            else:
                textbutton _("8") text_selected_idle_color "#474646" text_selected_hover_color "#000000" action [SetVariable('cg_page', 7), ShowMenu("gallery")] at slotfade

            if cg_page == 8:
                textbutton _("9") action [SetVariable('cg_page', 8), ShowMenu("gallery")] at slotfade
            else:
                textbutton _("9") text_selected_idle_color "#474646" text_selected_hover_color "#000000" action [SetVariable('cg_page', 8), ShowMenu("gallery")] at slotfade

            if cg_page == 9:
                textbutton _("10") action [SetVariable('cg_page', 9), ShowMenu("gallery")] at slotfade
            else:
                textbutton _("10") text_selected_idle_color "#474646" text_selected_hover_color "#000000" action [SetVariable('cg_page', 9), ShowMenu("gallery")] at slotfade

            if cg_page == 10:
                textbutton _("11") action [SetVariable('cg_page', 10), ShowMenu("gallery")] at slotfade
            else:
                textbutton _("11") text_selected_idle_color "#474646" text_selected_hover_color "#000000" action [SetVariable('cg_page', 10), ShowMenu("gallery")] at slotfade

            if cg_page == 11:
                textbutton _("12") action [SetVariable('cg_page', 11), ShowMenu("gallery")] at slotfade
            else:
                textbutton _("12") text_selected_idle_color "#474646" text_selected_hover_color "#000000" action [SetVariable('cg_page', 11), ShowMenu("gallery")] at slotfade

        frame background None:
            grid 1 4:
                ypos 50
                xpos 588

                $ i = 0

                for gal_item in gallery_cg_items:
                    $ i += 1
                    if i <= (cg_page+1)*gal_cells and i>cg_page*gal_cells:
                        add g_cg.make_button(gal_item + " butt", gal_item + " butt", "GUI/locked.png", background=None, xpadding=0, top_padding=0, xmargin = 0, top_margin=0, bottom_margin=34)
                for j in range(i, (cg_page+1)*4):
                    null



        hbox:
            xpos 175
            ypos 67
            style_group "stitle"

            label _("Gallery")

        vbox:
            xpos 115
            ypos 470
            style_group "navigation"

            textbutton _("     Movies") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("movies_1") at slotfade
            textbutton _("     CG Gallery") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("gallery") at slotfade
            textbutton _("     Music Room") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("music_1") at slotfade
            if main_menu:
                textbutton _("     Main Menu") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action Return() at slotfade
            else:
                textbutton _("     Main Menu") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action MainMenu() at slotfade


        vbox:
            xpos 765
            ypos 15
            imagebutton idle "return_idle" hover "return_hover" activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action Return() at returnfade


init python:
#    #This is where the gallery is defined. If you want to change the CG names you must also change them in the list below

    gallery_cg_items = ["cg_1", "cg_2", "cg_3", "cg_4", "cg_5", "cg_6", "cg_7", "cg_8", "cg_9", "cg_10", "cg_11", "cg_12", "cg_13", "cg_14", "cg_15", "cg_16", "cg_17", "cg_18", "cg_19", "cg_20",
        "cg_21", "cg_22", "cg_23", "cg_24", "cg_25", "cg_26", "cg_27", "cg_28", "cg_29", "cg_30", "cg_31", "cg_32", "cg_33", "cg_34", "cg_35", "cg_36", "cg_37", "cg_38", "cg_39", "cg_40", "cg_41", "cg_42", "cg_43", "cg_44", "cg_45", "cg_46", "cg_47", "cg_48"]

    thumbnail_x = 162
    thumbnail_y = 95
    gal_cells = 4

    g_cg = Gallery()
    for gal_item in gallery_cg_items:
        g_cg.button(gal_item + " butt")
        g_cg.image(gal_item)
        g_cg.unlock(gal_item)
        if gal_item == "cg_6":
            g_cg.image("cg_6 var")
            g_cg.unlock("cg_6 var")
        if gal_item == "cg_7":
            g_cg.image("cg_7 var")
            g_cg.unlock("cg_7 var")
            g_cg.image("cg_7 var2")
            g_cg.unlock("cg_7 var2")
        if gal_item == "cg_14":
            g_cg.image("cg_14 var")
            g_cg.unlock("cg_14 var")
        if gal_item == "cg_15":
            g_cg.image("cg_15 var")
            g_cg.unlock("cg_15 var")
        if gal_item == "cg_16":
            g_cg.image("cg_16 var")
            g_cg.unlock("cg_16 var")
            g_cg.image("cg_16 var2")
            g_cg.unlock("cg_16 var2")
    g_cg.transition = fade
    cg_page=0
    g_cg.hover_border = "GUI/frame_hover.png"
    g_cg.idle_border = "GUI/frame.png"



init +1 python:

    for gal_item in gallery_cg_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))

image border:
    "GUI/frame.png"


########### These are the variables that show whether the movies were seen or not (i.e "unlocked" in the gallery)
init:

    if persistent.movie_1_seen == None:
        $persistent.movie_1_seen = False

    if persistent.movie_2_seen == None:
        $persistent.movie_2_seen = False

    if persistent.movie_3_seen == None:
        $persistent.movie_3_seen = False

    if persistent.movie_4_seen == None:
        $persistent.movie_4_seen = False

    if persistent.movie_5_seen == None:
        $persistent.movie_5_seen = False

    if persistent.movie_6_seen == None:
        $persistent.movie_6_seen = False



screen movies_1():
    tag menu
    add "GUI/clouds.png"
    window:
        at slidemenu
        background Transform(Frame("GUI/base.png",0,0), alpha=persistent.window_opacity)

        add "GUI/book.png"


        hbox:
            xpos 230
            ypos 127
            style_group "page"
            textbutton _("1") action ShowMenu("movies_1")
            textbutton _("2") action ShowMenu("movies_2")


        vbox:
            xpos 594
            ypos 56
            if persistent.movie_1_seen:
                imagebutton idle "movie_1" action Jump("movie_1") at barfade
            else:
                add "GUI/locked.png"

        vbox:
            xpos 594
            ypos 200
            if persistent.movie_2_seen:
                imagebutton idle "movie_2" action Jump("movie_2") at barfade
            else:
                add "GUI/locked.png"

        vbox:
            xpos 594
            ypos 344
            if persistent.movie_3_seen:
                imagebutton idle "movie_3" action Jump("movie_3") at barfade
            else:
                add "GUI/locked.png"

        vbox:
            xpos 594
            ypos 488
            if persistent.movie_4_seen:
                imagebutton idle "movie_4" action Jump("movie_4") at barfade
            else:
                add "GUI/locked.png"


        hbox:
            xpos 175
            ypos 67
            style_group "stitle"

            label _("Movies")

        vbox:
            xpos 115
            ypos 470
            style_group "navigation"

            textbutton _("     Movies") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("movies_1") at slotfade
            textbutton _("     CG Gallery") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("gallery") at slotfade
            textbutton _("     Music Room") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("music_1") at slotfade
            if main_menu:
                textbutton _("     Main Menu") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action Return() at slotfade
            else:
                textbutton _("     Main Menu") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action MainMenu() at slotfade

        vbox:
            xpos 765
            ypos 15
            imagebutton idle "return_idle" hover "return_hover" activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action Return() at returnfade


screen movies_2():
    tag menu
    add "GUI/clouds.png"
    window:
        at slidemenu
        background Transform(Frame("GUI/base.png",0,0), alpha=persistent.window_opacity)

        add "GUI/book.png"


        hbox:
            xpos 230
            ypos 127
            style_group "page"
            textbutton _("1") action ShowMenu("movies_1")
            textbutton _("2") action ShowMenu("movies_2")


        vbox:
            xpos 594
            ypos 56
            if persistent.movie_5_seen:
                imagebutton idle "movie_5" action Jump("movie_5") at barfade
            else:
                add "GUI/locked.png"

        vbox:
            xpos 594
            ypos 200
            if persistent.movie_6_seen:
                imagebutton idle "movie_6" action Jump("movie_6") at barfade
            else:
                add "GUI/locked.png"



        hbox:
            xpos 175
            ypos 67
            style_group "stitle"

            label _("Movies")

        vbox:
            xpos 115
            ypos 470
            style_group "navigation"

            textbutton _("     Movies") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("movies_1") at slotfade
            textbutton _("     CG Gallery") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("gallery") at slotfade
            textbutton _("     Music Room") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("music_1") at slotfade
            if main_menu:
                textbutton _("     Main Menu") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action Return() at slotfade
            else:
                textbutton _("     Main Menu") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action MainMenu() at slotfade

        vbox:
            xpos 765
            ypos 15
            imagebutton idle "return_idle" hover "return_hover" activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action Return() at returnfade


########## The labels show the appropriate movies. If you want to change paths to the movies you should change them here as well.

label movie_1:

    $ renpy.movie_cutscene('Movies/movie_1.mp4',delay=None, loops=0, stop_music=True)
    call screen movies_1

label movie_2:

    $ renpy.movie_cutscene('Movies/movie_2.mpg',delay=None, loops=0, stop_music=True)
    call screen movies_1

label movie_3:

    $ renpy.movie_cutscene('Movies/movie_3.mpg',delay=None, loops=0, stop_music=True)
    call screen movies_1

label movie_4:

    $ renpy.movie_cutscene('Movies/movie_4.mpg',delay=None, loops=0, stop_music=True)
    call screen movies_1

label movie_5:

    $ renpy.movie_cutscene('Movies/movie_5.mpg',delay=None, loops=0, stop_music=True)
    call screen movies_2

label movie_6:

    $ renpy.movie_cutscene('Movies/movie_6.mpg',delay=None, loops=0, stop_music=True)
    call screen movies_2

##################

screen music_1():
    tag menu
    add "GUI/clouds.png"
    window:
        at slidemenu
        background Transform(Frame("GUI/base.png",0,0), alpha=persistent.window_opacity)

        add "GUI/book.png"

        hbox:
            xpos 230
            ypos 127
            style_group "page"
            textbutton _("1") action ShowMenu("music_1")
            textbutton _("2") action ShowMenu("music_2")


        vbox:
            xpos 495
            ypos 69
            spacing 0
            xsize 300
            style_group "music"

            if current_playing == 1:
                textbutton (musicList["Music/01 Vast Blue Sea -Japanese ver.-.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/01 Vast Blue Sea -Japanese ver.-.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/01 Vast Blue Sea -Japanese ver.-.mp3"), SetVariable("current_playing", 1)] at buttonfade

            if current_playing == 2:
                textbutton (musicList["Music/02 the town we live in.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/02 the town we live in.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/02 the town we live in.mp3"), SetVariable("current_playing", 2)] at buttonfade

            if current_playing == 3:
                textbutton (musicList["Music/03 a world forgotten.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/03 a world forgotten.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/03 a world forgotten.mp3"), SetVariable("current_playing", 3)] at buttonfade


            if current_playing == 4:
                textbutton (musicList["Music/04 march of the waves.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/04 march of the waves.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/04 march of the waves.mp3"), SetVariable("current_playing", 4)] at buttonfade

            if current_playing == 5:
                textbutton (musicList["Music/05 ivory flower.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/05 ivory flower.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/05 ivory flower.mp3"), SetVariable("current_playing", 5)] at buttonfade

            if current_playing == 6:
                textbutton (musicList["Music/06 fighting spirit.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/06 fighting spirit.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/06 fighting spirit.mp3"), SetVariable("current_playing", 6)] at buttonfade

            if current_playing == 7:
                textbutton (musicList["Music/07 spunky youth.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/07 spunky youth.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/07 spunky youth.mp3"), SetVariable("current_playing", 7)] at buttonfade

            if current_playing == 8:
                textbutton (musicList["Music/08 wonderland.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/08 wonderland.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/08 wonderland.mp3"), SetVariable("current_playing", 8)] at buttonfade

            if current_playing == 9:
                textbutton (musicList["Music/09 waves in the blue.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/09 waves in the blue.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/09 waves in the blue.mp3"), SetVariable("current_playing", 9)] at buttonfade

            if current_playing == 10:
                textbutton (musicList["Music/10 aria to the stars.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/10 aria to the stars.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/10 aria to the stars.mp3"), SetVariable("current_playing", 10)] at buttonfade

            if current_playing == 11:
                textbutton (musicList["Music/11 aquamarine skies.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/11 aquamarine skies.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/11 aquamarine skies.mp3"), SetVariable("current_playing", 11)] at buttonfade

            if current_playing == 12:
                textbutton (musicList["Music/12 unforgettable memories.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/12 unforgettable memories.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/12 unforgettable memories.mp3"), SetVariable("current_playing", 12)] at buttonfade

            if current_playing == 13:
                textbutton (musicList["Music/13 mischievous hour.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/13 mischievous hour.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/13 mischievous hour.mp3"), SetVariable("current_playing", 13)] at buttonfade

        hbox:
            xpos 175
            ypos 67
            style_group "stitle"

            label _("Music")

        vbox:
            xpos 115
            ypos 470
            style_group "navigation"

            textbutton _("     Movies") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("movies_1") at slotfade
            textbutton _("     CG Gallery") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("gallery") at slotfade
            textbutton _("     Music Room") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("music_1") at slotfade
            if main_menu:
                textbutton _("     Main Menu") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action Return() at slotfade
            else:
                textbutton _("     Main Menu") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action MainMenu() at slotfade

        vbox:
            xpos 765
            ypos 15
            imagebutton idle "return_idle" hover "return_hover" activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action Return() at returnfade

screen music_2():
    tag menu
    add "GUI/clouds.png"
    window:
        at slidemenu
        background Transform(Frame("GUI/base.png",0,0), alpha=persistent.window_opacity)

        add "GUI/book.png"

        hbox:
            xpos 230
            ypos 127
            style_group "page"
            textbutton _("1") action ShowMenu("music_1")
            textbutton _("2") action ShowMenu("music_2")


        vbox:
            xpos 495
            ypos 69
            spacing 0
            xsize 300
            style_group "music"
            if current_playing == 14:
                textbutton (musicList["Music/14 fractured truth.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/14 fractured truth.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/14 fractured truth.mp3"), SetVariable("current_playing", 14)] at buttonfade

            if current_playing == 15:
                textbutton (musicList["Music/15 withering heart.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/15 withering heart.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/15 withering heart.mp3"), SetVariable("current_playing", 15)] at buttonfade

            if current_playing == 16:
                textbutton (musicList["Music/16 tranquility.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/16 tranquility.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/16 tranquility.mp3"), SetVariable("current_playing", 16)] at buttonfade

            if current_playing == 17:
                textbutton (musicList["Music/17 monster.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/17 monster.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/17 monster.mp3"), SetVariable("current_playing", 17)] at buttonfade

            if current_playing == 18:
                textbutton (musicList["Music/18 home sweet home.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/18 home sweet home.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/18 home sweet home.mp3"), SetVariable("current_playing", 18)] at buttonfade

            if current_playing == 19:
                textbutton (musicList["Music/19 battle cry.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/19 battle cry.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/19 battle cry.mp3"), SetVariable("current_playing", 19)] at buttonfade

            if current_playing == 20:
                textbutton (musicList["Music/20 mother.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/20 mother.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/20 mother.mp3"), SetVariable("current_playing", 20)] at buttonfade

            if current_playing == 1:
                textbutton (musicList["Music/21 Vast Blue Sea -English ver.-.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/21 Vast Blue Sea -English ver.-.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/21 Vast Blue Sea -English ver.-.mp3"), SetVariable("current_playing", 1)] at buttonfade

            if current_playing == 22:
                textbutton (musicList["Music/22 So Spiragnor -mermaid ver.-.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/22 So Spiragnor -mermaid ver.-.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/22 So Spiragnor -mermaid ver.-.mp3"), SetVariable("current_playing", 22)] at buttonfade

            if current_playing == 23:
                textbutton (musicList["Music/23 So Spiragnor.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/23 So Spiragnor.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/23 So Spiragnor.mp3"), SetVariable("current_playing", 23)] at buttonfade

            if current_playing == 24:
                textbutton (musicList["Music/24Oh Mother Dear.mp3"]) background "GUI/stop.png" action [mr.Stop(), SetVariable("current_playing", 0)] at buttonfade
            else:
                textbutton (musicList["Music/24 Oh Mother Dear.mp3"]) background "GUI/play.png" insensitive_background "GUI/pref.png" action [mr.Play("Music/24 Oh Mother Dear.mp3"), SetVariable("current_playing", 24)] at buttonfade

        hbox:
            xpos 175
            ypos 67
            style_group "stitle"

            label _("Music")

        vbox:
            xpos 115
            ypos 470
            style_group "navigation"

            textbutton _("     Movies") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("movies_1") at slotfade
            textbutton _("     CG Gallery") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("gallery") at slotfade
            textbutton _("     Music Room") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("music_1") at slotfade
            if main_menu:
                textbutton _("     Main Menu") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action Return() at slotfade
            else:
                textbutton _("     Main Menu") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action MainMenu() at slotfade

        vbox:
            xpos 765
            ypos 15
            imagebutton idle "return_idle" hover "return_hover" activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action Return() at returnfade


screen music_3():
    tag menu
    add "GUI/clouds.png"
    window:
        at slidemenu
        background Transform(Frame("GUI/base.png",0,0), alpha=persistent.window_opacity)

        add "GUI/book.png"

        hbox:
            xpos 230
            ypos 127
            style_group "page"
            textbutton _("1") action ShowMenu("music_1")
            textbutton _("2") action ShowMenu("music_2")

        vbox:
            xpos 495
            ypos 69
            spacing 0
            xsize 300
            style_group "music"

        hbox:
            xpos 175
            ypos 67
            style_group "stitle"

            label _("Music")

        vbox:
            xpos 115
            ypos 470
            style_group "navigation"

            textbutton _("     Movies") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("movies_1") at slotfade
            textbutton _("     CG Gallery") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("gallery") at slotfade
            textbutton _("     Music Room") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action ShowMenu("music_1") at slotfade
            if main_menu:
                textbutton _("     Main Menu") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action Return() at slotfade
            else:
                textbutton _("     Main Menu") activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action MainMenu() at slotfade

        vbox:
            xpos 765
            ypos 15
            imagebutton idle "return_idle" hover "return_hover" activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action Return() at returnfade


########## Here's where you add the names and time that will be shown in the Music Room
init python:
    musicList = {
        "Music/01 Vast Blue Sea -Japanese ver.-.mp3":['Vast Blue Sea -Japanese ver.-  ', '2:30'],
        "Music/02 the town we live in.mp3":['the town we live in  ', '4:13'],
        "Music/03 a world forgotten.mp3":['a world forgotten  ', '5:22'],
        "Music/04 march of the waves.mp3":['march of the waves  ', '5:05'],
        "Music/05 ivory flower.mp3":['ivory flower  ', '5:26'],
        "Music/06 fighting spirit.mp3":['fighting spirit  ', '4:00'],
        "Music/07 spunky youth.mp3":['spunky youth  ', '2:25'],
        "Music/08 wonderland.mp3":['wonderland  ', '4:29'],
        "Music/09 waves in the blue.mp3":['waves in the blue  ', '4:33'],
        "Music/10 aria to the stars.mp3":['aria to the stars  ', '4:50'],
        "Music/11 aquamarine skies.mp3":['aquamarine skies  ', '4:29'],
        "Music/12 unforgettable memories.mp3":['unforgettable memories  ', '4:07'],
        "Music/13 mischievous hour.mp3":['mischievous hour  ', '4:43'],
        "Music/14 fractured truth.mp3":['fractured truth  ', '4:39'],
        "Music/15 withering heart.mp3":['withering heart  ', '5:51'],
        "Music/16 tranquility.mp3":['tranquility  ', '4:52'],
        "Music/17 monster.mp3":['monster  ', '4:16'],
        "Music/18 home sweet home.mp3":['home sweet home  ', '5:00'],
        "Music/19 battle cry.mp3":['battle cry  ', '4:20'],
        "Music/20 mother.mp3":['mother  ', '6:14'],
        "Music/21 Vast Blue Sea -English ver.-.mp3":['Vast Blue Sea -English ver.-  ', '2:30'],
        "Music/22 So Spiragnor -mermaid ver.-.mp3":['So Spiragnor -mermaid ver.-  ', '1:46'],
        "Music/23 So Spiragnor.mp3":['So Spiragnor  ', '1:44'],
        "Music/24 Oh Mother Dear.mp3":['Oh Mother Dear  ', '1:44']

        }
    mr = MusicRoom(fadeout=1.0)
    for track in musicList:
        mr.add(track, always_unlocked=False)




init -2:
    style music_button:
        xalign 0.0
        left_padding 25
        top_padding 0

    style music_button_text:
        idle_color "#333333"
        insensitive_color "#c3c1b7"
        hover_color "#000000"
        text_align 0.0
        font "GUI/Fonts/NotoSansCJKjp-Light.otf"
    $current_playing = 0

    style entry_button:
        background None
        #hover_background "GUI/ctc.png"
        selected_background "GUI/ctc.png"
        top_padding 0
        bottom_padding 0

    style entry_button_text:
        idle_color "#333333"
        insensitive_color "#c3c1b7"
        hover_color "#000000"
        text_align 0.0
        font "GUI/Fonts/NotoSansCJKjp-DemiLight.otf"
        size 18
        first_indent -20

    style entry_text:
        color "#333333"
        text_align 0.0
        font "GUI/Fonts/NotoSansCJKjp-Light.otf"
        size 18
        justify True
        first_indent 15


screen encyclopedia():
    tag menu
    if main_menu:
        add "GUI/clouds.png"
    window:
        at slidemenu
        background Transform(Frame("GUI/base.png",0,0), alpha=persistent.window_opacity)

        add "GUI/book.png"

#        hbox:
#            xpos 230
#            ypos 127
#            style_group "page"
#            textbutton _("1") action ShowMenu("music_1")
#            textbutton _("2") action ShowMenu("music_2")
#            textbutton _("3") action ShowMenu("music_3")


        vbox:
            style_group "entry"
            xpos 125
            ypos 135
            xsize 300

            textbutton _("           Ancient Aquadine") action SetVariable("encyclopedia", 1) at buttonfade
            textbutton _("           Aqua Festival") action SetVariable("encyclopedia", 2) at buttonfade
            textbutton _("           Aqua Temple") action SetVariable("encyclopedia", 3) at buttonfade
            textbutton _("           aquamarine eyes") action SetVariable("encyclopedia", 4) at buttonfade
            textbutton _("           aquamarine crystals") action SetVariable("encyclopedia", 5) at buttonfade
            textbutton _("           Bridge of Sorrow") action SetVariable("encyclopedia", 6) at buttonfade
            textbutton _("           endamier") action SetVariable("encyclopedia", 7) at buttonfade
            textbutton _("           Golden Sea") action SetVariable("encyclopedia", 8) at buttonfade
            textbutton _("           Grand Opera House") action SetVariable("encyclopedia", 9) at buttonfade
            textbutton _("           greater spirits") action SetVariable("encyclopedia", 10) at buttonfade
            textbutton _("           Helix Beach") action SetVariable("encyclopedia", 11) at buttonfade
            textbutton _("           Lazeul") action SetVariable("encyclopedia", 12) at buttonfade
            textbutton _("           lesser spirits") action SetVariable("encyclopedia", 13) at buttonfade
            textbutton _("           medium") action SetVariable("encyclopedia", 14) at buttonfade
            textbutton _("           Mythology of the Merfolk {p}    Civilization") action SetVariable("encyclopedia", 15) at buttonfade
            textbutton _("           The Tale of Urus") action SetVariable("encyclopedia", 16) at buttonfade
            textbutton _("           undine") action SetVariable("encyclopedia", 17) at buttonfade

        vbox:
            xpos 480
            ypos 150
            style_group "entry"
            xsize 280
            spacing 20

            if encyclopedia == 1:
                text ("Ancient Aquadine") font "GUI/Fonts/goodvibes.otf" size 28 xalign 0.5 first_indent 0
                text ("An underwater kingdom created by Levios in order to protect the merfolks from the humans. After his daughter Oneptu fell in love with a sailor many years later, she decided to live with him on the surface. Over time, more merfolks wanted to learn what living on the surface was like, so they followed her. Eventually, no one was left, leaving the kingdom to fall into ruin.")

            if encyclopedia == 2:
                text ("Aqua Festival") font "GUI/Fonts/goodvibes.otf" size 28 xalign 0.5 first_indent 0
                text ("An open school event that celebrates the founding of Aqua High each year. Because the school was built with the vast support of merfolk believers, the festival focuses on the town's culture. From holding plays that retell the merfolk lore to an abundance of seafood stands, many consider this festival to be one of the largest tributes to Levios.")

            if encyclopedia == 3:
                text ("Aqua Temple") font "GUI/Fonts/goodvibes.otf" size 28 xalign 0.5 first_indent 0
                text ("It was built, based on drawings of what was believed to be Ancient Aquadinian architecture, intended to honor the sea deity Levios. The temple currently houses some sort of jar, an artifact found by the S.S. Newport crew. Some believe that it could be related to the underwater civilization.")

            if encyclopedia == 4:
                text ("Aquamarine eyes") font "GUI/Fonts/goodvibes.otf" size 28 xalign 0.5 first_indent 0
                text ("Merfolks possess aquamarine colored eyes. Tears shed from these eyes are believed to be the origin of aquamarine. Those with aquamarine eyes can see the undines and Ancient Aquadine.")

            if encyclopedia == 5:
                text ("Aquamarine crystals") font "GUI/Fonts/goodvibes.otf" size 28 xalign 0.5 first_indent 0
                text ("Legend has it that aquamarine crystals were made from the tears of a merfolk and have the ability to protect those who are lost at sea. They can reverse the effects of magic and are often used for healing. However, the greater the magic, the larger the shard required.")

            if encyclopedia == 6:
                text ("Bridge of Sorrow") font "GUI/Fonts/goodvibes.otf" size 28 xalign 0.5 first_indent 0
                text ("The carvings contain images of a sailor and a mermaid who fell in love. They depict and convey that their love ultimately caused the end of Ancient Aquadine, which is how it got its name. However, ever since Torrie Liyun got engaged there, it ironically became a famous site where couples get together or propose.")

            if encyclopedia == 7:
                text ("Endamier") font "GUI/Fonts/goodvibes.otf" size 28 xalign 0.5 first_indent 0
                text ("A life threatening disease that causes merfolks to undergo abnormal physical changes, which could turn them into full sea creatures. Endamier can be cured, but it requires a large aquamarine crystal shard. Symptoms are leg pain, breathing difficulty, distorted vision, brain tumor, and lung tumor.")

            if encyclopedia == 8:
                text ("Golden Sea") font "GUI/Fonts/goodvibes.otf" size 28 xalign 0.5 first_indent 0
                text ("A field filled with daffodils, widely known as one of the memorable sights in Sylphyr.")

            if encyclopedia == 9:
                text ("Grand Opera House") font "GUI/Fonts/goodvibes.otf" size 28 xalign 0.5 first_indent 0
                text ("This building, recognized by architects worldwide, was contructed about 200 years ago. Nearly 8000 people were hired to construct this building and it holds approximately 3000 seats, making it the oldest and largest opera house in Aquadine. Nowadays, it's not only used for opera and classical music, but a large variety of other performances as well.")

            if encyclopedia == 10:
                text ("Greater spirits") font "GUI/Fonts/goodvibes.otf" size 28 xalign 0.5 first_indent 0
                text ("Beings that were originally divine or powerful in their past lives. Unlike lesser spirits, greater spirits are able to take on a host body. If they do, then a medium is no longer required for communication.")

            if encyclopedia == 11:
                text ("Helix Beach") font "GUI/Fonts/goodvibes.otf" size 28 xalign 0.5 first_indent 0
                text ("One of the famous beaches in Aquadine, known for its beautiful conchs and seashells, hence the name. Sometimes, people turn them into accessories or souvenirs in special stores.")


            if encyclopedia == 12:
                text ("Lazeul") font "GUI/Fonts/goodvibes.otf" size 28 xalign 0.5 first_indent 0
                text ("A realm where most undines reside. Levios forfeited his immortality to create this space after Ancient Aquadine fell. It also serves as a gate to forever conceal Ancient Aquadine from the world.")

            if encyclopedia == 13:
                text ("Lesser spirits") font "GUI/Fonts/goodvibes.otf" size 28 xalign 0.5 first_indent 0
                text ("Beings, like undines, that wander aimlessly while invisible to the naked eye.")

            if encyclopedia == 14:
                text ("Medium") font "GUI/Fonts/goodvibes.otf" size 28 xalign 0.5 first_indent 0
                text ("One who can see and hear the spirits. This ability can be inherited by a parent. Mediums are particularly useful when communicating with the lesser spirits or other spirits that do not have a host body.")

            if encyclopedia == 15:
                text ("Mythology {p}of the {p}Merfolk Civilization") font "GUI/Fonts/goodvibes.otf" size 28 xalign 0.5 text_align 1.0 first_indent 0
                text ("A recorded collection of information referring to merfolk traits and history, written by a firm believer of Ancient Aquadine.")

            if encyclopedia == 16:
                text ("The Tale of Urus") font "GUI/Fonts/goodvibes.otf" size 28 xalign 0.5 first_indent 0
                text ("One of many fairy tales of the merfolks. This one in particular is about Urus, one of Levios's most trusted and loyal followers. Despite being Juna's closest friend, she fell in love with Levios.")

            if encyclopedia == 17:
                text ("Undine") font "GUI/Fonts/goodvibes.otf" size 28 xalign 0.5 first_indent 0
                text ("The lesser spirits of merfolks that pass away, which take the form of jellyfish.")




        hbox:
            xpos 155
            ypos 67
            style_group "stitle"

            label _("Encyclopedia")


        vbox:
            xpos 765
            ypos 15
            imagebutton idle "return_idle" hover "return_hover" activate_sound "sound/AQD_CLICK.mp3" hover_sound "sound/AQD_HOVER.mp3" action Return() at returnfade

        vbox:
            xpos 680
            ypos 575

            style_group "prefbutton"
            textbutton _("Return") action Return() at buttonfade

init -2 python:
    encyclopedia=1
