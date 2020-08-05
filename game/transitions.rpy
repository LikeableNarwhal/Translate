transform slotfade:
    on idle:
        alpha 0.9
    on selected_idle:
        alpha 0.9
    on hover:
        alpha 0.9
        linear 0.5 alpha 1
    on selected_hover:
        alpha 0.9
        linear 0.5 alpha 1    



transform buttonfade:

    on idle:
        alpha 1.0

    on hover:
            alpha 0.5
            linear 0.3 alpha 1.5  

    on selected_hover:
            alpha 0.5
            linear 0.3 alpha 1.5  


transform returnfade:

    on idle:
        alpha 1.0
        yoffset 0

    on hover:
            alpha 0.7 
            linear .3 alpha 1.0 yoffset -2


transform slidemenu:
    on show:
        ypos 0
        easein .5 ypos 720

    on hide:
        yoffset 0
        easeout .5 yoffset -720   

transform barfade:

    on idle:
        alpha 1.0
    on hover:
            alpha 0.8
            linear 0.3 alpha 1.1
    on selected_hover:
            alpha 0.8
            linear 0.3 alpha 1.1            
       

transform slide:
    on show:
        yoffset 50
        easein .5 yoffset 0
    on hide:
        easeout .5 yoffset 30
        
image return_hover:
    "GUI/return.png"
    subpixel True
    block:
        linear .3 yoffset -1
        linear .3 yoffset 1
        repeat
    

image return_idle:
    "GUI/return.png"