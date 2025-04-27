print("""
+------+       +------+       +------+       +------+       +------+
 |`.    |`.     |\     |\      |      |      /|     /|     .'|    .'|
 |  `+--+---+   | +----+-+     +------+     +-+----+ |   +---+--+'  |
 |   |  |   |   | |    | |     |      |     | |    | |   |   |  |   |
 +---+--+   |   +-+----+ |     +------+     | +----+-+   |   +--+---+
  `. |   `. |    \|     \|     |      |     |/     |/    | .'   | .'
    `+------+     +------+     +------+     +------+     +------+'

    .+------+     +------+     +------+     +------+     +------+.
  .' |    .'|    /|     /|     |      |     |\     |\    |`.    | `.
 +---+--+'  |   +-+----+ |     +------+     | +----+-+   |  `+--+---+
 |   |  |   |   | |    | |     |      |     | |    | |   |   |  |   |
 |  ,+--+---+   | +----+-+     +------+     +-+----+ |   +---+--+   |
 |.'    | .'    |/     |/      |      |      \|     \|    `. |   `. |
 +------+'      +------+       +------+       +------+      `+------+'
 '
      """)

print("""Welcome to Treasure Island.
Your mission is to find the treasure""")

choice1 = input("Your journey starts now... Where do you want to go? Left or Right ").lower()

if choice1 == "left":
    choice2 = input('You reach a shimmering lake,' \
                    'its surface rippling with secrets.'\
                    'A small boat bobs nearby, but the water teems with shadows. '\
                    'Do you swim across or wait for a safer option?' \
                    'Type "wait" to wait for the boat. ' \
                    'Type "Swim" to swim across. ').lower()
    if choice2 == "wait":
        choice3 = input('you spot the boat drifting closer, '
                        'and you hop in with a relieved sigh. ' \
                        'Safely across, you face three mysterious doors: red, blue, and yellow. ' \
                        'The red one glows with an eerie heat, ' \
                        'the blue one echoes with strange growls, '
                        'and the yellow one sparkles with promise. ' \
                        'Which door do you choose? ' \
                        'Type "Red" or"Yellow" or "Blue" ')
        if choice3 == "red":
            print("""    ,.   (   .      )        .      "
                        ("     )  )'     ,'        )  . (`     '`
                      .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
                      _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..""")
            print('you reach for the handle, ' \
                  'only to be engulfed in a burst of fire. ' \
                  'Game Over')
        elif choice3 == "blue":
            print("""
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,""")
            print('the door creaks open, and ferocious beasts leap out, devouring you. ' \
                  'Game Over')
        elif choice3 == "yellow":
            print('the door swings open to reveal'\
                  'a chest overflowing with gold and jewels! '\
                  'You’ve done it—You Win!')
        else:
            print("a trapdoor opens beneath you, and you fall into darkness. Game Over")
    else:
        print("a sudden splash reveals a hungry trout that attacks you. Game Over.")
else:
    print("the ground gives way, and you tumble into a dark hole. Game Over.")