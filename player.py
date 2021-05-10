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
		arr_dep = list(scenario_data_values())[:self.nb_slow + self.nb_fast]
		self.depart = {"slow": [d[1] for d in arr_dep[:self.nb_slow]], "fast": [d[1] for d in arr_dep[self.nb_slow:self.nb_fast + self.nb_slow]]}
		self.arrival = {"slow": [d[0] for d in arr_dep[:self.nb_slow]], "fast": [d[0] for d in arr_dep[self.nb_slow:self.nb_fast + self.nb_slow]]}

	def set_prices(self, prices):
		self.prices = prices

	def compute_all_load(self):
		load = np.zeros(self.horizon)
		for time in range(self.horizon):
			load[time] = self.compute_load(time)
		return load

	def take_decision(self, time):
		#mettre self.l_1_v1g  ?
		l_1_v1g = compute_all_load(self)
		l_2_v1g = compute_all_load(self)
		l_3_v1g = compute_all_load(self)
		l_4_v1g = compute_all_load(self)
		l_1_v2g = compute_all_load(self)
		l_2_v2g = compute_all_load(self)
		l_3_v2g = compute_all_load(self)
		l_4_v2g = compute_all_load(self)
		if (time == self.horizon) and 
		(3*0.25 > l_1_v1g[time] or 3*0.25 > l_2_v1g[time] 
		 or 22*0.25 > l_3_v1g[time] or 22*0.25 > l_4_v1g[time]):
			# on paie une amende de 5euros par vehicule
		l_4 = l_1_v1g + l_2_v1g + l_3_v1g + l_4_v1g + l_1_v2g + l_2_v2g + l_3_v2g + l_4_v2g
		while (abs( l_4[time]) <= 40) 
		and (l_1_v1g[time] <= 3 and l_2_v1g[time] <= 3) 
		and (l_3_v1g[time] <= 22 and l_4_v1g[time] <= 22)
		and (abs(l_1_v2g[time]) <= 3 and abs(l_2_v2g[time]) <= 3) 
		and (abs(l_3_v2g[time]) <= 22 and abs(l_4_v2g[time]) <= 22):
			
		return 0

	def compute_load(self, time):
		load = self.take_decision(time)
		# do stuff?
		return load

	def reset(self):
		# reset all observed data
		pass
