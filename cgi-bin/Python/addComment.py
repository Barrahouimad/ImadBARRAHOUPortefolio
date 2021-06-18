#!/usr/bin/python3
# coding:utf-8

##
#  Ecriture dans fichier "guestbook.html"
#  Paramètres reçus par méthode POST
#
 
import cgi, cgitb , datetime

# Lecture des données formulaire
form = cgi.FieldStorage() 
nom = form.getvalue('nom')
prenom = form.getvalue('prenom')
email = form.getvalue('email')
comment = form.getvalue('comment')
x = datetime.datetime.now()

gb = open("/home/ginf2022/ibarrahou/public_html/comments.html", "a")
gb.write('<div class="card" style="height:320px;border:1px brown solid;border-radius: 10px;font-size: 27px;margin-right: 24%;margin-left:22%;margin-top:10px;">')
gb.write('<div style="font-size:130%;margin-left:10%;margin-top:70px;margin-right:15%;">')
gb.write('<em style="color:brown;">De : </em>&nbsp;&nbsp;&nbsp;'+str(nom)+" ")
gb.write(str(prenom)+" <br />")
gb.write('<em style="color:brown;">Email : </em>&nbsp;&nbsp<span style="color:black">' +
         str(email)+"</span><br>")
gb.write('<em style="color:brown;">Message : </em>&nbsp;&nbsp;<span style="color:chite">' +
         str(comment.replace('\n', '<br>'))+"</span><br>")
gb.write('</div>')
gb.write('</div>')

gb.close()

# Sortie sur UA de l'accusé de réception
print ("Content-type: text/html; charset=UTF-8\n")
a = """
<!DOCTYPE html>
<html>
<head>
<title>Merci!...</title>
</head>
<body>
<script>document.location.href='http://yasmina.emi.ac.ma/~ibarrahou/comments.html'</script>
</body>
</html>
"""
print(a)
