language = int(input('to continue,select language: 1.Azerbaijan,2.English,3.Russian:'))
if language ==1:
    xidmet=int(input('Eziz abonent hansi xidmeti secmey isdiyirsiz?'))
    if xidmet ==1:
        print('Sizi internet prablemine cavabdeh olan insana qosuram')
    elif xidmet ==2:
        print('Sizi kampaniyalara cavabdeh olan insana qosuram')
elif language ==2:
    service = int(input('for which service did you call?'))
    if service ==1:
        print('I will connect you to person who is responsible for internet issue')
    elif service ==2:
        print('I will connect you to person who is responsible for joining any companies about Azercell')
elif language ==3:
    service2 = int(input('как мы можем вам помочь?'))
    if service2==1:
        print('я соединю вас с человеком который отвечает за мобильный интернет')
    elif service2 ==2:
        print('я соединю вас с человеком который отвечает за компании связанные с Азерсел')
        


