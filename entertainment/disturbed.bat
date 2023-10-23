@echo off
title ----------Disturbed----------
:menu
cls 
echo.                                                                                                
echo               ::::::::-.  ::: .::::::. :::::::::::; ...    ::: ::::::..   :::::::.  .,::::::  :::::::-.  
echo                  ;;,   `';,;;;;;;`    ` ;;;;;;;;''  ;;     ;;  ;;``;;;;   ;;;'';;' ;;;;''''   ;;,   `';,
echo                  [[     [[[[['[==/[[[[,     [[     [['     [[[ [[[,/[[['   [[[__[[\. [[cccc    `[[     [[
echo                  $$,    $$$$$  '''    $     $$     $$      $$$ $$$$$$c     $$""""Y$$ $$""""     $$,    $$
echo                  888_,o8P'888 88b    dP     88,    88    .d888 888b "88bo,_88o,,od8P 888oo,__   888_,o8P'
echo                 MMMMMP"`  MMM  "YMmMY"      MMM     "YmmMMMM"" MMMM   "W" ""YUMMMP"  """"YUMMM  MMMMP"`                                                                                       
echo      .____------------------------------------------------------------------------------------------------____.                                                                                                                                                                                                         
echo                                                  1. start                                                                     
echo                                                  2. How to play                                                             
echo                                                  3. credits                                                                      
echo                                                  4. exit                                                                    
echo                                                                            (game still in development)                              
set /p answer=Type the number of your option and press the enter key:
if %answer%==1 goto start
if %answer%==2 goto howtoplay
if %answer%==3 goto credits
if %answer%==4 goto exit
:howtoplay
cls
echo Hey, just type the number of the option and
echo press the enter key!
pause
goto menu
:exit
cls
set /p answer=Don't go away, there is a monster under your bed! (y/n)
if %answer%==y goto y
if %answer%==n goto n
:y
cls
exit /b
:n
cls
goto menu
:credits
cls
echo             _ __            _ _ _              
echo            ( /  )         /( / ) )         /    
echo             /--(  __,  __/  / / /  __,  __/  
echo            /   \_(_/(_(_/_ / / (_ (_/(_(_/ 
echo    -----------------------------------------------
echo. 
echo Game created by RedMad 16 it's my first game with command prompt! hope you like it :)
echo ENJOY!
pause
goto menu
:start
cls
echo             .
echo               .
echo           . .
echo              ...
echo           \~~~~~/
echo            \   /
echo             \ /
echo              V
echo              !  
echo              !
echo             ---
echo _____________________________________
echo 1. Investigate
echo 2. Sleep
echo -------------------------------------
echo You live in a small city in America here it's so silent,
echo after going to have a drink with your firends you decide to go to sleep. . .
echo.
echo at the 2am to the 3am you heard some crunches in your
echo flat you try to sleep but you can't that noise is so loud
set /p answer=do you want to investigate or try to sleep?
if %answer%==1 goto investigate
if %answer%==2 goto sleep
:sleep
cls
echo you fall asleep but you didn't wake up anymore
echo YOUR LAST BREATH HAS BEEN LEFT
pause
goto menu
:investigate
cls
echo _____________________________________
echo 1. kitchen
echo 2. bathroom
echo -------------------------------------
echo your living room is full of blood:
set /p answer=do you want to go in kitchen or in your bathroom?
if %answer%==2 goto bathroom
if %answer%==1 goto kitchen
:bathroom
cls
echo you enter in the bath and you see a monster in your mirror, he picks you. YOUR LAST BREATH HAS BEEN LEFT
pause
goto menu
:kitchen
cls

echo           ______
echo        .-"      "-.
echo       /            \
echo      ^|              ^|
echo      ^|,  .-.  .-. , ^|
echo      ^| )(__/  \__)( ^|
echo      ^|/     /\    \ ^|
echo      (_     ^^      _)
echo        \_^|IIIIII^|_/
echo        ^| \IIIIII/ ^|
echo        \          /
echo         `--------`
echo _____________________________________
echo 1. run
echo 2. fight
echo -------------------------------------
echo in your kitchen you see a skeleton with a sword that stares at you. . .
set /p answer=do you want to run or fight?
if %answer%==2 goto fight
if %answer%==1 goto run
:fight
cls
echo             _____   _____
echo            /     \ /     \
echo       ,   ^|       '       ^|
echo       I __L________       L_____
echo  O====IE__________/     ./_____/
echo       I      \.       ./
echo       `        \.   ./
echo                  \ /
echo                   '                
echo you try to fight him with your bare hands, but suddently you lose your energies
echo and the skeleton kills you. YOUR LAST BREATH HAS BEEN LEFT
pause
goto menu
:run
cls
echo _____________________________________
echo 1. left
echo 2. right
echo -------------------------------------
echo you know that you can't fight him, you run in the street in search of help
set /p answer=do you go left or right?
if %answer%==1 goto left
if %answer%==2 goto right
:right
cls                    
echo                                # #### ####
echo                                ### \/#### /####
echo                               ##\/#/ \/##/_/##/_#
echo                             ###  \/###/ \/ # ###
echo                           ##_\_#\_\##  #/###_/_####
echo                          ## #### # \ # /  #### ##/##
echo                           __#_--###`#  {,###---###-~
echo                                     \ }{
echo                                      {}}
echo                                     ( 0 )
echo                                      {{}
echo                                      {}}
echo                                      {}{    
echo There is a big Tree with an eye on the center, in a few seconds his stick sprout from the land
echo and they suck you up. YOUR LAST BREATH HAS BEEN LEFT
pause
goto menu
:left
cls
echo                 _(
echo             ___^|_^|_________
echo            /___^|_^|_________\
echo       ()  /_________________\
echo   `'.()))/___________________\'-.'`'.
echo  .,'(())()   ____     ____  ^|,.'     '-.
echo     )(()))   )~~(     )~~(  ^|. '-. ()`'.
echo    ()()(())  ^|__^|     ^|__^|  ^| `'.,(())
echo   ())()(()))      __          ^|     ()))()
echo   ()((())()))    ^|  ^|        ^|    (()()))
echo  ()))(()()())    ^|  ^|          ^|    )(()(()
echo  (()((())(()------------------- (())(())
echo  ~^~ ^" ^"  ^~^   ^"   ~^~    ^~^~(()(()

echo walking some things around you disappears. But then you find the home when you were a child,
echo you decide to enter to see what's in,
pause
goto doors
:doors
cls  
echo     ________
echo     ^| _  _ ^|
echo     ^|^| ^|^| ^|^|      
echo     ^|^|_^|^|_^|^|
echo     ^| _  _o^| 
echo     ^|^| ^|^| ^|^|
echo     ^|^|_^|^|_^|^|    
echo     ^|______^|
echo _____________________________________
echo 1. first
echo 2. second
echo 3. third
echo -------------------------------------
echo all of what you see are three doors
echo the first have near a statue of a devil, the second have nothing, and the third have 
echo near a statue of an angel with a book
set /p answer=do you want to enter in the first the second or the third?
if %answer%==1 goto first
if %answer%==2 goto second
if %answer%==3 goto third
:first
cls
echo         \_______/
echo     `.,-'\_____/`-.,'
echo      /`..'\ _ /`.,'\
echo     /  /`.,' `.,'\  \
echo    /__/__/     \__\__\__
echo    \  \  \     /  /  /
echo     \  \,'`._,'`./  /
echo      \,'`./___\,'`./
echo     ,'`-./_____\,-'`.
echo         /       \
echo you decide to go in the first, walking you see a giant spider, the door
echo behind you closed, the spider caugh you with his webs
echo and in a second kill you YOUR LAST BREATH HAS BEEN LEFT
pause 
goto menu
:second
cls
echo you decide to go in the second, here you find a cliff
echo seeing that it's impassable you turn back
pause
goto doors
:third
cls
echo                      @
echo                    @@@@
echo                  @ @!!@
echo                    @!!@  @
echo               --____!!____--
echo                _____!!_____
echo _____________________________________
echo 1. no
echo 2. yes
echo -------------------------------------
echo you decide to go in the third, here you find a fountain, with something
echo that glitters in it
set /p answer=do you want to see what's in? 
if %answer%==1 goto no
if %answer%==2 goto yes
:yes
cls
echo it was the head of an anglerfish, it in a second eats you
echo YOUR LAST BREATH HAS BEEN LEFT
pause
goto menu
:no
cls
echo _____________________________________
echo 1. no
echo 2. yes
echo -------------------------------------
echo hoping that's something bad you continue to walk. . .
echo you find the exit from the back of your home
echo continuing to walk you see a cave
set /p answer=do you want to enter? [yes/no]
if %answer%==2 goto yeah
if %answer%==1 goto nope
:yeah
cls
echo walking in the cave it gets dark step by step, suddently with a bit of light
echo you see a bear, you try to run, but it instantly kil you YOUR LAST BREATH HAS BEEN LEFT
pause 
goto menu
:nope
cls
echo          ,~"""~.
echo       ,-/       \-.
echo     .' '`._____.'` `.  
echo     `-._         _,-'
echo         `--...--'
echo _____________________________________
echo 1. no
echo 2. yes
echo -------------------------------------
echo you decide to not enter. . .
echo you continue to walk around in the path, you see a farmer with a sword in the back,
echo he tell you that he lost his hat somewhere,
set /p answer=do you want to help him?
if %answer%==1 goto fuck
if %answer%==2 goto yepa
:fuck
cls
echo             _____   _____
echo            /     \ /     \
echo       ,  ^|       '       ^|
echo       I __L________       L_____
echo  O====IE__________/     ./_____/
echo       I      \.       ./
echo       `        \.   ./
echo                  \ /
echo                   '
echo.                 
echo you decide to not help him, in a second the farmer
echo extracts his sword and he pierces you YOUR LAST BREATH HAS BEEN LEFT
pause
goto menu
:yepa
cls
echo _____________________________________
echo 1. first
echo 2. second
echo -------------------------------------
echo you decide to help him and he says that he think he lost it
echo in the castle over there
echo you enter in the castle there are two corridors, 
set /p answer=in what corridor do you want to go? [first/second]
if %answer%==2 goto seconda
if %answer%==1 goto firsta
:firsta
cls
echo the door close suddently, the walls shrink
echo until they crush yourself YOUR LAST BREATH HAS BEEN LEFT
pause
goto menu
:seconda
cls
echo _____________________________________
echo 1. first
echo 2. second
echo 3. third
echo -------------------------------------
echo you decide tho go in the second, there is a strong light in this room. . .
echo there are others three corridors,
set /p answer=do you want to go in the third, second or first?
if %answer%==3 goto thirdr
if %answer%==2 goto secondr
if %answer%==1 goto firstr
:thirdr
cls
goto firsta
:secondr
cls
goto firsta
:firstr
cls
echo          ,~"""~.
echo       ,-/       \-.
echo     .' '`._____.'` `.  
echo     `-._         _,-'
echo         `--...--'
echo you enter in a library, it's so quiet and the moonlight enter by a window
echo you search for the hat, at the end you find it and you come back
pause
cls
echo           ,
echo           I ______________________
echo     O=====IE_____________________/
echo           I
echo           '
echo you come back to the farmer, you give him the hat
echo and he such as a prize give you his sword!
pause
cls
echo           ______
echo        .-"      "-.
echo       /            \
echo      ^|              ^|
echo      ^|,  .-.  .-. , ^|
echo      ^| )(__/  \__)( ^|
echo      ^|/     /\    \ ^|
echo      (_     ^^      _)
echo        \_^|IIIIII^|_/
echo        ^| \IIIIII/ ^|
echo        \          /
echo         `--------`
echo _____________________________________
echo 1. yes
echo -------------------------------------
echo you continue to go down the path, suddently you see
echo the skeleton of your house, 
set /p answer=do you want to fight him? (you have a high chanche of winning)
if %answer%==1 goto yep
:yep
cls
set /a ran=%random%
if /i %ran% GTR 10000 goto :win
if /i %ran% LSS 10000 goto :lose
echo Batch chose the number %ran%
:lose
cls
echo             _____   _____
echo            /     \ /     \
echo       ,   ^|       '       ^|
echo       I __L________       L_____
echo  O====IE__________/     ./_____/
echo       I      \.       ./
echo       `        \.   ./
echo                  \ /
echo                   '
echo.                 
echo battling him you have a chance to kill him, you lose the chance...
echo repeat the adventure and retry!
echo YOUR LAST BREATH HAS BEEN LEFT (bad ending)
pause
goto menu
:win
cls
echo you pierce him, he is dead
echo your eyes tarnish and in a few second you wake up in your bed for some crunches in your flat
echo your last breath will be released another time. . .
echo you waked up from this nightmare. . . do you?
pause
cls
echo             _ __            _ _ _              
echo            ( /  )         /( / ) )         /    
echo             /--(  __,  __/  / / /  __,  __/  
echo            /   \_(_/(_(_/_ / / (_ (_/(_(_/ 
echo    -----------------------------------------------
echo GAME MADE BY RedMad 16 I hope you liked my game :D (happy ending)
echo YOUR LAST BREATH WILL BE RELEASED ANOTHER DAY. . .
pause
goto menu
