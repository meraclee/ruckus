# Declare characters used by this game.
# The color argument colorizes the name of the character.

define n = Character("Nora", color="#3F9314")
define u = Character("Unknown", color="#AAA7A4")
define r = Character("River", color="#86d5e4")
define m = Character("Maddox Clarke", color="#F00D3D")
define mala = Character("Malakai", color="#857B67")
define p = Character("Perla", color="#d97ff0")
define d = Character("Dallas Genovese", color="#EE090D")
define c = Character("Old Conductor")
define f = Character("Felix", color="#f29727")

# The game starts here.

label start:
    # Scene 1
    # Play opening background track on loop.
    play music "audio/relax.mp3" fadein 1.0 volume 0.5

    # Show a brick path background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg brick
    with fade

    "{i}You and your friends stand on a train station platform. {/i}"
    "{i}Other travelers pass through- you see some families with young children,
    elderly couples, traveling performers, and what looks to be a band
    wearing black suits carrying their instruments.{/i}"
    "{i}A young conductor asks the passengers waiting to see their tickets.{/i}"

    # This shows a Malakai placeholder sprite.
    show male happy 1

    mala "The Aristocrat, huh?"
    "This transcontinental train takes passengers from Chicago to New York.
    This'll be my first time on one of these."
    "This is Malakai, my close friend and a member of the gang. He
    isn't the brightest but I can always count on his strength
    when we're in a tough spot."
    hide male happy 1

    # This shows a Nora placeholder sprite.
    show female happy

    "This is Nora, my girlfriend and another member of the gang. She's a bit of
    a pyromaniac."
    n "If he was telling the truth, then the explosives should be on
    this train."
    r "Which car?"
    n "Not sure. Which means we'll have to search the entire train."
    "{i}A conductor calls out, and passengers begin to board the train.
    Some of the train staff help the band load their instruments into storage.{/i}"
    "It'll take several days to reach New York, so we might as well enjoy our
    trip as much as we can..."
    # Stop initial background music.
    stop music fadeout 1.0

    # Scene 2
    # Display black background
    scene bg black

    n "Wake up."

    n "River, wake up."
    "Your eyes shoot open."
    scene bg tree
    show female happy
    play music "audio/mystery.mp3" fadein 1.0

    n "Can you hear me?"
    "{i}Groggily, you quickly sit up. The last thing you remember was laying
    down in the sleeper car.{/i}"
    r "Nora, what's happening?"
    n "I think the train is being robbed!"
    r "Where's Malakai?"
    n "He was going to get something to eat. Hasn't come back."
    r "Looks like somebody got the jump on us."
    r "Let's go."

    # Scene 3
    scene bg busstop

    show male2 smirk

    m "Oi, River!"
    "Maddox stands in the train corridor holding Malakai by the collar of
    his shirt."
    m "I see he's one of yours, eh?"
    r "How do you know my name?"
    m "Oh, pardon me. I forgot to introduce myself."
    m "The name's Maddox Clarke. Ring any bells?"
    "Of course I had heard of the Clarke family-
    one of the most powerful families in Chicago."
    r "Clarke... You're a member of the Clarke family?"

    hide male2 smirk
    show male2 angry
    m "River... What are you planning to do onboard this train?"
    "He already knows about the kind of operations we do.
    What should I tell him?"
    label choices:
    menu:
        "What are you doing here?":
            jump choices1_a
        "...":
            jump choices1_b
    label choices1_a:
    m "We're going to take control of this train- and kill half the people!"
    m "Or perhaps all of them, depending on the circumstances."
    jump choices1_common
    label choices1_b:
    m "It doesn't matter. All the passengers aboard this train will die."
    m "If me and my Black Suits don't get what we want."
    jump choices1_common
    label choices1_common:
    r "You're going to hold the train hostage? For what?"
    hide male2 angry
    show male2 smirk
    "Maddox cackles maniacally."
    m "Next time, make sure you and your gang stay out of our way."
    m "Our business isn't with you."
    "He tosses Malakai toward us, and he slumps forward, completely beat."
    "Suddenly, a gunshot rings out, freezing everyone in the corridor.
    Sounds like it came from the dining car."
    "Maddox looks confused. Looks like it wasn't his doing."

    # Scene 4
    n "Hey, River."
    r "Yeah?"
    n "You ever hear about that old urban legend?"
    r "What?"
    n "You know, the one about what always happens on trains. At night."
    r "I'm... not familiar."
    n "They say that on trains... there is one who follows the shadow of the rails."
    n "A monster that chases trains and devours them under cover of moonless nights."
    n "The Rail Tracer."
    n "Nobody can tell that it has caught up with a train until..."
    # Scene 4.5


    # Scene 5
    scene bg bed day
    play music "audio/fastmystery.mp3" fadein 1.0
    # This shows a Dallas placeholder.
    show male happy 2
    "Dallas Genovese is a deadbeat delinquent and short tempered."
    "He's the son of the Genovese crime family,
    which leaves him largely untouchable."
    d "Everybody stay on the ground!"
    d "I don't want anyone making any sudden moves. Me and my boys
    will gladly put a bullet between your eyes."
    d "Now, who here knows the special formula?"
    d "Eh? You better speak up, or people here will start dying!"
    "He grabs a woman by her shoulder and hoists her up to her feet."
    "She shrieks as he places the tommy gun at her abdomen."
    d "I'm going to count to three, and if I don't hear any of you
    speaking, I'm putting a bullet in her."

    label choices2:
    menu:
        "Drop the gun, Dallas.":
            jump choices2_a
        "What do you want, Dallas?":
            jump choices2_b
    label choices2_a:
    d "Eh? Who the hell are you?"
    d "Do you know who you're dealing with?"
    jump choices2_common
    label choices2_b:
    d "Eh? Who the hell are you?"
    d "Do you have the elixir? The formula?"
    label choices2_common:
    "He points the gun towards me."
    d "Looks like we got a hero here, boys."
    "His gang gives a hearty laugh."
    d "So. You're gonna tell me you have the formula? Or just here to waste
    my time?"
    r "What formula?"
    d "Tsk tsk. Wrong answer, boyo."
    "I don't know what formula he's talking about. But looks like he's not after
    the explosives we were after."
    "Perhaps there's more going on in this train than we realized."

    # This ends the game.
    return
