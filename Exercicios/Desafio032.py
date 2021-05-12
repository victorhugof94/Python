import datetime
ano = int(input('qual ano para analise e de aperta 0 sera o ano atual:'))
if ano == 0:
    ano == datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print('o ano {} é bissexto'.format(ano))
else:
    print('o ano {} nao é bissexto'.format(ano))
