import requests
import sys
import threading
import os
import persistence

from bill import Bill
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

users = {}

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    userSender = request.values.get('From', '').lower().split(":")[1]
    print(userSender, file=sys.stdout)
    resp = MessagingResponse()
    msg = resp.message()

    if 'registrar' in incoming_msg:

        if userSender in users:
            msg.body("Você já está registrado!")
        else:
            users[userSender] = []
            msg.body("Bem-vindo, você concluiu seu registro!")
            persistence.writeJSON(users)
           
    elif 'conta' in incoming_msg:
        content = incoming_msg.split(",")

        if userSender in users:
            users[userSender].append(Bill(content[1], content[2], content[3]))
            msg.body("Conta registrada!")
        else:
            msg.body("Apenas usuários registrados podem anotar contas!\nEnvie *registrar* para realizar seu registro!")

        persistence.writeJSON(users)

    elif 'listar' in incoming_msg:

        if userSender in users:
            notes = "\n".join(list(map(str, users[userSender])))
            msg.body(notes if notes != "" else "Você não possui contas registradas!\nEnvie *ajuda* para saber como registrar sua conta!")
        else:
            msg.body("Apenas usuários registrados podem listar contas!\nEnvie *registrar* para realizar seu registro!")

    elif 'pagar' in incoming_msg:

        if userSender in users:
            desc = incoming_msg.split(",")[1]
            removed = False

            for conta in users[userSender]:
                if conta.description == desc:
                    users[userSender].remove(conta)
                    msg.body("Ok! Sua conta já foi retirada dos nossos registros!")
                    persistence.writeJSON(users)
                    removed = True

            if not removed:
                msg.body("Não consegui encontrar sua conta, por favor use o comando *listar* e garanta que usou o nome de conta igual ao que foi registrado.")
        
        else:

            msg.body("Vi aqui que você ainda não se registrou, por favor envie *ajuda* para saber como proceder!")
            
    elif 'gato' in incoming_msg:
        msg.media('https://cataas.com/cat')

    elif 'ajuda' in incoming_msg:
        helpMsg = "Bem-vind@ ao AdaBot, sua assistente pessoal!\n"
        helpMsg += "Minha função é lembrar você de suas contas, para assim evitar que você esqueça de realizar o pagamento.\n"
        helpMsg += "Para começar a usar meus serviços basta enviar *registrar* para mim, e você já poderá registrar suas contas e usufruir de meus lembretes.\n"
        helpMsg += "Feito seu registro para cadastrar uma conta, envie uma mensagem com o seguinte formato *conta,<nome da conta>,<valor da conta>,<data de vencimento>*.\n"
        helpMsg += "Substitua os campos com entre <> pela respectiva informação, use . para separar casas decimais e dd/mm/aaaa como formato de data.\n"
        helpMsg += "Para ver suas contas, basta me enviar a mensagem *listar*.\n"
        helpMsg += "Todos os dias, às 08:00 horas, enviarei um lembrete para você avisando das suas contas que estão a menos de sete dias de vencer.\n"
        helpMsg += "Após realizar o pagamento de uma conta, basta me enviar *pagar,<nome da conta>* para que eu a retire dos registros, lembre-se de usar o mesmo nome de conta que foi registrado.\n"
        helpMsg += "Além disso, caso necessite de um momento de fofura no seu dia, basta me enviar *gato* e te mandarei uma foto fofa de um gatinho.\n"

        msg.body(helpMsg)

    else:
        msg.body('Desculpe, mas não entendi sua solicitação, por favor envie *ajuda* para saber o que posso fazer!')

    return str(resp)

@app.route('/')
def hello():
    return redirect("https://www.github.com/issilva5/adabot")

@app.route('/cron', methods=['GET'])
def cron():
    return 'Hello World'

if __name__ == '__main__':
    users = persistence.loadJSON()
    port = int(os.environ.get("PORT", 5000))
    threading.Thread(target=app.run, kwargs={'host': '0.0.0.0','port': port}).start()
    
