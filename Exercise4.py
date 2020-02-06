
hero = {'Name':'Holder1', 'Speciality':'Something', 'Age':'Holder3', 'Weapon':'holder4'}
hero['Name'] = input('What do you want the hero to be called?:').lower().strip()
hero['Speciality'] = input('What is his speciality?:').lower().strip()
hero['Age'] = input('What is his age?:').strip()
hero['Weapon'] = input('Finally, what is his weapon?:').lower().strip()


quest= {'Beginning':'holder1', 'Middle':'holder2', 'End':'holder3',  'Hero':hero, 'Villen' : 'placedholder5'}


quest['Beginning'] = f'There once was a man named {quest["Hero"]["Name"]}, he flew around the world using his magic {quest["Hero"]["Weapon"]}. He was then attacked by the evil villian'
quest['Middle'] = f'The batle was crazy and they fought till the princess was saved. He was great at {quest["Hero"]["Speciality"]}'
quest['End'] = f'They then lived happily ever after after they bought a castle in the mountains. They lived together for {str(100-int(quest["Hero"]["Age"]))} years'


print(quest['Beginning'] + '\n' + quest['Middle'] + '\n' + quest['End'] + '\n' + 'The End')

