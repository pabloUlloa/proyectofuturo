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
    var t = document.createTextNode("
		.unidad{
			text-align: justify;
			cursor: pointer;
		    opacity: 0.8;
	    	filter: Alpha(opacity=80); /* IE8 and earlier */
		}

		.unidad:hover{
		    opacity: 1;
	    	filter: Alpha(opacity=100); /* IE8 and earlier */
		}

		.modulo{
			text-align: justify;
			cursor: pointer;
		    opacity: 0.8;
	    	filter: Alpha(opacity=80); /* IE8 and earlier */
		}

		.modulo:hover{
		    opacity: 1;
	    	filter: Alpha(opacity=100); /* IE8 and earlier */
		}
    ");
    x.appendChild(t);
    document.head.appendChild(x);
}