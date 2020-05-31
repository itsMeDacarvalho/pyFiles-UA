# -*- coding: utf-8 -*-
# @Author: danielcarvalho
# @Date:   2016-12-11 07:09:09
# @Last Modified by:   danielcarvalho
# @Last Modified time: 2016-12-11 07:40:20

import cherrypy

class makeTeamTable(object):
	"""docstring for makeTeamTable"""
	@cherrypy.expose
	def index(self):
		return """<html>
		  <head><title>Sum 2 Numbers</title></head>
		  <body>
		  	<form method="GET" action="getPlayersInFile">
		  		<input type="text" name="filename">
		  		<button type="submit">Load Team</button>
		  	</form>
		  </body>
		  </html>"""



	@cherrypy.expose
	def getPlayersInFile(self, filename = None):
		file = open(filename, 'r')

		listWithTeam = []
		
		for i in range(1,13):
			listWithTeam.append(file.readline())

		print(listWithTeam)

		return """<html>
      			<head><title>Team</title></head>
	      		<body>
	      			<table style="width:100%">
	      				<tr align="center">
	      					<th>Name</th>
	      				</tr>
	      				<tr align="center">
	      					<td>{}</td>
	      				</tr>
	      				<tr align="center">
	      					<td>{}</td>
	      				</tr>
	      				<tr align="center">
	      					<td>{}</td>
	      				</tr>
	      				<tr align="center">
	      					<td>{}</td>
	      				</tr>
	      				<tr align="center">
	      					<td>{}</td>
	      				</tr>
	      				<tr align="center">
	      					<td>{}</td>
	      				</tr>
	      				<tr align="center">
	      					<td>{}</td>
	      				</tr>
	      				<tr align="center">
	      					<td>{}</td>
	      				</tr>
	      				<tr align="center">
	      					<td>{}</td>
	      				</tr>
	      				<tr align="center">
	      					<td>{}</td>
	      				</tr>
	      				<tr align="center">
	      					<td>{}</td>
	      				</tr>
	      			</table>
	      			
	      			<p align="center">Treinador: {}</p>
	      		</body>
	    		</html>""".format(listWithTeam[0].rstrip(), listWithTeam[1].rstrip(), listWithTeam[2].rstrip(), listWithTeam[3].rstrip(), listWithTeam[4].rstrip(), listWithTeam[5].rstrip(), listWithTeam[6].rstrip(), listWithTeam[7].rstrip(), listWithTeam[8].rstrip(), listWithTeam[9].rstrip(), listWithTeam[10].rstrip(), listWithTeam[11].rstrip())

if __name__ == '__main__':
	cherrypy.quickstart(makeTeamTable())




