from flask import *
from threading import Thread, Event

game = Flask(__name__)

@game.route('/')
def Main():
	position = {'Lat':[18.75414051,18.75396019,18.75419829,18.7545326,18.75448434,18.7547935],
				'Lon':[73.4051574,73.40542495,73.40600096,73.4063778,73.40681233,73.4070973]}
	return render_template('code.html',result=position)

if __name__ == '__main__':
	game.run()

