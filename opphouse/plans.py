# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 16:04:16 2018

@author: V



schedule todolist
    web
        do

    truck app
        do
        integrate admin

    truck admin app - python, android, web?
        gets from web/can be input manually
    
    dock 
        integrate truck,web & overflow
        migrate log
        more logging
        fix up any temps/hacks

    overflow app
        do
    barcode app 
        login thru epos
        app launching w/o admin
        fix up stuff/make look nicer/
    clock
        do

    statisticsnet
        do
        integrate into s
        handlers to make sql objects interoperable

    better bug reporting



    
helpful resources:
    https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/modwsgi/ (Apache)
    https://www.html5rocks.com/en/tutorials/speed/parallax/ (HTML5 Parallax)
    https://scrimba.com/g/gR8PTE (CSS Grid)
    https://ultimatedjango.com/learn-django/lessons/create-the-project-base-template/(navbar/django templating)
    https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django (good in-depth tutorial)
current site 
    problems:
        convoluted way of scheduling pickups
        stupid expensive, largely bootstrap
        barely optimized for mobile (line wraps, horizontalgroup buttons, non-persistent menu(stylistic but still), nonclickable phone #'s,basic forms, dreamweaver rly intended for static/old webpages)
        "thirft store","our work" repurposed for sponsorships lol 
        no https
        redundant contact, different zips means hardcoded instead of shared vars (sloppy!!)
        very late 90's early00's vibe (Dreamweaver templates pretty outdated nowadays)
        contact/contact-us domain confusion on runaround leads to dead pages (on roughly half of the pages the "Sign Up To Volunteer" button redirects to an old page, but not on others - hardcoded repeated headache)
        no parallax for sections w buttons (main screen/WFH)
            parallax thru js (stellar.js) - inefficient?
        bootstrap grid instead of native CSS - even more javascript for basic structure, oldish
            looks weird @ different resolutions
        jquery starting to get old, not a big strike against it tho 
    



index
about
events
volunteer
donate
thrift
WfH
Contact
docs - video?

end goal:
    all necessary pages
    RECREATE FIRST, then add fancy
    figure out how to pattern non-img'd events
    
    SEO hacking
        twitter good for SEO https://www.youtube.com/watch?v=T3GsJgxAB9Q&list=PL7Nf-MXzozDLSk9nLsAkosV9h3C4eBXgn&index=13
    TinyMCE for wsyiwyg page editor (https://www.youtube.com/watch?v=bJeTEDRvGVA&list=PL7Nf-MXzozDLSk9nLsAkosV9h3C4eBXgn&index=4)
    
    editable container for info under pic on mainpage (commented-out Statefarm bit )
        checkbox for whether or not is shown
    sitemap (https://www.youtube.com/watch?v=xAXMqiPSY34)
    captcha contact
    retina (js or otherwise)
    basic slide animations (jq or greensock)
    user-editable translations thru admin - ES, maybe ZH
        "Translator" group connected to specific language - ISO639-1 code included
        has different ways of showing if text is already translated manually
            if not will be google translated (don't want to have to query it each time - saved in other file?)
                https://cloud.google.com/translate/docs/translating-text#translate_translate_text-protocol

   
    get royalty-free page rip if possible
    clickable asterisk scrolls down to page info
    editable sponsors - scrollbar?
        "WebEditor"(or similar) Group can edit sponsors & events
        paypal linked to adding to sponsor in some form?

    format notes
        parallax in mainpictures
        drop shadow from header

    pickup scheduling form 
        sends info to android app db 
            (REST sending to GCM- w authentification: https://techstricks.com/api-authentication-django-and-android-apps/)
        employees in group "Pickup" can change pickup data & call api
       
    active sales 

    Marketplace (https://www.youtube.com/watch?v=9Wbfk16jEOk)
        connected to fb &/ ebay
            facebook app - out of date? (https://www.youtube.com/watch?v=jxDHNSW28bs&index=10&list=PL7Nf-MXzozDLSk9nLsAkosV9h3C4eBXgn)
        https://developers.facebook.com/docs/marketing-apisre
    "Is Dock Open" badge
        auto open/closed based on hours,have some way (floor app?) to send closing signal
    map w all marked pts - maybe not since gmaps is dumb now?
        figure out details abt cloud pricing/nonprofit api discounts
        use OpenStreetMap for planning fastest route? or google credits if low volume 

    more in-depth social media integration
   

    Use Model Forms!!! - crispy too?
    DB backup manager (fixtures?)

    Way down the line goals:
        eventually make better video than that movie maker shit
        connect fancy lights maybe (https://www.youtube.com/watch?v=5zhReMb_Yek&pbjreload=10)
    
done:
    git-ify'd :) 
todo:
    media folders
    event reads from db
    
data structures:
    Event Data Structure:
        Title
        Description (w headers etc)
        Datetime
        Location
        Image
        URL
    WFH Data Structure:
        Car Info:
            [Donor]
              is car located at donor address [if not, additional field]
            Year/Make/Model
            Mileage
            Does it Run?
            Have The Title?
            VIN
            How Did You Hear About Us
     Donor Structure:
            Name
            Address
            Phone
            Email
            IP
            
    Pickup Item Info:
        [Donor]
        Item Descriptions
        Uploadable images
        Stop type

"""
namedict={'James Ward':{'phone':'$thrift_phone','email':'jamesw@opportunityhouse.us','role':'pickup'},
          'Sunny Tyler':{'email':'sunnyt@opportunityhouse.us'}}
locdict={'Thrift Store':{'address':'107 Peabody Rd','phone':7074466246},
          'Shelter':{'address':'267 Bennett Hill Court','phone':7074471988,'email':'iwanttohelp@opportunityhouse.us'},
          'Corporate':{'phone':7074514874,'address':'P.O. Box 6593'}}