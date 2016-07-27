import webbrowser
import time

url = "https://www.youtube.com/watch?v=86MY-quTiJs"
tempo = 1

print "Iniciado em: ", time.ctime()
while (tempo <= 3):
    time.sleep(3600)
    webbrowser.open(url)
    tempo += 1
    
