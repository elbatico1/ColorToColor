#Color To Color
A [Sublime Text][] Package to convert Web Colors In any format: Hex, Rgb, Hsl, Hsv and Names.
#Installation
You'll need `git` installed in your `$PATH`.
##OSX
    $ cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
    $ git clone https://github.com/elbatico1/ColorToColor.git
##Linux
    $ cd ~/.config/Sublime-Text-3/Packages/
    $ git clone https://github.com/elbatico1/ColorToColor.git
##Windows - PowerShell
- If you need, install [GitHub][] for windows.

    $ cd "~/AppData/Roaming/Sublime Text 3/Packages/"
    $ git clone https://github.com/elbatico1/ColorToColor.git

#Usage
Just select your entry and press `ctrl`+`shift`+`alt`+`c`, either `Window`, `OSX` or `Linux`.

The command is also present under `Tool`->`ColorToColor`

A popup window will show five possible choices:

    name : color name if present
    hex : hex value in format #ffffff
    rgb : rgb color in format rgb(255, 255, 255)
    hsl : hsl color in format hsl(360, 100.0%, 100.0%)
    hsv : hsv color in format hsv(360, 100.0, 100.0)

#Todo

Future version may includes support for `alpha channel`.

  [Sublime Text]: http://www.sublimetext.com/
  [Package Control]: https://sublime.wbond.net/installation
  [GitHub]: https://windows.github.com/
#Versions
- v1.0.0 - First Commit
