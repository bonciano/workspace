###############################################################################################
##          Enviar correo electrónico a lista de personas con adjunto personalizado          ##
###############################################################################################

# Importo las librerías que voy a utilizar
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Configuro los parámetros del servidor y personalizo el mensaje
smtp = 'smtp.gmail.com'
mail_emisor = '@gmail.com'
password = ''
lista_destinatarios = 'lista_mails.txt'
asunto_mail = 'Prueba de envío de mail desde python'
formato_archivo = '.txt'
html = '''\
        <html>
            <body style="color:#0077b6">
                <p>
                    Hola Persona, cómo estás?<br>
                    Te adjunto un archivo para que veas. Cualquier duda, a disposición.<br>
                    Saludos,<br>
                    Empresa S.A.
                </p>
            </body>
        </html>
        '''

# Lógica de envío de mail a través de una lista de mails con archivos adjuntos
with open(lista_destinatarios,'r') as archivo:
    for linea in archivo:
        linea = linea.replace('\n','')
        campos = linea.split(';')
        mail = campos[0]
        arch = campos[1]
        sender_email = mail_emisor
        receiver_email = mail
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = asunto_mail
        cuerpo_mail = MIMEText(html, 'html')
        message.attach(cuerpo_mail)
        file = arch+formato_archivo
        attachment = open(file,'rb')
        obj = MIMEBase('application','octet-stream')
        obj.set_payload((attachment).read())
        encoders.encode_base64(obj)
        obj.add_header('Content-Disposition','attachment; filename= '+file)
        message.attach(obj)
        my_message = message.as_string()
        email_session = smtplib.SMTP(smtp,587)
        email_session.starttls()
        email_session.login(sender_email, password)
        email_session.sendmail(sender_email,receiver_email,my_message)
        email_session.quit()

# Mensaje de confirmación de envío
print('Los mails fueron enviados correctamente.')
