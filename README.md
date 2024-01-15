# Setup

for running you first have to install the libraries that aren't in the standard library so dotenv and mysql.connctor, to do so run (mysql.connector is useful only if run the intended way (with a mysql database if not it's not needed)

  ```
  pip install python-dotenv
  pip install mysql.conncetor
  ```
You shouldn't need to modify anything in main.py as it shoud be running without problems, only thing is to suport other databases as i created it thinking about MYSQL but understandably not everyone would want to use it, in the future i might upload different versions interfacing with different databases but won't be coming soon.
Also important is if you have a different email provider than gmail to change in main.py the smtp server it interfaces with to the one your provider uses. 


You need to modify the .env file and the generate.py to give the programs the values/access it needs and the contents of the mail itself.
You also need to modify the file_names and image_names files as they are intended to store the names of the attachments depending on type, if they are empty no attachments will be sent.

For image attachments write names/path in image_names.txt each image should have a different line for files do the same but with the file_names.txt file.

The code presents a comment for each line making it easier even for the least tech savy to understand it as it was created for use as a divulgation newsletter meant to be written not necessarely by programmers.


--------------------------------------------------------------------------
###### originally created for a uni project but decided to make it public because who doesn't love open source
