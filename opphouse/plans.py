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
        "Close Dock Early" button
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
            integrate git?



    
helpful resources:
    https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/modwsgi/ (Apache)
    https://www.html5rocks.com/en/tutorials/speed/parallax/ (HTML5 Parallax)
    https://scrimba.com/g/gR8PTE (CSS Grid)
    https://ultimatedjango.com/learn-django/lessons/create-the-project-base-template/(navbar/django templating)
    https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django (good in-depth tutorial)
    https://www.youtube.com/watch?v=-oWIyFYyNQw&list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW&index=26 (eps 23-28 are good overview of form details)
    https://www.youtube.com/watch?v=zojnkKGRXp0 (form mixins ~8 min)
    https://www.youtube.com/watch?v=8QKOaTYvYUA (CSS-Only Collapsing Menubar w animations - for when mobile-sized)
    http://www.dwuser.com/education/content/creating-responsive-tiled-layout-with-pure-css/ (css squarecard)
    https://demo.itsupportguides.com/ajax-upload-for-gravity-forms/multi-page-form-ajax-enabled/ (forms + AJAK)
    https://www.youtube.com/watch?v=3cRT1RmCyKg (deploy django w nginx & gunicorn)
    https://jossingram.wordpress.com/2015/04/22/a-list-of-wagtails-streamfield-icons/ (wagtail streamfield icons for custom blocks)
    https://www.w3schools.com/howto/howto_js_form_steps.asp (multistep)
    https://css-tricks.com/using-svg/ (good info on using svg's w html/css)
    https://despreneur.com/15-best-websites-to-download-free-icons/ (good list of attribution-free icon sites, make sure to check!!!)
    https://ahackersday.com/blog/djitter-how-to-build-a-twitter-clone-using-django-2-0-part-one/
current site 
    problems:
        shutterstock images ew
        video "TO FIND OUT MORE INFORMAION ABOUT DONATION" should be plural - Jittery R
        home image has transparent overlay, no other pages - maybe intentional, most likely lazy
                NOPE, its bc they changed it to an overlay w 10%
        most requests of special resized images return 404, implying most of javascript was just stuff they put bc "thats how we do it" w/o actually understanding
        convoluted way of scheduling pickups
        stupid expensive, largely bootstrap
        barely optimized for mobile (line wraps, horizontalgroup buttons, non-persistent menu(stylistic but still), nonclickable phone #'s,basic forms, dreamweaver rly intended for static/old webpages)
        "thirft store"
        "our work" repurposed for sponsorships lol 
        no https - bad for SEO
        their own URL only links to them on main page, only page which doesn't load socmedia footer
        parallax gets screwy on small screens
        redundant contact, different zips means hardcoded instead of shared vars (sloppy!!)
        very late 90's early00's vibe (Dreamweaver templates pretty outdated nowadays)
        "get in involved" on thrift store page (even main page has different lol)
        Donation Exclusion list has inconsistent formatting
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
            <i> is technically italic, but bootstrap (the free package this company is selling to you) has that as its default for icon
            font-awesome stuff rly is just pretending to be text - ends up loading hundreds (thousands?) of unneccessary images just for the ~10 being used
            if icon can't load, no alt-text:
                visually impaired users don't get anything, which isn't necessarily awful when its a tiny icon but stil
        volunteer page doesn't have location for shelter (footer doesn't count, be consistent)
        map loads whole-ass html page, unneccessary & slow tho not technically ~wrong~
        at some zoom levels social media overlaps edge
        wfh has no fade-in
        donate boxes should alternate at least
                map pin moves arbitrarily
                inconsistent capitalization
        article section isnt padded on mobile-size
                only clickable is tiny texts
        "about us" reloads page when not already pointing to index
                points to "supportive services" div instead of div container for some reason, not necessarily bad just weird, implies opportunityhouse.us and opportunityhouse.us/index don't point to the same place
END GOAL:
    
    RECREATE FIRST, then add fancy
        all necessary pages
        SPRITES
                render small svg on upload page - need to learn a bit of react?
                icons as document collection?
                https://css-tricks.com/svg-sprites-use-better-icon-fonts/
                https://www.creativebloq.com/features/the-complete-guide-to-svg/6
                https://css-tricks.com/using-svg/
                https://css-tricks.com/svg-fallbacks/
                https://stackoverflow.com/questions/38722155/wagtail-how-do-i-populate-the-choices-in-a-choiceblock-from-a-different-model ?
         layout:            
            base
                make $.php redirect to appropriate page of new site
                template tags for menu/soc?
                    https://djangobook.com/basic-template-tags-filters/
                    https://docs.djangoproject.com/en/2.1/howto/custom-template-tags/
                get royalty-free page rip if possible
                        make repeat
                        make as ::after/::before content
                parallax in mainpicture
                
                Header:
                    make socmedia hug rhs
                    drop shadow from header
                    img centers when only one in line
                    When menu button visible menu becomes vertical      
                            if button not visible, then menu shows regardless of checked state - Javascript?
                            dotted line separator when vertical
                Footer:
                    other soc media area
                    black
            home
            events
            view 
            volunteer
            donate

            thrift
                    embed video, can change later
            WfH
                multi-step form (https://stackoverflow.com/questions/5478432/making-a-django-form-class-with-a-dynamic-number-of-fields,https://www.caktusgroup.com/blog/2018/05/07/creating-dynamic-forms-django/)
                colorful error box
                accepts nonsense for everything but email & Phone
                wheelsforhope@ohousesolano.com
            Contact
                    clickable intended target to contact?
            docs - video?
    Article section (tries to figure out date title etc from url)
            URL
            Image
            Title
            Date
            Author
            Publication
            Blurb


    throw together spreadsheet of pricing difference (https://docs.google.com/spreadsheets/d/1wkseKZ3j3e-UH9up9c-58f7nyBXildynh7NiN8scjJ0/edit#gid=0)
        emphasize manager-editibility & overpaying for the level we have atm
        run speedtests to compare
        VPS comparisons https://www.webstack.de/blog/e/cloud-hosting-provider-comparison-2017/
            "Scaleways network is good, sadly inconsistent, but as with OVH you don't pay for any overusage. If you need to push a lot of public bandwidth, you should go with Vultr, otherwise OVH is a great fit. If you need predictable performance you should think about DigitalOcean or Linode."
        nice-looking graphsa
        mention ~famous django users~ (Instagram, PBS, NASA)
        Digital Ocean reliably like 1000 concurrent visiters, we'll be fine: https://www.quora.com/How-many-unique-visitors-can-DigitalOceans-10-plan-handle-per-day-on-WordPress
        "I can make that video in one hour"
        SLACK for group messages/team communication 
            can be separated department from department as wanted
            (popular users: NASA)
            lightweight phone apps
            optional sms notification
            free unless you plan on having more than 10,000 (searchable) messages 
            mailchimp, dropbox, polls, etc integrations
            integration with google drive
                examples - bot notifies when schedule is updated
            Bots can do whatever you want
        have rough skeletons of other easily addable features
                Dock button transmit from android
                Marketplace sketchup
               
    ARIA accessibility (https://www.youtube.com/watch?v=g9Qff0b-lHk)
       
    Admin
            make char lens consistent
            auto-resize images?

    proxy for drivers? http://benlopatin.com/using-django-proxy-models/
        other alternatives https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#proxy 
        maybe thru personal info?
            https://stackoverflow.com/questions/11472606/adding-fields-to-users-personal-info-in-django-admin-page
    class-based views ?
        https://www.youtube.com/watch?v=TrJtYmfTWiA&list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW&index=37

    SEO hacking
        twitter good for SEO https://www.youtube.com/watch?v=T3GsJgxAB9Q&list=PL7Nf-MXzozDLSk9nLsAkosV9h3C4eBXgn&index=13
        slugs help w SEO?

    GraphQL (graphene) for more specific API calls?

    editable container for info under pic on mainpage (commented-out Statefarm bit )
        Title, Subtitle, Button Text, Button Redirect
        checkbox for whether or not is shown 
        includes 50px padding below & line
    
       
    sitemap (https://www.youtube.com/watch?v=xAXMqiPSY34)
    captcha in contact/pickup
    retina (js or otherwise)
    basic slide animations (jq or greensock)?
    user-editable translations thru admin - ES, maybe ZH
        Wagtail includes
        knows which translation to provide for other pages?
        "Translator" group connected to specific language - ISO639-1 code included
        has different ways of showing if text is already translated manually
            if not will be google translated (don't want to have to query it each time - saved in other file?)
                https://cloud.google.com/translate/docs/translating-text#translate_translate_text-protocol

  
    pickup scheduling form 
        AJAX form so wont refresh - same w WFH
        sends info to android app db 
            (REST sending to GCM- w authentification: https://techstricks.com/api-authentication-django-and-android-apps/)

        employees in group "Pickup" can change pickup data & call api
        which stops are in which trips editable by truckscheduler javascript applet
        "I want to be notified again " + minute range from 0 - 60 +"mins before arrival"

    API stuff
        tests - https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1
        authentication - 
        
        have specific pickups accessible to specific customers, authorize thru key sent to email?
            scheduling status/updateable & eventually push notification updates?
            editable info until manager locks-in to trip details
    Use Model Forms!!! - crispy too?
        formsets helpful for multiple repeated (sales? still good to know abt if not useful here) https://whoisnicoleharris.com/2015/01/06/implementing-django-formsets.html
    Admin:
       More JS https://docs.djangoproject.com/en/2.1/ref/contrib/admin/javascript/
       Able to generate documentation: https://docs.djangoproject.com/en/2.1/ref/contrib/admin/admindocs/
    DB backup manager (fixtures?)
    TripScheduler:
        integration to/from gdocs
        write custom templating to be able to index? or just use some other js language? dunno
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
                make sure equal or under 10MB
                10 slides ~5 secs each
        connect fancy lights maybe (https://www.youtube.com/watch?v=5zhReMb_Yek&pbjreload=10)
        copy other opphouses for SEO - donation bins also cool https://opphouse.org/contact-us/#warehouse
        integrate clock
        wishlist
        Marketplace (https://www.youtube.com/watch?v=9Wbfk16jEOk)
            connected to fb &/ ebay
                facebook app - out of date? (https://www.youtube.com/watch?v=jxDHNSW28bs&index=10&list=PL7Nf-MXzozDLSk9nLsAkosV9h3C4eBXgn)
            https://developers.facebook.com/docs/marketing-apisre
    
        active sales 
            make selected sale type affect boxes (generic #1 #2 selected by box?)
        Seasonal decoration

    

DONE:
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
        Menu button for base w rough sliding
        Only shows call to action if not blank
        fade-in for header text (https://stackoverflow.com/questions/11679567/using-css-for-fade-in-effect-on-page-load#11681331)
    Home
        About-Us redirect working (make sure tiles don't mess it up)
    
        Sponsors
            skeleton
            variable sized grid 
            whole grid clickable, alignment janky but working 
    General:
        git-ify'd :) 
        Media folders more specific 
        Page Model mostly implemented
        Map Block w host chooser
         
    Thrift:
        clickable asterisk scrolls down to page info
        Dock Widget:
            mostly done
            auto open/closed based on hours, accessible thru API
    Wagtail:



TODO:
    Icon
    more in-depth social media integration
            overlay specific color,different color on hover
            have inv masks?
            populates fields based on url
            socialmedia blocks

    SASS?
    maps:
        make able to reference location model address
        google maps: figure out details abt cloud pricing/nonprofit api discounts
        https://github.com/springload/wagtailgmaps for addresses?
    Specific Page Content doesn't seem to load saved info in editor
    Redis for better caching
    CMS stuff (Wagtail?)
        https://docs.wagtail.io/en/v2.1.1/getting_started/integrating_into_django.html
    mailing list (UGLY!), move sponsors
    Page model implementation smoother
          'Page' model controls menu stuff
           only webadmin can add/remove, webmanager can edit/view (until CMS)
         
            titletext can be img
            somehow can add in things like hours/wfh overlay?
                (subtitle type?)
       
    "Is Dock Open" badge
            careful abt server clock - hide if thinks is before like 2010 or smth
            "scheduled" different than "early"
    FIX SPONSOR BOX SIZE???
    make sure things look ok w/o grid!!!
    fix server time error
    contact map
    Events:
         better grids for events
            event images uploadable from url
            (several container choices? - have some sorta logic to determine which fields to show, decided in view?)
            figure out how to pattern non-img'd events
            Photo-Only Event
        dropdown box for fb
        if price is 0 change $ to 'free'
        format event times better
        attachable documents (wsyiwyg?)
    gridless image card centering (absolute padding?)
    
    Make menu button less janky
    page title form shows {title}+"Opportunity House | Vacaville's Homeless Shelter"
    logo changes sizes on screen change
    multistep form 
    get menu button placement down/which size mediaqueries do what fine-tuned
    sponsors images
        Sponsors w/o images have nice text
        make sure cards on last row are centered
        figure out whether limit vert or hor based on imsize
        only "WebManager"(or similar) Group can edit sponsors & events
        paypal linked to adding to sponsor in some form?
        sidescrolling mode
        
    socmedia footer - socmedia Model to keep consistent/editable
            snapchat/youtube/paypal as other options for logos
    location model/box
        "infoblock" used in streamfield
        boxfn which gives a box for specified N
        donateblurb
        volunteerblurb
        INCLUSION on every page - https://stackoverflow.com/questions/10859769/django-multiple-template-inheritance-is-this-the-right-style#10860682

    
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