from random import sample, randint

def random_generator():
	rand_generator = sample(range(7, 12), 3)
	quantity = sample(range(1, 7), 3)
	expected_goal = randint(50,240)

	buttons = []

	for i in range(3):
		buttons.append(((rand_generator[i] * expected_goal)/(sum(rand_generator)) / quantity[i]))

	return = buttons[0]*quantity[0] + buttons[1]*quantity[1] + buttons[2]*quantity[2]

if __name__ == '__main__':
	goal = random_generator()
	counter = 0

	while goal > counter:
		print str(goal - counter) + ' left'
		player_input = raw_input('>> Enter button (1, 2, 3): ')
		counter += buttons[int(player_input) - 1]

	if goal == counter:
		print 'YOU WIN!!'
	else:
		print 'YOU LOSE, TRY AGAIN'