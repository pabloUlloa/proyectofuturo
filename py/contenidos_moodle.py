# -*- coding: cp1252 -*-
import json
import codecs
import os
import webbrowser
import parser
from random import randint

RAMOS=["json/algebra1.json",
       "json/algebra2.json",
       "json/calculo1.json",
       "json/calculo2.json",
       "json/calculo3.json",
       "json/ecua.json",
       "json/electro.json",
       "json/fisica1.json",
       "json/fisica2.json"]
RUTA=[""]

def lanzar(url):
    webbrowser.open_new_tab(url)

def formatJson(s):
    return json.dumps(s,ensure_ascii=False,sort_keys=False,indent=4)

def loadJson(ruta):
    with codecs.open(ruta,'r',encoding='utf-8') as f:
        s=f.read()
        f.close()
    return json.loads(s)

def saveJson(ruta,Json):
    with codecs.open(ruta,'w',encoding='utf-8') as f:
        f.write(formatJson(Json))
        f.close()
    return None

def cls():
    os.system('cls')

def dnld():
    print "Actualizando archivos desde servidor"
    os.system("git pull")
    raw_input("Archivos actualizados exitosamente, presiona Enter para continuar")
    
def upld():
    print "Actualizando archivos hacia el servidor"
    os.system("git add .")
    os.system("git commit -m \"commit autogenerado id "+str(randint(1,100000))+"\"")
    os.system("git push")
    raw_input("Archivos actualizados exitosamente, presiona Enter para continuar")

def sync():
    print "Actualizando archivos desde servidor"
    os.system("git pull")
    print "Actualizando archivos hacia el servidor"
    os.system("git add .")
    os.system("git commit -m \"commit autogenerado id "+str(randint(1,100000))+"\"")
    os.system("git push")
    raw_input("Archivos actualizados exitosamente, presiona Enter para continuar")

def banner():
    cls()
    print "\n"+"="*43+"\n===\t\tProyecto Futuro\t\t===\n"+"="*43+"\n\n\n"
    print u"""Opciones globales:
\tMENU\t=> Ir a men� principal
\tSALIR\t=> Salir de aplicaci�n
\tVOLVER\t=> Volver al nivel anterior
\tGENERAR\t=> Generar la salida en HTML
\tDWNLD\t=> Descargar archivos desde el servidor externo
\tUPLD\t=> Cargar archivos hacia el servidor externo
\tSYNC\t=> Sincronizar archivos con el servidor externo (DWNLD & UPLD)
"""

def inp(s):
    r=raw_input(s+u"\n> ")
    if r.upper()=="EXIT" or r.upper()=="SALIR":
        exit(1)
    elif r.upper()=="MENU":
        menu()
    elif r.upper()=="GENERAR":
        generar()
    elif r.upper()=="SYNC":
        sync()
        menu()
    elif r.upper()=="DWNLD":
        dnld()
        menu()
    elif r.upper()=="UPLD":
        upld()
        menu()
    return r

def eligeRamo():
    opciones=u"""
Elige una asignatura
1) �lgebra I para Ingenier�a
2) �lgebra II para Ingenier�a
3) C�lculo I para Ingenier�a
4) C�lculo II para Ingenier�a
5) C�lculo III para Ingenier�a
6) Ecuaciones Diferenciales para Ingenier�a
7) Electricidad y Magnetismo para Ingenier�a
8) F�sica 1 para Ingenier�a
9) F�sica 2 para Ingenier�a
"""
    banner()
    print opciones
    opc=inp("")
    if opc=="VOLVER":
        menu()
    while opc not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print u"ingresa una opci�n v�lida"
        inp("Enter para continuar")
        banner()
        print opciones
        opc=inp("")
    return opc

def verUnidades(ramo):
    opciones=u"\nElige una unidad\n"
    i=1
    for u in ramo[u'unidades']:
        opciones+=str(i).encode('utf-8')+u") "+u[u'nombre']+u"\n"
        i+=1
    banner()
    print ramo[u'asignatura']
    print opciones
    unidad=inp("")
    if unidad.upper()=="VOLVER":
        verRamo(ramo)
    try:
        while int(unidad)-1 not in range(len(ramo[u'unidades'])):
            print u"ingresa una opci�n v�lida"
            inp("Enter para continuar")
            verUnidades(ramo)
        verModulos(ramo,int(unidad)-1)
    except ValueError:
        print u"ingresa una opci�n v�lida"
        inp("Enter para continuar")
        verUnidades(ramo)

def verModulos(ramo,unidad):
    opciones=u"\nElige un m�dulo\n"
    i=1
    for u in ramo[u'unidades'][unidad][u'modulos']:
        opciones+=str(i).encode('utf-8')+u") "+u[u'nombre']+u"\n"
        i+=1
    banner()
    print ramo[u'asignatura']+u"\n\t"+ramo[u'unidades'][unidad][u'nombre']
    print opciones
    modulo=inp("")
    if modulo.upper()=="VOLVER":
        verUnidades(ramo)
    try:
        while int(modulo)-1 not in range(len(ramo[u'unidades'][unidad][u'modulos'])):
            print u"ingresa una opci�n v�lida"
            inp("Enter para continuar")
            verModulos(ramo,unidad)
        verVideos(ramo,unidad,int(modulo)-1)
    except ValueError:
        print u"ingresa una opci�n v�lida"
        inp("Enter para continuar")
        verModulos(ramo,unidad)

def verVideos(ramo,unidad,modulo):
    opciones=u"\nPara ver un video, elige uno del listado\nPara agregar un video escribe AGREGAR\nPara eliminar escribe ELIMINAR\nPara modificar escribe MODIFICAR\n\nVideos:\n"
    i=1
    for u in ramo[u'unidades'][unidad][u'modulos'][modulo][u'videos']:
        opciones+=str(i).encode('utf-8')+u") "+u[u'nombre']+u"\n"
        i+=1
    banner()
    print ramo[u'asignatura']+u"\n\t"+ramo[u'unidades'][unidad][u'nombre']+u"\n\t\t"+ramo[u'unidades'][unidad][u'modulos'][modulo][u'nombre']
    print opciones
    opc=inp("")
    if opc.upper()=="VOLVER":
        verModulos(ramo,unidad)
    try:
        if opc.upper()=="AGREGAR":
            agregarVideo(ramo,unidad,modulo)
        elif opc.upper()=="ELIMINAR":
            eliminarVideo(ramo,unidad,modulo)
        elif opc.upper()=="MODIFICAR":
            modificarVideo(ramo,unidad,modulo)
        while int(opc)-1 not in range(len(ramo[u'unidades'][unidad][u'modulos'][modulo][u'videos'])):
            print u"ingresa una opci�n v�lida"
            inp("Enter para continuar")
            verVideos(ramo,unidad,modulo)
        lanzar(ramo[u'unidades'][unidad][u'modulos'][modulo][u'videos'][int(opc)-1][u'url'])
        verVideos(ramo,unidad,modulo)
    except ValueError:
        print u"ingresa una opci�n v�lida"
        inp("Enter para continuar")
        verVideos(ramo,unidad,modulo)

def agregarVideo(ramo,unidad,modulo):
    banner()
    print ramo[u'asignatura']+u"\n\t"+ramo[u'unidades'][unidad][u'nombre']+u"\n\t\t"+ramo[u'unidades'][unidad][u'modulos'][modulo][u'nombre']
    nombre=inp(u"Ingresa el nombre del video: ")
    url=inp(u"Ingresa la URL del video: ")
    video={u"nombre":nombre,u"url":url}
    ramo[u'unidades'][unidad][u'modulos'][modulo][u'videos'].append(video)
    saveJson(RUTA[0],ramo)
    ramo=loadJson(RUTA[0])
    verVideos(ramo,unidad,modulo)

def eliminarVideo(ramo,unidad,modulo):
    opciones=u"\nElige el video que deseas eliminar\n"
    i=1
    for u in ramo[u'unidades'][unidad][u'modulos'][modulo][u'videos']:
        opciones+=str(i).encode('utf-8')+u") "+u[u'nombre']+u"\n"
        i+=1
    banner()
    print ramo[u'asignatura']+u"\n\t"+ramo[u'unidades'][unidad][u'nombre']+u"\n\t\t"+ramo[u'unidades'][unidad][u'modulos'][modulo][u'nombre']
    print opciones
    opc=inp("")
    if opc.upper()=="VOLVER":
        verVideos(ramo,unidad,modulo)
    try:
        while int(opc)-1 not in range(len(ramo[u'unidades'][unidad][u'modulos'][modulo][u'videos'])):
            print u"ingresa una opci�n v�lida"
            inp("Enter para continuar")
            verVideos(ramo,unidad,modulo)
        ramo[u'unidades'][unidad][u'modulos'][modulo][u'videos'].pop(int(opc)-1)
        saveJson(RUTA[0],ramo)
        ramo=loadJson(RUTA[0])
        verVideos(ramo,unidad,modulo)
    except ValueError:
        print u"ingresa una opci�n v�lida"
        inp("Enter para continuar")
        eliminarVideo(ramo)

def modificarVideo(ramo,unidad,modulo):
    opciones=u"\nElige el video que deseas modificar\n"
    i=1
    for u in ramo[u'unidades'][unidad][u'modulos'][modulo][u'videos']:
        opciones+=str(i).encode('utf-8')+u") "+u[u'nombre']+u"\n"
        i+=1
    banner()
    print ramo[u'asignatura']+u"\n\t"+ramo[u'unidades'][unidad][u'nombre']+u"\n\t\t"+ramo[u'unidades'][unidad][u'modulos'][modulo][u'nombre']
    print opciones
    opc=inp("")
    if opc.upper()=="VOLVER":
        verVideos(ramo,unidad,modulo)
    try:
        while int(opc)-1 not in range(len(ramo[u'unidades'][unidad][u'modulos'][modulo][u'videos'])):
            print u"ingresa una opci�n v�lida"
            inp("Enter para continuar")
            verVideos(ramo,unidad,modulo)
        nombre=inp(u"Ingresa el nombre del video: ")
        url=inp(u"Ingresa la URL del video: ")
        if "http://" not in url:
            url="http://"+url
        video={u"nombre":nombre,u"url":url}
        ramo[u'unidades'][unidad][u'modulos'][modulo][u'videos'][int(opc)-1]=video
        saveJson(RUTA[0],ramo)
        ramo=loadJson(RUTA[0])
        verVideos(ramo,unidad,modulo)
    except ValueError:
        print u"ingresa una opci�n v�lida"
        inp("Enter para continuar")
        modificarVideos(ramo,unidad,modulo)

def menu():
    r=int(eligeRamo())-1
    RUTA[0]=RAMOS[r]
    ramo=loadJson(RUTA[0])
    verUnidades(ramo)


def formatoUnidad(u,i):
    n=u"Unidad "+str(i).encode("utf-8")+u": "+u[u'nombre']
    colapses=""
    for mid in u[u'toggleId']:
        colapses+=u"colapsID('"+mid.encode("utf-8")+u"');"
    formato="""

<hr />
<p class="unidad" onclick=\""""+colapses+"""" style="cursor:pointer;"><span>"""+n+"""</span></p>

"""
    return formato

def formatoModulo(n,j,i):
    mid=str(i)+" "+str(j)
    n1=u"M�dulo "+str(j).encode("utf-8")+u": "
    formato="""

\t<hr />
\t<p class="modulo" onclick="colapsarClase('modulo"""+str(mid).encode("utf-8")+"""')" style="cursor:pointer;">
\t<span class="numeroModulo">"""+n1+"""</span><span class="nombreModulo">"""+n+"""</span>
\t</p>"""
    return formato

def formatoVideo(n,u,i,j):
    mid=str(i)+" "+str(j)
    embed=u.replace("watch?v=","embed/")
    vid=embed.replace("https","http").replace("http://www.youtube.com/embed/","")
    formato="""
\t<div class="modulo"""+str(mid).encode("utf-8")+"""" style="margin-left:30px;display:none;">
\t<p class="video" onclick="colapsID('"""+vid+"""');" style="cursor:pointer;margin-left:30px;">
\t<span style="margin-left: 50px;">"""+n+"""</span>
\t</p>
\t<div id=\""""+vid+"""" style="display: none;"><center>
\t<iframe src=\""""+embed+"""?rel=0" allowfullscreen="" frameborder="0" height="169" width="300"></iframe>
\t</center></div>
\t</div>
"""
    return formato

def noVideo(i,j):
    mid=str(i)+" "+str(j)
    vid=str(randint(1,10000))
    n1=u"[Videos a�n no disponibles]"
    formato="""
\t<div class="modulo"""+str(mid).encode("utf-8")+"""" style="margin-left:30px;display:none;">
\t<p class="video" onclick="colapsID('"""+vid.encode("utf-8")+"""');" style="cursor:pointer;margin-left:30px">
\t<span style="margin-left: 50px;">"""+n1+"""</span>
\t</p>
\t</div>
"""
    return formato


def generar():
    for ruta in RAMOS:        
        r=loadJson(ruta)
        out=u""
        colapses=u""
        i=1
        for u in r[u'unidades']:
            out+=u"="*77+u"\n"+str(i).encode("utf-8")+u" "+u[u'nombre']+u"\n"+u"="*77+u"\n"
            out+=formatoUnidad(u,i)+u"\n\n"
            j=1
            for m in u[u'modulos']:
                out+=u"\t"+u"-"*77+u"\n\t"+str(j).encode("utf-8")+u" "+m[u'nombre']+u"\n\t"+u"-"*77+u"\n"
                out+=formatoModulo(m[u'nombre'],j,i)+u"\n"
                if len(m[u'videos'])==0:
                    out+=noVideo(i,j)
                for v in m[u'videos']:
                    out+=formatoVideo(v[u'nombre'],v[u'url'],i,j)
                j+=1
                out+=u"\n"*4
            out+=u"\n\n"
            for mid in u[u'toggleId']:
                colapses+=u"colapsID('"+mid.encode("utf-8")+u"');\n"
            i+=1
            out+=u"\n"*12
        out=out+u"#"*77+u"\n\n<p><br /></p>\n<script>\n"+colapses+"</script>\n<p><br /></p>"
        with codecs.open("html/"+ruta.split("/")[1].split(".")[0]+".txt",'w',encoding='utf-8') as f:
            f.write(out)
            f.close()
    menu()

menu()
