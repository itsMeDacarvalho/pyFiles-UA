# -*- coding: utf-8 -*-
# @Author: danielcarvalho
# @Date:   2016-12-24 04:05:01
# @Last Modified by:   danielcarvalho
# @Last Modified time: 2016-12-24 04:11:24

teams = ["Porto", "Benfica", "Sporting", "Braga"]

for (i, team) in enumerate(teams):
	for x in range(i+1, len(teams)):
		print("{} x {}".format(team, teams[x]))