# -*- coding: utf-8 -*-
# @Author: danielcarvalho
# @Date:   2016-12-11 05:55:51
# @Last Modified by:   danielcarvalho
# @Last Modified time: 2016-12-11 06:34:31

import cherrypy

class showTeam(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head><title>Team</title></head>
          <body>
          	<table style="width:50%">
          		<tr align="center">
          			<th>Number</th>
          			<th>Name</th>
          			<th>Age</th>
          		</tr>
          		<tr>
          			<td>1</td>
          			<td>Casillas</td>
          			<td>35</td>
          		</tr>
          		<tr>
          			<td>2</td>
          			<td>Marcano</td>
          			<td>26</td>
          		</tr>
          		<tr>
          			<td>3</td>
          			<td>Felipe</td>
          			<td>27</td>
          		</tr>
          		<tr>
          			<td>4</td>
          			<td>Maxi</td>
          			<td>31</td>
          		</tr>
          		<tr>
          			<td>5</td>
          			<td>Layun</td>
          			<td>27</td>
          		</tr>
          		<tr>
          			<td>6</td>
          			<td>Oliver</td>
          			<td>21</td>
          		</tr>
          		<tr>
          			<td>7</td>
          			<td>Otavio</td>
          			<td>20</td>
          		</tr>
          		<tr>
          			<td>8</td>
          			<td>Danilo</td>
          			<td>21</td>
          		</tr>
          		<tr>
          			<td>9</td>
          			<td>Corona</td>
          			<td>23</td>
          		</tr>
          		<tr>
          			<td>10</td>
          			<td>Jota</td>
          			<td>21</td>
          		</tr>
          		<tr>
          			<td>11</td>
          			<td>Andre Silva</td>
          			<td>20</td>
          		</tr>
          	</table>
          </body>
        </html>"""


if __name__ == '__main__':
	cherrypy.quickstart(showTeam())