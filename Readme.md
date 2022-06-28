
# Frotz

Python interface for running text-based games using Dumb Frotz.

This is made based with ```PyFrotz``` [(github)](https://github.com/thilina27/pyFrotz#pyfrotz) 
(not required to install this package).
Only tested on Windows 10.
## Requirements

Only requirement is to have ```Dumb Frotz```
[(windows)](http://www.ifarchive.org/indexes/if-archiveXinfocomXinterpretersXfrotz.html)

## Usage

Use command line to play the game.

```python
from Frotz import Frotz

# load your game file
data = 'games\zork1.z5'
# Dumb Frotz location
dfrotz =  "C:\dfrotz.exe"
game = Frotz(data, dfrotz)

# use it inside code
game_intro = game.get_intro()
print(game_intro)

# send command to game
output = game.do_command("open")
print(output)
```

To run games interactively in the terminal.

```python
from Frotz import Frotz
data = 'games\zork1.z5'
game = Frotz(data, "C:\dfrotz.exe")
game.play_loop()
```

## Games

few dames are provided in this repo,more games are available 
[here](http://www.ifarchive.org/indexes/if-archiveXgamesXzcode.html).

## Miscellaneous

If you are the copyright holder for any of these game files and object to their distribution in this repository, 
e-mail the owner at madhusanka.thilina(a-t)gmail.com.
