var isExtended = 0;

function slideSideBar(){

	new Effect.toggle('MobileSideBarContents', 'blind', {scaleX: 'true', scaleY: 'true;', scaleContent: false});
	
	if(isExtended==0){
		$('MobileSideBarTab').childNodes[0].src = $('MobileSideBarTab').childNodes[0].src.replace(/(\.[^.]+)$/, '-active$1');
		
		new Effect.Fade('MobileSideBarContents',
   	{ duration:1.0, from:0.0, to:1.0 });
		
		isExtended++;
	}
	else{
		$('MobileSideBarTab').childNodes[0].src = $('MobileSideBarTab').childNodes[0].src.replace(/-active(\.[^.]+)$/, '$1');
		
		new Effect.Fade('MobileSideBarContents',
   	{ duration:1.0, from:1.0, to:0.0 });
		
		isExtended=0;
	}
	
}

function init(){
	Event.observe('MobileSideBarTab', 'click', slideSideBar, true);
}

Event.observe(window, 'load', init, true);
