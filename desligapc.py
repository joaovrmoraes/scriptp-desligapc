import subprocess
from datetime import datetime

data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")
data_e_hora_em = data_e_hora_atuais.strftime("%d%m%Y%H%M")

with open("config/pc.txt", "r") as tf:
    lines = tf.read().split(',')

with open("config/msg.txt", "r") as tf:
    msg = tf.read()

for line in lines:
    Computer_List = [line]
    for Computer in Computer_List:
        print("Desligando o PC:" + Computer)
        a = subprocess.getoutput(
            "shutdown /m \\\\" + Computer + " /f /s /c"+msg+"/t 60"+msg) + '\n'
        arquivo = open('logs/log['+data_e_hora_em+'].txt', 'a')
        arquivo.write(Computer + ' : ')
        if len(a) > 2:
            arquivo.write("Desligado  [" +
                          data_e_hora_em_texto + "]\n")
        else:
            arquivo.write("Ok  [" +
                          data_e_hora_em_texto + "]\n")
        arquivo.close()
