[![Stories in Ready](https://badge.waffle.io/ACollectionOfAtoms/imgshare.png?label=ready&title=Ready)](https://waffle.io/ACollectionOfAtoms/imgshare)
# imgshare
###What?
For Mac OSX, this application automatically uploads screen caps (cmnd+shift+4) to imgur, and provides a link to the image.
###Why!?
During my college years I found it tedious to share photos of math/physics/chemistry problems with friends. This expedites the process. There are (probably) apps that already do this but...I'm also completing this project for my own edification! 

##Progess so far.
The program is functional in that it provides the user with a link of the screencap following file creation but, the execution of this process still needs work! The link is currently provided in the terminal, and the user does not have many options (which album to upload to etc.). Therefore the current version is at an "exceedingly alpha" stage.

###Logging in
The imgur API requires the user to retrieve a PIN that is specifically made for the user and the registered application.

![Logging in](http://i.imgur.com/MTW2dxZ.png )

###Let it sit in the tray
The program then sits in the tray and scans the desktop directory.

![Tray sittin'](http://i.imgur.com/f3hMnxA.png)

###Link provided
Once a picture is taken, the link is provided in a pop-up balloon. Clicking it sends it to the clipboard

![Balloon](http://i.imgur.com/njKMiRD.png)

###Next steps:
* Create OSX app for alpha release?
* Update visuals (login window/icon, balloon icon)
* Catch start up and upload errors (if imgur is overloaded, program fails)
* Give the user more options!

