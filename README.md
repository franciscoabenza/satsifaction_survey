# satsifaction_survey
Install Requirments:
`pip install -r requirements.txt`

After installation, start MariaDB Server:

"""Create a new user on MariaDB
Here is how to do this

Connect to the MySQL command line:
sudo mysql -uroot -p
Create a new database:
CREATE DATABASE <dbname>;

In this step and the following, replace all variables between <…> by the name you want to use
Now, create the new user:
CREATE USER '<username>'@'localhost' IDENTIFIED BY '<password>';
Then, allow this new user to do anything on the database we just created:
GRANT ALL PRIVILEGES ON <dbname>.* TO '<username>'@'localhost';
Finally, reload the permissions with:
FLUSH PRIVILEGES;"""

`mysql.server start`
To auto-start MariaDB Server, use Homebrew's services functionality, which configures auto-start with the launchctl utility from launchd:

`brew services start mariadb`
After MariaDB Server is started, you can log in as your user:

mysql
Or log in as root:

`sudo mysql -u root`

run: `uvicorn main:app --reload`

Enter the URL:
http://localhost:8000/
