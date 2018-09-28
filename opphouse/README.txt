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








	any specific questions/problems, talk to V - vsliupas@gmail.com, (707)999-0997
