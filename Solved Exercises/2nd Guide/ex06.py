# -*- coding: utf-8 -*-
# @Author: danielcarvalho
# @Date:   2016-12-26 17:33:47
# @Last Modified by:   danielcarvalho
# @Last Modified time: 2016-12-28 03:59:38

def troco(preco, pagamento, caixa):
	tipo = ["1 centimo", "2 centimos", "5 centimos", "10 centimos", "20 centimos", "50 centimos", "1€", "2€"]
	caixa_final = [0] * 8

	if pagamento-preco == 0:
		return caixa

	if pagamento-preco > 0:
		excesso = pagamento-preco
	
	while excesso != 0 and sum(caixa) > 0:
		if (excesso >= 200) and (caixa[7] > 0):
			excesso = excesso - 200
			caixa_final[7] = caixa_final[7] + 1
			caixa[7] = caixa[7] -1

		elif (excesso >= 100) and (caixa[6] > 0):
			excesso = excesso - 100
			caixa_final[6] = caixa_final[6] + 1
			caixa[6] = caixa[6] -1

		elif (excesso >= 50) and (caixa[5] > 0):
			excesso = excesso - 50
			caixa_final[5] = caixa_final[5] + 1
			caixa[5] = caixa[5] -1

		elif (excesso >= 20) and (caixa[4] > 0):
			excesso = excesso - 20
			caixa_final[4] = caixa_final[4] + 1
			caixa[4] = caixa[4] -1

		elif (excesso >= 10) and (caixa[3] > 0):
			excesso = excesso - 10
			caixa_final[7] = caixa_final[7] + 1
			caixa[3] = caixa[3] -1

		elif (excesso >= 5) and (caixa[2] > 0):
			excesso = excesso - 5
			caixa_final[2] = caixa_final[2] + 1
			caixa[2] = caixa[2] -1

		elif (excesso >= 2) and (caixa[1] > 0):
			excesso = excesso - 2
			caixa_final[1] = caixa_final[1] + 1
			caixa[1] = caixa[1] -1

		elif (excesso >= 1) and (caixa[0] > 0):
			excesso = excesso - 1
			caixa_final[0] = caixa_final[0] + 1
			caixa[0] = caixa[0] -1

	if excesso == 0:
		put_comma = False
		show_message = "Entregue -> "
		for i in range(0, len(caixa_final)):
			if caixa_final[i] != 0:
				if not put_comma:
					show_message = show_message + "{} x {}".format(caixa_final[i], tipo[i])
					put_comma = True
				else:
					show_message = show_message + " + {} x {}".format(caixa_final[i], tipo[i])
		print(show_message)
		print(caixa)
	else:
		print("Moedas insuficientes para fornecer troco")

troco(1200, 1700, [2,2,2,2,2,2,2,2])




