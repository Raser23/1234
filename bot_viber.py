from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

bot_configuration = BotConfiguration(
	name='Test1',
	avatar='http://viber.com/avatar.jpg',
	auth_token='4997a6745427d777-56d2e40dd6d22a6a-f686b9bac502445c'
)
viber = Api(bot_configuration)

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/incoming', methods=['POST'])
def incoming():
	print("received request. post data: {0}".format(request.get_data()))
	# handle the request here
	return Response(status=200)

context = ('server.crt', 'server.key')
app.run(host='0.0.0.0', port=443, debug=True, ssl_context=context)