# HV20.08 The game

For this challenge, we get a highly obfuscated perl script. When we run the program, we get a command line version of tetris. Some of the blocks seem to consist of the characters of our flag. Presumably, we would be able to read the whole flag if we just survive long enough, but with the unmodified version of the script this is just impossible because blocks are arriving too fast.

Therefore, I started to deobfuscate the script. The first and most obvious step is to use Perls `deparse` module, which already gives us a more readable version of the script (see [deparsed.pl](./deparsed.pl)):

```bash
perl -MO=Deparse game.pl > deparsed.pl
```

Of course, the script also contained some indirection using `eval`. The easiest way to bypass this obfuscation step is to change the outer eval statement to `print` and see what the script actually evaluates (see [cracked.pl](./cracked.pl)). Afterwards, I took the output and combined it with the rest of the script (see [cracked2.pl](./cracked2.pl)). Finally, I formatted the code using an [online tool](https://www.tutorialspoint.com/online_perl_formatter.htm) and got a somehow readable version of the code (see [formatted.pl](./formatted.pl)).

The first thing that caught my attention was a suspicious string: `####H#V#2#0#{#h#t#t#p#s#:#/#/#w#w#w#.#y#o#u#t#u#b#e#.#c#o#m#/#w#a#t#c#h#?#v#=#d#Q#w#4#w#9#W#g#X#c#Q#}###`. It appears like this is the sequence of blocks and already contains our flag. I removed all the `#` and got the following "flag": _HV20{https://www.youtube.com/watch?v=dQw4w9WgXcQ}_. Naive me clicked on the link and I got rickrolled, so time to look a little bit closer.

My next idea was that the script somehow prints the correct flag once you finish the game. I modified the speed by adjusting the tick interval (`select( undef, undef, undef, 0.28 );`) to 0.28 seconds and enjoyed a few rounds of tetris. Unfortunately, there was no success screen after finishing the game, so I had to take a closer look at the source code.

After a while, I found the following piece of code, which seems to modify certain characters of our flag string after they got rendered in the block (note that `$_b` is the character making up the block):

```perl
sub n {
    $bx = 5;
    $by = 0;
    $bi = int( rand( scalar @BB ) );
    $__ = $BB[$bi];
    $_b = $FF[$sc];
    $sc > 77 && $sc < 98 && $sc != 82 && eval( '$_b' . "=~y#$Q#$_Q#" )
      || $sc == 98 && $_b =~ s/./0/;
```

This seems to modify the video id in our YouTube link. As the step happens after the block got used, we never see the actual id on the screen. However, I added a few lines to log the output of this operation to a file. After completing the game once again, I could simply look up the modified values from my log file and finally got a valid flag:

**Flag:** HV20{https://www.youtube.com/watch?v=Alw5hs0chj0}

As solving the game manually is a little bit odd, I also identified the function which is responsible for the collision detection logic (`_s( $__, $_b, $bx, $by - 1 );`). I simply commented it out and removed the sleep. Afterwards, the game would solve itself and write the flag to the log file in a couple of seconds. The final version of the script can be found at [cracked-final.pl](./cracked-final.pl).
