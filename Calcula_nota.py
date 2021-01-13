def calcular_media(notas): #função 
	quantidade = len(notas)
	soma = sum(notas)
	media = soma / quantidade
	return media
def verificar_aprovacao(media):
	if media >= 6:
	  print('Aluno aprovado!')
	else: 
	  print('Aluno reprovado!')

notas = [10, 8, 9, 7]
media = calcular_media(notas)
print ('O aluno tirou', media)
verificar_aprovacao(media)
