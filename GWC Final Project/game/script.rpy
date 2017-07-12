### GWC Final Project by Seok Hee Hong, Brynn Jones, Star Riley, Kenyetta Akowa
# The script of the game goes in this file.
#-------------------------------------------------------------------------------
##CHARACTERS
#define  = Character(_(''), color="#FFFFFF")

#MAIN -----need to change the color for each character
define z = Character(_('Z'), color="#c8ffc8")  #AKA PROTAG-KUN
define Brazil = Character(_('Natalia Perez'), color="#c8ffc8")
define China = Character(_('Liling Wong'), color="#c8ffc8")
define England = Character(_('James Williams'), color="#c8ffc8")
define France = Character(_('Lucas Henry'), color="#c8ffc8")
define Japan = Character(_('Yuno Akizawa'), color="#c8ffc8")
define Russia = Character(_('Isidor Mikhailov'), color="#c8ffc8")
define NKorea = Character(_('Jinsoo'), color="#c8ffc8")
define SKorea = Character(_('Jisoo'), color="#c8ffc8")
define Italy = Character(_('Antonio Amadi'), color="#c8ffc8")
define Spain = Character(_('Ximena Hernandez '), color="#c8ffc8")
define Canada = Character(_('Lola Wright'), color="#c8ffc8")
define USA = Character(_('Jaime Black'), color="#c8ffc8")   #FALSE MASTERMIND
define Vietnam = Character(_('Kim-ly Mai'), color="#c8ffc8")   #TINY MASTERMIND
define Singapore = Character(_('Mengyao Shen'), color="#c8ffc8")   #ACTUAL MASTERMIND
define Philippines = Character(_('Mahalia Andrada'), color="#c8ffc8")   #NPC
define Germany = Character(_('Dieck Berhtram'), color="#c8ffc8")   #NPC
define NewZealand = Character(_('Georgia Reid'), color="#c8ffc8")   #NPC

#SECONDARY
define unknown = Character(_('???'), color="#FFFFFF")  #IF THE CHARACTER IS UNKNOWN OR HIDDEN IDENTITY
define note = Character(_('Note:'), color="#FFFFFF")

#EXTRA
define mb = Character(_('Mr. Black'), color="#FFFFFF")
define mbc = Character(_('Mr. Black\'s Child'), color="#FFFFFF")
define emp = Character(_('Employee'), color="#FFFFFF")
define com = Character(_('Intercom'), color="#FFFFFF")
define mk = Character(_('Ms. Karen'), color="#FFFFFF")
define gm = Character(_('Grown Man'), color="#FFFFFF")
define ym = Character(_('Young Man'), color="#FFFFFF")
define jj = Character(_('James Jefferson'), color="#FFFFFF")


define narration = nvl_narrator
#define narration = Character(kind=nvl)

#-------------------------------------------------------------------------------
###IMAGES
##CHARACTERS
image MB = 'sprites/Masterminds/Mengyao Shen (Singapore)/Mr_Black.png'
image MB = 'sprites/Masterminds/Mengyao Shen (Singapore)/Mengayo_angry.png'
image MB = 'sprites/Masterminds/Mengyao Shen (Singapore)/Mengayo_whin.png'
image MB = 'sprites/Masterminds/Mengyao Shen (Singapore)/Mengayo_surpried.png'
image MB = 'sprites/Masterminds/Mengyao Shen (Singapore)/Mengayo_looking.png'
image MB = 'sprites/Masterminds/Mengyao Shen (Singapore)/Mengayo_happy.png'
image Kim = 'sprites/Masterminds/Kim-ly Mai (Mastermind)(Vietnam)/Kim-ly_happy.png'
image Kim = 'sprites/Masterminds/Kim-ly Mai (Mastermind)(Vietnam)/Kim-ly_angry.png'
image Kim = 'sprites/Masterminds/Kim-ly Mai (Mastermind)(Vietnam)/Kim-ly_Teeth-smile.png'
image Kim = 'sprites/Masterminds/Kim-ly Mai (Mastermind)(Vietnam)/Kim-ly_calm.png'
image Kim = 'sprites/Masterminds/Kim-ly Mai (Mastermind)(Vietnam)/Kim-ly_cry.png'
image Kim = 'sprites/Masterminds/Kim-ly Mai (Mastermind)(Vietnam)/Kim-ly_oh.png'
image Kim = 'sprites/Masterminds/Kim-ly Mai (Mastermind)(Vietnam)/Kim-ly_sad.png'
image Kim = 'sprites/Masterminds/Kim-ly Mai (Mastermind)(Vietnam)/Kim-ly_smile.png'
image Kim = 'sprites/Masterminds/Kim-ly Mai (Mastermind)(Vietnam)/Kim-ly_surprised.png'
image Kim = 'sprites/Masterminds/Kim-ly Mai (Mastermind)(Vietnam)/Kim-ly_upset.png'
image Jaime = 'sprites/Masterminds/Jaime Black (False Mastermind)(American)/Jaime_happy.png'
image Jaime = 'sprites/Masterminds/Jaime Black (False Mastermind)(American)/Jaime_neutral.png'
image Jaime = 'sprites/Masterminds/Jaime Black (False Mastermind)(American)/Jaime_mad.png'
image Jaime = 'sprites/Masterminds/Jaime Black (False Mastermind)(American)/Jaime_sad.png'
image Jaime = 'sprites/Masterminds/Jaime Black (False Mastermind)(American)/Jaime_scared.png'
image Dieck = 'sprites/NPC/Non-Playable Characters/Dieck Berhtram (NPC)(Germany)/Dieck_happy.png'
image Dieck = 'sprites/NPC/Non-Playable Characters/Dieck Berhtram (NPC)(Germany)/Dieck_wink.png'
image Dieck = 'sprites/NPC/Non-Playable Characters/Dieck Berhtram (NPC)(Germany)/Dieck_surprise.png'
image Dieck = 'sprites/NPC/Non-Playable Characters/Dieck Berhtram (NPC)(Germany)/Dieck_pokerface.png'
image Dieck = 'sprites/NPC/Non-Playable Characters/Dieck Berhtram (NPC)(Germany)/Dieck_mad.png'
image Dieck = 'sprites/NPC/Non-Playable Characters/Dieck Berhtram (NPC)(Germany)/Dieck_dissapointed.png'
image Georgia = 'sprites/NPC/Non-Playable Characters/Georgia Reid (New Zealand)/Georgia_happy.png'
image Georgia = 'sprites/NPC/Non-Playable Characters/Georgia Reid (New Zealand)/Georgia_mad.png'
image Georgia = 'sprites/NPC/Non-Playable Characters/Georgia Reid (New Zealand)/Georgia_shy.png'
image Georgia = 'sprites/NPC/Non-Playable Characters/Georgia Reid (New Zealand)/Georgia_surprised.png'
image Georgia = 'sprites/NPC/Non-Playable Characters/Georgia Reid (New Zealand)/Georgia_surprised2.png'
image Georgia = 'sprites/NPC/Non-Playable Characters/Georgia Reid (New Zealand)/pokerface.png'
image Mahalia = 'sprites/NPC/Non-Playable Characters/Mahalia Andrada (NPC)/(Philippines) Mahalia_angry.png'
image Mahalia = 'sprites/NPC/Non-Playable Characters/Mahalia Andrada (NPC)/(Philippines) Mahalia_angry2.png'
image Mahalia = 'sprites/NPC/Non-Playable Characters/Mahalia Andrada (NPC)/(Philippines) Mahalia_closeeye.png'
image Mahalia = 'sprites/NPC/Non-Playable Characters/Mahalia Andrada (NPC)/(Philippines) Mahalia_halfclose.png'
image Mahalia = 'sprites/NPC/Non-Playable Characters/Mahalia Andrada (NPC)/(Philippines) Mahalia_mad.png'
image Mahalia = 'sprites/NPC/Non-Playable Characters/Mahalia Andrada (NPC)/(Philippines) Mahalia_pokerface.png'
image Mahalia = 'sprites/NPC/Non-Playable Characters/Mahalia Andrada (NPC)/(Philippines) Mahalia_shout.png'
image Mahalia = 'sprites/NPC/Non-Playable Characters/Mahalia Andrada (NPC)/(Philippines) Mahalia_smile.png'
image Mahalia = 'sprites/NPC/Non-Playable Characters/Mahalia Andrada (NPC)/(Philippines) Mahalia_smile2.png'
image Mahalia = 'sprites/NPC/Non-Playable Characters/Mahalia Andrada (NPC)/(Philippines) Mahalia_surprised.png'
image Mahalia = 'sprites/NPC/Non-Playable Characters/Mahalia Andrada (NPC)/(Philippines) Mahalia_sympathy.png'
image Antonio = 'sprites/Participants/Participants/Antonio Amadi (Italy)/Antonio_Annoyed.png'
image Antonio = 'sprites/Participants/Participants/Antonio Amadi (Italy)/Antonio_Nuetral.png'
image Antonio = 'sprites/Participants/Participants/Antonio Amadi (Italy)/Antonio_Psyched.png'
image Antonio = 'sprites/Participants/Participants/Antonio Amadi (Italy)/Antonio_Shooketh.png'
image Antonio = 'sprites/Participants/Participants/Antonio Amadi (Italy)/Antonio_Worried.png'


#BACKGROUNDS
image 0_outside = 'backgrounds/0_outside.jpg'
image 0_office = 'backgrounds/0_office.jpg'
image 1_clearbluesky = 'backgrounds/1_clearbluesky.jpg'
image 1_Dormroom = 'backgrounds/1_Dormroom.jpg'
image 1_Flower = 'backgrounds/1_Flower.jpg'
image 1_Warehouse.jpg = 'backgrounds/1_Flower.jpg'
image Library_Day = 'backgrounds/f_tool.jpg'
image Flower_Night = 'backgrounds/flower_night.jpg'
image Forest_Night = 'backgrounds/forest_night.jpg'
image Library_Night = 'backgrounds/Library_Night.jpg'
image Dormroom_OpenDrawer = 'backgrounds/room.jpg'
image Room_Night = 'backgrounds/Room_Night.jpg'
image SunsetSky = 'backgrounds/Subsetsky.jpg'

#-------------------------------------------------------------------------------
# The game starts here.

label start:

label prologue:
    scene 0_outside with fade

    mb "Do you have the ship ready?"
    emp "Sir, yes sir!"
    
    mbc "Are you {i}sure{/i} that you’re going to layout this plan?"

    mb "Are you questioning my decisions? Please tell me that one of my bright children is not telling me if my plan is good or not."
    mbc "No, Father. I’m just saying that this plan is rather… immoral… for the goal that you want to achieve."
    mbc "I will always respect your authority, but if this ends up in flames,  I would prefer to not go down with you."
    mb "We’re playing an innocent role now, hm? When you have a plan, you always follow it till the end; no matter the cost."
    com "Mr. Black-"
    mb "Unless, of course, you are deemed unworthy for it?"
    mbc "..."
    com "{i}Mr. Black.{/i} The conference meeting has already started in room CS4. I repeat-" 
    mb "Let’s carry on with this conversation some other time."
    mbc "I would prefer not to, but later." 

    scene 0_office with fade
    
    mk "Mr. Black. You're late. Had too many drinks last night that you couldn't get your head straight?"
    mb "You’re not far off from wrong, Ms. Karen. I’m also not far off from wrong when I say that I saw your wife with another woman."
    mk "You little-"
    gm "Hey! The president, James Jefferson, is walking in!"
    #Mr. Black looks at the door and sees a man
    "Hmmm...James Jefferson... So that's the president retiring today… My, my, he surely is making the right decision."
    jj "Hello everyone. I'm sorry that I am late, but let’s cut to the chase. I’m very certain that you have more things to do outside of this room."
    jj "As you three have might figured out, I see you as potential candidates for running our first program, Central Organization Decoded Environment of Teens With Ability (CODETWA)."
    ym "Well…"
    jj "Yes?"
    ym "I might be young, but that only proves of how much I can emotionally connect with the students. Because of this, I believe that I can be the leader for this arrangement."
    mk "Wait! I think that I can handle with running this program. I know how kids act, so I'm used to teaching-"
    ym "Just because you can get pregnant and have kids doesn't mean that you can run a facility while looking after them! President, I would be your wisest choice."
    "A small smirk grew on my lips. I couldn’t help but to admire his confidence, but that wouldn’t last too long with me in the room."
    mb "And what if you weren’t his wisest choice?"
    ym "Huh…?"
    mb "What if he deemed all of your contributions to be meaningless, therefore compared to us two, you weren’t even a thought that slipped into his mind?"
    ym "Eh, well...I’m not so-"
    mb "Hm, if you really were confident in this role that you oh-so desire, you would already know how to handle not getting it if someone else snatches it away from your tight grasp."
    mb "After all, how can your sympathetic asset compete against someone who has that and more…?"
    narration "And when he noticed Jefferson’s irises focusing now on him, Mr. Black knew for certain that the crown was now in his hands, and no one can snatch it away from him."
    narration "Not even in death."
<<<<<<< HEAD
    
    # This Ends Prologue
#--------------------------------------------------------------------
# Beginning of Chapter One

label chapterOne: 
    scene 0_outside with fade
    #Protag-kun opens eyes 
    z "Hmmm….ugh. Where am I?"
    #Protag-kun sees a flower with a note next to it
    z "What’s this? A sparkling flower?"
    z "Let me actually see what this is." 
    #Protag-kun opens the note
    note "Greetings,  Z. You probably don’t know anything right about now. Heh, well, of course, you don’t! Unless I used the wrong drug on you…"
    note "Anyways, you are about to enter a world filled with mystery. It is important that you set your mind only on the truth and to not let despair seep into your soul."
    note "You are everyone’s hope and everyone is counting on you. Don’t ever forget that."
    z "...kre"
    note "You may still be confused and utterly baffled Z, but trust me; everything will unfold itself soon." 
    "I’m confused and baffled at the very fact that I received a note from a flower"
    z "Great, all that I learned about myself is my name, Z. Well, that’s better than Bob or something-"
    #Protag-kun hears the bushes around xhem, and xhe stands up and turns around
    z "I ain’t playing these games. Show yourself!"
    #Protag-kun gets into defense mode
    unknown "Hey! It’s just me."
    z "The only “me” I know is myself, so-"
    unknown "Alright. Alright I was going to step out in the first place. Don’t get ahead of yourself buddy."
    #Protag-kun sees a girl step out of the bushes with a green bow and some unique clothes that Protag-kun never seen before)(She looks at the ground with her hand next to her mouth contemplating about something)
    "Maybe she’s worried because she doesn’t know where we are either. I should to console her!"

    
    
    # This Ends Chapter One
#--------------------------------------------------------------------
# Beginning of Chapter Two

label chapterTwo: 
    
    # This Ends Chapter Two


    return
