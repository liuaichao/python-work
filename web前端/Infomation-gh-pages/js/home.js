// JavaScript Document


;
var ROOT_URL ='';
$(function(){
	
	var planetTravelConfig = {
		flyStarImage	: [ [ ROOT_URL +'images/star-fly-1.png' , 23 ,23 ] ],
		flashStarImage	: [ [ ROOT_URL +'images/star-flash-1.png' , 30 ,27 ] , [ ROOT_URL +'images/star-flash-2.png' , 40 ,40 ], [ ROOT_URL +'images/star-flash-2.png' , 40 ,40 ] ],
		flashStarDensity	: 0.3 	,
		flyMakeStarTime		: 5000 , 
		flyMakestarNum		: 2  	
	};
	
	if( '\v' == 'v' ){ /*如果是 IE6,7,8*/
		planetTravelConfig.flyMakeStarTime	=  8000 ; 
		planetTravelConfig.flyMakestarNum	=  1 
	} 
	
	$('body').planetTravel(planetTravelConfig);	
/*	if(is_home){
		$('body').css({'overflow':'hidden'});
	}*/
	
	
	julying.gridMenu.menu = Array(		
		{ name : 'about-me' ,  	pos : rand( 1 , 15 )  },
		{ name : 'contact-me' , pos : rand( 20 ,35 )  },
		{ name : 'blog' ,  		pos : rand( 40 , 55 )  },						
		{ name : 'link' , 		pos : rand( 60 , 70 ) }
	); 
	julying.gridMenu.init('#julyingGridMenu') ;
	$('strong[name=replace]').each(function(){
		$(this).html( $(this).attr('val'));
	});
	
});
