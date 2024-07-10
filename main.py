import win32evtlog
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

server_smtp = "smtp.gmail.com"
port = 587

email_sender = 'seuemail@gmail.com'
email_password ='senha de app google'

email_receiver = 'emailenvio@gmail.com'
subject = 'BKP Server 01'

# Variável para o corpo do e-mail
email_body = ""

# Criação do objeto MIMEMultipart para o e-mail
message = MIMEMultipart()
message["From"] = email_sender
message["To"] = email_receiver
message["Subject"] = subject
message.attach(MIMEText(email_body, "html")) 

log_type = 'System'
computer_name = '.'

# Abrir o log de eventos
event_log_handle = win32evtlog.OpenEventLog(computer_name, log_type)

try:
    # Ler eventos do log (últimos 10 eventos)
    events = win32evtlog.ReadEventLog(event_log_handle, win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ, 0)
    
    messages = []

    for event in events:
        message_text = event.StringInserts  # Renomeando para evitar conflito com 'message'
        if message_text is not None:
            messages.append(message_text)
        print(f'Evento ID: {event.EventID}, Tipo: {event.EventType}, Mensagem: {message_text}')

    # Verifica se há mensagens no log
    if messages:
        last_message = messages[-1]
        # numeros referen aos tipos de erros encontrados nos logs do windows 
        error_codes = ['20', '10001', '15', '3', '7000', '7032', '7031', '7023', '7009', '1058', '6008', '5774']
        
        # Verifica se algum dos códigos de erro está presente em last_message
        if any(code in str(last_message) for code in error_codes):
            email_body = """<h1>Erro ao subir o backup</h1>"""
            print("Erro no backup (verificar).")
        else:
            email_body = """<h1>Sucesso ao subir o backup</h1>"""
            print("Backup subiu.")
    else:
        email_body = """<h1>Sucesso ao subir o backup (sem erros no log)</h1>"""
        print("Backup subiu (sem erros no log).")

    # Atualiza o corpo do e-mail no objeto message
    message.attach(MIMEText(email_body, "html"))

    try:
        server = smtplib.SMTP(server_smtp, port)
        server.starttls()
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_receiver, message.as_string())
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar e-mail: {str(e)}')
    finally:
        server.quit()

finally:
    # Fechar o log de eventos
    win32evtlog.CloseEventLog(event_log_handle)
