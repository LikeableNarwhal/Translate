label start:

$ save_name = "common route"
#(Begin game. CG illustration of the ancient times between the humans and the merfolk. Levios is in the center. Play new world music.)

play music "Music/03 a world forgotten.mp3"
scene cg_1 with flash

"Long ago, a devastating drought ravaged the land."

"Their soil was too parched to grow crops and their livestock dwindled in number. Heat strokes, hunger, and dehydration took the lives of countless villagers."

"Without the necessary resources for survival, the villagers turned to Levios, the sea deity, and prayed for food and clean water."

"Levios granted them their wish, but only under one condition - that the merfolk would be allowed to live peacefully among them. And for many decades, they did."

"Over time, however, the merfolk were gradually discriminated against because they were considered abnormal half-humans - inferior beings."

"Levios became enraged and created an underwater kingdom, now known as Ancient Aquadine, to personally lead and protect the merfolk himself..."

"Until one day, the ancient civilization ceased to exist."

#(End new world music.)
stop music fadeout 1.0

#EXT. Canal - Day

#(Play relaxing gondola riding music. Play sound effect of oar pushing water. Ciel, Mr. Bello, and Violetta are present. Violetta looks stoic.)
scene canal_day with fadehold
play music "Music/09 waves in the blue.mp3"
play sound "sound/Reddevitzer_Hoeft_03.mp3" loop

voice "voice/Ciel_over_here.mp3"
show MrBello_normal_casual1_flip at midleft with renpy.transition(dissolve, layer="master")
show Violetta_stoic_casual1_flip at center with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform1_flip at farleft with renpy.transition(dissolve, layer="master")
Ciel "And so, the people of the land named this town 'Aquadine' as a tribute to the sea deity. This is also one of many statues sculpted by believers of the merfolk lore."

voice "voice/Violetta_really.mp3"
hide Violetta_stoic_casual1_flip at center with renpy.transition(dissolve, layer="master")
show Violetta_annoyed_casual1 at center with renpy.transition(dissolve, layer="master")
Violetta "Are we seriously supposed to believe that mermaids existed?"

#(smiles)
hide Robin_normal_uniform1_flip at farleft with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform2_flip at farleft with renpy.transition(dissolve, layer="master")
Ciel "It's perfectly understandable that most people share the same skepticism, especially those who aren't from here."

#(normal)
hide Robin_happy_uniform2_flip at farleft with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform2_flip at farleft with renpy.transition(dissolve, layer="master")
Ciel "Even today, people continue to debate over the validity of the lore, despite the lack of reliable evidence. However, it's impossible to ignore that the beliefs of our ancestors shaped much of our culture."

#(smiles)
hide Robin_normal_uniform2_flip at farleft with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform1_flip at farleft with renpy.transition(dissolve, layer="master")
Ciel "As a result, the desire to please Levios drove the town to become one of the best in the world at controlling water pollution. Aquadine even prides itself as a top exporter in both seafood and bottled freshwater."

hide MrBello_normal_casual1_flip at midleft with renpy.transition(dissolve, layer="master")
show MrBello_normal_casual1 at midleft with renpy.transition(dissolve, layer="master")
Bello "Pardon for the interruption, but I was wondering if you had any suggestions for a nice cup of coffee."

#(normal)
voice "voice/Robin_hm.mp3"
hide Robin_happy_uniform1_flip at farleft with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform2_flip at farleft with renpy.transition(dissolve, layer="master")
Ciel "Actually, we're near one right now. Next to the statue, you'll find the Frezner Café - a family owned business that has been around for over fifty years."

#(smiles)
hide Robin_normal_uniform2_flip at farleft with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform1_flip at farleft with renpy.transition(dissolve, layer="master")
Ciel "They serve some of the best coffee and sweets in town, so I highly recommend you pay a visit. If you'd like, I could book a reservation for you two."

#(smiles)
voice "voice/MrBello_thank you.mp3"
hide MrBello_normal_casual1 at midleft with renpy.transition(dissolve, layer="master")
show MrBello_happy_casual1 at midleft with renpy.transition(dissolve, layer="master")
Bello "That would be great. Thank you."

hide Robin_normal_uniform2_flip at farleft with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform2_flip at farleft with renpy.transition(dissolve, layer="master")
Ciel "My pleasure. If you have any other questions, please don't hesitate to ask."

#(curious)
voice "voice/Violetta_hey.mp3"
hide Violetta_annoyed_casual1 at center with renpy.transition(dissolve, layer="master")
show Violetta_normal_casual1 at center with renpy.transition(dissolve, layer="master")
Violetta "Is there...a marble store around here?"

#(curious)
voice "voice/Ciel_oh.mp3"
hide Robin_happy_uniform2_flip at farleft with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform2_flip at farleft with renpy.transition(dissolve, layer="master")
Ciel "Marbles...?"

hide MrBello_happy_casual1 at midleft with renpy.transition(dissolve, layer="master")
show MrBello_nervous_casual1 at midleft with renpy.transition(dissolve, layer="master")
Bello "My daughter has been collecting marbles since she was a kid. I could never understand why, but she absolutely loves them."

#(embarrassed)
hide Violetta_normal_casual1 at center with renpy.transition(dissolve, layer="master")
show Violetta_embarrassed_casual1 at center with renpy.transition(dissolve, layer="master")
Violetta "Daddy!!!"

#(smiles)
hide Robin_surprised_uniform2_flip at farleft with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform1_flip at farleft with renpy.transition(dissolve, layer="master")
Ciel "There's no need to be ashamed about what you like, though it is the first time anyone's asked me about marbles."

#(normal)
hide Robin_happy_uniform1_flip at farleft with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform1_flip at farleft with renpy.transition(dissolve, layer="master")
Ciel "You might have some luck checking the souvenir shops in the mall. I can write you a list when we get back."

#(smiles)
hide MrBello_nervous_casual1 at midleft with renpy.transition(dissolve, layer="master")
show MrBello_happy_casual1_flip at midleft with renpy.transition(dissolve, layer="master")
Bello "Isn't that great? Let's go there together after the tour."

#(smiles)
hide Violetta_embarrassed_casual1 at center with renpy.transition(dissolve, layer="master")
show Violetta_normal_casual1 at center with renpy.transition(dissolve, layer="master")
Violetta "All right. Thanks, Dad..."

hide Robin_normal_uniform1_flip at farleft with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform2_flip at farleft with renpy.transition(dissolve, layer="master")
Ciel "(It must be nice...for a family to spend time like this. I wish I could do that more often...)"

#(End relaxing gondola music. Hide all characters. Ciel sings for the rest of the scene.)
stop music fadeout 1.0
stop sound fadeout 1.0
hide MrBello_happy_casual1_flip at midleft with renpy.transition(dissolve, layer="master")
hide Violetta_normal_casual1 at center with renpy.transition(dissolve, layer="master")
hide Robin_normal_uniform2_flip at farleft with renpy.transition(dissolve, layer="master")
show Robin_asleep_uniform1_flip at farleft with renpy.transition(dissolve, layer="master")
play music "Music/23 So Spiragnor.mp3"

"As the gondolier continues to tour the family, his smile gradually fades away. Instead, his voice takes its place - a voice that soon breaks into a barcarolle."

hide Robin_asleep_uniform1_flip at farleft with renpy.transition(dissolve, layer="master")
show Robin_asleep_uniform2_flip at farleft with renpy.transition(dissolve, layer="master")
"Gentle rows rhythmically push through the water as calmly as the soothing breeze. The white gondola rides casually over the clear waves and glides through a narrow passage."

hide Robin_asleep_uniform2_flip at farleft with renpy.transition(dissolve, layer="master")
"People, enchanted by the song, open their windows and stop to listen as the sound of his voice travels across the canal."

#(Anya and Diana appear. Diana looks surprised, while Anya is stoic.)
voice "voice/Diana_gasps.mp3"
show Diana_surprised_casual3 at midright with renpy.transition(dissolve, layer="master")
show Anya_normal_casual1 at center with renpy.transition(dissolve, layer="master")
Diana "It's...Ciel's voice, isn't it? Ciel is singin' today!"

voice "voice/Anya_whatever.mp3"
hide Anya_normal_casual1 at center with renpy.transition(dissolve, layer="master")
show Anya_normal_casual2 at center with renpy.transition(dissolve, layer="master")
Anya "Good for you, Diana."

#(worried)
hide Diana_surprised_casual3 with renpy.transition(dissolve, layer="master")
show Diana_embarrassed_casual1 at midright with renpy.transition(dissolve, layer="master")
Diana "Where's my phone? Where's my phone?!"

#(Hide Diana.)
hide Diana_embarrassed_casual1 with renpy.transition(dissolve, layer="master")
"Anya continues drawing the canal, while trying to ignore Diana - who is scrambling frantically for her phone."

#(Diana appears excited.)
voice "voice/Diana_later.mp3"
show Diana_happy_casual2 at midright with renpy.transition(dissolve, layer="master")
Diana "Catch ya later, Anya!"

#(Diana leaves.)
hide Diana_happy_casual2 at midright with renpy.transition(easeoutright, layer="master")
"Without wasting another second, Diana hurries along before she misses her chance."

voice "voice/Anya_good_bye.mp3"
hide Anya_normal_casual2 at center with renpy.transition(dissolve, layer="master")
show Anya_normal_casual1 at center with renpy.transition(dissolve, layer="master")
Anya "Bye."

#EXT. Plaza - Day
scene plaza_day with renpy.transition(wiperight, layer="master")

#(Ciel is still singing.)
"Diana inches her way through a crowd of people who are also attracted to the sound of Ciel's voice. She is absolutely determined to get a picture with him."

show Diana_laugh_casual3_flip at midleft with renpy.transition(easeinleft, layer="master")

#(rushed)
voice "voice/Diana_light_laughter.mp3"
Diana "I gotta hurry before I miss him!"

#(Hide Diana. Bumping sound effect.)
stop music fadeout 1.0
play sound "sound/Seq 2.1 Hit #3 96 HK1.mp3"
hide Diana_laugh_casual3_flip with renpy.transition(dissolve, layer="master")
show plaza_day with hpunch
"As Diana chases after his voice, she bumps into someone and all of their belongings fall with them."

#(Diana appears shocked.)
voice "voice/Diana_gasps.mp3"
show Diana_surprised_casual1_flip at midleft with renpy.transition(dissolve, layer="master")
Diana "My bad! You okay?"

#(Elisabeth appears, while wearing a sun hat and dress.)
play music "Music/05 ivory flower.mp3"
show Elisabeth_nervous_casual1 at midright with renpy.transition(dissolve, layer="master")

#(Elisabeth)
voice "voice/Elisabeth_forgive_me.mp3"
unknown "I am fine. Are you injured?"

voice "voice/Diana_sorry_bout_that.mp3"
hide Diana_surprised_casual1_flip at midleft with renpy.transition(dissolve, layer="master")
show Diana_nervous_casual1_flip at midleft with renpy.transition(dissolve, layer="master")
Diana "Nah, I'm good. Sorry 'bout that!"

#(Diana looks serious.)
hide Diana_nervous_casual1_flip at midleft with renpy.transition(dissolve, layer="master")
show Diana_serious_casual3_flip at midleft with renpy.transition(dissolve, layer="master")
"Diana stares at the other girl for a moment, as if she recognizes her from somewhere."

#(realizes, gasps)
voice "voice/Diana_oh.mp3"
hide Diana_serious_casual3_flip at midleft with renpy.transition(dissolve, layer="master")
show Diana_surprised_casual1_flip at midleft with renpy.transition(dissolve, layer="master")
Diana "Wait, I know you! You're-!"

#(smiles)
hide Elisabeth_nervous_casual1 with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_casual1_flip at midright with renpy.transition(dissolve, layer="master")
unknown "Farewell."

#(Elisabeth leaves.)
hide Elisabeth_normal_casual1_flip with renpy.transition(easeoutright, layer="master")
stop music fadeout 1.0
"Still stunned, Diana is speechless as she gets a better look at the blonde. It doesn't take long before she cracks a smile."

#(excited)
voice "voice/Diana_light_laughter.mp3"
hide Diana_surprised_casual1_flip with renpy.transition(dissolve, layer="master")
show Diana_laugh_casual3_flip at midleft with renpy.transition(dissolve, layer="master")
Diana "I can't believe she's here in Aquadine! Gotta get a picture with her!"

#(realizes)
voice "voice/Diana_gasps.mp3"
hide Diana_laugh_casual3_flip with renpy.transition(dissolve, layer="master")
show Diana_surprised_casual1_flip at midleft with renpy.transition(dissolve, layer="master")
Diana "Oh no, my phone! I just got this darn thing!"

hide Diana_surprised_casual1_flip with renpy.transition(easeoutbottom, layer="master")
"As Diana picks up her cracked smartphone from the ground, the other girl disappears into the crowd."

show Diana_sad_casual1 at center with renpy.transition(easeinbottom, layer="master")
Diana "(Man, where'd she go? I just saw her.)"

#(normal)
hide Diana_sad_casual1 at center with renpy.transition(dissolve, layer="master")
show Diana_normal_casual3 at center with renpy.transition(dissolve, layer="master")
Diana "(Well, at least I can still snap a picture of Ciel.)"

#(Camera click sound effect.)
play sound "sound/StartSelect,UI,set57,camera mechanics,servo,clicks clacks,meaty,operative,forward.mp3"
"*click*"

#(End Ciel's singing. Anya appears.)
stop sound fadeout 1.0
play music "Music/08 wonderland.mp3"
voice "voice/Anya_wow.mp3"
show Anya_normal_casual2_flip at left with renpy.transition(dissolve, layer="master")
Anya "Done yet?"

#(nervous smile)
voice "voice/Diana_sorry_bout_that.mp3"
hide Diana_normal_casual3 at center with renpy.transition(dissolve, layer="master")
show Diana_laugh_casual1 at center with renpy.transition(dissolve, layer="master")
Diana "Yeah, sorry 'bout that. Ya headin' home?"

voice "voice/Anya_maybe.mp3"
hide Anya_normal_casual2_flip at left with renpy.transition(dissolve, layer="master")
show Anya_normal_casual1_flip at left with renpy.transition(dissolve, layer="master")
Anya "Maybe."

#(sighs)
voice "voice/Diana_well.mp3"
hide Diana_laugh_casual1 at center with renpy.transition(dissolve, layer="master")
show Diana_nervous_casual3 at center with renpy.transition(dissolve, layer="master")
Diana "I am, but my mom's gonna have me help around the café again. She's a real slave driver, ya know?"

hide Anya_normal_casual1_flip at left with renpy.transition(dissolve, layer="master")
show Anya_nervous_casual2_flip at left with renpy.transition(dissolve, layer="master")
Anya "Sounds troublesome."

#(smiles)
hide Diana_nervous_casual3 at center with renpy.transition(dissolve, layer="master")
show Diana_normal_casual3 at center with renpy.transition(dissolve, layer="master")
Diana "I know right? Oh yeah, guess what."

#(sighs)
voice "voice/Anya_hm.mp3"
hide Anya_nervous_casual2_flip at left with renpy.transition(dissolve, layer="master")
show Anya_normal_casual1_flip at left with renpy.transition(dissolve, layer="master")
Anya "What...?"

#(excited)
hide Diana_normal_casual3 at center with renpy.transition(dissolve, layer="master")
show Diana_grin_casual2 at center with renpy.transition(dissolve, layer="master")
Diana "I saw Elisabeth Rhodes today! I had no idea she'd be here! Can't believe I didn't know 'bout it!"

#(shrugs)
hide Anya_normal_casual1_flip at left with renpy.transition(dissolve, layer="master")
show Anya_normal_casual2_flip at left with renpy.transition(dissolve, layer="master")
Anya "Meh, just another human."

#(shocked)
voice "voice/Diana_gasps.mp3"
hide Diana_grin_casual2 at center with renpy.transition(dissolve, layer="master")
show Diana_surprised_casual1 at center with renpy.transition(dissolve, layer="master")
Diana "She's a celebrity! What else could ya ask for?"

#(grins)
voice "voice/Anya_actually.mp3"
hide Anya_normal_casual2_flip at left with renpy.transition(dissolve, layer="master")
show Anya_nervous_casual3_flip at left with renpy.transition(dissolve, layer="master")
Anya "An alien. I think that'd be more interesting than some singer."

#(laughs)
voice "voice/Diana_light_laughter.mp3"
hide Diana_surprised_casual1 at center with renpy.transition(dissolve, layer="master")
show Diana_laugh_casual3 at center with renpy.transition(dissolve, layer="master")
Diana "You're so weird. Anyway, Elisabeth is pretty easy-goin', unlike somebody I know."

#(blushes)
voice "voice/Anya_Im_fine.mp3"
hide Anya_nervous_casual3_flip at left with renpy.transition(dissolve, layer="master")
show Anya_embarrassed_casual3_flip at left with renpy.transition(dissolve, layer="master")
Anya "Mock me all you like, but aliens are adorable."

#(normal)
voice "voice/Diana_what_do_ya_think.mp3"
hide Diana_laugh_casual3 at center with renpy.transition(dissolve, layer="master")
show Diana_happy_casual2 at center with renpy.transition(dissolve, layer="master")
Diana "By the way, wanna stop by the café today? My mom hasn't seen you in forever."

#(uninterested)
hide Anya_sad_casual3_flip at left with renpy.transition(dissolve, layer="master")
show Anya_normal_casual1_flip at left with renpy.transition(dissolve, layer="master")
Anya "No thanks."

#(pleads)
hide Diana_happy_casual2 at center with renpy.transition(dissolve, layer="master")
show Diana_sad_casual3 at center with renpy.transition(dissolve, layer="master")
Diana "Just hang out with me for a bit longer. Pretty please?"

#(stoic)
voice "voice/Anya_whatever.mp3"
hide Anya_normal_casual1_flip at left with renpy.transition(dissolve, layer="master")
show Anya_normal_casual2_flip at left with renpy.transition(dissolve, layer="master")
hide Diana_sad_casual3 at center with renpy.transition(dissolve, layer="master")
show Diana_happy_casual3 at center with renpy.transition(dissolve, layer="master")
Anya "*sigh* All right. It's not like I've got anthing better to do anyway..."

#(End casual outdoor music.)
stop music fadeout 1.0

#INT. Frezner Café - Day
scene cafe_day with renpy.transition(dissolve, layer="master")

#(Play casual outdoor music.)
play music "Music/12 unforgettable memories.mp3"

"Aquadine's famous café has a classic charm, as it is decorated with an array of fresh vines and traditional paintings. Old wine bottles and flower vases occupy the shelves, among other antiques."

show Susan_normal_cafe1_flip at left with renpy.transition(dissolve, layer="master")
show Diana_normal_casual3 at midright with renpy.transition(dissolve, layer="master")
show Anya_normal_casual2 at right with renpy.transition(dissolve, layer="master")
"Anya and Diana wait near a well-kept jukebox, while a lady in her 40s is serving a customer."

#(Anya and Diana are present. Anya is stoic, while Diana is smiling.)

voice "voice/Diana_whats_up.mp3"
hide Diana_normal_casual3 at midright with renpy.transition(dissolve, layer="master")
show Diana_happy_casual2 at midright with renpy.transition(dissolve, layer="master")
Diana "Mom, I'm home!"

#(Susan appears stoic.)
voice "voice/Susan_get_moving.mp3"
hide Susan_normal_cafe1_flip at left
show Susan_serious_cafe1_flip at left
with renpy.transition(dissolve, layer="master")
Susan "Diana, hurry and get that table's order."

#(nervous smile)
hide Diana_happy_casual2 at midright with renpy.transition(dissolve, layer="master")
show Diana_nervous_casual1 at midright with renpy.transition(dissolve, layer="master")
Diana "See what I mean?"

#(smiles)
voice "voice/Susan_hey_there.mp3"
hide Susan_serious_cafe1_flip at left with renpy.transition(dissolve, layer="master")
show Susan_normal_cafe1_flip at left with renpy.transition(dissolve, layer="master")
Susan "Anya, it's been a while."

#(nervous smile)
voice "voice/Anya_well.mp3"
hide Anya_normal_casual2 at right with renpy.transition(dissolve, layer="master")
show Anya_nervous_casual2 at right with renpy.transition(dissolve, layer="master")
Anya "I guess it has..."

#(suspicious)
voice "voice/Susan_wait.mp3"
hide Susan_normal_cafe1_flip at left with renpy.transition(dissolve, layer="master")
show Susan_serious_cafe1_flip at left with renpy.transition(dissolve, layer="master")
Susan "You're buying something, right?"

voice "voice/Anya_maybe.mp3"
hide Anya_nervous_casual2 at right with renpy.transition(dissolve, layer="master")
show Anya_nervous_casual3 at right with renpy.transition(dissolve, layer="master")
Anya "Probably."

#(smiles)
hide Susan_serious_cafe1_flip at left
show Susan_laugh_cafe1_flip at left
with renpy.transition(dissolve, layer="master")
voice "voice/Susan_enjoy.mp3"
Susan "Great! Have a seat! Let Diana know if you need anything, okay?"

#(Hide Anya.)
hide Anya_nervous_casual3 at farright with renpy.transition(easeoutright, layer="master")
"After responding with a mere nod, Anya finds an empty table and quickly makes herself at home - reflecting how well she's known them."

#(Fade to white and back briefly. Anya is present, but Diana and Susan are not.)
scene cafe_day with fadehold
show Anya_normal_casual1_flip at left with renpy.transition(dissolve, layer="master")
show Diana_normal_maid3 at center with renpy.transition(dissolve, layer="master")
"Dressed in her maid uniform, Diana returns with two cups of coffee and notices Anya occupied with her sketchbook."

#(Diana realizes as she appears.)
voice "voice/Diana_oh.mp3"
hide Diana_normal_maid3 at center with renpy.transition(dissolve, layer="master")
show Diana_surprised_maid1 at center with renpy.transition(dissolve, layer="master")
Diana "Oh! That's the one ya drew today, isn't it?"

voice "voice/Anya_exactly.mp3"
Anya "Yeah."

#(normal)
hide Diana_surprised_maid1 at center with renpy.transition(dissolve, layer="master")
show Diana_normal_maid3 at center with renpy.transition(dissolve, layer="master")
Diana "That reminds me. I have a teeny tiny favor to ask of ya."

#(suspicious)
voice "voice/Anya_hm.mp3"
hide Anya_normal_casual1_flip at left with renpy.transition(dissolve, layer="master")
show Anya_normal_casual2_flip at left with renpy.transition(dissolve, layer="master")
Anya "How teeny tiny...?"

#(Diana smiles.)
hide Diana_normal_maid3 at center with renpy.transition(dissolve, layer="master")
show Diana_happy_maid2 at center with renpy.transition(dissolve, layer="master")
"Diana proudly whips out her phone and shows off her picture of Ciel. She's like a kid who just pulled the best toy out of a cereal box."

voice "voice/Diana_what_do_ya_think.mp3"
hide Diana_happy_maid2 at center with renpy.transition(dissolve, layer="master")
show Diana_grin_maid2 at center with renpy.transition(dissolve, layer="master")
Diana "Could ya draw Ciel for me? I really wanna hang another picture of him in my room."

#(surprised)
voice "voice/Anya_wow.mp3"
hide Anya_normal_casual2_flip at left with renpy.transition(dissolve, layer="master")
show Anya_surprised_casual1_flip at left with renpy.transition(dissolve, layer="master")
Anya "You already cracked your phone?"

#(nervous smile)
voice "voice/Diana_um.mp3"
hide Diana_grin_maid2 at center with renpy.transition(dissolve, layer="master")
show Diana_nervous_maid1 at center with renpy.transition(dissolve, layer="master")
Diana "Yeah...it happened durin' the whole bumpin' into Elisabeth fiasco."

#(suspicious)
hide Anya_surprised_casual1_flip at left with renpy.transition(dissolve, layer="master")
show Anya_normal_casual1_flip at left with renpy.transition(dissolve, layer="master")
Anya "What's in it for me?"

#(smiles)
voice "voice/Diana_mhmm.mp3"
hide Diana_nervous_maid1 at center with renpy.transition(dissolve, layer="master")
show Diana_happy_maid3 at center with renpy.transition(dissolve, layer="master")
Diana "Your drink is on the house!"

hide Anya_normal_casual1_flip at left with renpy.transition(dissolve, layer="master")
show Anya_nervous_casual1_flip at left with renpy.transition(dissolve, layer="master")
"Anya's eyes roll down at the cup of coffee she just sipped. She then looks back at Diana, who has the brightest smile on her face."

Anya "(That explains why she suddenly wanted to treat me to some coffee. How prudent...)"

#(stoic)
voice "voice/Anya_actually.mp3"
hide Anya_nervous_casual1_flip at left with renpy.transition(dissolve, layer="master")
show Anya_normal_casual2_flip at left with renpy.transition(dissolve, layer="master")
Anya "I'll just pay for it. It's only like 300 altos anyway."

#(begs)
hide Diana_happy_maid3 at center with renpy.transition(dissolve, layer="master")
show Diana_sad_maid1 at center with renpy.transition(dissolve, layer="master")
Diana "Please, Anya! Draw Ciel for me...!"

voice "voice/Anya_Im_fine.mp3"
hide Anya_normal_casual2_flip at left with renpy.transition(dissolve, layer="master")
show Anya_sad_casual1_flip at left with renpy.transition(dissolve, layer="master")
Anya "Not worth my time."

#(shocked)
voice "voice/Diana_gasps.mp3"
hide Diana_sad_maid1 at center with renpy.transition(dissolve, layer="master")
show Diana_surprised_maid3 at center with renpy.transition(dissolve, layer="master")
Diana "My act of kindness isn't even worth a gift from a friend?!"

#(annoyed)
voice "voice/Anya_is_that_clear.mp3"
hide Anya_sad_casual1_flip at left with renpy.transition(dissolve, layer="master")
show Anya_glare_casual1_flip at left with renpy.transition(dissolve, layer="master")
Anya "It's not an act of kindness if you expect something in return."

#(nearly cries)
hide Diana_surprised_maid3 at center with renpy.transition(dissolve, layer="master")
show Diana_sad_maid1 at center with renpy.transition(dissolve, layer="master")
Diana "I... I thought we were friends..."

#(realizes)
hide Anya_glare_casual1_flip at left with renpy.transition(dissolve, layer="master")
show Anya_sad_casual1_flip at left with renpy.transition(dissolve, layer="master")
Anya "..."

#(sighs)
voice "voice/Anya_whatever.mp3"
hide Anya_sad_casual1_flip at left with renpy.transition(dissolve, layer="master")
show Anya_embarrassed_casual3_flip at left with renpy.transition(dissolve, layer="master")
Anya "Okay, fine..."

#(smiles)
voice "voice/Diana_thanks.mp3"
hide Diana_sad_maid1 at center with renpy.transition(dissolve, layer="master")
show Diana_happy_maid3 at center with renpy.transition(dissolve, layer="master")
Diana "Thanks a bunch!"

#(annoyed)
voice "voice/Anya_well.mp3"
hide Anya_embarrassed_casual3_flip at left with renpy.transition(dissolve, layer="master")
show Anya_serious_casual1_flip at left with renpy.transition(dissolve, layer="master")
Anya "I know Ciel is really popular, but why do you like him? Isn't he just another gondolier?"

#(smirks)
voice "voice/Diana_light_laughter.mp3"
hide Diana_happy_maid3 at center with renpy.transition(dissolve, layer="master")
show Diana_laugh_maid3 at center with renpy.transition(dissolve, layer="master")
Diana "Everyone knows that he's the youngest gondolier in town, but he's also really kind and talented. Even a lot of the local girls ride with him."

#(nervous smile)
hide Anya_serious_casual1_flip at left with renpy.transition(dissolve, layer="master")
show Anya_nervous_casual2_flip at left with renpy.transition(dissolve, layer="master")
Anya "They don't seem very smart."

#(shrugs)
hide Diana_laugh_maid3 at center with renpy.transition(dissolve, layer="master")
show Diana_normal_maid3 at center with renpy.transition(dissolve, layer="master")
Diana "That's just how the fandom goes. I hear his granddaddy can be strict though, but he doesn't let that bother him when he's with customers."

#(Anya's expression returns to normal.)
hide Anya_nervous_casual2_flip at left with renpy.transition(dissolve, layer="master")
show Anya_normal_casual1_flip at left with renpy.transition(dissolve, layer="master")
"Anya drinks her coffee as she pretends to listen to Diana's constant rambling."

#(End casual outdoor music.)
stop music fadeout 1.0

#INT. Classroom - Morning
scene classroom_day with fadehold

#(Play classroom music.)
play music "Music/11 aquamarine skies.mp3"
"The following morning begins with a little more noise than usual as a bit of interesting news made its way around the school. Classes haven't started yet, so students are speculating as much as they please."

#(Diana and Cameron are present. Diana seems excited.)
show Cameron_normal_school2_flip at left with renpy.transition(dissolve, layer="master")
show Diana_grin_school2 at center with renpy.transition(dissolve, layer="master")

voice "voice/Diana_whats_up.mp3"
Diana "Hey, did ya hear that we're gonna get a transfer student?"

#(surprised)
voice "voice/Cameron_really.mp3"
hide Cameron_normal_school2_flip at left with renpy.transition(dissolve, layer="master")
show Cameron_surprised_school3_flip at left with renpy.transition(dissolve, layer="master")
Cameron "Oh, we are? I didn't hear anything about that."

#(smiles)
voice "voice/Diana_mhmm.mp3"
hide Diana_grin_school2 at center with renpy.transition(dissolve, layer="master")
show Diana_happy_school3 at center with renpy.transition(dissolve, layer="master")
Diana "Yeah, I'm kinda excited. They're sayin' it's someone outside of Aquadine."

#(curious)
hide Cameron_surprised_school3_flip at left with renpy.transition(dissolve, layer="master")
show Cameron_normal_school3_flip at left with renpy.transition(dissolve, layer="master")
Cameron "Who did you hear it from?"

#(smiles)
hide Diana_happy_school3 at center with renpy.transition(dissolve, layer="master")
show Diana_laugh_school3 at center with renpy.transition(dissolve, layer="master")
Diana "The teachers. I was passin' by the faculty room and they sounded kinda excited for some reason."

#(confused)
hide Cameron_normal_school3_flip at left with renpy.transition(dissolve, layer="master")
show Cameron_sad_school3_flip at left with renpy.transition(dissolve, layer="master")
Cameron "Hm. I wonder why."

#(shrugs)
voice "voice/Diana_dunno.mp3"
hide Diana_laugh_school3 at center with renpy.transition(dissolve, layer="master")
show Diana_normal_school1 at center with renpy.transition(dissolve, layer="master")
Diana "Dunno. Maybe she's really smart or somethin'."

#(School bell sound effect. Hide the characters.)
play sound "sound/243437__jm-studios__schoolbell-from-german-high-school.mp3"
hide Cameron_sad_school3_flip at left with renpy.transition(dissolve, layer="master")
hide Diana_normal_school1 at center with renpy.transition(dissolve, layer="master")
"The morning bell sounds, marking the beginning of the first class. Everyone takes their seats as the teacher steps inside."

#(Mr. Norton appears with a smile.)
voice "voice/MrNorton_hey_folks.mp3"
show MrNorton_laugh_casual1 at center with renpy.transition(dissolve, layer="master")
Norton "Mornin', class! We gotta transfer student from Sylphyr who'll be joinin' us today."

"Now that the rumors are confirmed, people seem surprised that the transfer would be coming to this class. Nearly everyone's attention is directed at the door, curious to meet the new face."

#(normal)
voice "voice/MrNotron_lemme_say_somethin.mp3"
hide MrNorton_laugh_casual1 at center with renpy.transition(dissolve, layer="master")
show MrNorton_normal_casual1 at center with renpy.transition(dissolve, layer="master")
Norton "Go on and introduce yourself."

#(Elisabeth appears with a smile. End classroom music and play classy music.)
stop music fadeout 1.0
play music "Music/05 ivory flower.mp3"
show Elisabeth_normal_school2 at right with renpy.transition(easeinright, layer="master")
"A girl with blonde hair stands in front of the class, only to find the stunned reactions on their faces."

#(normal)
voice "voice/Elisabeth_greetings.mp3"
hide Elisabeth_normal_school2 at right with renpy.transition(dissolve, layer="master")
show Elisabeth_happy_school3 at right with renpy.transition(dissolve, layer="master")
Elisabeth "Greetings, everyone. My name is Elisabeth Rhodes, and it is certainly a pleasure to meet you all."

play sound "sound/444163__cloe-king__clapping.mp3"
"The class cheers with excitement as they couldn't believe that Elisabeth Rhodes; the famous singer from Sylphyr is joining them as a fellow classmate."

"Despite Elisabeth already introducing herself, Diana still gazes on with disbelief, like she could be mixing her up with someone else. It's just too good to be true."

stop sound fadeout 1.0

#(surprised)
voice "voice/Diana_gasps.mp3"
show Diana_surprised_school1_flip at midleft with renpy.transition(dissolve, layer="master")
Diana "Is this...a dream?"

#(Elisabeth looks surprised.)
hide Elisabeth_happy_school3 at right with renpy.transition(dissolve, layer="master")
show Elisabeth_surprised_school2 at right with renpy.transition(dissolve, layer="master")
"Taken back by the coincidence, Elisabeth recognizes Diana and seems equally surprised. The chances of meeting each other again were so slim."

#(Elisabeth smiles.)
hide Elisabeth_surprised_school2 at right with renpy.transition(dissolve, layer="master")
show Elisabeth_happy_school2 at right with renpy.transition(dissolve, layer="master")
"She waves back to Diana in a way that is perfectly identical to how she bids her fans farewell after a concert. Without a doubt, it's her."

#(Diana appears excited.)
voice "voice/Diana_light_laughter.mp3"
hide Diana_surprised_school1_flip at midleft with renpy.transition(dissolve, layer="master")
show Diana_laugh_school2_flip at midleft with renpy.transition(dissolve, layer="master")
Diana "She's the real deal! Oh my goodness! This is the best day of my life!!!"

#(Cameron appears surprised.)
voice "voice/Cameron_incredible.mp3"
show Cameron_surprised_school2_flip at farleft with renpy.transition(easeinleft, layer="master")
Cameron "So that's why the teachers were so excited..."

#(chuckles)
voice "voice/MrNorton_laughs.mp3"
hide MrNorton_normal_casual1 at center with renpy.transition(dissolve, layer="master")
show MrNorton_laugh_casual1 at center with renpy.transition(dissolve, layer="master")
Norton "I know. I know. Elisabeth is famous and all, but she's still a classmate. Save all the fanboy, fangirl, fan-whatever business for later."

#(nervous smile)
voice "voice/Elisabeth_my_my.mp3"
hide Elisabeth_happy_school2 at right with renpy.transition(dissolve, layer="master")
show Elisabeth_nervous_school1 at right with renpy.transition(dissolve, layer="master")
Elisabeth "It appears an introduction is unnecessary."

#(proud)
voice "voice/MrNorton_oh_yeah.mp3"
hide MrNorton_laugh_casual1 at center with renpy.transition(dissolve, layer="master")
show MrNorton_normal_casual2 at center with renpy.transition(dissolve, layer="master")
Norton "In that case, I'll just talk 'bout myself!"

#(serious)
voice "voice/Diana_hey.mp3"
hide Diana_laugh_school2_flip at midleft with renpy.transition(dissolve, layer="master")
show Diana_serious_school3_flip at midleft with renpy.transition(dissolve, layer="master")
Diana "Boo! Nobody wants to know ya, Mr. Norton!"

#(normal)
hide MrNorton_normal_casual2 at center with renpy.transition(dissolve, layer="master")
show MrNorton_laugh_casual1 at center with renpy.transition(dissolve, layer="master")
Norton "Ya see, I wasn't exactly from around here either. Spent many years sailin' the seas and carryin' out missions on the good ol' S.S. Newport!"

#(surprised)
voice "voice/Elisabeth_how_wonderful.mp3"
hide Elisabeth_nervous_school1 at right with renpy.transition(dissolve, layer="master")
show Elisabeth_surprised_school2 at right with renpy.transition(dissolve, layer="master")
Elisabeth "You were a sailor? That's fascinating!"

#(nervous smile)
hide Cameron_surprised_school2_flip at farleft with renpy.transition(dissolve, layer="master")
show Cameron_nervous_school3_flip at farleft with renpy.transition(dissolve, layer="master")
Cameron "Annndd...there goes the spotlight."

#(grins)
hide MrNorton_laugh_casual1 at center with renpy.transition(dissolve, layer="master")
show MrNorton_normal_casual2_flip at center with renpy.transition(dissolve, layer="master")
Norton "Heh. I've been to all sorts of places, but there's somethin' special about this town. I'll tell ya that."

#(normal)
hide Elisabeth_surprised_school2 at right with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_school3 at right with renpy.transition(dissolve, layer="master")
Elisabeth "Have you been to Sylphyr?"

#(laughs)
voice "voice/MrNorton_you_bet.mp3"
hide MrNorton_normal_casual2_flip at center with renpy.transition(dissolve, layer="master")
show MrNorton_laugh_casual1_flip at center with renpy.transition(dissolve, layer="master")
Norton "You bet! I've been everywhere, Goldie."

#(confused)
voice "voice/Elisabeth_pardon.mp3"
hide Elisabeth_normal_school3 at right with renpy.transition(dissolve, layer="master")
show Elisabeth_sad_school2 at right with renpy.transition(dissolve, layer="master")
Elisabeth "Goldie?"

#(normal)
hide MrNorton_laugh_casual1_flip at center with renpy.transition(dissolve, layer="master")
show MrNorton_normal_casual2_flip at center with renpy.transition(dissolve, layer="master")
Norton "Yeah, that's your very own nickname! Ya like?"

#(nervous smile)
voice "voice/Elisabeth_well.mp3"
hide Elisabeth_sad_school2 at right with renpy.transition(dissolve, layer="master")
show Elisabeth_nervous_school1 at right with renpy.transition(dissolve, layer="master")
Elisabeth "Well..."

#(smiles)
voice "voice/MrNorton_laughs.mp3"
hide MrNorton_normal_casual2_flip at center with renpy.transition(dissolve, layer="master")
show MrNorton_laugh_casual1 at center with renpy.transition(dissolve, layer="master")
Norton "But man! With all of us shipmates bunched up together, it can get freakin' hot in there! Would've traded anythin' for some air!"

#(normal)
voice "voice/Cameron_hey.mp3"
hide Cameron_nervous_school3_flip at farleft with renpy.transition(dissolve, layer="master")
show Cameron_normal_school3_flip at farleft with renpy.transition(dissolve, layer="master")
Cameron "Now that you've mentioned it, is that why you never wear a suit like the other teachers?"

#(laughs)
hide MrNorton_laugh_casual1 at center with renpy.transition(dissolve, layer="master")
show MrNorton_laugh_casual2 at center with renpy.transition(dissolve, layer="master")
Norton "Haha! Right on the money, Karate Kid! Ya sure don't wanna see me sweat!"

#(excited)
hide Diana_serious_school3_flip at midleft with renpy.transition(dissolve, layer="master")
show Diana_grin_school1_flip at midleft with renpy.transition(dissolve, layer="master")
Diana "(Maybe if he keeps this up, we'll stall out the clock!)"

#(realizes)
voice "voice/MrNorton_almost_forgot.mp3"
hide MrNorton_laugh_casual2 at center with renpy.transition(dissolve, layer="master")
show MrNorton_surprised_casual1 at center with renpy.transition(dissolve, layer="master")
Norton "Oh! Almost forgot, but I got a class to teach!"

#(nervous smile)
hide Diana_grin_school1_flip at midleft with renpy.transition(dissolve, layer="master")
show Diana_nervous_school1_flip at midleft with renpy.transition(dissolve, layer="master")
Diana "(Never mind...)"

#(normal)
hide MrNorton_surprised_casual1 at center with renpy.transition(dissolve, layer="master")
show MrNorton_normal_casual1 at center with renpy.transition(dissolve, layer="master")
Norton "There's a seat over there, Goldie."

#(Hide Elisabeth.)
hide Elisabeth_nervous_school1 at right with renpy.transition(easeoutright, layer="master")
"With all eyes still on her, Elisabeth strolls down a few rows towards the empty seat by the corner."

#(smiles)
hide MrNorton_normal_casual1 at center with renpy.transition(dissolve, layer="master")
show MrNorton_normal_casual2 at center with renpy.transition(dissolve, layer="master")
Norton "Open up your history books, folks. It's time...to go back in time!"

#(Hide Cameron.)
hide Cameron_normal_school3_flip at farleft with renpy.transition(dissolve, layer="master")

#(chuckles)
voice "voice/Diana_light_laughter.mp3"
hide Diana_nervous_school1_flip at midleft with renpy.transition(dissolve, layer="master")
show Diana_laugh_school2_flip at midleft with renpy.transition(dissolve, layer="master")
Diana "Wow. That was kinda lame, Mr. Norton."

voice "voice/MrNorton_laughs.mp3"
hide MrNorton_normal_casual2 at center with renpy.transition(dissolve, layer="master")
show MrNorton_laugh_casual2 at center with renpy.transition(dissolve, layer="master")
Norton "Thanks for volunteerin', Chatterbox! Go ahead and start us off on page 64."

#(shocked)
voice "voice/Diana_hey.mp3"
hide Diana_laugh_school2_flip at midleft with renpy.transition(dissolve, layer="master")
show Diana_surprised_school1_flip at midleft with renpy.transition(dissolve, layer="master")
Diana "What?!"

#(normal)
voice "voice/MrNorton_who_do you_think_I_am.mp3"
hide MrNorton_laugh_casual2 at center
show MrNorton_serious_casual1 at center with renpy.transition(dissolve, layer="master")
Norton "Page 64."

#(sad)
voice "voice/Diana_sorry_bout_that.mp3"
hide Diana_surprised_school1_flip at midleft with renpy.transition(dissolve, layer="master")
show Diana_sad_school3_flip at midleft with renpy.transition(dissolve, layer="master")
Diana "Wish I could go back in time..."

#(End classy music. Fade to the scene after class. School bell sound effect.)
stop music fadeout 1.0
scene classroom_day with fadehold
play music "Music/11 aquamarine skies.mp3"
play sound "sound/243437__jm-studios__schoolbell-from-german-high-school.mp3"

"After a more tense lesson than normal, class finally concludes for the day. However, no one is rushing out the doors like they usually do, which is a rare sight."

#(Play classroom music. Mr. Norton appears.)
voice "voice/MrNorton_hey_folks.mp3"
show MrNorton_normal_casual1_flip at midleft with renpy.transition(dissolve, layer="master")
Norton "That's it for today, folks. Also, could someone show Elisabeth around before the next class?"

#(Diana appears excited.)
voice "voice/Diana_oh.mp3"
show Diana_laugh_school2_flip at farleft with renpy.transition(easeinleft, layer="master")
Diana "I'll do it, Mr. Norton!"

#(Mr. Norton looks focused.)
hide MrNorton_normal_casual1_flip at midleft with renpy.transition(dissolve, layer="master")
show MrNorton_serious_casual2_flip at midleft with renpy.transition(dissolve, layer="master")
"Several other students desperately volunteer as well, but Mr. Norton is looking elsewhere."

"After scanning the lively room, he spots a bookworm reading alone at his desk - someone who couldn't care less about helping some new student. He's the perfect target."

#(normal)
hide MrNorton_serious_casual2_flip at midleft with renpy.transition(dissolve, layer="master")
show MrNorton_normal_casual2_flip at midleft with renpy.transition(dissolve, layer="master")
Norton "Romeo, I got a mission for you."

#(End classroom music. Play scholarly music. Robin appears stoic.)
stop music fadeout 1.0
play music "Music/04 march of the waves.mp3"
show Robin_stoic_school1 at midright with renpy.transition(dissolve, layer="master")
Robin "..."

voice "voice/MrNorton_whats goin_on.mp3"
hide MrNorton_normal_casual2_flip at midleft with renpy.transition(dissolve, layer="master")
show MrNorton_serious_casual2_flip at midleft with renpy.transition(dissolve, layer="master")
Norton "Earth to Romeo."

#(glares)
voice "voice/Robin_no.mp3"
hide Robin_stoic_school1 at midright with renpy.transition(dissolve, layer="master")
show Robin_serious_school2 at midright with renpy.transition(dissolve, layer="master")
Robin "Could you stop calling me that? My name isn't Romeo."

#(smiles)
voice "voice/MrNorton_you_bet.mp3"
hide MrNorton_serious_casual2_flip at midleft with renpy.transition(dissolve, layer="master")
show MrNorton_normal_casual2_flip at midleft with renpy.transition(dissolve, layer="master")
Norton "Sure, it is! Anyway, show the new girl around, would ya?"

#(shocked)
voice "voice/Diana_gasps.mp3"
hide Diana_laugh_school2_flip at farleft with renpy.transition(dissolve, layer="master")
show Diana_surprised_school1_flip at farleft with renpy.transition(dissolve, layer="master")
Diana "What?! Why Four-Eyes of all people? He barely talks to anyone."

hide MrNorton_normal_casual2_flip at midleft with renpy.transition(dissolve, layer="master")
show MrNorton_normal_casual2_flip at midleft with renpy.transition(dissolve, layer="master")
"With Mr. Norton's overwhelming presence before him, Robin twitches. He knows all too well there's no escape once his teacher's mind is made up."

#(sighs)
hide Robin_serious_school2 at midright with renpy.transition(dissolve, layer="master")
show Robin_serious_school1 at midright with renpy.transition(dissolve, layer="master")
Robin "Fine..."

#(smiles)
voice "voice/MrNotron_see_ya_around.mp3"
hide MrNorton_normal_casual2_flip at midleft with renpy.transition(dissolve, layer="master")
show MrNorton_laugh_casual1_flip at midleft with renpy.transition(dissolve, layer="master")
Norton "Attaboy! I'll leave her to you."

#(Elisabeth appears concerned.)
voice "voice/Elisabeth_forgive_me.mp3"
show Elisabeth_sad_school2 at farright with renpy.transition(easeinright, layer="master")
Elisabeth "If it is too much of a hassle, I will not require any assistance."

#(normal)
voice "voice/MrNorton_dont_worry_about_that.mp3"
hide MrNorton_laugh_casual1_flip at midleft with renpy.transition(dissolve, layer="master")
show MrNorton_normal_casual2_flip at midleft with renpy.transition(dissolve, layer="master")
Norton "Aw, no need to be shy. You two will get along just fine."

#(Robin's expression is stoic, while Elisabeth is smiling.)
hide Elisabeth_sad_school2 at farright with renpy.transition(easeinright, layer="master")
show Elisabeth_normal_school2 at farright with renpy.transition(dissolve, layer="master")
"As Robin reluctantly closes his book, Elisabeth greets him with a smile. That sight alone is enough to make any boy fall head over heels for her, but he doesn't waver."

voice "voice/Elisabeth_if_you_dont_mind.mp3"
hide Elisabeth_normal_school2 at farright with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_school3 at farright with renpy.transition(dissolve, layer="master")
Elisabeth "It appears I have an appointment with you."

voice "voice/Robin_whatever.mp3"
hide Robin_serious_school1 at midright with renpy.transition(dissolve, layer="master")
show Robin_stoic_school2 at midright with renpy.transition(dissolve, layer="master")
Robin "Sounds like it."

#(Robin and Elisabeth leave.)
hide Elisabeth_normal_school3 at farright with renpy.transition(easeoutright, layer="master")
hide Robin_stoic_school2 at midright with renpy.transition(easeoutright, layer="master")
"The two of them begin their school tour, leaving the rest of the class frustrated and disappointed."

#(Cameron appears curious.)
voice "voice/Cameron_hey.mp3"
show Cameron_serious_school3 at right with renpy.transition(easeinright, layer="master")
Cameron "What are you trying to pull, Mr. Norton?"

#(smiles)
hide MrNorton_normal_casual2_flip at midleft with renpy.transition(dissolve, layer="master")
show MrNorton_laugh_casual1_flip at midleft with renpy.transition(dissolve, layer="master")
Norton "Now, kids. Romeo hardly talks to anyone and the girl is new here, so I just want to make sure we all get along."

#(doubtful)
voice "voice/Cameron_really.mp3"
hide Cameron_serious_school3 at right with renpy.transition(dissolve, layer="master")
show Cameron_normal_school3 at right with renpy.transition(dissolve, layer="master")
Cameron "Really? That looked more like a set up."

#(laughs)
voice "voice/MrNorton_laughs.mp3"
hide MrNorton_laugh_casual1_flip at midleft with renpy.transition(dissolve, layer="master")
show MrNorton_laugh_casual2_flip at midleft with renpy.transition(dissolve, layer="master")
Norton "I've got no idea what you're talkin' about."

#(upset)
voice "voice/Diana_I_dont_believe_it.mp3"
hide Diana_surprised_school1_flip at farleft with renpy.transition(dissolve, layer="master")
show Diana_sad_school1_flip at farleft with renpy.transition(dissolve, layer="master")
Diana "But I wanted to interview her and stuff..."

#(chuckles)
voice "voice/Cameron_light_laughter.mp3"
hide Cameron_normal_school3 at right with renpy.transition(dissolve, layer="master")
show Cameron_laugh_school2 at right with renpy.transition(dissolve, layer="master")
Cameron "Come on, Diana. We all know you just wanted to stall through the next class."

#(nervous smile)
voice "voice/Diana_well.mp3"
hide Diana_sad_school1_flip at farleft with renpy.transition(dissolve, layer="master")
show Diana_nervous_school3_flip at farleft with renpy.transition(dissolve, layer="master")
Diana "I've got no idea what you're talkin' about..."

#(End scholarly music.)
stop music fadeout 1.0

#INT. Hallway - Morning
scene hallway_day with renpy.transition(dissolve, layer="master")

#(Play classroom music.)
play music "Music/11 aquamarine skies.mp3"

"With several students watching from the windows, Robin seems more anxious than ever to finish the tour. He's clearly not comfortable with this much attention."

#(Robin and Elisabeth appear. Robin seems annoyed.)
show Elisabeth_normal_school2_flip at left with renpy.transition(dissolve, layer="master")
show Robin_stoic_school1 at center with renpy.transition(dissolve, layer="master")
Robin "Let's just get this over with."

#(apologetic)
voice "voice/Elisabeth_forgive_me.mp3"
hide Elisabeth_normal_school2_flip at left with renpy.transition(dissolve, layer="master")
show Elisabeth_sad_school3_flip at left with renpy.transition(dissolve, layer="master")
Elisabeth "Allow me to apologize for interrupting your reading. You appeared to be enjoying that book."

#(shrugs)
voice "voice/Robin_whatever.mp3"
hide Robin_stoic_school1 at center with renpy.transition(dissolve, layer="master")
show Robin_stoic_school2 at center with renpy.transition(dissolve, layer="master")
Robin "It's fine. Mr. Norton is just doing whatever he wants. Can't do much about it."

#(smiles)
voice "voice/Elisabeth_my_my.mp3"
hide Elisabeth_sad_school3_flip at left with renpy.transition(dissolve, layer="master")
show Elisabeth_happy_school3_flip at left with renpy.transition(dissolve, layer="master")
Elisabeth "He certainly is an amusing teacher. I have yet to meet one as charismatic as him."

#(normal)
hide Robin_stoic_school2 at center with renpy.transition(dissolve, layer="master")
show Robin_normal_school1 at center with renpy.transition(dissolve, layer="master")
Robin "I guess. Well, you made a pretty big commotion today."

#(nervous smile)
voice "voice/Elisabeth_well.mp3"
hide Elisabeth_happy_school3_flip at left with renpy.transition(dissolve, layer="master")
show Elisabeth_nervous_school2_flip at left with renpy.transition(dissolve, layer="master")
Elisabeth "It appears so. I was rather surprised to learn that I am also well-known in Aquadine."

#(curious)
voice "voice/Robin_hm.mp3"
hide Robin_normal_school1 at center with renpy.transition(dissolve, layer="master")
show Robin_stoic_school1 at center with renpy.transition(dissolve, layer="master")
Robin "What do you do?"

#(surprised)
voice "voice/Elisabeth_pardon.mp3"
hide Elisabeth_nervous_school2_flip at left with renpy.transition(dissolve, layer="master")
show Elisabeth_surprised_school1_flip at left with renpy.transition(dissolve, layer="master")
Elisabeth "You...really do not know who I am?"

#(stoic)
voice "voice/Robin_no.mp3"
hide Robin_stoic_school1 at center with renpy.transition(dissolve, layer="master")
show Robin_stoic_school2 at center with renpy.transition(dissolve, layer="master")
Robin "Nope. Just some blonde girl who transferred in this morning."

#(smiles)
hide Elisabeth_surprised_school1_flip at left with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_school3_flip at left with renpy.transition(dissolve, layer="master")
Elisabeth "A blunt choice of words. But, as you know now, I am Elisabeth Rhodes - a famous concert singer from Sylphyr."

#(curious)
hide Robin_stoic_school2 at center with renpy.transition(dissolve, layer="master")
show Robin_surprised_school1 at center with renpy.transition(dissolve, layer="master")
Robin "A singer, huh? You plan on performing here, too?"

#(solemn)
voice "voice/Elisabeth_you_see.mp3"
hide Elisabeth_normal_school3_flip at left with renpy.transition(dissolve, layer="master")
show Elisabeth_sad_school2_flip at left with renpy.transition(dissolve, layer="master")
Elisabeth "I recently moved to Aquadine due to my father's business, so I am uncertain at the moment."

#(normal)
hide Robin_surprised_school1 at center with renpy.transition(dissolve, layer="master")
show Robin_stoic_school1 at center with renpy.transition(dissolve, layer="master")
Robin "Even if that's the reason why you moved, you could still perform here if you wanted. There are several opera houses here."

#(nervous smile)
voice "voice/Elisabeth_if_you_dont_mind.mp3"
hide Elisabeth_sad_school2_flip at left with renpy.transition(dissolve, layer="master")
show Elisabeth_nervous_school2_flip at left with renpy.transition(dissolve, layer="master")
Elisabeth "I have...actually taken a break from my career. Let us move on, shall we?"

#(Elisabeth leaves.)
hide Elisabeth_nervous_school2_flip at left with renpy.transition(easeoutleft, layer="master")
"Elisabeth walks on ahead, leaving Robin a bit surprised by her reaction. However, his demeanor reverts the moment she makes a wrong turn."

#(stoic)
hide Robin_stoic_school1 at center with renpy.transition(dissolve, layer="master")
show Robin_normal_school1 at center with renpy.transition(dissolve, layer="master")
Robin "Do you even know where you're going?"

#(Elisabeth appears embarrassed.)
voice "voice/Elisabeth_how_embarrassing.mp3"
show Elisabeth_embarrassed_school1_flip at left with renpy.transition(easeinleft, layer="master")
Elisabeth "Pardon, but would you be so kind to guide me?"

#(shrugs)
hide Robin_normal_school1 at center with renpy.transition(dissolve, layer="master")
show Robin_normal_school2 at center with renpy.transition(dissolve, layer="master")
Robin "That's why I'm here."

#INT. Cafeteria - Morning
scene cafeteria_day with fadehold

"After a brief tour around the school, Robin and Elisabeth enter the cafeteria. Other than the lunch ladies getting things ready, it's pretty much empty."

#(Robin and Elisabeth appear. Robin's expression is stoic.)
show Elisabeth_normal_school2_flip at left with renpy.transition(dissolve, layer="master")
show Robin_stoic_school3 at center with renpy.transition(dissolve, layer="master")
Robin "And finally, here's the cafeteria."

#(excited)
voice "voice/Elisabeth_my_my.mp3"
hide Elisabeth_normal_school2_flip at left with renpy.transition(dissolve, layer="master")
show Elisabeth_happy_school3_flip at left with renpy.transition(dissolve, layer="master")
Elisabeth "Oh, I am anxious to try out your menu! Do you enjoy sharing meals here with your friends?"

#(shrugs)
voice "voice/Robin_later.mp3"
hide Robin_stoic_school3 at center with renpy.transition(dissolve, layer="master")
show Robin_stoic_school1 at center with renpy.transition(dissolve, layer="master")
Robin "Uh, sure. Anyway, I guess that's that."

#(Robin leaves.)
hide Robin_stoic_school1 at center with renpy.transition(easeoutright, layer="master")

"Without much further ado, Robin starts walking. It's painfully clear he doesn't want to waste another minute of his time."

#(surprised)
voice "voice/Elisabeth_one_moment.mp3"
hide Elisabeth_happy_school3_flip at left with renpy.transition(dissolve, layer="master")
show Elisabeth_surprised_school1_flip at left with renpy.transition(dissolve, layer="master")
Elisabeth "One moment!"

#(Robin appears annoyed.)
show Robin_serious_school1 at midright with renpy.transition(easeinright, layer="master")
Robin "(Huh? What does she want now?)"

#(normal)
voice "voice/Elisabeth_you_see.mp3"
hide Elisabeth_surprised_school1_flip at left with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_school2_flip at left with renpy.transition(dissolve, layer="master")
Elisabeth "I wish to thank you for showing me around. To be honest, I was nervous after learning that I would be transferring schools."

#(doubtful)
voice "voice/Robin_really.mp3"
hide Robin_serious_school1 at midright with renpy.transition(dissolve, layer="master")
show Robin_stoic_school1 at midright with renpy.transition(dissolve, layer="master")
Robin "Nervous? Aren't you an idol or something?"

#(nervous smile)
hide Elisabeth_normal_school2_flip at left with renpy.transition(dissolve, layer="master")
show Elisabeth_nervous_school3_flip at left with renpy.transition(dissolve, layer="master")
Elisabeth "You are correct. It does seem ironic for me to say something strange like that..."

#(stoic)
hide Robin_stoic_school1 at midright with renpy.transition(dissolve, layer="master")
show Robin_normal_school1 at midright with renpy.transition(dissolve, layer="master")
Robin "You're weird."

#(laughs)
voice "voice/Elisabeth_forgive_me.mp3"
Elisabeth "You may be right. Forgive me."

#(curious)
hide Robin_normal_school1 at midright with renpy.transition(dissolve, layer="master")
show Robin_stoic_school1 at midright with renpy.transition(dissolve, layer="master")
Robin "Do you miss your hometown?"

#(solemn)
hide Elisabeth_nervous_school3_flip at left with renpy.transition(dissolve, layer="master")
show Elisabeth_sad_school2_flip at left with renpy.transition(dissolve, layer="master")
Elisabeth "Well, I've lived my whole life in Sylphyr. Perhaps I require some time to grow accustomed to these changes."

#(smiles)
voice "voice/Elisabeth_you_are_too_kind.mp3"
hide Elisabeth_sad_school2_flip at left with renpy.transition(dissolve, layer="master")
show Elisabeth_happy_school2_flip at left with renpy.transition(dissolve, layer="master")
Elisabeth "Thank you again for your time. I shall take my leave now."

#(normal)
voice "voice/Robin_as_a_matter.mp3"
hide Robin_stoic_school1 at midright with renpy.transition(dissolve, layer="master")
show Robin_surprised_school2 at midright with renpy.transition(dissolve, layer="master")
Robin "Actually...there's one more place I haven't shown you."

#(curious)
hide Elisabeth_happy_school2_flip at left with renpy.transition(dissolve, layer="master")
show Elisabeth_surprised_school1_flip at left with renpy.transition(dissolve, layer="master")
Elisabeth "Oh? And where would that be?"

hide Robin_surprised_school2 at midright with renpy.transition(dissolve, layer="master")
show Robin_stoic_school1 at midright with renpy.transition(dissolve, layer="master")
Robin "Just follow me."

#(End classroom music. Screen is black. Footsteps sound effect.)
stop music fadeout 1.0
scene black with fadehold
play sound "sound/365412__rutgermuller__japan-matsudo-hotel-stairwell-footsteps.mp3"
"A few footsteps echo through the barren stairway before they reach the top floor. With Elisabeth following behind him, Robin reaches for the door and opens it."

#(Door opening sound effect.)
stop sound fadeout 1.0
play sound "sound/15419__pagancow__dorm-door-opening.mp3"
"After shielding their eyes from the overwhelming sunlight, they could nearly see the entire ocean from the rooftop."

#EXT. School Rooftop - Day
scene rooftop_day with fadehold

#(Play relaxing gondola music. Robin and Elisabeth appear. Elisabeth looks surprised.)
play music "Music/09 waves in the blue.mp3"

voice "voice/Elisabeth_how_wonderful.mp3"
show Elisabeth_surprised_school2_flip at left with renpy.transition(dissolve, layer="master")
show Robin_stoic_school1 at center with renpy.transition(dissolve, layer="master")
Elisabeth "Beautiful... You can see so much of the town from up here."

hide Robin_stoic_school1 at center with renpy.transition(dissolve, layer="master")
show Robin_stoic_school3 at center with renpy.transition(dissolve, layer="master")
Robin "Yeah. The sound of the seagulls chirping over the soothing waves, the smell of the ocean as the cool breeze presses against our faces, and a bird's eye view of the town..."

hide Robin_stoic_school3 at center with renpy.transition(dissolve, layer="master")
show Robin_normal_school1 at center with renpy.transition(dissolve, layer="master")
Robin "This...is my favorite place."

#(giggles)
voice "voice/Elisabeth_my_my.mp3"
hide Elisabeth_surprised_school2_flip at left with renpy.transition(dissolve, layer="master")
show Elisabeth_happy_school3_flip at left with renpy.transition(dissolve, layer="master")
Elisabeth "Really now? I thought you would have said the library."

#(chuckles)
voice "voice/Robin_chuckles.mp3"
hide Robin_normal_school1 at center with renpy.transition(dissolve, layer="master")
show Robin_laugh_school1 at center with renpy.transition(dissolve, layer="master")
Robin "Way to judge someone by his looks, but that's not what I meant."

#(normal)
hide Robin_laugh_school1 at center with renpy.transition(dissolve, layer="master")
show Robin_normal_school3 at center with renpy.transition(dissolve, layer="master")
Robin "This whole town is my favorite place. That's why I can understand how much you miss your home."

#(Elisabeth's expression also returns to normal.)
hide Robin_normal_school3 at center with renpy.transition(dissolve, layer="master")
show Robin_normal_school1 at center with renpy.transition(dissolve, layer="master")
hide Elisabeth_happy_school3_flip at left with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_school2_flip at left with renpy.transition(dissolve, layer="master")
"For a while, neither of them say a word as they continue to savor the scenery in silence."

voice "voice/Robin_hm.mp3"
hide Robin_normal_school1 at center with renpy.transition(dissolve, layer="master")
show Robin_normal_school2 at center with renpy.transition(dissolve, layer="master")
Robin "Since you're already here, you may as well learn what the outside world is like. You can even tell your friends about your experiences in Aquadine whenever you visit them."

#(smiles)
hide Robin_normal_school2 at center with renpy.transition(dissolve, layer="master")
show Robin_happy_school1 at center with renpy.transition(dissolve, layer="master")
Robin "You never know what the future will hold."

hide Elisabeth_normal_school2_flip at left with renpy.transition(dissolve, layer="master")
show Elisabeth_surprised_school2_flip at left with renpy.transition(dissolve, layer="master")
"After getting lost examining the wondrous town from a distance, she looks at Robin, who is smiling for the first time this tour."

#(curious)
voice "voice/Elisabeth_forgive_me.mp3"
hide Elisabeth_surprised_school2_flip at left with renpy.transition(dissolve, layer="master")
show Elisabeth_nervous_school1_flip at left with renpy.transition(dissolve, layer="master")
Elisabeth "What was your name again?"

hide Robin_happy_school1 at center with renpy.transition(dissolve, layer="master")
show Robin_normal_school2 at center with renpy.transition(dissolve, layer="master")
Robin "Robin. Robin Liyun."

#(teases)
hide Elisabeth_nervous_school1_flip at left with renpy.transition(dissolve, layer="master")
show Elisabeth_happy_school3_flip at left with renpy.transition(dissolve, layer="master")
Elisabeth "May I call you 'Mr. Bookworm' instead? I believe that nickname suits you quite well."

#(serious)
voice "voice/Robin_no.mp3"
hide Robin_normal_school2 at center with renpy.transition(dissolve, layer="master")
show Robin_stoic_school1 at center with renpy.transition(dissolve, layer="master")
Robin "'Robin' will do."

#(smiles)
voice "voice/Elisabeth_you_see.mp3"
hide Elisabeth_happy_school3_flip at left with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_school2_flip at left with renpy.transition(dissolve, layer="master")
Elisabeth "You remind me of someone... Someone I met a long time ago."

#(normal)
hide Elisabeth_normal_school2_flip at left with renpy.transition(dissolve, layer="master")
show Elisabeth_happy_school2_flip at left with renpy.transition(dissolve, layer="master")
Elisabeth "Thank you again for guiding me and for sharing this view. I will never forget it."

#(End relaxing gondola music.)
stop music fadeout 1.0

#EXT. Cloud Company - Evening
scene cloud_company_night with fadehold

#(Play a girl's voice singing Ciel's song.)
play sound "sound/Reddevitzer_Hoeft_03.mp3" loop

"After another long tour, Ciel sculls towards the dock and reaches for his rope. He extends his hand to help his passengers off the gondola."

#(Ciel appears with a smile.)
voice "voice/Ciel_thank_you.mp3"
show Robin_happy_uniform2_night at midright with renpy.transition(dissolve, layer="master")
Ciel "Thank you for choosing the Cloud Company. Have a good evening."

play music "Music/22 So Spiragnor -mermaid ver.-.mp3"
hide Robin_happy_uniform2_night at midright with renpy.transition(dissolve, layer="master")
show Robin_stoic_uniform2_night at midright with renpy.transition(dissolve, layer="master")
"Once they go their separate ways, Ciel stretches before grabbing the doorknob. But just as he nearly opens it, he hears a familiar song."

#(shocked)
hide Robin_stoic_uniform2_night at midright with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform2_night at midright with renpy.transition(dissolve, layer="master")
Ciel "(This song. It's...my song. It's faint, but she has a nice voice.)"

#(Himmel is calling Ciel from inside and is off screen.)
voice "voice/Himmel_laughs.mp3"
Himmel "Ciel, did your voice change? You sound like a little girl!"

hide Robin_surprised_uniform2_night at midright with renpy.transition(dissolve, layer="master")
show Robin_sad_uniform2_night at midright with renpy.transition(dissolve, layer="master")
Ciel "No, Grandfather. Someone else is singing my song and I kind of want to follow it."

#(End mermaid song.)
stop music fadeout 1.0
"His response is met with a brief moment of silence. But soon enough, Ciel could hear someone rushing out the door."

#(Himmel appears outside bewildered. Play strange sounding music.)
stop sound fadeout 1.0
play music "Music/13 mischievous hour.mp3"
voice "voice/Himmel_aiya.mp3"
show Himmel_surprised_uniform1_night_flip at midleft with renpy.transition(easeinleft, layer="master")
Himmel "Aiya! What are you doing?! Do you not know about...the sirens?"

voice "voice/Ciel_why_yes.mp3"
hide Robin_sad_uniform2_night at midright with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform2_night at midright with renpy.transition(dissolve, layer="master")
Ciel "Yes, I-"

#(smiles)
voice "voice/Himmel_grandpa_will_speak.mp3"
hide Himmel_surprised_uniform1_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Himmel_laugh_uniform2_night_flip at midleft with renpy.transition(dissolve, layer="master")
Himmel "It's okay! Grandpa will tell you!"

#(serious)
voice "voice/Himmel_long_ago.mp3"
hide Himmel_laugh_uniform2_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Himmel_normal_uniform1_night_flip at midleft with renpy.transition(dissolve, layer="master")
Himmel "*ahem* They are beautiful, yet dangerous creatures who lure sailors towards rocks with their song. Then crash! They all drown."

#(doubtful)
hide Robin_surprised_uniform2_night at midright with renpy.transition(dissolve, layer="master")
show Robin_serious_uniform2_night at midright with renpy.transition(dissolve, layer="master")
Ciel "Isn't that just a myth?"

#(whines)
hide Himmel_normal_uniform1_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Himmel_surprised_uniform2_night_flip at midleft with renpy.transition(dissolve, layer="master")
Himmel "This whole town was built on mythology! You of all people should know that!"

#(shrugs)
hide Robin_serious_uniform2_night at midright with renpy.transition(dissolve, layer="master")
show Robin_stoic_uniform1_night at midright with renpy.transition(dissolve, layer="master")
Ciel "Never said I believed in it."

hide Himmel_surprised_uniform2_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Himmel_nervous_uniform1_night_flip at midleft with renpy.transition(dissolve, layer="master")
Himmel "But you are just a boy! You are too young to die!!!!"

#(nervous smile)
hide Robin_stoic_uniform1_night at midright with renpy.transition(dissolve, layer="master")
show Robin_nervous_uniform2_night at midright with renpy.transition(dissolve, layer="master")
Ciel "I'll...be back in a bit."

#(shrugs)
voice "voice/Himmel_fine.mp3"
hide Himmel_nervous_uniform1_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Himmel_normal_uniform1_night_flip at midleft with renpy.transition(dissolve, layer="master")
Himmel "Fine. But if you are still alive, go buy some groceries. Salmon is 30 percent off today."

#(End strange music.)
stop music fadeout 1.0

#EXT. Shore - Night
scene shore with fadehold

#(Play softer gondola music.)
play music "Music/22 So Spiragnor -mermaid ver.-.mp3"

"The sound of her voice leads Ciel's gondola through a shore he hardly visits. A few ghost-like jellyfish appear around him, but he doesn't seem surprised."

#(Ciel appears chuckling.)
show Robin_happy_uniform2_night_flip at left with renpy.transition(easeinleft, layer="master")
Ciel "(Well, I survived the rocks. So much for the sirens. Grandfather can be really weird sometimes.)"

#(normal)
hide Robin_happy_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
Ciel "(And these jellyfish... I remember seeing them when I was younger. I tried telling people about them, but no one ever believed me.)"

#(ponders)
hide Robin_surprised_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
show Robin_sad_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
Ciel "(I used to think they were part of my imagination or something, but Mother can see them, too. Always wondered why.)"

#(smiles)
voice "voice/Ciel_how_are_you.mp3"
hide Robin_sad_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform1_night_flip at left with renpy.transition(dissolve, layer="master")
Ciel "It's been a while since I've seen you guys. How are you?"

"The jellyfish don't respond."

#(nervous smile)
hide Robin_happy_uniform1_night_flip at left with renpy.transition(dissolve, layer="master")
show Robin_nervous_uniform1_night_flip at left with renpy.transition(dissolve, layer="master")
Ciel "Of course they can't talk."

#(Ciel looks surprised.)
stop music fadeout 1.0
hide Robin_nervous_uniform1_night_flip at left with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
"However, something did change - the girl's singing stopped. Ciel turns towards her direction and his eyes widen; he can't believe his eyes."

#(Transition into CG illustration of the mermaid.)
scene cg_2 with fadehold
play music "Music/03 A World Forgotten.mp3"

#(surprised)
voice "voice/Robin_could_it_be.mp3"
Ciel "A...siren?!"

#(doubtful)
Ciel "(Wait, what am I saying? That's a mermaid.)"

Ciel "..."

#(realizes)
Ciel "A mermaid?!"

"Frightened, the mermaid quickly dives underwater and swims away as fast as she could, leaving Ciel speechless."

#(Sound of splashing water. Transition back to scene. Ciel appears shocked.)
play sound "sound/9508__petenice__splash.mp3"
scene shore with fadehold

show Robin_surprised_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
Ciel "(I don't believe it... Did I really see a mermaid...?)"

#(Hide Ciel.)
hide Robin_surprised_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
"Despite his astonishment, Ciel quickly wanders around the shore to search for clues. He spends about half an hour looking, but comes up short."

#(Ciel appears disappointed.)
voice "voice/Robin_hm.mp3"
hide Robin_surprised_uniform2_night_flip at farleft with renpy.transition(dissolve, layer="master")
show Robin_sad_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
Ciel "Nothing..."

#(Ciel's expression returns to normal.)
hide Robin_sad_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
"The jellyfish linger by, as if they're watching over him. He stares back and cracks a smile."

#(nervous smile)
hide Robin_normal_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
show Robin_nervous_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
Ciel "Heh. I suppose you guys wouldn't have anything to say, would you?"

stop music fadeout 1.0

#EXT. Canal - Night
scene canal_night with fadehold

#(Play softer gondola music.)
play music "Music/10 aria to the stars.mp3"

"Ciel's gondola makes its way back to the canal - a view that looks even more stunning now than during the day."

#(Ciel appears pondering.)
show Robin_sad_uniform2_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "(I know I saw a girl who looked like a mermaid, but was she real? It was dark, so maybe I was seeing things.)"

#(Cameron appears in the restaurant uniform.)
voice "voice/Cameron_hey.mp3"
show Cameron_normal_waiter2_night at midright with renpy.transition(easeinright, layer="master")
Cameron "Hey, Ciel. How've you been?"

#(smiles)
voice "voice/Ciel_hello.mp3"
hide Robin_sad_uniform2_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform2_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "I'm doing fine. Thanks for asking."

#(curious)
hide Cameron_normal_waiter2_night at midright with renpy.transition(dissolve, layer="master")
show Cameron_sad_waiter3_night at midright with renpy.transition(dissolve, layer="master")
Cameron "What are you doing out here so late? I thought your company closed a while ago."

#(normal)
hide Robin_happy_uniform2_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform1_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "It is, but I'm just out on a late scull. What about you?"

#(normal)
hide Cameron_sad_waiter3_night at midright with renpy.transition(dissolve, layer="master")
show Cameron_normal_waiter2_night at midright with renpy.transition(dissolve, layer="master")
Cameron "Just taking out the trash. We're about to close up for the night."

hide Robin_normal_uniform1_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_stoic_uniform2_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "(Cameron works for his family's restaurant whenever they need extra hands. But since they're usually busy, he's almost always helping them out.)"

Ciel "(Young Pizzeria is a highly recommended restaurant for tourists and locals alike, so their success is actually comparable to the Frezner Café.)"

#(curious)
hide Robin_stoic_uniform2_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform1_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "By the way, did you hear someone singing earlier?"

#(ponders)
voice "voice/Cameron_what.mp3"
hide Cameron_normal_waiter2_night at midright with renpy.transition(dissolve, layer="master")
show Cameron_sad_waiter3_night at midright with renpy.transition(dissolve, layer="master")
Cameron "It's kind of noisy in the restaurant, so probably not. Was it you?"

#(normal)
voice "voice/Robin_no.mp3"
hide Robin_surprised_uniform1_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform2_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "No, but it was my song though."

#(grins)
voice "voice/Cameron_light_laughter.mp3"
hide Cameron_sad_waiter3_night at midright with renpy.transition(dissolve, layer="master")
show Cameron_laugh_waiter2_night at midright with renpy.transition(dissolve, layer="master")
Cameron "You mean Torrie's song?"

#(nervous smile)
hide Robin_normal_uniform2_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_nervous_uniform2_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "Right. Torrie's song."

#(concerned)
voice "voice/Cameron_I_was_wondering.mp3"
hide Cameron_laugh_waiter2_night at midright with renpy.transition(dissolve, layer="master")
show Cameron_sad_waiter3_night at midright with renpy.transition(dissolve, layer="master")
Cameron "How is she doing by the way? Do you know?"

#(normal)
hide Robin_nervous_uniform2_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform1_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "From what I've heard, she seems better these days and she's even reading more often."

#(normal)
hide Cameron_sad_waiter3_night at midright with renpy.transition(dissolve, layer="master")
show Cameron_normal_waiter2_night at midright with renpy.transition(dissolve, layer="master")
Cameron "That's good. I heard that she had trouble seeing and walking, so I was worried."

#(concerned)
hide Robin_normal_uniform1_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_stoic_uniform2_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "Yeah, it's an extremely rare disease that the doctors never witnessed before. They're not exactly sure what caused it or how to cure it."

#(solemn)
hide Cameron_normal_waiter2_night at midright with renpy.transition(dissolve, layer="master")
show Cameron_sad_waiter3_night at midright with renpy.transition(dissolve, layer="master")
Cameron "Robin doesn't like talking about it, and I heard that guests other than family weren't allowed."

#(solemn)
voice "voice/Robin_Im_sorry.mp3"
hide Robin_stoic_uniform2_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_sad_uniform2_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "Sorry, but I hope you understand. It'd be overwhelming for her to see so many unexpected visitors."

hide Cameron_sad_waiter3_night at midright with renpy.transition(dissolve, layer="master")
show Cameron_sad_waiter2_night at midright with renpy.transition(dissolve, layer="master")
Cameron "Yeah. Before you came along, she was the most requested gondolier in town. I'm sure there are countless people who are eager to see her."

#(smiles)
hide Robin_sad_uniform2_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform1_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "In any case, I'll talk to Robin. You've known him for a while, so I'm sure we can let you visit."

#(surprised)
voice "voice/Cameron_really.mp3"
hide Cameron_sad_waiter2_night at midright with renpy.transition(dissolve, layer="master")
show Cameron_surprised_waiter3_night at midright with renpy.transition(dissolve, layer="master")
Cameron "Really?! I mean, I hope it's not too much trouble."

#(chuckles)
hide Robin_happy_uniform1_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform2_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "You're fine."

#(smiles)
voice "voice/Cameron_you_have_my_thanks.mp3"
hide Cameron_surprised_waiter3_night at midright with renpy.transition(dissolve, layer="master")
show Cameron_happy_waiter2_night at midright with renpy.transition(dissolve, layer="master")
Cameron "Thanks! I have to get back now, so I'll see you later."

#(Cameron leaves.)
hide Cameron_happy_waiter2_night at midright with renpy.transition(easeoutright, layer="master")
"Cameron returns to the restaurant to finish cleaning up for the night."

#(normal)
Ciel "(Cameron is such a worrywart, but he's a cool guy. Anyway, I better get back before Grandfather starts complaining again.)"

#(End softer gondola music.)
stop music fadeout 1.0

#INT. Torrie's Room, Hospital - Night
scene hospital_night with fadehold

#(Play motherly music.)
play music "Music/16 tranquility.mp3"
"Robin goes to the hospital to pay his mother a visit. With the intention of spending the night, he brought a change of clothes and a toothbrush."

#(Robin and Torrie are present. Robin looks surprised.)
show Robin_surprised_school3_night at center with renpy.transition(dissolve, layer="master")
show Torrie_normal_gown1_night_flip at left with renpy.transition(dissolve, layer="master")
Robin "Mother, you're still up? It's late."

#(smiles)
voice "voice/Torrie_Robin.mp3"
hide Torrie_normal_gown1_night_flip at left with renpy.transition(dissolve, layer="master")
show Torrie_happy_gown2_night_flip at left with renpy.transition(dissolve, layer="master")
Torrie "I had a feeling you'd be stopping by, so I stayed up a little longer."

#(concerned)
voice "voice/Robin_dont_worry.mp3"
hide Robin_surprised_school3_night at center with renpy.transition(dissolve, layer="master")
show Robin_sad_school1_night at center with renpy.transition(dissolve, layer="master")
Robin "You need to get some rest. Don't worry about me."

#(Torrie's expression returns to normal.)
hide Torrie_happy_gown2_night_flip at left with renpy.transition(dissolve, layer="master")
show Torrie_normal_gown1_night_flip at left with renpy.transition(dissolve, layer="master")
"Torrie sets the book to the side and gives Robin her undivided attention."

voice "voice/Torrie_how_are_you.mp3"
Torrie "How was your day?"

#(stoic)
hide Robin_sad_school1_night at center with renpy.transition(dissolve, layer="master")
show Robin_stoic_school2_night at center with renpy.transition(dissolve, layer="master")
Robin "Mostly the same. We had a transfer student though, so Mr. Norton made me show her around."

#(interested)
voice "voice/Torrie_oh.mp3"
hide Torrie_normal_gown1_night_flip at left with renpy.transition(dissolve, layer="master")
show Torrie_curious_gown2_night_flip at left with renpy.transition(dissolve, layer="master")
Torrie "Her? What's her name?"

voice "voice/Ciel_Elisabeth.mp3"
hide Robin_stoic_school2_night at center with renpy.transition(dissolve, layer="master")
show Robin_stoic_school1_night at center with renpy.transition(dissolve, layer="master")
Robin "Elisabeth Rhodes. Do you know her?"

#(surprised)
hide Torrie_curious_gown2_night_flip at left with renpy.transition(dissolve, layer="master")
show Torrie_surprised_gown2_night_flip at left with renpy.transition(dissolve, layer="master")
Torrie "The singer from Sylphyr? That's exciting! Maybe you could be friends."

#(concerned)
hide Robin_stoic_school1_night at center with renpy.transition(dissolve, layer="master")
show Robin_sad_school1_night at center with renpy.transition(dissolve, layer="master")
Robin "With someone like me? She'll find out what everyone thinks of me sooner or later..."

#(End motherly music. Torrie is laughing.)
stop music fadeout 1.0
hide Torrie_surprised_gown2_night_flip at left with renpy.transition(dissolve, layer="master")
show Torrie_happy_gown1_night_flip at left with renpy.transition(dissolve, layer="master")
Torrie "But you two have something in common. After all, I heard that you've been singing lately...Ciel."

hide Robin_sad_school1_night at center with renpy.transition(dissolve, layer="master")
show Robin_surprised_school2_night at center with renpy.transition(dissolve, layer="master")
"The room turns quiet enough that one could faintly hear crickets chirping outside. But after a brief moment, Robin fixes his glasses."

#(serious)
voice "voice/Robin_really.mp3"
hide Robin_surprised_school2_night at center with renpy.transition(dissolve, layer="master")
show Robin_serious_school2_night at center with renpy.transition(dissolve, layer="master")
Robin "How many times do I have to tell you, Mother? Just call me 'Robin'."

#(Play motherly music.)
play music "Music/16 tranquility.mp3"

#(giggles)
voice "voice/Torrie_my_my.mp3"
hide Torrie_happy_gown1_night_flip at left with renpy.transition(dissolve, layer="master")
show Torrie_laugh_gown2_night_flip at left with renpy.transition(dissolve, layer="master")
Torrie "Right, I'm sorry. The nurses just can't stop talking about you."

hide Robin_serious_school2_night at center with renpy.transition(dissolve, layer="master")
show Robin_serious_school1_night at center with renpy.transition(dissolve, layer="master")
Robin "I hope you didn't tell them about me."

#(smiles)
voice "voice/Torrie_dont_worry.mp3"
hide Torrie_laugh_gown2_night_flip at left with renpy.transition(dissolve, layer="master")
show Torrie_happy_gown2_night_flip at left with renpy.transition(dissolve, layer="master")
Torrie "Don't worry. I didn't say a word."

#(concerned)
hide Robin_serious_school1_night at center with renpy.transition(dissolve, layer="master")
show Robin_sad_school3_night at center with renpy.transition(dissolve, layer="master")
Robin "Anyway, how are you feeling? Did Dr. Wudman say anything?"

#(solemn)
voice "voice/Torrie_well.mp3"
hide Torrie_happy_gown2_night_flip at left with renpy.transition(dissolve, layer="master")
show Torrie_sad_gown1_night_flip at left with renpy.transition(dissolve, layer="master")
Torrie "My condition worsened a little, but I'm still doing okay."

#(solemn)
hide Robin_sad_school3_night at center with renpy.transition(dissolve, layer="master")
show Robin_sad_school1_night at center with renpy.transition(dissolve, layer="master")
Robin "I see... Hopefully, everything works out."

#(smiles)
hide Torrie_sad_gown1_night_flip at left with renpy.transition(dissolve, layer="master")
show Torrie_happy_gown2_night_flip at left with renpy.transition(dissolve, layer="master")
Torrie "When I get better, we can go sculling together. I'm excited to see how much you've improved."

#(normal)
hide Robin_sad_school1_night at center with renpy.transition(dissolve, layer="master")
show Robin_normal_school1_night at center with renpy.transition(dissolve, layer="master")
Robin "Yeah, it's been so long since I've seen you with the oar. Brings back memories."

#(normal)
hide Torrie_happy_gown2_night_flip at left with renpy.transition(dissolve, layer="master")
show Torrie_normal_gown2_night_flip at left with renpy.transition(dissolve, layer="master")
Torrie "Do you remember those fresh pretzels we used to eat by that dock? We used to go there almost every weekend."

#(realizes)
voice "voice/Robin_interesting.mp3"
hide Robin_normal_school1_night at center with renpy.transition(dissolve, layer="master")
show Robin_grin_school2_night at center with renpy.transition(dissolve, layer="master")
Robin "Those were so good, especially when you dip them in warm cheese! And the smell of the butter would just lure people in."

#(smiles)
hide Robin_grin_school2_night at center with renpy.transition(dissolve, layer="master")
show Robin_happy_school1_night at center with renpy.transition(dissolve, layer="master")
Robin "There's a family that sells them near the floating market. I'll bring some when I come back."

#(normal)
hide Torrie_normal_gown2_night_flip at left with renpy.transition(dissolve, layer="master")
show Torrie_normal_gown1_night_flip at left with renpy.transition(dissolve, layer="master")
Torrie "It's okay. You don't have to."

#(surprised)
voice "voice/Robin_what.mp3"
hide Robin_happy_school1_night at center with renpy.transition(dissolve, layer="master")
show Robin_sad_school2_night at center with renpy.transition(dissolve, layer="master")
Robin "How come? I thought you liked them, too."

#(smiles)
voice "voice/Torrie_I_love_you.mp3"
hide Torrie_normal_gown1_night_flip at left with renpy.transition(dissolve, layer="master")
show Torrie_happy_gown2_night_flip at left with renpy.transition(dissolve, layer="master")
Torrie "We'll go together next time, okay?"

#(normal)
hide Robin_sad_school2_night at center with renpy.transition(dissolve, layer="master")
show Robin_normal_school1_night at center with renpy.transition(dissolve, layer="master")
Robin "Okay."

#(End motherly music. Fade to pitch black with white words appearing to convey sleep.)
stop music fadeout 1.0
scene black with fadehold
play sound "sound/365412__rutgermuller__japan-matsudo-hotel-stairwell-footsteps.mp3"
"It's past midnight and Robin spends the night in his mother's hospital room, resting over the couch."

#(troubled)
Robin "(I don't know how much longer it'll take before I can pay off all of these bills, but I'll keep working for her sake. And that mermaid... That was a mermaid, right?)"

"Robin tilts his head and gazes over the moon by the window. His eyes can't stay open for much longer and he soon falls asleep."

stop sound fadeout 1.0

#EXT. Ancient Aquadine - Day
scene ancient_aquadine_day with fadehold

#(Play new world music.)
play music "Music/03 a world forgotten.mp3"

"As Ciel slowly opens his eyes, he finds himself immersed in the deep blue ocean. His fingers reach out towards the radiant sunlight that glimmers over the surface."

#(Ciel appears stoic.)
show Robin_stoic_uniform4_night at center with renpy.transition(dissolve, layer="master")
Ciel "(Where am I?)"

#(surprised)
hide Robin_stoic_uniform4_night at center with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform4_night at center with renpy.transition(dissolve, layer="master")
Ciel "(Wait... Am I breathing underwater?)"

"Schools of fish wander past him, directing his gaze towards a massive chunk of stone."

#(suspicious)
hide Robin_surprised_uniform4_night at center with renpy.transition(dissolve, layer="master")
show Robin_stoic_uniform3_night at center with renpy.transition(dissolve, layer="master")
Ciel "(What is this?)"

"Trying to get a better look, Ciel swims closer and places his hand over part of the ruins. It is covered with strange inscriptions, possibly an ancient language."

#(shocked)
voice "voice/Robin_could_it_be.mp3"
hide Robin_stoic_uniform3_night at center
show Robin_surprised_uniform5_night at center with renpy.transition(dissolve, layer="master")
Ciel "Could this be...?"

#(Levios)
voice "voice/Levios_you_see.mp3"
unknown "Yes, you stand before Aquadine. The true city of Aquadine."

hide Robin_surprised_uniform5_night at center with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform4_night at center with renpy.transition(dissolve, layer="master")
"Ciel frantically looks around to see which direction the voice is coming from, but no one was there."

voice "voice/Levios_hmph.mp3"
unknown "You are not to tell anyone what you witnessed this evening."

#(serious)
hide Robin_surprised_uniform4_night at center with renpy.transition(dissolve, layer="master")
show Robin_serious_uniform3_night at center with renpy.transition(dissolve, layer="master")
Ciel "What are you talking about?"

voice "voice/Levios_fool.mp3"
unknown "The young mermaid."

#(surprised)
hide Robin_serious_uniform3_night at center with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform4_night at center with renpy.transition(dissolve, layer="master")
Ciel "(Wait... Did I really see a mermaid? And how does he know I saw her?)"

#(serious)
voice "voice/Robin_hm2.mp3"
hide Robin_surprised_uniform4_night at center with renpy.transition(dissolve, layer="master")
show Robin_serious_uniform3_night at center with renpy.transition(dissolve, layer="master")
Ciel "Who are you?"

#(Earthquake rumble sound effect.)
hide Robin_serious_uniform3_night at center with renpy.transition(dissolve, layer="master")
scene ancient_aquadine_day with hpunch
play sound "sound/222521__uagadugu__cracking-earthquake-cracking-soil-cracking-stone.mp3"

"Suddenly, the ruins begin to shake and collapse, as if an earthquake is occurring underwater. A larger building breaks apart and tumbles towards him."

"Ciel desperately tries to swim away, but he can't escape. His cries are muted by the crashing stones' impact."

#(End earthquake sound effect. Fade to black. End new world music.)
stop sound fadeout 1.0
stop music fadeout 1.0
scene black with fadehold
"Robin wakes up in the middle of the night, panting heavily. He notices his mother is still sound asleep before breathing a sigh of relief."

#(relieved)
Robin "It was just a dream..."

#INT. Classroom - Morning
scene classroom_day with fadehold

#(Play classroom music.)
play music "Music/11 aquamarine skies.mp3"

"It's another early morning for Robin as he is the first to arrive in the vacant classroom, which means the perfect time for a nap."

#(asleep)
show Robin_asleep_school2 at farright with renpy.transition(dissolve, layer="master")
Robin "(Living two lives sure takes a toll. Sometimes, I wish I could just sleep all day...)"

#(Diana appears excited, full of energy.)
voice "voice/Diana_whats_up.mp3"
show Diana_laugh_school2_flip at center with renpy.transition(dissolve, layer="master")
Diana "Hey, Four-Eyes! What's up?"

#(annoyed)
Robin "(So much for my nap. Maybe if I pretend I'm asleep, she'll stop bothering me.)"

hide Diana_laugh_school2_flip at center with renpy.transition(dissolve, layer="master")
show Diana_normal_school1_flip at center with renpy.transition(dissolve, layer="master")
Diana "Tell me how it went."

Robin "(Why is she always so persistent? Just leave me alone already...)"

#(annoyed)
voice "voice/Diana_hey.mp3"
hide Diana_normal_school1_flip at center with renpy.transition(dissolve, layer="master")
show Diana_serious_school3_flip at center with renpy.transition(dissolve, layer="master")
Diana "Come on. Get up. I know you're awake."

#(serious)
hide Robin_asleep_school2 at farright with renpy.transition(dissolve, layer="master")
show Robin_stoic_school2 at farright with renpy.transition(dissolve, layer="master")
Robin "What do you want, Diana?"

#(curious)
voice "voice/Diana_light_laughter.mp3"
hide Diana_serious_school3_flip at center with renpy.transition(dissolve, layer="master")
show Diana_laugh_school3_flip at center with renpy.transition(dissolve, layer="master")
Diana "I wanna know how your tour went with Elisabeth. Did ya learn anythin' about her?"

hide Robin_stoic_school2 at farright with renpy.transition(dissolve, layer="master")
show Robin_stoic_school3 at farright with renpy.transition(dissolve, layer="master")
Robin "Nothing happened."

#(surprised)
hide Diana_laugh_school3_flip at center with renpy.transition(dissolve, layer="master")
show Diana_surprised_school1_flip at center with renpy.transition(dissolve, layer="master")
Diana "Really? Then again, I guess that's not too surprisin' comin' outta ya."

#(solemn)
hide Diana_surprised_school1_flip at center with renpy.transition(dissolve, layer="master")
show Diana_sad_school1_flip at center with renpy.transition(dissolve, layer="master")
Diana "(Poor guy. Elisabeth is outta his league after all, but I'll cheer him up.)"

#(smiles)
voice "voice/Diana_what_do_ya_think.mp3"
hide Diana_sad_school1_flip at center with renpy.transition(dissolve, layer="master")
show Diana_happy_school1_flip at center with renpy.transition(dissolve, layer="master")
Diana "Wanna grab some coffee after school? My treat."

#(serious)
voice "voice/Robin_no.mp3"
hide Robin_stoic_school3 at farright with renpy.transition(dissolve, layer="master")
show Robin_serious_school1 at farright with renpy.transition(dissolve, layer="master")
Robin "No."

#(grins)
voice "voice/Diana_oh.mp3"
hide Diana_happy_school1_flip at center with renpy.transition(dissolve, layer="master")
show Diana_grin_school3_flip at center with renpy.transition(dissolve, layer="master")
Diana "We can go to Frezner Café! Ya know ya can't resist the best coffee in town!"

#(smiles)
hide Diana_grin_school3_flip at center with renpy.transition(dissolve, layer="master")
show Diana_happy_school3_flip at center with renpy.transition(dissolve, layer="master")
Diana "I know you're really bogged down right now, but a day out can really do ya wonders. Come out and smell that coffee!"

#(confused)
voice "voice/Robin_hm.mp3"
hide Robin_serious_school1 at farright with renpy.transition(dissolve, layer="master")
show Robin_sad_school1 at farright with renpy.transition(dissolve, layer="master")
Robin "Huh? What are you talking about?"

#(Mr. Norton appears with a smile.)
voice "voice/MrNorton_hey_folks.mp3"
show MrNorton_normal_casual1_flip at midleft with renpy.transition(easeinleft, layer="master")
Norton "Morning, fellas. What's goin' on?"

"Mr. Norton sees Robin's face buried in his arms."

#(curious)
voice "voice/MrNorton_whats goin_on.mp3"
hide MrNorton_normal_casual1_flip at midleft with renpy.transition(dissolve, layer="master")
show MrNorton_serious_casual1_flip at midleft with renpy.transition(dissolve, layer="master")
Norton "What happened to him?"

#(normal)
voice "voice/Diana_well.mp3"
hide Diana_happy_school3_flip at center with renpy.transition(dissolve, layer="master")
show Diana_nervous_school1_flip at center with renpy.transition(dissolve, layer="master")
Diana "It didn't work out, but there are plenty of other fish in the sea."

#(smirks)
hide MrNorton_serious_casual1_flip at midleft with renpy.transition(dissolve, layer="master")
show MrNorton_laugh_casual2_flip at midleft with renpy.transition(dissolve, layer="master")
Norton "Ya tried your luck, Romeo! I didn't get my first girlfriend till I was 28, but man she was a looker!"

#(annoyed)
voice "voice/Robin_what.mp3"
hide Robin_sad_school1 at farright with renpy.transition(dissolve, layer="master")
show Robin_serious_school3 at farright with renpy.transition(dissolve, layer="master")
Robin "I'm just tired, damn it!"

#(School bell sounds.)
play sound "sound/243437__jm-studios__schoolbell-from-german-high-school.mp3"
"A few more students enter the room as the bell sounds, and Robin is visibly upset."

hide Robin_serious_school3 at farright with renpy.transition(dissolve, layer="master")
show Robin_serious_school1 at farright with renpy.transition(dissolve, layer="master")
Robin "(Curses...)"

#(End classroom music. Fade to the next scene.)
stop music fadeout 1.0

#INT. Library - Afternoon
scene library_day with fadehold

#(Play scholarly music.)
play music "Music/04 march of the waves.mp3"

"Study hall eventually comes after another class period. With nothing better to do, Robin walks into the library with a grumpy mood."

voice "voice/Robin_hm.mp3"
show Robin_stoic_school1_flip at midleft with renpy.transition(dissolve, layer="master")
Robin "(Good, barely anyone is here. I can finally take a nap.)"

hide Robin_stoic_school1_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_asleep_school2_flip at midleft with renpy.transition(dissolve, layer="master")
"Robin's tired body crumbles over an empty table. As he tries to sleep, he's reminded of the events that occurred the night before."

Robin "(I never thought mermaids actually existed. Always thought it was just a myth, but after seeing one in person, I'm convinced that they're real.)"

Robin "(And that dream... Whose voice was that and why did I see Ancient Aquadine? I have so many questions, yet no answers.)"

hide Robin_asleep_school2_flip at midleft with renpy.transition(dissolve, layer="master")
"Abandoning his plan to sleep through the period, Robin follows his curiousity and decides to look around the bookshelves."

#(Robin appears stoic.)
show Robin_stoic_school2_flip at midleft with renpy.transition(dissolve, layer="master")
Robin "(This school library actually has more books on merfolk mythology than most libraries in the world.)"

hide Robin_stoic_school2_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_stoic_school1_flip at midleft with renpy.transition(dissolve, layer="master")
Robin "(Our school's founder was not only a wealthy man, but a firm believer of Ancient Aquadine as well. He collected all sorts of related books in hopes to educate, or convert, his students.)"

hide Robin_stoic_school1_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_sad_school1_flip at midleft with renpy.transition(dissolve, layer="master")
Robin "(The only issue is deciphering whether a document is reliable or not, especially without any physical evidence. Even though that's been a problem for centuries, there are still a handful of believers that support the merfolk existence.)"

hide Robin_sad_school1_flip at midleft with renpy.transition(dissolve, layer="master")
"Robin walks past a few shelves until one book, titled 'Mythology of the Merfolk Civilization', catches his eye. He reads a few pages."

#(normal)
voice "voice/Robin_hm2.mp3"
show Robin_stoic_school2_flip at midleft with renpy.transition(dissolve, layer="master")
Robin "(This seems like it'll be worth a read. Guess I'll just check it out.)"

#(Robin looks surprised.)
hide Robin_stoic_school2_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_surprised_school2_flip at midleft with renpy.transition(dissolve, layer="master")
"As he walks over to the front desk, Robin trips over his shoelace and loses balance."

Robin "Wh-Wh-Whoaa!"

#(End scholarly music. Screen shakes.)
stop music fadeout 1.0
play sound "sound/Seq 2.1 Hit #3 96 HK1.mp3"
hide Robin_surprised_school2_flip at midleft with renpy.transition(dissolve, layer="master")
show library_day with hpunch

"A girl with straight black hair, who was sitting at a nearby table, sees the book over the marble floor and picks it up."

#(Play distant music. Anya appears.)
play music "Music/08 wonderland.mp3"

voice "voice/Anya_wow.mp3"
show Anya_normal_school2 at midright with renpy.transition(dissolve, layer="master")
Anya "Here."

"As Anya returns it to Robin, she notices that it's a book about merfolk and is taken back."

voice "voice/Robin_Im_sorry.mp3"
show Robin_sad_school3_flip at midleft with renpy.transition(dissolve, layer="master")
Robin "Thanks."

#(curious)
voice "voice/Anya_hm.mp3"
hide Anya_normal_school2 at midright with renpy.transition(dissolve, layer="master")
show Anya_surprised_school1 at midright with renpy.transition(dissolve, layer="master")
Anya "Merfolk?"

#(nervous smile)
hide Robin_sad_school3_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_nervous_school2_flip at midleft with renpy.transition(dissolve, layer="master")
Robin "Y-Yeah... I just felt like reading up on Aquadine's history, but it's still debatable whether they actually existed or not."

#(normal)
hide Anya_surprised_school1 at midright with renpy.transition(dissolve, layer="master")
show Anya_normal_school3 at midright with renpy.transition(dissolve, layer="master")
Anya "I see."

#(Anya leaves.)
hide Anya_normal_school3 at midright with renpy.transition(easeoutright, layer="master")
"Without wasting another word, Anya flips her hair and walks away."

#(curious)
hide Robin_nervous_school2_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_sad_school1_flip at midleft with renpy.transition(dissolve, layer="master")
Robin "(Have I met her before...?)"

#(End distant music.)
stop music fadeout 1.0

#EXT. Cloud Company - Evening
scene cloud_company_night with fadehold

#(Play softer gondola music.)
play music "Music/10 aria to the stars.mp3"
play sound "sound/Reddevitzer_Hoeft_03.mp3"

"Later that evening, Ciel guides his customer across a canal, lit with street lamps on both sides. Through the lights' reflection, he sculls gently enough so that one could just barely hear the sound of his oar."

"It is almost as if the gondola is floating through the indigo sky, surrounded by a swarm of dancing fireflies. Once they finally reach the Cloud Company, Ciel lets his customer off at the dock and bows to her after the tour."

#(Ciel and Staci appear. Ciel is smiling.)
voice "voice/Ciel_thank_you.mp3"
show Robin_happy_uniform1_night at right with renpy.transition(dissolve, layer="master")
show Staci_normal_casual1_night_flip at left with renpy.transition(dissolve, layer="master")
Ciel "Thank you for choosing the Cloud Company. Have a good night."

#(Staci, smiles)
voice "voice/Staci_giggle.mp3"
hide Staci_normal_casual1_night_flip at left with renpy.transition(dissolve, layer="master")
show Staci_happy_casual1_night_flip at left with renpy.transition(dissolve, layer="master")
unknown "It was fun! I'll see you again sometime."

#(Staci leaves. Staci looks stoic.)
hide Staci_happy_casual1_night_flip at left with renpy.transition(easeoutleft, layer="master")
"After waving 'goodbye' to her, he looks towards the shore's direction, curious whether the mermaid will show up again."

#(End softer gondola music and transition into the strange music. Himmel appears grumpy.)
stop music fadeout 1.0
play music "Music/13 mischievous hour.mp3"
voice "voice/Himmel_grandpa_will_speak.mp3"
show Himmel_normal_uniform2_night_flip at left with renpy.transition(easeinleft, layer="master")
Himmel "Robin, time to fix dinner! Grandpa is very hungry!"

#(serious)
hide Robin_happy_uniform1_night at right with renpy.transition(dissolve, layer="master")
show Robin_sad_uniform2_night at right with renpy.transition(dissolve, layer="master")
Ciel "I'll be out for a little longer, Grandfather. And stop calling me 'Robin' while I'm in uniform. You'll blow my cover."

#(angry)
voice "voice/Himmel_aiya.mp3"
hide Himmel_normal_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
show Himmel_surprised_uniform1_night_flip at left with renpy.transition(dissolve, layer="master")
Himmel "You want your grandpa to starve? No? Then come inside!"

#(solemn)
hide Robin_sad_uniform2_night at right with renpy.transition(dissolve, layer="master")
show Robin_sad_uniform1_night at right with renpy.transition(dissolve, layer="master")
Ciel "Just give me an hour. I want to spend some time alone."

#(normal)
voice "voice/Himmel_hmm_pondering.mp3"
hide Himmel_surprised_uniform1_night_flip at left with renpy.transition(dissolve, layer="master")
show Himmel_normal_uniform1_night_flip at left with renpy.transition(dissolve, layer="master")
Himmel "*sigh* Take this lantern and don't be out too late."

#(smiles)
hide Robin_sad_uniform1_night at right with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform2_night at right with renpy.transition(dissolve, layer="master")
Ciel "Thank you, Grandfather. I won't be long."

#(curious)
hide Himmel_normal_uniform1_night_flip at left with renpy.transition(dissolve, layer="master")
show Himmel_nervous_uniform1_night_flip at left with renpy.transition(dissolve, layer="master")
Himmel "Did you find out who was singing that night?"

#(nervous smile)
voice "voice/Robin_dont_worry.mp3"
hide Robin_happy_uniform2_night at right with renpy.transition(dissolve, layer="master")
show Robin_nervous_uniform2_night at right with renpy.transition(dissolve, layer="master")
Ciel "O-Oh. I didn't, but I still wanted to look around some more."

#(adamant)
voice "voice/Himmel_fine.mp3"
hide Himmel_nervous_uniform1_night_flip at left with renpy.transition(dissolve, layer="master")
show Himmel_surprised_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
Himmel "Fine. Just watch out for sirens!"

#(chuckles)
voice "voice/Robin_chuckles.mp3"
hide Robin_nervous_uniform2_night at right with renpy.transition(dissolve, layer="master")
show Robin_laugh_uniform1_night at right with renpy.transition(dissolve, layer="master")
Ciel "You worry too much, Grandfather. I came back last time, so I'll be fine."

#(concerned)
hide Himmel_surprised_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
show Himmel_sad_uniform1_night_flip at left with renpy.transition(dissolve, layer="master")
Himmel "That is what they all say, before they disappear....forever."

#(End strange music.)
stop music fadeout 1.0

#EXT. Shore - Evening
scene shore with fadehold

#(Play softer gondola music.)
play music "Music/10 aria to the stars.mp3"

"With the lantern attached to the ferro, Ciel cautiously glides towards the mystical shore. Once again, he sees the ghost-like jellyfish wandering in the sky."

#(Ciel appears stoic.)
show Robin_stoic_uniform2_night_flip at left with renpy.transition(easeinleft, layer="master")
Ciel "(These jellyfish are here again, but I don't see the mermaid. She wasn't singing tonight, so maybe she isn't here.)"

#(solemn)
hide Robin_sad_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
show Robin_stoic_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
Ciel "(After seeing me, I wouldn't be surprised if she never came here again. She seemed...afraid of me.)"

#(curious)
hide Robin_sad_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
show Robin_stoic_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
Ciel "(But how did she know Mother's song? I'm sure I've never met her until that night.)"

#(Water splash sound effect. Ciel looks surprised.)
play sound "sound/9508__petenice__splash.mp3"
"A sudden splash catches Ciel off guard. He immediately looks in that direction, but it's still too dark to see."

voice "voice/Robin_what.mp3"
hide Robin_stoic_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
Ciel "What was that?!"

#(Hide Ciel.)
hide Robin_surprised_uniform2_night_flip at left with renpy.transition(dissolve, layer="master")
"With his unoccupied hand, Ciel swings his rope around the closest tree branch and ties it. After setting foot on rocks, he grabs the lantern and walks around the shore."

#(Ciel appears concerned.)
show Robin_sad_uniform5_night_flip at left with renpy.transition(dissolve, layer="master")
Ciel "Are you afraid of me? It's okay. You can trust me."

"Ciel points his lantern wherever he could, but he doesn't see anyone nor get a response."

#(sighs)
hide Robin_sad_uniform5_night_flip at left with renpy.transition(dissolve, layer="master")
show Robin_sad_uniform3_night_flip at left with renpy.transition(dissolve, layer="master")
Ciel "(It was probably a fish or something...)"

#(Ciel looks surprised.)
hide Robin_sad_uniform3_night_flip at left with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform4_night_flip at left with renpy.transition(dissolve, layer="master")
"As he turns away, Ciel spots someone from the corner of his view; his eyes widen once more."

#(Transition into next CG - the same illustration of the mermaid. Dialogue will take place there. Mermaid appears.)
scene cg_2 with fadehold

"A blue haired mermaid emerges from the water - unmistakably the same mermaid from before."

#(surprised)
Ciel "(She's not swimming away this time?)"

"Nervous and scared, she stares back at him with her aquamarine eyes. Her arms act as an invisible wall - a sign that she's on her guard."

Ciel "(No, she's definitely still scared. I'm not entirely sure, but maybe she's a little curious about me, too. About humans...)"

#(curious)
voice "voice/Robin_could_it_be.mp3"
Ciel "Are you the mermaid who sang yesterday?"

"She remains silent, but nods cautiously."

#(surprised)
Ciel "(She understands me?! Maybe she could speak, too!)"

#(curious)
Ciel "What is your name?"

"The mermaid doesn't respond. However, she seems more careful about keeping her distance."

#(ponders)
voice "voice/Robin_hm.mp3"
Ciel "(Hm... There has to be something I can do to prove I'm harmless. I really want to learn more about her.)"

#(Ciel smiles.)

"To her surprise, Ciel offers his hand as a sign of peace. She examines his extended hand, then his smile. The mermaid raises her hand ever so slightly, almost tempted to trust him."

"However, she pulls back at the last second and immediately swims away in fear."

#(Mermaid leaves. Sound of splashing water. Return to scene.)
play sound "sound/9508__petenice__splash.mp3"
scene shore with fadehold

#(disappointed)
show Robin_sad_uniform3_night_flip at left with renpy.transition(dissolve, layer="master")
Ciel "(That didn't turn out too well, but maybe we'll meet again one day...)"

hide Robin_sad_uniform3_night_flip at left with renpy.transition(dissolve, layer="master")
"As the night's sky falls darker, the moonlight glistens over the river and Ciel sculls away."

#(End softer gondola music.)
stop music fadeout 1.0

#EXT. Plaza - Afternoon
scene plaza_day with fadehold

#(Play casual outdoor music. Ciel is present.)
play music "Music/12 unforgettable memories.mp3"
show Robin_normal_uniform3_flip at midleft with renpy.transition(dissolve, layer="master")
"On the following afternoon, Ciel passes by a dark haired girl who is drawing in her sketchbook. Since she's listening to music, she doesn't notice one of her pencils rolling off the case."

#(Ciel realizes it.)
hide Robin_normal_uniform3_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform3_flip at midleft with renpy.transition(dissolve, layer="master")
"While Ciel walks over to retrieve it, he recognizes the girl from school. However, he pretends he's never met her before in order to protect his alias."

#(Ciel appears with a smile.)
voice "voice/Ciel_hello.mp3"
hide Robin_surprised_uniform3_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform5_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "Excuse me, miss. You dropped your pencil."

#(End casual outdoor music. Play distant music. Anya appears.)
stop music fadeout 1.0
play music "Music/08 wonderland.mp3"
show Anya_normal_casual2 at midright with renpy.transition(dissolve, layer="master")
Anya "Thanks."

#(Ciel smiles nervously.)
hide Robin_happy_uniform5_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_nervous_uniform4_flip at midleft with renpy.transition(dissolve, layer="master")
"Without sparing him another word, Anya accepts the pencil and goes right back to her drawing. Ciel, on the other hand, isn't sure whether to keep walking or try having a brief conversation with her."

#(Ciel looks surprised.)
hide Robin_nervous_uniform4_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform4_flip at midleft with renpy.transition(dissolve, layer="master")
"However, just as he decides to leave for lunch, Ciel notices her sketch of the Bridge of Sorrow."

#(grins)
voice "voice/Robin_interesting.mp3"
hide Robin_surprised_uniform4_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_grin_uniform5_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "I'm very impressed by your drawing. Any particular reason why you're drawing the Bridge of Sorrow?"

hide Anya_normal_casual2 at midright with renpy.transition(dissolve, layer="master")
show Anya_serious_casual1 at midright with renpy.transition(dissolve, layer="master")
"Anya looks at Ciel for a second before turning back to her drawing. She seems a bit annoyed by the unwanted attention."

#(nervous smile)
hide Robin_grin_uniform5_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_nervous_uniform4_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "I-It's okay. You don't have to answer if you don't want to. I was just curious."

voice "voice/Anya_well.mp3"
hide Anya_serious_casual1 at midright with renpy.transition(dissolve, layer="master")
show Anya_normal_casual2 at midright with renpy.transition(dissolve, layer="master")
Anya "The carvings depict the tale of a man and a mermaid who fell in love. My mom used to tell it to me often before bed."

Anya "This man here was a young sailor who set out to sea alone in his small wooden ship. He wanted to explore the world and learn about all sorts of different creatures."

hide Anya_normal_casual2 at midright with renpy.transition(dissolve, layer="master")
show Anya_sad_casual3 at midright with renpy.transition(dissolve, layer="master")
Anya "But one night, a violent storm destroyed the ship and the sailor fell deep into the ocean. For a brief moment, he saw a glimpse of Ancient Aquadine before losing consciousness."

Anya "The wandering mermaid saw the man and the wooden ship submerge, so she quickly swam to his aid."

hide Anya_sad_casual3 at midright with renpy.transition(dissolve, layer="master")
show Anya_normal_casual3 at midright with renpy.transition(dissolve, layer="master")
Anya "When he woke up, he was surprised to find himself by the shore, but he even more so to see a worried mermaid before him. It was love at first sight."

#(smiles)
voice "voice/Ciel_thank_you.mp3"
hide Robin_nervous_uniform4_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform5_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "You know the tale quite well. Thank you for sharing."

Ciel "(Well, I already knew the story, but I guess it's nice to hear someone else tell it for once.)"

#(Anya leaves. Ciel looks surprised.)
hide Anya_normal_casual3 at midright with renpy.transition(easeoutright, layer="master")
"After checking the time on the street clock, Anya closes her sketchbook and leaves without saying 'goodbye'."

#(stoic)
hide Robin_happy_uniform5_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_stoic_uniform3_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "(That was abrupt, but whatever. I should probably get going, too. What time is it anyway?)"

#(Ciel looks shocked.)
hide Robin_stoic_uniform3_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform4_flip at midleft with renpy.transition(dissolve, layer="master")
"After checking the time for himself, Ciel gets up as well. But the expression he makes is much different from Anya's."

Ciel "(Only twenty minutes left before the next appointment?! I wasted too much time here!)"

#(End distant music.)
stop music fadeout 1.0

#EXT. Cloud Company - Afternoon
scene cloud_company_day with fadehold

#(Play casual outdoor music.)
play music "Music/12 unforgettable memories.mp3"
play sound "sound/Reddevitzer_Hoeft_03.mp3" loop

"Without a chance to eat, Ciel hurries back to the Cloud Company and notices a girl waiting by the dock."

#(Ciel appears curious.)
show Robin_stoic_uniform3 at right with renpy.transition(easeinright, layer="master")
Ciel "(Could she be my customer...? I didn't get a chance to check her name on the schedule.)"

#(Ciel looks surprised.)
stop music fadeout 1.0
hide Robin_stoic_uniform3 at right with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform4 at right with renpy.transition(dissolve, layer="master")
"The girl notices his presence and slowly faces him. Much to his surprise, it's a familiar face - an understatement to say the least."

voice "voice/Robin_could_it_be.mp3"
Ciel "Elisabeth...?"

#(End casual outdoor music. Play classy music. Elisabeth appears with a smile.)
stop sound fadeout 1.0
play music "Music/05 ivory flower.mp3"
voice "voice/Elisabeth_greetings.mp3"
show Elisabeth_happy_casual2_flip at midleft with renpy.transition(dissolve, layer="master")
Elisabeth "Good afternoon."

hide Robin_surprised_uniform4 at right with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform3 at right with renpy.transition(dissolve, layer="master")
Ciel "(Shoot, I'm not Robin right now. I need to be more careful about what I say.)"

#(smiles)
voice "voice/Ciel_hello.mp3"
hide Robin_surprised_uniform3 at right with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform5 at right with renpy.transition(dissolve, layer="master")
Ciel "It's so nice to finally meet you! Welcome to Aquadine, Miss Rhodes! Hopefully, I didn't keep you waiting long."

#(normal)
hide Elisabeth_happy_casual2_flip at midleft with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_casual3_flip at midleft with renpy.transition(dissolve, layer="master")
Elisabeth "Not at all. I am still rather early."

#(normal)
hide Robin_happy_uniform5 at right with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform5 at right with renpy.transition(dissolve, layer="master")
Ciel "You're very kind. My name is Ciel and I will be your tour guide for the day."

#(giggles)
voice "voice/Elisabeth_my_my.mp3"
hide Elisabeth_normal_casual3_flip at midleft with renpy.transition(dissolve, layer="master")
show Elisabeth_happy_casual1_flip at midleft with renpy.transition(dissolve, layer="master")
Elisabeth "How nostalgic. It has certainly been a while since I went on a tour."

#(smiles)
voice "voice/Robin_interesting.mp3"
hide Robin_normal_uniform5 at right with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform5 at right with renpy.transition(dissolve, layer="master")
Ciel "Ah, so this isn't your first time. Do you remember which company served you in the past?"

#(normal)
hide Elisabeth_happy_casual1_flip at midleft with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_casual3_flip at midleft with renpy.transition(dissolve, layer="master")
Elisabeth "Yes. In fact, it was this one."

hide Robin_happy_uniform5 at right with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform3 at right with renpy.transition(dissolve, layer="master")
Ciel "Is that so? In that case, welcome again! Are there any particular sights you would like to visit?"

#(smiles)
hide Elisabeth_normal_casual3_flip at midleft with renpy.transition(dissolve, layer="master")
show Elisabeth_happy_casual3_flip at midleft with renpy.transition(dissolve, layer="master")
Elisabeth "Surprise me."

#(normal)
voice "voice/Ciel_why_yes.mp3"
hide Robin_happy_uniform3 at right with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform5 at right with renpy.transition(dissolve, layer="master")
Ciel "As you wish. If you would, please follow me to the gondola."

#(End classy music.)
stop music fadeout 1.0

#EXT. Canal - Afternoon
scene canal_day with fadehold

#(Play relaxing gondola music.)
play music "Music/09 waves in the blue.mp3"
play sound "sound/Reddevitzer_Hoeft_03.mp3" loop

"After helping her onto the gondola, they begin travelling through a canal. Regardless of who he is serving, Ciel shows all of his customers the same kindness."

#(Ciel and Elisabeth appear.)
voice "voice/Ciel_how_are_you.mp3"
show Robin_normal_uniform2_flip at left with renpy.transition(easeinleft, layer="master")
show Elisabeth_normal_casual2_flip at center with renpy.transition(easeinleft, layer="master")
Ciel "You said you've ridden on a gondola before, right? How did you like it?"

#(ponders)
voice "voice/Elisabeth_you_see.mp3"
hide Elisabeth_normal_casual2_flip at center with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_casual3 at center with renpy.transition(dissolve, layer="master")
Elisabeth "Let's see... It was not a particular moment or sight that made it so memorable, but the whole experience of exploring a new town. Even as a mere child, I loved everything about it."

#(normal)
hide Elisabeth_normal_casual3 at center with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_casual1 at center with renpy.transition(dissolve, layer="master")
Elisabeth "However, my parents actually were not present during the previous ride. It was only me and the gondolier."

#(surprised)
hide Robin_normal_uniform2_flip at left with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform2_flip at left with renpy.transition(dissolve, layer="master")
Ciel "But weren't you really young back then? Your parents shouldn't have let you go alone like that."

#(nervous smile)
voice "voice/Elisabeth_well.mp3"
hide Elisabeth_normal_casual1 at center with renpy.transition(dissolve, layer="master")
show Elisabeth_nervous_casual1 at center with renpy.transition(dissolve, layer="master")
Elisabeth "To be honest, I snuck out of the hotel and acted on my own accord. I was thoroughly punished for my actions when I returned..."

#(smiles)
voice "voice/Robin_chuckles.mp3"
hide Robin_surprised_uniform2_flip at left with renpy.transition(dissolve, layer="master")
show Robin_laugh_uniform1_flip at left with renpy.transition(dissolve, layer="master")
Ciel "Wow. You're a lot more bold than you appear."

#(normal)
hide Elisabeth_nervous_casual1 at center with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_casual1 at center with renpy.transition(dissolve, layer="master")
Elisabeth "My friends in Sylphyr used to tell me that quite often."

#(normal)
voice "voice/Robin_hm.mp3"
hide Robin_laugh_uniform1_flip at left with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform2_flip at left with renpy.transition(dissolve, layer="master")
Ciel "That reminds me. I toured a family from that town a few days ago. The Bello family."

#(smiles)
hide Elisabeth_normal_casual1 at center with renpy.transition(dissolve, layer="master")
show Elisabeth_happy_casual3 at center with renpy.transition(dissolve, layer="master")
Elisabeth "Yes. The Bellos told me all about you and convinced me to ride your gondola."

#(surprised)
voice "voice/Ciel_oh.mp3"
hide Robin_normal_uniform2_flip at left with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform1_flip at left with renpy.transition(dissolve, layer="master")
Ciel "You know them?"

#(normal)
hide Elisabeth_happy_casual3 at center with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_casual2 at center with renpy.transition(dissolve, layer="master")
Elisabeth "Indeed. In fact, they are staying over at my mansion for a few days. Mr. Bello sends his regards."

#(nervous smile)
hide Robin_surprised_uniform1_flip at left with renpy.transition(dissolve, layer="master")
show Robin_nervous_uniform2_flip at left with renpy.transition(dissolve, layer="master")
Ciel "I am very grateful, but his daughter didn't seem too fond of the tour."

#(smiles)
voice "voice/Elisabeth_rest_assured.mp3"
hide Elisabeth_normal_casual2 at center with renpy.transition(dissolve, layer="master")
show Elisabeth_happy_casual3 at center with renpy.transition(dissolve, layer="master")
Elisabeth "Quite the contrary. Violetta absolutely loved it."

#(surprised)
voice "voice/Robin_really.mp3"
hide Robin_nervous_uniform2_flip at left with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform2_flip at left with renpy.transition(dissolve, layer="master")
Ciel "Really? That wasn't the impression I got."

hide Elisabeth_happy_casual3 at center with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_casual3 at center with renpy.transition(dissolve, layer="master")
Elisabeth "Violetta tends to hide her true feelings under her apathetic personality, but she certainly sang praises of you. I've never seen her so happy before."

#(smiles)
hide Robin_surprised_uniform2_flip at left with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform1_flip at left with renpy.transition(dissolve, layer="master")
Ciel "Sounds like I have to live up to those expectations."

#(Ciel and Elisabeth's expressions return to normal.)
hide Robin_happy_uniform1_flip at left with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform2_flip at left with renpy.transition(dissolve, layer="master")
hide Elisabeth_normal_casual3 at center with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_casual1_flip at center with renpy.transition(dissolve, layer="master")
"As the gondola rides farther into the canal, an old, yet well-kept, temple appears in their sight. Naturally, Ciel prepares to talk about it."

voice "voice/Ciel_over_here.mp3"
hide Robin_normal_uniform2_flip at left with renpy.transition(dissolve, layer="master")
show Robin_grin_uniform1_flip at left with renpy.transition(dissolve, layer="master")
Ciel "If you look ahead, you'll notice the Aqua Temple, which was modeled after what was believed to be Ancient Aquadinian architecture. It was built as a tribute to the sea deity Levios after the underwater civilization diminished."

#(curious)
voice "voice/Elisabeth_forgive_me.mp3"
hide Elisabeth_normal_casual1_flip at center with renpy.transition(dissolve, layer="master")
show Elisabeth_sad_casual2 at center with renpy.transition(dissolve, layer="master")
Elisabeth "Why is this town named Aquadine? Clearly, it is not underwater."

#(smiles)
hide Robin_grin_uniform1_flip at left with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform1_flip at left with renpy.transition(dissolve, layer="master")
Ciel "That's a good question. The townspeople changed its name to Aquadine to honor the civilization Levios created. The previous Aquadine is now often referred to as Ancient Aquadine."

hide Elisabeth_sad_casual2 at center with renpy.transition(dissolve, layer="master")
show Elisabeth_surprised_casual1 at center with renpy.transition(dissolve, layer="master")
Elisabeth "Did such a place actually exist? An underwater civilization?"

#(normal)
voice "voice/Robin_as_a_matter.mp3"
hide Robin_happy_uniform1_flip at left with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform2_flip at left with renpy.transition(dissolve, layer="master")
Ciel "To be honest, no one knows. Much of this town was built up on mythology and some adamant believers firmly support them, but there isn't enough concrete evidence."

Ciel "Nevertheless, the mythology has had a clear impact on our culture. As we continue our tour, you may recognize that other buildings appear inspired by the temple."

hide Elisabeth_surprised_casual1 at center with renpy.transition(dissolve, layer="master")
show Elisabeth_surprised_casual2_flip at center with renpy.transition(dissolve, layer="master")
Elisabeth "Is that garden part of the temple?"

#(smiles)
voice "voice/Ciel_why_yes.mp3"
hide Robin_normal_uniform2_flip at left with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform1_flip at left with renpy.transition(dissolve, layer="master")
Ciel "Yes, it is. The gates seem to be open, so it's available to the public at this time."

#(normal)
voice "voice/Elisabeth_if_you_dont_mind.mp3"
hide Elisabeth_surprised_casual2_flip at center with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_casual1_flip at center with renpy.transition(dissolve, layer="master")
Elisabeth "I would like have a little picnic over there if you don't mind."

Ciel "Not at all. Please take your time and enjoy your meal, miss."

hide Robin_happy_uniform1_flip at left with renpy.transition(dissolve, layer="master")
show Robin_nervous_uniform2_flip at left with renpy.transition(dissolve, layer="master")
Ciel "(Well, that's a first. I've never had a guest ask for a lunch break before, but maybe she's willing to share...)"

#(Hide the characters.)
hide Elisabeth_normal_casual1_flip at center with renpy.transition(dissolve, layer="master")
hide Robin_nervous_uniform2_flip at left with renpy.transition(dissolve, layer="master")
"Making sure that no other gondolas were passing by, Ciel turns towards the garden and finds a place to disembark."

#(CG illustration of Ciel and Elisabeth having a picnic in the garden. End relaxing gondola music. Play flowery music.)
stop sound fadeout 1.0
stop music fadeout 1.0
scene cg_3 with fadehold
play music "Music/18 home sweet home.mp3"
"Elisabeth takes out an abundance of food from her picnic basket - much more than Ciel ever imagined."

"A bottle of orange juice, a wide variety of colorful macarons, and scrumptious baguettes stuffed with rare roast beef decorate the large blanket."

#(Stomach growling sound effect.)
play sound "sound/52293__xxbirdoxx__stomach-growl-pish-01.mp3"
"A disturbance is in the air - the sound of an unidentified creature growling from Ciel's stomach. Elisabeth, nearly taking a bite out of her baguette, turns and sees a starving gondolier beside her."

#(solemn)
scene cg_3 var with renpy.transition(dissolve, layer="master")
Ciel "(This is what happens when you skip a meal...)"

#(smiles)
scene cg_3 var2 with renpy.transition(dissolve, layer="master")
stop sound fadeout 1.0
voice "voice/Elisabeth_my_my.mp3"
Elisabeth "Oh dear. I've brought far too much food for this trip, but could I really finish this all on my own? What ever shall I do?"

"She gives Ciel a quick glance and smiles before taking her first bite, leaving him helpless as she devours it."

#(shocked)
scene cg_3 var3 with renpy.transition(dissolve, layer="master")
Ciel "(I thought you were nice...)"

#(giggles)
Elisabeth "I am merely teasing you. Would you care to join me?"

#(normal)
scene cg_3 var4 with renpy.transition(dissolve, layer="master")
voice "voice/Ciel_thank_you.mp3"
Ciel "Thanks. I appreciate it."

#(Elisabeth looks surprised.)
scene cg_3 var5 with renpy.transition(dissolve, layer="master")
"Ciel snatches a baguette and wolfs it all down in an instant. At that very moment, he is anything but a handsome gondolier."

Elisabeth "My my. You seem to have quite the appetite there."

#(nervous smile)
scene cg_3 var6 with renpy.transition(dissolve, layer="master")
Ciel "Sorry. I woke up late and haven't eaten this morning."

#(smiles)
scene cg_3 var7 with renpy.transition(dissolve, layer="master")
voice "voice/Elisabeth_rest_assured.mp3"
Elisabeth "Well, there is plenty left. Please help yourself."

#(Ciel looks surprised.)
scene cg_3 var3 with renpy.transition(dissolve, layer="master")
"Elisabeth devours her baguette almost as quickly as he did; she didn't exactly stay true to her ladylike image either."

Ciel "Wow, that was fast!"

#(giggles)
Elisabeth "You seem to enjoy eating swiftly, so I wished to share that pleasure. Perhaps we should have a contest."

#(normal)
scene cg_3 var4 with renpy.transition(dissolve, layer="master")
voice "voice/Robin_really.mp3"
Ciel "You're weird."

#(smiles)
scene cg_3 with renpy.transition(dissolve, layer="master")
Elisabeth "Thank you. I will accept that as a compliment."

#(curious)
scene cg_3 var8 with renpy.transition(dissolve, layer="master")
Ciel "By the way, this is a lot of food here. Were you going to eat all of this on your own?"

#(curious)
Elisabeth "Of course. Is that a problem?"

#(nervous smile)
scene cg_3 with renpy.transition(dissolve, layer="master")
voice "voice/Robin_no.mp3"
Ciel "No, not at all. Forget I asked that."

Ciel "(But DAAMMMNNN!! This is way too much for one person! I thought she was one of those girls who always watches what she eats.)"

#(normal)
voice "voice/Elisabeth_if_you_dont_mind.mp3"
Elisabeth "How long have you been giving tours?"

#(normal)
Ciel "If we're talking about customers, it's been about four years now. But my mother taught me the oar when I was a kid."

#(smiles)
scene cg_3 var4 with renpy.transition(dissolve, layer="master")
voice "voice/Elisabeth_how_wonderful.mp3"
Elisabeth "For someone who looks around my age, you seem to have quite a bit of experience. I am still unfamiliar with this town, so your assistance is most appreciated."

#(normal)
scene cg_3 with renpy.transition(dissolve, layer="master")
Elisabeth "My last visit here was during my childhood, so some memories are vague. However, there was one pleasant experience I will never forget."

#(curious)
scene cg_3 var8 with renpy.transition(dissolve, layer="master")
voice "voice/Robin_hm.mp3"
Ciel "Was it something you ate?"

#(giggles)
scene cg_3 var3 with renpy.transition(dissolve, layer="master")
voice "voice/Elisabeth_my_my.mp3"
Elisabeth "Honestly? Did you form that question solely based on my love for food? Quite the shallow observation."

#(nervous smile)
scene cg_3 var4 with renpy.transition(dissolve, layer="master")
Ciel "(Says the girl who calls me 'Mr. Bookworm'...)"

#(normal)
scene cg_3 var7 with renpy.transition(dissolve, layer="master")
Ciel "All right. What was it?"

#(smiles)
Elisabeth "I am afraid that must remain a secret, but I will say that I am glad you are the one giving the tour."

#(smirks)
scene cg_3 var3 with renpy.transition(dissolve, layer="master")
voice "voice/Ciel_oh.mp3"
Ciel "Oh? You're interested in me?"

#(giggles)
voice "voice/Elisabeth_well.mp3"
Elisabeth "No, that's not what I meant. Everyone speaks highly of you - about how great of a gondolier you are. I simply wished to witness it for myself."

#(smiles)
Elisabeth "They say your tours bring out the best of Aquadine."

#(surprised)
Ciel "(Is this the same girl I was talking to at school? She can still tease me like before, but I remember her being more shy.)"

Ciel "(Maybe she's finally getting used to living here. But even then, I wouldn't have expected her to request a tour so soon.)"

#(normal)
scene cg_3 var4 with renpy.transition(dissolve, layer="master")
Ciel "I'm honored, but there's more to it isn't there? Like, did someone convince you to explore the town?"

#(smiles)
scene cg_3 with renpy.transition(dissolve, layer="master")
voice "voice/Elisabeth_pardon.mp3"
Elisabeth "How did you know? Are you-?"

#(proud)
scene cg_3 var9 with renpy.transition(dissolve, layer="master")
Ciel "I am psychic!"

#(surprised)
scene cg_3 var6 with renpy.transition(dissolve, layer="master")
voice "voice/Elisabeth_it_cannot_be.mp3"
Elisabeth "*gasp* You predicted what I intended to say!"

#(grins)
voice "voice/Robin_chuckles.mp3"
scene cg_3 var5 with renpy.transition(dissolve, layer="master")
Ciel "I told you, didn't I? I'm psychic."

#(normal)
scene cg_3 with renpy.transition(dissolve, layer="master")
Elisabeth "Very well. How old was I when I had my debut as a singer?"

#(normal)
voice "voice/Robin_hm.mp3"
Ciel "Uh, sixteen."

#(giggles)
scene cg_3 var4 with renpy.transition(dissolve, layer="master")
Elisabeth "Nope."

#(curious)
scene cg_3 var3 with renpy.transition(dissolve, layer="master")
Ciel "Fifteen?"

#(smiles)
scene cg_3 var8 with renpy.transition(dissolve, layer="master")
Elisabeth "Correct."

#(smiles)
scene cg_3 with renpy.transition(dissolve, layer="master")
Ciel "I knew it."

#(Ciel and Elisabeth laugh together.)
scene cg_3 var7 with renpy.transition(dissolve, layer="master")
"After sharing a few laughs, they gaze at the roaming clouds and share a few sweets."

#(surprised)
scene cg_3 var3 with renpy.transition(dissolve, layer="master")
Ciel "These macarons are delicious! Where did you buy these?"

#(smiles)
voice "voice/Elisabeth_you_are_too_kind.mp3"
Elisabeth "Why thank you! To be honest, I actually baked them myself."

voice "voice/Robin_really.mp3"
Ciel "Really?! I've recommended my customers to several pastry stores, but only a few can compare to this. Have you been to the Frezner Café?"

#(normal)
scene cg_3 var8 with renpy.transition(dissolve, layer="master")
voice "voice/Elisabeth_forgive_me.mp3"
Elisabeth "No, I have not. However, I've read several great reviews on it and hope to try it soon."

#(grins)
scene cg_3 with renpy.transition(dissolve, layer="master")
Ciel "Most of those reviews were written by guys, right?"

#(confused)
scene cg_3 var5 with renpy.transition(dissolve, layer="master")
Elisabeth "Yes. I noticed that, but never understood why."

#(nervous smile)
Ciel "You'll find out when you get there, but I can guarantee that their pastries and coffee are actually good."

#(normal)
scene cg_3 var8 with renpy.transition(dissolve, layer="master")
voice "voice/Elisabeth_how_wonderful.mp3"
Elisabeth "That sounds reassuring. Baking is a humble hobby of mine, yet I am often eager to try new creations."

#(normal)
Ciel "Then you should definitely visit them when you're free. It's really close to the plaza, so I'll show you where it is on the way back."

#(smiles)
scene cg_3 var4 with renpy.transition(dissolve, layer="master")
Elisabeth "Thank you very much!"

#(End flowery music.)
stop music fadeout 1.0

#EXT. Grand Opera House - Afternoon
scene opera_house_day with fadehold

#(Play relaxing gondola music.)
play music "Music/09 waves in the blue.mp3"
play sound "sound/Reddevitzer_Hoeft_03.mp3" loop

"The tour resumes as they come across a significantly larger sight - one that Elisabeth seems to recognize."

#(Ciel and Elisabeth appear. Elisabeth looks amazed.)
voice "voice/Elisabeth_how_wonderful.mp3"
show Robin_normal_uniform2 at right with renpy.transition(easeinright, layer="master")
show Elisabeth_surprised_casual1 at center with renpy.transition(easeinright, layer="master")
Elisabeth "Ah, that's the Grand Opera House, isn't it? It is one of the largest opera houses in the world."

#(smiles)
voice "voice/Ciel_why_yes.mp3"
hide Robin_normal_uniform2 at right with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform1 at right with renpy.transition(dissolve, layer="master")
Ciel "That's right. Looks like I won't have to explain too much here."

#(normal)
hide Elisabeth_surprised_casual1 at center with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_casual3_flip at center with renpy.transition(dissolve, layer="master")
Elisabeth "My manager always talked about concert tours and had plans for Aquadine in the future. Do you come here frequently?"

#(stoic)
voice "voice/Robin_no.mp3"
hide Robin_happy_uniform1 at right with renpy.transition(dissolve, layer="master")
show Robin_stoic_uniform2 at right with renpy.transition(dissolve, layer="master")
Ciel "I pass by it almost every day, but I haven't watched a performance. Never really had the time for it."

Ciel "(Or the money.)"

#(giggles)
voice "voice/Elisabeth_my_my.mp3"
hide Elisabeth_normal_casual3_flip at center with renpy.transition(dissolve, layer="master")
show Elisabeth_happy_casual3_flip at center with renpy.transition(dissolve, layer="master")
Elisabeth "It seems there is much of this town even you have yet to see. For such a renowned gondolier, I must say I am rather disappointed."

#(normal)
hide Robin_stoic_uniform2 at right with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform1 at right with renpy.transition(dissolve, layer="master")
Ciel "You're right. Even for someone like me, there's still so much I haven't seen, but I think it's better that way."

#(curious)
voice "voice/Elisabeth_pardon.mp3"
hide Elisabeth_happy_casual3_flip at center with renpy.transition(dissolve, layer="master")
show Elisabeth_sad_casual2_flip at center with renpy.transition(dissolve, layer="master")
Elisabeth "How so?"

#(smiles)
voice "voice/Robin_as_a_matter.mp3"
hide Robin_normal_uniform1 at right with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform1 at right with renpy.transition(dissolve, layer="master")
Ciel "There's something for me to learn every day, whether it's meeting new people or seeing different places. It'd be pretty boring if I already knew every little thing about Aquadine."

#(smiles)
hide Elisabeth_sad_casual2_flip at center with renpy.transition(dissolve, layer="master")
show Elisabeth_happy_casual3_flip at center with renpy.transition(dissolve, layer="master")
Elisabeth "Well said. Another boy from my new school told me something similar recently."

Ciel "(Another boy. Another me.)"

#(curious)
hide Robin_happy_uniform1 at right with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform2 at right with renpy.transition(dissolve, layer="master")
Ciel "How about you? Did you watch a performance while you were here?"

#(normal)
hide Elisabeth_happy_casual3_flip at center with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_casual2_flip at center with renpy.transition(dissolve, layer="master")
Elisabeth "Unfortunately, I did not, but I'm planning to."

#(smiles)
voice "voice/Ciel_oh.mp3"
hide Robin_normal_uniform2 at right with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform1 at right with renpy.transition(dissolve, layer="master")
Ciel "In that case, how about we take a look inside? Even when it's not being used, it's open to the public."

#(smiles)
voice "voice/Elisabeth_if_you_dont_mind.mp3"
hide Elisabeth_normal_casual2_flip at center with renpy.transition(dissolve, layer="master")
show Elisabeth_happy_casual3_flip at center with renpy.transition(dissolve, layer="master")
Elisabeth "Really? I'd love to!"

#(End relaxing gondola music.)
stop sound fadeout 1.0
stop music fadeout 1.0

#INT. Concert Hall, Grand Opera House - Afternoon
scene concert_hall_day with fadehold

#(Play quality time music.)
play music "Music/16 tranquility.mp3"

"Despite the concert hall's vacancy at this hour, it's always packed during a show. The room's significant size and luxurious decor give the impression that it is reserved for only the best performers."

#(Ciel and Elisabeth appear. Elisabeth isn't wearing her sunglasses and she looks amazed.)
voice "voice/Elisabeth_how_wonderful.mp3"
show Elisabeth_surprised_casual1_night at midright with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
Elisabeth "Wow, the size of this opera house never ceases to amaze me. And it is really well-kept."

voice "voice/Robin_as_a_matter.mp3"
hide Robin_normal_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform5_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "The Grand Opera House holds true to its name. Nearly 8000 people were hired to construct this building about 200 years ago, yet it still leaves present-day architects in awe."

hide Robin_normal_uniform5_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform5_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "It holds approximately 3000 seats, making it the oldest and largest opera house in Aquadine. Nowadays, it's not only used for opera and classical music, but a large variety of other performances as well."

#(smiles)
hide Elisabeth_surprised_casual1_night at midright with renpy.transition(dissolve, layer="master")
show Elisabeth_happy_casual3_night at midright with renpy.transition(dissolve, layer="master")
Elisabeth "By the way, you're quite the singer yourself. I had the pleasure of listening to your song recently."

#(normal)
voice "voice/Ciel_oh.mp3"
hide Robin_happy_uniform5_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "Oh. I just sing casually during my tours sometimes, but unlike you, I'm no professional."

hide Elisabeth_happy_casual3_night at midright with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_casual2_night at midright with renpy.transition(dissolve, layer="master")
"They let their eyes gaze the grandiose hall in silence, as if they could imagine an actual performance happening - one of Elisabeth's performances to be exact."

#(ponders)
hide Robin_normal_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "(It's really easy to see Elisabeth singing onstage. With news of her being in town, having her perform here would be a no-brainer.)"

hide Robin_surprised_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_sad_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "(But when I brought it up at school, she didn't seem comfortable about it. She loves it here, so I wonder why...)"

#(giggles)
voice "voice/Elisabeth_my_my.mp3"
hide Elisabeth_normal_casual2_night at midright with renpy.transition(dissolve, layer="master")
show Elisabeth_happy_casual3_night at midright with renpy.transition(dissolve, layer="master")
Elisabeth "You were spacing out again. Do I bore you?"

#(realizes)
hide Robin_sad_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform4_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "O-Oh, not at all. I was just wanted to ask you something."

#(normal)
voice "voice/Elisabeth_pardon.mp3"
hide Elisabeth_happy_casual3_night at midright with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_casual3_night at midright with renpy.transition(dissolve, layer="master")
Elisabeth "Yes?"

#(curious)
hide Robin_surprised_uniform4_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform5_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "Do you enjoy singing?"

#(surprised)
hide Elisabeth_normal_casual3_night at midright with renpy.transition(dissolve, layer="master")
show Elisabeth_surprised_casual1_night at midright with renpy.transition(dissolve, layer="master")
Elisabeth "..."

#(smiles)
voice "voice/Elisabeth_well.mp3"
hide Elisabeth_surprised_casual1_night at midright with renpy.transition(dissolve, layer="master")
show Elisabeth_nervous_casual2_night at midright with renpy.transition(dissolve, layer="master")
Elisabeth "Of course I do. Why would I sing if there was no passion for it?"

#(ponders)
hide Robin_normal_uniform5_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_sad_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "(She hesitated. Elisabeth is definitely hiding something, but I probably shouldn't pry into it.)"

#(normal)
hide Robin_sad_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform5_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "You don't have to have a passion for music to sing. To me, singing is merely a form of expression - not an art."

#(confused)
hide Elisabeth_nervous_casual2_night at midright with renpy.transition(dissolve, layer="master")
show Elisabeth_sad_casual3_night at midright with renpy.transition(dissolve, layer="master")
Elisabeth "You sing without passion?"

voice "voice/Robin_hm.mp3"
hide Robin_happy_uniform5_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "Think of it as someone who likes to doodle in a notebook, but doesn't plan on being an artist."

#(normal)
hide Elisabeth_sad_casual3_night at midright with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_casual2_night at midright with renpy.transition(dissolve, layer="master")
Elisabeth "Ah, I can understand that analogy. It's only a shame because you possess great potential."

#(nervous smile)
hide Robin_normal_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_nervous_uniform4_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "Gee. You're making me sound like I'm the chosen one. Like, I was destined to sing or something."

#(sad)
voice "voice/Elisabeth_crying.mp3"
hide Elisabeth_normal_casual2_night at midright with renpy.transition(dissolve, layer="master")
show Elisabeth_crying_casual3_night at midright with renpy.transition(dissolve, layer="master")
Elisabeth "Oh, Lord Ciel! Lend us your aid! Only with the power of your divine voice may the forest be saved from great calamity! We beg of you!"

#(grins)
hide Robin_nervous_uniform4_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_grin_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "Fear not, My Lady! Your prayers have been heard and they shall be granted! For I am Lord Ciel, master of the high seas!"

#(giggles)
voice "voice/Elisabeth_how_embarrassing.mp3"
hide Elisabeth_crying_casual3_night at midright with renpy.transition(dissolve, layer="master")
show Elisabeth_embarrassed_casual1_night at midright with renpy.transition(dissolve, layer="master")
Elisabeth "That was very cute. Perhaps we should resume our little play onstage."

#(chuckles)
voice "voice/Robin_chuckles.mp3"
hide Robin_grin_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_laugh_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "Yeah, our audience is waiting. All zero of them."

#(normal)
hide Elisabeth_embarrassed_casual1_night at midright with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_casual2_night at midright with renpy.transition(dissolve, layer="master")
Elisabeth "Regardless of which path is chosen, everyone must start somewhere. If the seats are empty now, the audience can only grow from here."

#(normal)
hide Robin_laugh_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_normal_uniform5_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "Wise words. How long have you been singing?"

#(smiles)
hide Elisabeth_normal_casual2_night at midright with renpy.transition(dissolve, layer="master")
show Elisabeth_happy_casual3_night at midright with renpy.transition(dissolve, layer="master")
Elisabeth "Ever since I was a little girl."

#(smiles)
hide Robin_normal_uniform5_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "Talk about a young prodigy. Your parents must be really proud of you."

#(sad)
hide Elisabeth_happy_casual3_night at midright with renpy.transition(dissolve, layer="master")
show Elisabeth_sad_casual2_night at midright with renpy.transition(dissolve, layer="master")
Elisabeth "No, you are mistaken. Before I found success, I fell short of countless expectations and was never truly passionate about singing."

#(curious)
hide Robin_happy_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_sad_uniform5_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "Then why did you pursue this career?"

voice "voice/Elisabeth_you_see.mp3"
hide Elisabeth_sad_casual2_night at midright with renpy.transition(dissolve, layer="master")
show Elisabeth_sad_casual1_night at midright with renpy.transition(dissolve, layer="master")
Elisabeth "You see...my parents were often busy with work, so they would hire specialists to teach me all sorts of skills. It was their method of keeping me occupied while they were away."

Elisabeth "Music lessons, however, were of particular interest to my mother because she used to sing in a choir herself. Even then, I did not care."

Elisabeth "It was just another chore - another specialist hired to teach me a worthless skill. But for once, my mother encouraged me to keep practicing and she would always listen."

#(slight smile)
hide Elisabeth_sad_casual1_night at midright with renpy.transition(dissolve, layer="master")
show Elisabeth_softsmile_casual3_night at midright with renpy.transition(dissolve, layer="master")
Elisabeth "Through singing, I could finally feel a connection with my mother and it was the closest bond I had with her."

Elisabeth "That feeling was enough for me to keep singing after all these years...to see her smile and praise me. She even gave me these hair ribbons as a gift, and I wear them every day."

#(solemn)
hide Robin_sad_uniform5_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_sad_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "I see..."

#(concerned)
voice "voice/Elisabeth_forgive_me.mp3"
hide Elisabeth_softsmile_casual3_night at midright with renpy.transition(dissolve, layer="master")
show Elisabeth_sad_casual1_night at midright with renpy.transition(dissolve, layer="master")
Elisabeth "Forgive me. I've spoken too much."

#(smiles)
voice "voice/Robin_dont_worry.mp3"
hide Robin_sad_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_happy_uniform5_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "No, you're fine. It's rare, but I actually enjoy listening to my customers' stories. It's nice to learn about their experiences and where they've been."

#(normal)
hide Elisabeth_sad_casual1_night at midright with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_casual2_night at midright with renpy.transition(dissolve, layer="master")
Elisabeth "For some reason, I too feel comfortable sharing a little bit of my past with you. Perhaps it is your welcoming personality that allows people to open up."

#(nervous smile)
hide Robin_happy_uniform5_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_nervous_uniform4_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "(Well, I just like it because I can save my breath during tours...)"

#(curious)
hide Elisabeth_normal_casual2_night at midright with renpy.transition(dissolve, layer="master")
show Elisabeth_normal_casual3_night at midright with renpy.transition(dissolve, layer="master")
Elisabeth "Now it is your turn. Why do you sing?"

#(solemn)
hide Robin_nervous_uniform4_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_sad_uniform4_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "While it's common for gondoliers to sing during their tours, I usually don't do it for entertainment. Singing helps me relieve stress, and it's how I keep calm whenever I'm reminded of my problems."

#(concerned)
voice "voice/Elisabeth_if_you_dont_mind.mp3"
hide Elisabeth_normal_casual3_night at midright with renpy.transition(dissolve, layer="master")
show Elisabeth_sad_casual2_night at midright with renpy.transition(dissolve, layer="master")
Elisabeth "Mind if I ask what troubles you?"

hide Robin_sad_uniform4_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_sad_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "I'd rather not say. It's personal..."

#(Ciel looks surprised.)
hide Robin_sad_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform4_night_flip at midleft with renpy.transition(dissolve, layer="master")
"Recognizing his change of mood, Elisabeth rests her hand over Ciel's to assure him that it's okay. She stares into his eyes with sincere concern."

Elisabeth "There are times when someone is in need and require the support of others. Please do not hold back. I will listen."

"Taken back by how considerate and kind she is, Ciel stutters. Deep down, it looks like he wants to talk about it, as if he's been holding in his feelings for a long time."

"Finally, a few words escape his lips."

#(solemn)
hide Robin_surprised_uniform4_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_sad_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "The problem I face also happens to be the reason why I give tours. My mother..."

hide Elisabeth_sad_casual2_night at midright with renpy.transition(dissolve, layer="master")
show Elisabeth_sad_casual3_night at midright with renpy.transition(dissolve, layer="master")
Elisabeth "Your mother?"

#(Ciel's expression looks stunned.)
hide Robin_sad_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_surprised_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
"Just before he utters another word, he stops himself. Given the situation about his identities, Ciel seems afraid to share more about his past."

#(nervous smile)
hide Robin_surprised_uniform3_night_flip at midleft with renpy.transition(dissolve, layer="master")
show Robin_nervous_uniform5_night_flip at midleft with renpy.transition(dissolve, layer="master")
Ciel "Sorry, it's getting late. We should head back now."

hide Elisabeth_sad_casual3_night at midright with renpy.transition(dissolve, layer="master")
show Elisabeth_sad_casual2_night at midright with renpy.transition(dissolve, layer="master")
Elisabeth "Of course..."

#(Hide the characters.)
hide Robin_nervous_uniform5_night_flip at midleft with renpy.transition(dissolve, layer="master")
hide Elisabeth_sad_casual2_night at midright with renpy.transition(dissolve, layer="master")
"Ignoring the tense atmosphere, Ciel escorts her outside before wrapping up the tour like usual."

scene black with fadehold

stop music fadeout 1.0
stop sound fadeout 1.0

$renpy.movie_cutscene("Movies/movie_1.mp4")
$persistent.movie_1_seen = True

scene cg_5 with fadehold

"Thank you for visiting the Aquadine demo! If you enjoyed this tour, we hope to see you again!"

#(End quality time music.)
stop music fadeout 1.0

return
