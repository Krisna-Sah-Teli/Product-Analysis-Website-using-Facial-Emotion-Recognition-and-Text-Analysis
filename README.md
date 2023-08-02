# Product-Analysis-Website-using-Facial-Emotion-Recognition-and-Text-Analysis
This project is a website development based project where CNN, CV and Text Blob are used to make it practical. With the help of this website, company can get overall idea about their product prior lunching into market. This website allow company to upload the image of product along with its special features and that will be reviewed by number of users and website will collect all those reviews, facial emotions of users, feedback and finally displays graphical analysis to the company.


## Steps For Running the project
### a. Create a virtual environment
i. Open cmd
ii. install virtualenv (pip install virtualenv)
iii. now make a virtual environment of any name(say ashish)
command: virtualenv ashish
### b. Note the path of where the environment is created
### c. Start the environment. Command: ashish\scripts\activate
Note: ashish is the virtual environment name
### d. Now, install required packages in the environment
i. Install tensorflow (pip install tensorflow)
ii. Install keras (pip install keras)
iii. Install pillow (pip install pillow)
iv. install Django (pip install Django)
v. install textblob (pip install textblob)
### e. Now download all the project files from the given link.(Do not close the cmd) A zip file will be downloaded. Open the zip file, you will get a hci folder.
Extract it to a location
### f. In the cmd, go to the location where the folder was extracted.
### g. do cd hci.
### h. Now, execute the following command:
python manage.py runserver
This will start the Django server.
### i. Now go to your browser and type 127.0.0.1:8000 in the address bar and press enter. You will be redirected to the homepage of the website.
If you would like to access already created accounts for company and reviewer, they are mentioned below:
Company section: email: company@gmail.com password: company123
Reviewer section: email: krishna@gmail.com password:krishna123
