import requests

# Pegar a informação que você quer
requisicao = requests.get("https://www.infomoney.com.br/cotacoes/b3/etf/etf-ethe11/grafico/")
requisicao_dicionario = requisicao.json()
cotacao = float(requisicao_dicionario['cotacaoethe11']['bid'])
print(cotacao)

# enviar email

import smtplib
import email.message


def enviar_email(cotacao):
    corpo_email = f"""
    <p>ETHE11 está acima de R$20.00. Cotação atual:R${cotacao}</p>

    """

    msg = email.message.Message()
    msg['Subject'] = "ETHE11 está acima de R$20.00. "
    msg['From'] = 'brilharmeditacao@gmail.com'
    msg['To'] = 'brilharmeditacao@gmail.com'
    password = 'uqrrsyuowexecsgd'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


if cotacao < 20.0:
    enviar_email(cotacao)

# deploy - heroku

