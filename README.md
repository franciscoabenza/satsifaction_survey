# satsifaction_survey
Install Requirments:
`pip install -r requirements.txt`

After installation, start MariaDB Server:

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
