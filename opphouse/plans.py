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

    truck admin app - python, android, web
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
    https://www.youtube.com/watch?v=-oWIyFYyNQw&list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW&index=26 (eps 23-28 are good overview of form details)
    https://www.youtube.com/watch?v=zojnkKGRXp0 (form mixins ~8 min)

current site 
    problems:
        convoluted way of scheduling pickups
        stupid expensive, largely bootstrap
        barely optimized for mobile (line wraps, horizontalgroup buttons, non-persistent menu(stylistic but still), nonclickable phone #'s,basic forms, dreamweaver rly intended for static/old webpages)
        "thirft store","our work" repurposed for sponsorships lol 
        no https
        sponsors make 
        parallax gets screwy on small screens
        redundant contact, different zips means hardcoded instead of shared vars (sloppy!!)
        very late 90's early00's vibe (Dreamweaver templates pretty outdated nowadays)
        "get in involved"
        contact/contact-us domain confusion on runaround leads to dead pages (on roughly half of the pages the "Sign Up To Volunteer" button redirects to an old page, but not on others - hardcoded repeated headache)
            fixed as of October, changed to email button w 50/50 shot of emailing Sunny or nicholasC
        no parallax for sections w buttons (main screen/WFH)
            parallax thru js (stellar.js) - inefficient?
        bootstrap grid instead of native CSS - even more javascript for basic structure, oldish
            looks weird @ different resolutions 
        jquery starting to get old, not a big strike against it tho 
        wufoo forms for WFH additional expense
        see if can submit phony form
        old events are just commented out
        sidegap on mobile
        logo gets jittery near threshhold

   
END GOAL:
    
    RECREATE FIRST, then add fancy
        all necessary pages
         layout:
            base
                template tags for menu/soc?
                get royalty-free page rip if possible
                parallax in mainpicture
                
                Header:
                    when big enough logo & menu on same row, when too small menu collapses into single collapsible toggle button (which gets hidden on zoom in)
                    drop shadow from header
            home
            about
                subset of home
            events
            view 
            volunteer
            donate
            thrift
            WfH
                multi-step form (https://stackoverflow.com/questions/5478432/making-a-django-form-class-with-a-dynamic-number-of-fields,https://www.caktusgroup.com/blog/2018/05/07/creating-dynamic-forms-django/)
                colorful error box
                accepts nonsense for everything but email & Phone

            Contact
            docs - video?

    throw together spreadsheet of pricing difference
    Apache 
        https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/modwsgi/ - get to run w django
        nginx instead?
    Event stuff
        figure out how to pattern non-img'd events
        Photo-Only Event (several container choices?)
        dropdown box for fb
    proxy for drivers? http://benlopatin.com/using-django-proxy-models/
        other alternatives https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#proxy 
        maybe thru personal info?
            https://stackoverflow.com/questions/11472606/adding-fields-to-users-personal-info-in-django-admin-page
    class-based views ?
        https://www.youtube.com/watch?v=TrJtYmfTWiA&list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW&index=37

    SEO hacking
        twitter good for SEO https://www.youtube.com/watch?v=T3GsJgxAB9Q&list=PL7Nf-MXzozDLSk9nLsAkosV9h3C4eBXgn&index=13
        slugs help w SEO?

    TinyMCE for wsyiwyg page editor (https://www.youtube.com/watch?v=bJeTEDRvGVA&list=PL7Nf-MXzozDLSk9nLsAkosV9h3C4eBXgn&index=4)
    GraphQL (graphene) for more specific API calls?
    editable container for info under pic on mainpage (commented-out Statefarm bit )
        checkbox for whether or not is shown 

    CSS Grid for moving based on screensize (https://www.youtube.com/watch?v=M3qBpPw77qo)
    sitemap (https://www.youtube.com/watch?v=xAXMqiPSY34)
    captcha in contact/pickup
    retina (js or otherwise)
    basic slide animations (jq or greensock)
    user-editable translations thru admin - ES, maybe ZH
        knows which translation to provide for other pages?
        "Translator" group connected to specific language - ISO639-1 code included
        has different ways of showing if text is already translated manually
            if not will be google translated (don't want to have to query it each time - saved in other file?)
                https://cloud.google.com/translate/docs/translating-text#translate_translate_text-protocol

    Photo-Only Event (several container choices?)
    clickable asterisk scrolls down to page info
    editable sponsors - scrollbar?
        "WebManager"(or similar) Group can edit sponsors & events
        paypal linked to adding to sponsor in some form?

    ~Major Sponsors~
    format notes
        make pictures editab+le thru admin
    

    pickup scheduling form 
        AJAX form so wont refresh - same w WFH
        sends info to android app db 
            (REST sending to GCM- w authentification: https://techstricks.com/api-authentication-django-and-android-apps/)

        employees in group "Pickup" can change pickup data & call api
        which stops are in which trips editable by truckscheduler javascript applet
        "I want to be notified again " + minute range from 0 - 60 +"mins before arrival"

    active sales 
        make selected sale type affect boxes (generic #1 #2 selected by box?)

    Marketplace (https://www.youtube.com/watch?v=9Wbfk16jEOk)
        connected to fb &/ ebay
            facebook app - out of date? (https://www.youtube.com/watch?v=jxDHNSW28bs&index=10&list=PL7Nf-MXzozDLSk9nLsAkosV9h3C4eBXgn)
        https://developers.facebook.com/docs/marketing-apisre

    "Is Dock Open" badge
        auto open/closed based on hours,have some way (floor app & dock app) to send closing signal outside of regular times
            careful abt server clock - hide if thinks is before like 2010

    map w all marked pts - maybe not since gmaps is dumb now?
        figure out details abt cloud pricing/nonprofit api discounts
        use OpenStreetMap for planning fastest route? or google credits if low volume 

    more in-depth social media integration
    API stuff
        tests - https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1
        authentication
        get better url scheme working
        have specific pickups accessible to specific customers, authorize thru key sent to email?
            scheduling status/updateable & eventually push notification updates?
            editable info until manager locks-in to trip details
    Use Model Forms!!! - crispy too?
        formsets helpful for multiple repeated (sales? still good to know abt if not useful here) https://whoisnicoleharris.com/2015/01/06/implementing-django-formsets.html

    DB backup manager (fixtures?)
    TripScheduler:
        integration to/from gdocs
        get pickups from db/other methods
            AJAX
        each trip gets attached to date & employee(s)
        lock-in trip (no longer donor-changeable, sends to pickup app)
        animations (marching ants,)

    Way down the line goals:
        eventually make better video than that movie maker shit
        connect fancy lights maybe (https://www.youtube.com/watch?v=5zhReMb_Yek&pbjreload=10)
    
DONE:
    git-ify'd :) 
    Truckscheduler 
        base html/js/css skeleton
    API     
        Accessible

    Event  
        reads from db models

    WfH
        Form skeleton
    Base
        CSS grid skeleton for menu
            somewhat responsive
    
TODO:
    media folders more specific 
    fix server time error
    logo changes sizes on screen change
    json multistep form 
    

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