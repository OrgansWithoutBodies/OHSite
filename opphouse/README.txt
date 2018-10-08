

__version__=='0.0.2'
IF YOU'RE TAKING OVER THIS PROJECT:
	Written in Django - python framework for dynamic webpages, plenty of videos on YouTube & stuff to figure out
		plans.py has some good resources in it too
	if you're not familiar with coding in general, DON'T USE TEXT EDIT or anything like that, I like using Sublime Text but any IDE should work - highlights different parts & has syntax completion/checking
	
	lots of separate pages/files make things look more complicated than it actually is, mostly because of how Django likes it, part bc of me:

		models.py - data classes website uses 
		strings.py - document with all text on site, all in one location so easier to change repeated text & specify translations (my fault)
		tests.py - automated tests to see if everything still works, hopefully i've created some already 
		views.py - takes python data and routes it to the HTML template 
		templates folder - html files, {} are django templates to copy boilerplate code



	common bugfixes:
		go to settings.py & change DEBUG to TRUE, !!!MAKE SURE TURN DEBUG=FALSE in settings.py WHEN DEPLOYING!!!

		in commandline, navigate to folder w manage.py, then type: 
			python manage.py makemigrations
				<PRESS ENTER>
			python manage.py migrate

		whenever new info (new models/new info models are asked to store) is added into models.py, migrations must be made then executed  -  don't do this unless you know what you're doing!!!!

		Connectivity Issues: Check DigitalOcean/NGINX configuration

	STACK INFORMATION -  L(inux)E(Nginx - idk why it's an E)S(qlite)P(ython/Django) Stack technologies/interfaces you should at least familiarize yourself with a lil' bit  - most LAMP stack tutorials would help, but ignore PHP/MySql stuff
			DigitalOcean.com VPS droplet [web hosting company, we buy a small share of their server which hosts our server, they give us uptime & metrics]
				running CENTOS 7 x64 [Operating System - flexible robust flavor of Linux]
					serving with NGINX [Server responsible for taking in HTTP REQUEST, letting other processes do their thing, then return an HTTP RESPONSE - 2nd most used worldwide so lots of docs, maybe too many]
						thru GUNICORN as gateway [translates HTTP stuff into Python - mostly shouldn't need to be changed if everything's configured right - DO has config documentation]
							for DJANGO (PYTHON) framework project [Backend for server, framework for creating rich HTML templates & data-models]
								saving data to SQLITE database [Saves data locally in an SQL file, doesn't need to be run on its own ]
			GIT as version control 

			DigitalOcean is very well documented, go there if there's an error on the server end (can't talk to IP address at all), CENTOS is documented but somewhat technical - most sites you should be able to just copy & paste the right commands but don't do anything too messy - if you're familiar with Mac/Linux command line then you'll be alright - CENTOS not super different from Ubuntu ("yum" instead of "apt-get", other syntactic differences), nearly identical to RedHatEnterpriseLinux("RHEL 7") (but free!!) any errors guides should be identical
				DO provides an in-browser shell command line, if you're not familiar with SSH
				If you want, you can enable desktop mode on CENTOS to help debug - idk if DO's in-browser shell supports that but it'd probably be very very laggy
				good linux tutorials here: https://www.youtube.com/channel/UCvA_wgsX6eFAOXI8Rbg_WiQ/playlists
					If you want to learn how to do CentOs/Linux without breaking everything, DigitalOcean's plans charge ~ 0.5 cent an hour, so you can try configuring up a server following their tutorials & lots of google. have fun :)
					answers to problems i had:
						If u end up deleting python2 on accident (like me...) this helps https://stackoverflow.com/questions/28923393/bash-usr-bin-yum-usr-bin-python-bad-interpreter-permission-denied#28923523
						how to configure firewalld (CENTOS firewall) to work w django's port https://www.vultr.com/docs/how-to-install-django-on-centos-7
						common nginx/gunicorn setup errors: https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04#troubleshooting-nginx-and-gunicorn

			If the problem is something specific about the site or a specific page, look through the DJANGO project
				DJANGO & PYTHON (3) super well documented, any specific errors/desires are usually google-able, basic coding knowledge should be enough to figure out python syntax
					https://www.fullstackpython.com/ has some great links & info --- VERY GOOD LEARNING/FRAMEWORK INFO
			No Jquery/bootstrap/fancy javascript plugins on Django site, i didn't want that headache
				used CSS-GRID for size-responsive styling (somewhat new), older machines get served mobile version of site (each <div> is usually its own row)
			Server Security	
				https://www.fullstackpython.com/web-application-security.html
				https://plusbryan.com/my-first-5-minutes-on-a-server-or-essential-security-for-linux-servers
			If you want to upload files from your local machine to the droplet, i'd recommend using SFTP 
				Filezilla/PUTTY have GUI enabled
				setting up FTP is covered on DO documentation 
			good linux info here: https://www.youtube.com/channel/UCvA_wgsX6eFAOXI8Rbg_WiQ/playlists
			Services offered: HTTP, HTTPS, SSH, (S)FTP,	SMTP?
	any specific questions/problems, talk to V - vsliupas@gmail.com, (707)999-0997 - can usually SSH into project, unless they've taken that away
