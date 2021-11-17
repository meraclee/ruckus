# Declare characters used by this game.
# The color argument colorizes the name of the character.

define n = Character("Nora", color="#3F9314")
define u = Character("Unknown", color="#AAA7A4")
define r = Character("River", color="#86d5e4")
define m = Character("Maddox Clarke", color="#F00D3D")
define mala = Character("Malakai", color="#857B67")
define p = Character("Perla", color="#d97ff0")
define d = Character("Dallas Genovese", color="#EE090D")
define c = Character("Old Conductor", color="#665745")
define f = Character("Felix", color="#f29727")
define y = Character("Young Conductor", color="#f29727")

# Define image transformations. Transforms will stick.
transform left:
    xalign 0.1
    yalign 1.0
transform right:
    xalign 0.9
    yalign 1.0
transform slightleft:
    xalign 0.25
    yalign 1.0
transform slightright:
    xalign 0.75
    yalign 1.0
transform center:
    xalign 1.0
    yalign 1.0
# The game starts here.

label start:

    # Prologue
    scene bg beach night
    # Plays ambient spooky wind.
    play music "audio/softwind.mp3" fadein 1.0
    "A young conductor stands in the conductor's room, putting his cap on
    his head."
    "He begins to tell a story to his older colleague."
    y "How long have you been a conductor?"
    c "Eh? Many years, kid."
    y "And have you ever heard of what happens on trains like these?"
    c "What are you talking about?"
    y "That transcontinental trains like these disappear, overnight."
    y "On moonless nights- nights like tonight."
    c "What are you saying, huh?"
    y "There's a monster who devours entire trains, leaving nothing left."
    y "The legend of {i}the Rail Tracer{/i}."
    c "Yeah, maybe I've heard something like that before."
    c "It's all horseshit."
    y "Perhaps."
    y "Telling the story is a for sure way to make the Rail Tracer come."
    y "But there's but one way to guarantee a train's safety."
    c "And what's that?"
    stop music fadeout 1.0
    scene bg black

    # Scene 1
    # Play opening background track on loop.
    play music "audio/relax.mp3" fadein 1.0 volume 0.5

    # Show a brick path background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg sky 3
    with fade

## Italics for what protagonist is thinking, but not for what they see.

    "I stand on a train station platform with the other members of my gang."
    "Other travelers pass through- some families with young children,
    elderly couples, traveling performers, and what looks to be a band
    wearing black suits carrying their instruments."
    "A young conductor asks the passengers waiting to see their tickets."

    # This shows a Malakai placeholder sprite.
    show male happy 1

    mala "The Aristocrat, huh?"
    "{i}This transcontinental train takes passengers from Chicago to New York.
    This'll be my first time on one of these.{/i}"
    "This is Malakai, my close friend and a member of my gang. He
    isn't the brightest but I can always count on his strength
    when we're in a tough spot."
    hide male happy 1

    # This shows the Nora sprite.
    show nora default

    "This is Nora, my girlfriend and another member of the gang. She's a bit of
    a pyromaniac."
    n "If he was telling the truth, then the explosives should be on
    this train."
    show nora smirk
    r "Which car?"
    n "Not sure. Which means we'll have to search the entire train."
    "A conductor calls out, and passengers begin to board the train.
    Some of the train staff help the band load their instruments into storage."
    "{i}It'll take several days to reach New York, so we might as well enjoy our
    trip as much as we can...{/i}"
    # Stop initial background music.
    stop music fadeout 1.0

    # Scene 2
    # Display black background
    scene bg black
    with Dissolve(.5)

    n "Wake up."
    n "River, wake up."
    "My eyes shoot open."
    scene bg compartment
    show nora default
    play music "audio/mystery.mp3" fadein 1.0

    n "Can you hear me?"
    "Groggily, I quickly sit up. The last thing I remember was laying
    down in the sleeper car."
    r "Nora, what's happening?"
    n "I think the train is being robbed!"
    r "Where's Malakai?"
    n "He was going to get something to eat. Hasn't come back."
    r "Sounds like somebody got the jump on us."
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
    r "Clarke... You're the hitman."
    m "That's a bingo!"
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

    "Maddox lets out a jovial laugh."
    m "Next time, make sure you and your gang stay out of our way."
    m "Our business isn't with you."
    "Seems like today's my lucky day- I'm not the main target of a crazed hitman."
    "He tosses Malakai toward us, and he slumps forward on the ground, completely beat."
    "Nora and I help him to his feet while Maddox and his gang head down the train."
    "Suddenly, a gunshot rings out, freezing everyone in the corridor.
    Sounds like it came from the dining car."
    hide male2 smirk
    show male happy 1
    mala "Sorry boss. They got the jump on me."
    r "Don't worry about it."
    hide male happy 1
    show nora smirk
    n "I'm just glad you're okay."
    r "We can deal with them later."
    hide nora smirk

    # Scene 4
    scene bg bed night
    show nora flushed
    n "Hey, River."
    r "Yeah?"
    n "You ever hear about that old urban legend?"
    r "What?"
    n "You know, the one about what always happens on trains. At night."
    r "I'm... not familiar."
    n "They say that on trains... there is one who follows the shadow of the rails."
    n "A monster that chases trains and devours them under cover of moonless nights."
    n "{i}The Rail Tracer.{/i}"
    n "Nobody can tell that it has caught up with a train until..."
    r "Until what?"
    n "Until people start disappearing. One by one, until there's none left."
    n "And that's how entire trains disappear, as if they never existed."
    hide nora flushed
    show nora flushed:
        xalign 0.1
        yalign 1.0
    show male happy 1:
        xalign 0.9
        yalign 1.0
    mala "Yeah, but it's just a legend right?"
    mala "A ghost story to scare little kids?"
    r "It seems there's more than one threat to {i}the Aristocrat.{/i}"
    r "Okay, Malakai and I will go investigate the noise."
    r "Nora, search the back of the train for the explosives."
    r "I have a feeling we're going to need them."
    n "Sounds good."
    n "I'll meet both of you in the conductor's room."
    "Malakai gives her a thumbs up as Nora nods and leaves."
    "Malakai and I head toward the front of the train."

    # Scene 5
    scene black
    show bg restaurant 01
    play music "audio/fastmystery.mp3" fadein 1.0
    # This shows a Dallas placeholder.
    show male happy 2
    "Dallas Genovese is a deadbeat delinquent and short tempered."
    "He's the son of the Genovese crime family,
    which leaves him largely untouchable- or so he believes."
    d "Everybody stay on the ground!"
    d "I don't want anyone making any sudden moves. Me and my boys
    will gladly put a bullet between your eyes."
    d "Now, who here knows the special formula?"
    d "Eh? You better speak up, or people here will start dying!"
    "He grabs a woman by her shoulder and hoists her up to her feet."
    "She shrieks as he places the tommy gun at her abdomen. The barrel of the
    gun presses into her dress."
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
    "Is this elixir what Maddox is after as well?"
    mala "Don't speak to the boss that way."
    d "You forget who's in charge here, buddy?"
    d "I'm the boss."
    "He drops the woman and points the end of his gun towards Malakai."
    r "It's fine, Malakai, I-"
    m "DALLAS GENOVESE!"
    hide male happy 2
    "Ah, shit."
    "Maddox Clarke's booming voice makes the hair on my neck stand up."
    show male2 smirk
    m "You're being quite a nuisance to the passengers here."
    m "I'm sure they just want to enjoy a nice meal in peace, without
    being interrupted by some delinquent with a gun."
    hide male2 smirk
    show male happy 2
    d "Who the hell are you?!"
    "Maddox lets out a boisterious laugh."
    hide male happy 2
    show male2 smirk
    m "Maddox Clarke! Me and my Black Suits will be taking over the train,
    thank you for getting a head start."
    "His Black Suits emerge from behind him, each brandishing their own tommy
    guns already trained on Dallas and his cronies."
    "Dallas' shocked face tells me he's just as surprised about Maddox being here
    as I was."
    hide male2 smirk
    show male happy 2
    d "Wh-what? What the hell are you after?"
    hide male happy 2
    show male2 smirk
    m "It's simple. We don't get paid, the conductor crashes the train."
    m "Oh, and everyone here dies."
    "He flashes his trademark smile with his perfectly white teeth."

    "To be continued...."
    # This ends the game.
    return
