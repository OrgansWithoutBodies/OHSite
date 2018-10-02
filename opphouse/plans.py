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
        "thirft store"
        "our work" repurposed for sponsorships lol 
        no https
        their own URL only links to them on main page, only page which doesn't load socmedia footer
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
        major sponsors all specific artboards w simple outline/dropshadow??? weird & not flexible, easily do-able in pure html/css
        logo gets jittery near threshhold
        obvious that some effort was put in at first, then additional things added to site are half-assed patch jobs trying to repurpose template elements not tailored to us
        "attains self sufficiency" image dissapears on lowres
        Donate-> WFH is fucked up on mobile
        if home overlay buttons go to single-column they get fucked up
        <i> tag used as shortcut for icon is rly /awful/ practice
            <i> is technically italic, but twitter bootstrap (the free package this company is selling to you) has that as its default for icon
            if icon can't load, no alt-text:
                visually impaired users don't get anything, which isn't necessarily awful when its a tiny icon but stil
        volunteer page doesn't have location for shelter (footer doesn't count, be consistent)
END GOAL:
    
    RECREATE FIRST, then add fancy
        all necessary pages
         layout:
            base
                template tags for menu/soc?
                    https://djangobook.com/basic-template-tags-filters/
                    https://docs.djangoproject.com/en/2.1/howto/custom-template-tags/
                get royalty-free page rip if possible
                        make repeat
                parallax in mainpicture
                
                Header:
                    make socmedia hug rhs
                    when big enough logo & menu on same row, when too small menu collapses into single collapsible toggle button (which gets hidden on zoom in)
                    drop shadow from header
                Footer:
                    other soc media area
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
                wheelsforhope@ohousesolano.com
            Contact
                    clickable intended target to contact?
            docs - video?

    throw together spreadsheet of pricing difference
    ARIA accessibility (https://www.youtube.com/watch?v=g9Qff0b-lHk)
    Apache 
        https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/modwsgi/ - get to run w django
        nginx instead?
    Event stuff
        (several container choices? - have some sorta logic to determine which fields to show, decided in view?)
                figure out how to pattern non-img'd events
                Photo-Only Event
        dropdown box for fb
        if price is 0 change $ to free
        format event times
        attachable documents (wsyiwyg?)
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
    'Page' model has things like tab title, menu title, menuorder, mainpic, footerinfo, picoverlaytitle,
        only webadmin can add/remove, webmanager can edit/view (until CMS)
        "call to action"
        somehow can add in things like hours/wfh overlay
        
        swappable menuorder

    CSS Grid for moving based on screensize (https://www.youtube.com/watch?v=M3qBpPw77qo)
    sitemap (https://www.youtube.com/watch?v=xAXMqiPSY34)
    captcha in contact/pickup
    retina (js or otherwise)
    basic slide animations (jq or greensock)
    user-editable translations thru admin - ES, maybe ZH
        Django-CMS includes 
        knows which translation to provide for other pages?
        "Translator" group connected to specific language - ISO639-1 code included
        has different ways of showing if text is already translated manually
            if not will be google translated (don't want to have to query it each time - saved in other file?)
                https://cloud.google.com/translate/docs/translating-text#translate_translate_text-protocol

    clickable asterisk scrolls down to page info
    Sponsors
        "WebManager"(or similar) Group can edit sponsors & events
        paypal linked to adding to sponsor in some form?
        sidescrolling mode
        center last row?
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
            overlay specific color,different color on hover
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
            css grid:
                https://codepen.io/matuzo/post/animating-css-grid-layout-properties
                https://codepen.io/matuzo/pen/rmQvMG

    Way down the line goals:
        eventually make better video than that movie maker shit
        connect fancy lights maybe (https://www.youtube.com/watch?v=5zhReMb_Yek&pbjreload=10)
        copy other opphouses for SEO - donation bins also cool https://opphouse.org/contact-us/#warehouse
        integrate clock
        wishlist

DONE:
    git-ify'd :) 

    Truckscheduler 
        base html/js/css skeleton
    API     
        Accessible

    Event  
        reads from db models
        outline of placement

    WfH
        Form skeleton
    Base
        CSS grid skeleton for menu
            somewhat responsive

    Thrift-store
        skeleton
    Sponsors
        skeleton
        variable sized grid
    
TODO:
    media folders more specific 
    fix server time error
    logo changes sizes on screen change
    json multistep form 
    sponsors images/autowrap
    socmedia footer - socmedia Model to keep
            snapchat/youtube/paypal as other options for logos
    center major sponsor images
    location model/box
        boxfn which gives a box for 

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