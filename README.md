# AdaBot

Bem-vind@ à AdaBot, sua assistente pessoal!

Minha função é lembrar você de suas contas, para assim evitar que você esqueça de realizar o pagamento. Para começar a usar meus serviços basta clicar [aqui](https://wa.me/14155238886), enviar a mensagem **join throat-just** e em seguida **registrar**, e você já poderá registrar suas contas e usufruir de meus lembretes.

Feito seu registro, para cadastrar uma conta, envie uma mensagem com o seguinte formato **conta,[nome da conta],[valor da conta],[data de vencimento]**. Substitua os campos entre colchetes pela respectiva informação, use **.** para separar casas decimais e **dd/mm/aaaa** como formato de data.
Para ver suas contas, basta me enviar a mensagem **listar**.

Todos os dias, às 08:00 horas, enviarei um lembrete para você avisando das suas contas que estão a menos de sete dias de vencer.

Após realizar o pagamento de uma conta, basta me enviar **pagar,[nome da conta]** para que eu a retire dos registros, lembre-se de usar o mesmo nome de conta que foi registrado.

Além disso, caso necessite de um momento de fofura no seu dia, basta me enviar **gato** e te mandarei uma foto fofa de um gatinho.

Para ver essas informações basta me enviar **ajuda**.

## Informações

Bot para Whatsapp desenvolvido usado a API da [Twilio](https://www.twilio.com), do [Dropbox](https://www.dropbox.com/developers/documentation/http/overview) e Python 3.6, usando Flask e outras bibliotecas. O app está hospedado no [Heroku](https://www.heroku.com), e devido ao adormecimento deste, o serviço de alerta das contas que estão para vencer não está funcionando adequadamente.

## Variáveis de Ambiente

Para a execução da aplicação fazem-se necessárias a configuração de algumas variáveis de ambiente:

- account_sid: identificador da sua conta, fornecido pela Twilio.
- auth_token: token de autenticação da sua conta da Twilio.
- dropbox_token: token de autenticação do seu diretório na sua conta do dropbox.
- whatsapp: número utilizado pelo bot no formato **whatsapp:+14155238886**.
