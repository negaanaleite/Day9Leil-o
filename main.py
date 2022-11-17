from replit import clear
from art import logo
print(logo)

lances = {}
fim_lance = False

def encontar_maior_lance(maior_lance):
	lance_maior= 0
	vencedor = ""

	for licitante in maior_lance:	
		lance_valor = maior_lance[licitante]
		if lance_valor > lance_maior:
			lance_maior = lance_valor
			vencedor = licitante
	print(f"O vencedor é {vencedor} com um lance de ${maior_lance}")		

				
while not fim_lance:
	nome = input("Participante: ")
	dinheiro = int(input("Qual seu lance: R$"))
	lances[nome] = dinheiro
	deve_continuar = input("Existem outros Leiloeiros? Digite 'sim' ou 'não'.\n")
	if deve_continuar == "não":
		fim_lance = True
		encontar_maior_lance(lances)
	elif deve_continuar == "sim":
		clear()

			
	