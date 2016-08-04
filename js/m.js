function colapsarClase(c){
	if(c.length>1){
		var x = document.getElementsByClassName(c);
		for(i=0;i<x.length;i++){
			x[i].style.display=((x[i].style.display=='none')?'':'none');
		}
	}
}
function colapsarVideo(v){
	if(v.length>1){
		var x = document.querySelectorAll("[videoid='"+v+"']");
		for(i=0;i<x.length;i++){
			x[i].style.display=((x[i].style.display=='none')?'':'none');
		}
	}
}
function colapsarModulo(m){
	if(m.length>1){
		var x = document.querySelectorAll("[moduloid='"+m+"']");
		for(i=0;i<x.length;i++){
			x[i].style.display=((x[i].style.display=='none')?'':'none');
		}
	}
}
function colapsarUnidad(u){
	if(u.length>1){
		var x = document.querySelectorAll("[unidadid='"+u+"']");
		for(i=0;i<x.length;i++){
			x[i].style.display=((x[i].style.display=='none')?'':'none');
		}
	}
}
function colapsID(e){
	if(e.length>1){
		var x=document.getElementById(e);
		x.style.display=((x.style.display=='none')?'':'none');		
	}
}
function crearClases(){
	var x = document.createElement("STYLE");
    var t = document.createTextNode("\
		@font-face {\
			font-family: tizaCursiva;\
			src: url(http://rawgit.com/pabloUlloa/proyectofuturo/master/fonts/CoalhandLukeTRIAL.ttf);\
		}\
		@font-face {\
			font-family: tizaImprenta;\
			src: url(http://rawgit.com/pabloUlloa/proyectofuturo/master/fonts/Marker-Regular.otf);\
		}\
		.boton{\
			opacity: 0.7;\
			filter: Alpha(opacity=70); /* IE8 and earlier */\
		}\
		.modulo, .video{\
			text-align: justify;\
			font-size: 16px;\
			font-family: tizaCursiva;\
			cursor: pointer;\
			opacity: 0.8;\
			height: 30px;\
			filter: Alpha(opacity=80); /* IE8 and earlier */\
		}\
		.unidad{\
			font-size:24px;\
			text-align: justify;\
			font-family: tizaImprenta;\
			cursor: pointer;\
			opacity: 0.8;\
			height: 50px;\
			background:url(https://rawgit.com/pabloUlloa/proyectofuturo/master/img/unidad.png) no-repeat;\
			background-size:90%;\
		}\
		.modulo{\
			background:url(https://rawgit.com/pabloUlloa/proyectofuturo/master/img/orange.png) no-repeat;\
			background-size:90%;\
		}\
		.video{\
			background:url(https://rawgit.com/pabloUlloa/proyectofuturo/master/img/videoPostit.png) no-repeat;\
			background-size:90%;\
		}\
		.modulo:hover, .video:hover, .boton:hover{\
			opacity: 1;\
			filter: Alpha(opacity=100); /* IE8 and earlier */\
		}\
	");
    x.appendChild(t);
    document.head.appendChild(x);
}