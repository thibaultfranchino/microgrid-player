# python 3
# this class combines all basic features of a generic player
import numpy as np
import pandas as pa
random_lambda = np.random.rand(48)
class Player:

	def __init__(self):
		# some player might not have parameters
		self.parameters = 0
		self.horizon = 48
		self.nb_slow=2
		self.nb_fast=2
		self.pslow=3
		self.pfast=22
		self.capacite=10
		self.rho_c=0.95


	def set_scenario(self, scenario_data):
		self.data = scenario_data
		# depart et arr contiennent respectivement la liste des heures de départ et d'arrivée des véhicules à la date d
		d="01/01/2014"
		self.depart = list(scenario_data[(scenario_data["day"] == d)]["time_slot_dep"][:p.nb_slow + p.nb_fast])
		self.arr = list(scenario_data[(scenario_data["day"] == d)]["time_slot_arr"][:p.nb_slow + p.nb_fast])

	def set_prices(self, prices):
		self.prices = prices

	def compute_all_load(self):
		load = np.zeros(self.horizon)
		# on stocke dans une variable temporaire load_tmp la liste load pour pouvoir mettre les valeurs dans l'ordre dans load par la suite
		load_tmp=np.zeros(self.horizon)

		#chargement rend compte du fonctionnement du chargement des EVs
		chargement=np.zeros(self.nb_slow+self.nb_fast)

		
		# on fait une boucle sur les pas de temps de horizon
		# on remplit les valeurs de load_tmp au fur et a mesure en commencant par les EV lents
		for time in range(self.horizon):
			consommation=0

			for i in range(self.nb_slow):
				# on charge soit au chargement maximal (pslow) soit jusqu'au chargement complet (40 - consommation)
				# soit a la charge suffisante de 25% (10 - chargement[i])
				# pour choisir on prend le minimum de ces conditions (on charge seulement ce qui est necessaire)
				ajout = min((10 - chargement[i])/self.rho_c, min(self.pslow, 40 - consommation))
				chargement[i] += self.rho_c * ajout
				consommation += self.rho_c * ajout

			for i in range(self.nb_slow,self.nb_slow+self.nb_fast):
				#A EXPLIQUER
				ajout = min((10 - chargement[i])/self.rho_c, min(self.pfast, 40 - consommation))
				chargement[i] += self.rho_c * ajout
				consommation += self.rho_c * ajout
			
			load_tmp[time]=consommation

		# on fait correspondre les termes de load les plus importants aux prix les plus faibles
		minimum = np.min(self.depart)
		prices_copy=self.prices[:minimum].copy()
		k=0
		while k<minimum:
			arg_min = np.argmin(prices_copy)
			arg_max=np.argmax(load_tmp)
			load[arg_min]=load_tmp[arg_max]
			prices_copy[arg_min] = np.inf
			load_tmp[arg_max] = 0
			k+=1
			#load[t] = self.compute_load(t)
		print(load)
		return load

	def take_decision(self, time):
		# TO BE COMPLETED
		return 0

	def compute_load(self, time):
		load = self.take_decision(time)

		return load

	def reset(self):
		# reset all observed data
		pass

fichier=pa.read_csv(ev_scenario, sep = ";","ev_scenarios.csv")
p=Player()
p.__init__()
p.set_scenario(fichier)
p.set_prices(random_lambda)

l=p.compute_all_load()

# on implemente la fonction de cout
def cout(p,l):
	c=0
	for time in range(48):
		c+=l[time]*p[time]
	return c
print(cout(p.prices,l))

if __name__=="__main__":
	import os
	print(os.getcwd())
	fichier=pa.read_csv("ev_scenarios.csv") #mettre le chemin complet si cela ne marche pas
	p=Player()
	p.__init__()
	p.set_scenario(fichier)
	p.set_prices(random_lambda)
	
	l=p.compute_all_load()
