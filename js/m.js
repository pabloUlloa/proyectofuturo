function colapsarClase(c){
	if(c.length>1){
		var x = document.getElementsByClassName(c);
		for(i=0;i<x.length;i++){
			x[i].style.display=((x[i].style.display=='none')?'inline':'none');
		}
	}
}
function colapsarVideo(v){
	if(v.length>1){
		var x = document.querySelectorAll("[videoid='"+v+"']");
		for(i=0;i<x.length;i++){
			x[i].style.display=((x[i].style.display=='none')?'inline':'none');
		}
	}
}
function colapsarModulo(m){
	if(m.length>1){
		var x = document.querySelectorAll("[moduloid='"+m+"']");
		for(i=0;i<x.length;i++){
			x[i].style.display=((x[i].style.display=='none')?'inline':'none');
		}
	}
}
function colapsarUnidad(u){
	if(u.length>1){
		var x = document.querySelectorAll("[unidadid='"+u+"']");
		for(i=0;i<x.length;i++){
			x[i].style.display=((x[i].style.display=='none')?'inline':'none');
		}
	}
}
function colapsID(e){
	if(e.length>1){
		var x=document.getElementById(e);
		x.style.display=((x.style.display=='none')?'inline':'none');
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
			src: url(http://rawgit.com/pabloUlloa/proyectofuturo/master/fonts/MarkerRegularRegular2.ttf);\
		}\
		.boton{\
			opacity: 0.7;\
			filter: Alpha(opacity=70); /* IE8 and earlier */\
		}\
		.modulo span, .video span{\
			height: 30px;\
			position: absolute;\
			margin-top: 10px;\
		}\
		.video span{\
			font-size: 16px;\
			font-family: tizaCursiva;\
		}\
		.unidad{\
			height: 110px;\
			width: 610px;\
			background:url(https://rawgit.com/pabloUlloa/proyectofuturo/master/img/unidad.png) no-repeat;\
			opacity: 0.8;\
			filter: Alpha(opacity=80); /* IE8 and earlier */\
		}\
		.unidad span{\
			font-size:32px;\
			font-family: tizaImprenta;\
			cursor: pointer;\
			opacity: 0.8;\
			position: absolute;\
			margin-left: 7%;\
			margin-top: 65px;\
		}\
		.modulo{\
			background:url(https://rawgit.com/pabloUlloa/proyectofuturo/master/img/orange.png) no-repeat;\
			height: 40px;\
			opacity: 0.8;\
			filter: Alpha(opacity=80); /* IE8 and earlier */\
		}\
		.video{\
			background:url(https://rawgit.com/pabloUlloa/proyectofuturo/master/img/videoPostit.png) no-repeat;\
			height: 40px;\
			opacity: 0.8;\
			filter: Alpha(opacity=80); /* IE8 and earlier */\
		}\
		.modulo:hover, .video:hover, .boton:hover, .unidad:hover{\
			opacity: 1;\
			filter: Alpha(opacity=100); /* IE8 and earlier */\
		}\
		.nombreModulo{\
			margin-left:130px;\
			font-family:tizaImprenta;\
			font-size:22px;\
		}\
		.numeroModulo{\
			font-family:tizaCursiva;\
			margin-left:15px;\
		}\
	");
    x.appendChild(t);
    document.head.appendChild(x);
}