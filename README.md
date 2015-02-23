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

    $ cd "~/AppData/Roaming/Sublime Text 3/Packages/"
    $ git clone https://github.com/elbatico1/ColorToColor.git

####If you need, install [GitHub][] for windows.

#Usage
Just select your entry and press `ctrl`+`shift`+`alt`+`c`, either `Window`, `OSX` or `Linux`.

![ScreenShot](http://www.somethinglikethis.it/img/hosted/color_to_color.gif)

The command is also present under `Tool`->`ColorToColor`

A popup window will show five possible choices:

    name : color name if present
    hex : hex value in format #ffffff
    hexa : hex value with alpha format #ffffffff
    rgb : rgb color in format rgb(255, 255, 255)
    rgba : rgba color in format rgba(255, 255, 255, 1.0)
    hsl : hsl color in format hsl(360, 100.0%, 100.0%)
    hsla : hsla color in format hsla(360, 100.0%, 100.0%, 1.0)
    hsv : hsv color in format hsv(360, 100.0, 100.0)
    hsva : hsva color in format hsva(360, 100.0, 100.0, 1.0)

#Todo

- ~~Future version may includes support for `alpha channel`.~~
- Add Context Menu for convert all the value present in the current file

  [Sublime Text]: http://www.sublimetext.com/
  [Package Control]: https://sublime.wbond.net/installation
  [GitHub]: https://windows.github.com/
#Versions
- v1.0.0 - First Commit
- v1.1.0 - Add hexa, rgba, hsla, hsva
