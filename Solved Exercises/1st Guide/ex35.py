# -*- coding: utf-8 -*-
# @Author: danielcarvalho
# @Date:   2016-12-11 06:37:52
# @Last Modified by:   danielcarvalho
# @Last Modified time: 2016-12-11 07:07:07

import cherrypy

class sumTwoNumbers(object):
	@cherrypy.expose
	def index(self):
		return """<html>
		  <head><title>Sum 2 Numbers</title></head>
		  <body>
		  	<form method="GET" action="sumTwo">
		  		<input type="text" name="firstNumber">
		  		+
		  		<input type="text" name="secondNumber">
		  		<button type="submit">Sum</button>
		  	</form>
		  </body>
		  </html>"""

	@cherrypy.expose
	def sumTwo(self, firstNumber = None, secondNumber = None):
		sum = int(firstNumber) + int(secondNumber)
		return "{} + {} = {}".format(firstNumber, secondNumber, sum)


if __name__ == '__main__':
	cherrypy.quickstart(sumTwoNumbers())
