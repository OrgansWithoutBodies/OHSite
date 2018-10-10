from wagtail.core import blocks
from wagtail.core.models import Orderable
from wagtail.snippets.blocks import SnippetChooserBlock

import datetime

###WAGTAIL CUSTOM BLOCKS###

class LocBlock(SnippetChooserBlock):
	admin_text='snippet'
	class Meta:
			template='webapp/blocks/loc_block.html'

class ButtonBlock(blocks.StructBlock):#redundant?
	BUTTON_ACTIONS=(('EM','Email'),
		('CP',"Change Page"))

	button_text=blocks.CharBlock(required=True,max_length=20)
	button_action=blocks.ChoiceBlock(choices=BUTTON_ACTIONS)

class TwoPanelBlock(blocks.StructBlock):#Block arranged through CSS Grid, makes content mobile-friendly

	class ContentBlock(blocks.StreamBlock):
		rich_text=blocks.RichTextBlock()

	admin_text='mobile-friendly two-panel grid'

	LHScontent=ContentBlock(label="Left Hand Side Content, mobile-top")
	RHScontent=ContentBlock(label="Right Hand Side Content, mobile-bottom")
	class Meta:
		help_text='Mobile-Friendly Two Panel Grid'
		template='webapp/blocks/twopanel_block.html'

class MapBlock(blocks.StructBlock):#Block of embedded Map - user chooses which backend
#https://wiki.openstreetmap.org/wiki/Deploying_your_own_Slippy_Map
	MAP_CHOICES=(('GM',"Google Maps"),
		('OM',"Open Street Map"))
	maptext="Google Maps no longer provides a free embedded map (though it's effectively free if you don't call it in high volume - still needs payment info to get rid of 'development purposes only' overlay). Open Street Maps is free"
	map_provider=blocks.ChoiceBlock(choices=MAP_CHOICES,default="OM",help_text=maptext)
	#testing lat :38.345813 | testing Longitude: -121.948261 - library

#make location gettable from Location model's address
	map_long = blocks.CharBlock(required=True,max_length=255,default=-121.948261)
	map_lat = blocks.CharBlock(required=True,max_length=255,default=38.345813)
	map_zoom_level = blocks.CharBlock(default=14,required=True,max_length=3,help_text="higher is more zoomed out, lower is zoomed in")

 
	class Meta:
		icon='site'
		template='webapp/blocks/map_block.html'

class EventBlock(blocks.StructBlock):
	event=SnippetChooserBlock(target_model='webapp.Event')

class SocialBlock(blocks.StructBlock):#block of most recent posts to put into streamfield
#register as setting?https://www.youtube.com/watch?v=KJWCGq3IRNc
	profile=SnippetChooserBlock(target_model='webapp.SocialMedia')	
	numposts=blocks.IntegerBlock()#	
	class Meta:
		icon='group'
		help_text="adds a block of social media posts/events/etc"

class InfoBlock(blocks.StructBlock):
	icon=SnippetChooserBlock(target_model='webapp.Icon')
	title=blocks.CharBlock(required=False,max_length=20)
	subtitle=blocks.CharBlock(required=False,max_length=100)
	class Meta:
		icon='cogs'
		help_text="Atomic Element with Icon, header, and description. Reused for more complex blocks"