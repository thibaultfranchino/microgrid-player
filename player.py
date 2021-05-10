# python 3
# this class combines all basic features of a generic player
import numpy as np


class Player:

	def __init__(self):
		# some player might not have parameters
		self.parameters = 0
		self.horizon = 48

	def set_scenario(self, scenario_data):
		self.data = scenario_data

	def set_prices(self, prices):
		self.prices = prices

	def compute_all_load(self):
		load = np.zeros(self.horizon)
		for time in range(self.horizon):
			load[time] = self.compute_load(time)
		return load

	def take_decision(self, time):
		l_1_v1g = compute_all_load(self)
		l_2_v1g = compute_all_load(self)
		l_3_v1g = compute_all_load(self)
		l_4_v1g = compute_all_load(self)
		l_1_v2g = compute_all_load(self)
		l_2_v2g = compute_all_load(self)
		l_3_v2g = compute_all_load(self)
		l_4_v2g = compute_all_load(self)
		l_4 = l_1_v1g + l_2_v1g + l_3_v1g + l_4_v1g + l_1_v2g + l_2_v2g + l_3_v2g + l_4_v2g
		
		
		
		return 0

	def compute_load(self, time):
		load = self.take_decision(time)
		# do stuff?
		return load

	def reset(self):
		# reset all observed data
		pass
