from Frotz import Frotz

# load your game file
data = 'games\zork1.z5'
# dfrotz directory
# download from : http://www.ifarchive.org/if-archive/infocom/interpreters/frotz/dfrotz.zip
# ref : http://www.ifarchive.org/indexes/if-archiveXinfocomXinterpretersXfrotz.html
dfrotz =  "C:\dfrotz.exe"
game = Frotz(data, dfrotz)

# use it inside code
game_intro = game.get_intro()
print(game_intro)

# send command to game
output = game.do_command("open")
print(output)

# can use this to loop the game and play on console.
# data = 'games\zork1.z5'
# game = Frotz(data, "C:\zorkd\dfrotz.exe")
# game.play_loop()
