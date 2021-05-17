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
		# depart et arr contiennent respectivement la liste des heures de départ et d'arrivée des véhicules à la date d
		d="01/01/2014"
		self.depart=list(scenario_data[(scenario_data["day"] == d)]["time_slot_dep"][:p.nb_slow + p.nb_fast])
		self.arr = list(scenario_data[(scenario_data["day"] == d)]["time_slot_arr"][:p.nb_slow + p.nb_fast])

	def set_prices(self, prices):
		self.prices = prices

	def compute_all_load(self):
		load = np.zeros(self.horizon)
		loadbis=np.zeros(self.nb_slow+self.nb_fast)
		for time in range(self.horizon):
			conso=0
			for i in range(self.nb_slow):
				plus = self.rho_c * min(self.pslow, min((10 - loadbis[i])/self.rho_c, 40 - conso))
				loadbis[i] += plus
				conso += plus
			for i in range(self.nb_slow,self.nb_slow+self.nb_fast):
				plus=self.rho_c*min(self.pfast,min((10-loadbis[i])/self.rho_c,40-conso))
				loadbis[i]+=plus
				conso+=plus
			load[time]=conso
		compteur=self.horizon-1
		
		m = np.min(self.depart)
		prix=self.prices[:m].copy()
		arg_max=0
		compteur=0
		while compteur<m:
			arg_min = np.argmin(prix)


p.set_scenario(f)
p.set_prices(random_lambda)


l=p.compute_all_load()

#fonction de cout qui ne prend pas encore en compte les amendes si les voitures ne sont pas chargées à temps
def cout(p,l):
	c=0
	for time in range(48):
		c+=l[time]*p[time]
	return c
print(cout(p.prices,l))
