Documentação do Script de Monitoramento de Logs e Envio de E-mails
1. Introdução

Este script em Python utiliza a biblioteca pywin32 para monitorar os logs de eventos do Windows e 
enviar e-mails automáticos baseados nos eventos registrados. Ele é útil para verificar o status de operações 
críticas, como backups, através do monitoramento de mensagens específicas nos logs de aplicação.

2. Instalação da Biblioteca

Para utilizar este script, é necessário instalar a biblioteca pywin32 que fornece acesso à API do Windows para 
leitura de logs de eventos. Você pode instalar a biblioteca via pip com o seguinte comando:

bash
Copiar código
pip install pywin32

3. Funcionalidade do Script

O script main.py realiza as seguintes tarefas:

Acesso aos Logs de Eventos:

Utiliza a função OpenEventLog da biblioteca win32evtlog para abrir o log de eventos do Windows. 
O log utilizado é o de tipo Application, que geralmente contém informações sobre aplicativos e serviços.
Leitura dos Últimos Eventos:

Lê os últimos 10 eventos do log de forma reversa, utilizando ReadEventLog. Isso permite acessar informações 
recentes e relevantes para monitoramento.
Verificação de Eventos:

Verifica se o último evento contém a mensagem '5' (que referencia erros) no campo StringInserts. Se encontrado, 
interpreta como um erro no processo de backup, atualizando o corpo do e-mail para indicar o problema.
Envio de E-mail:

Utiliza o protocolo SMTP para enviar um e-mail informando sobre o status do backup. 
O e-mail é enviado utilizando a biblioteca smtplib, garantindo comunicação segura com o servidor SMTP do Gmail (smtp.gmail.com).
4. Configuração Necessária

Antes de executar o script, é necessário configurar a autenticação de aplicativos no Gmail para permitir o 
envio automático de e-mails. Certifique-se de configurar um e-mail e senha válidos no script:

python
Copiar código
email_sender = 'seu_email@gmail.com'  # E-mail remetente (requer autenticação de app)
email_password = 'sua_senha'  # Senha do e-mail remetente (autenticação de app)
email_receiver = 'destinatario@gmail.com'  # E-mail do destinatário
5. Execução

Execute o script main.py para iniciar o monitoramento dos logs e envio de e-mails conforme descrito. 
Certifique-se de que o computador esteja conectado à internet e que o servidor SMTP esteja acessível.

6. Considerações Finais

Este script é adequado para usuários iniciantes a intermediários que desejam automatizar o monitoramento de logs 
de eventos do Windows e receber notificações por e-mail sobre eventos específicos, 
como falhas ou sucesso em operações críticas como backups. 