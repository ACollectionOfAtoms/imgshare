[![Stories in Ready](https://badge.waffle.io/ACollectionOfAtoms/imgshare.png?label=ready&title=Ready)](https://waffle.io/ACollectionOfAtoms/imgshare)
<p align="center">
<img src="http://i.imgur.com/yllkIn8.png">
<h1 align="center">imgshare</h1>
</p>
For Mac OSX >= 10.8 , this application automatically uploads screen caps (cmnd+shift+4) to imgur, and provides a link to the image.

During my college years I found it tedious to share photos of math/physics/chemistry problems with friends. This expedites the process. There are (probably) apps that already do this but...I'm also completing this project for my own edification! 
###Logging in
The API requires the user to retrieve a PIN that is specifically made for the user and the registered application. The "Get PIN" button launches the users browser and directs them to retrieve this PIN.

![Logging in](http://i.imgur.com/Chpm7Ea.png)

###Let it sit in the tray
The program then sits in the tray awaiting the creation of a new screenshot.

![Tray sittin'](http://i.imgur.com/nwxtlsx.png)

###Link provided
Once a picture is taken, the link is provided in a pop-up balloon. Clicking it sends it to the clipboard. You can also choose to automatically send it to the clipboard, or only copy it using the menu. 

![Balloon](http://i.imgur.com/2HpjLfQ.png)

### Configurations
For now, all options are saved for the session only. 

![Options](http://i.imgur.com/w0sJAdz.png)

###Next steps:
  * Create OSX app for alpha release.
  * Implement launch on start up and save user settings.
  * Future: allow user to easily upload images on their computer or the web through right-click functionality.
  * Make the UI as pretty as the logo!

##Eager to use the pre-release?
####These are the Python 2.7 dependencies:
  * PyQt5
  * imgurpython
  * pyperclip

The last two can be installed via pip or homebrew, and perhaps another package manager of your choice. Unfortunately, you'll have to build Qt5 and PyQt5 to get everything working! (At least I had to...What a wonderful way to spend an evening.)

