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
			src: url(http://rawgit.com/pabloUlloa/proyectofuturo/master/fonts/Marker-Regular.ttf);\
		}\
		.boton{\
			opacity: 0.7;\
			filter: Alpha(opacity=70); /* IE8 and earlier */\
		}\
		.modulo span, .video span{\
			font-size: 16px;\
			font-family: tizaCursiva;\
			cursor: pointer;\
			opacity: 0.8;\
			height: 30px;\
			filter: Alpha(opacity=80); /* IE8 and earlier */\
		}\
		.unidad{\
			height: 110px;\
			width: 610px;\
			background:url(https://rawgit.com/pabloUlloa/proyectofuturo/master/img/unidad.png) no-repeat;\
		}\
		.unidad span{\
			font-size:32px;\
			font-family: tizaImprenta;\
			cursor: pointer;\
			opacity: 0.8;\
			position: absolute;\
			margin-left: 20%;\
			margin-top: 65px;\
		}\
		.modulo{\
			background:url(https://rawgit.com/pabloUlloa/proyectofuturo/master/img/orange.png) no-repeat;\
			background-size:80%;\
			height: 40px;\
		}\
		.video{\
			background:url(https://rawgit.com/pabloUlloa/proyectofuturo/master/img/videoPostit.png) no-repeat;\
			background-size:80%;\
			height: 40px;\
		}\
		.modulo:hover, .video:hover, .boton:hover{\
			opacity: 1;\
			filter: Alpha(opacity=100); /* IE8 and earlier */\
		}\
	");
    x.appendChild(t);
    document.head.appendChild(x);
}