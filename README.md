This is a project to try and create an easy UI for recording
selenium web driver clicks, saving them and then replaying
with a python unit-tester.

Requirements:
Python 2.7
Selenium Web Driver
PyQt4

Installation:
pip install selenium

Download and install latest PyQt4 from:
https://www.riverbankcomputing.com/software/pyqt/download


**************************************************************************************

My ASCII sketch of the UI next to the web driver browser
|V| == dropdown

__________________________    __________________________
|https://mysite.com      |   |  |btn_1| |V|  |Press|    |
|------------------------|   |  ------- ---  |Enter TXT||
| btn_1    search_bar_1  |   |               |Press ENTR|
| btn_2                  |   |_______________|Save JSON |
|________________________| 
