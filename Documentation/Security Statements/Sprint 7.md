# Sprint 7 Security Statement
Sprint 7 focused on completing the radio button prompt system, as well as getting the share button to take the current meme and copy it to the clipboard.  Some easter eggs within the program were also introduced.
As the radio button prompt system was covered in the last statement, please review that for more information on the reasoning behind the system.  With the share function now copying the image to the clipboard, 
the main security concerns lie with malicious input within the share function.  The share function works by taking the currently displayed image and converting it to bytes before handing it to the clipboard for
use in pasting the image.  Because the image is converted to bytes, care is taken to ensure that the program only takes images from within its own file store to ensure users do not upload their own malware 
to the clipboard by means of a malicious program converted to bytes.  Additionally, the image is converted using the RGB format in order to ensure that it is in fact an image.  Easter eggs are also implemented 
as per individual programmer's desire, and the main security concern is simply ensuring that the implemented easter eggs do not have any malicious code attached to them.
