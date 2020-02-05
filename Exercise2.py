
quest= {'Beginning':'holder1', 'Middle':'holder2', 'End':'holder3'}



quest['Beginning'] = f'There once was a man named Chris, he flew around the world using his magic wand. He was then attacked by the evil villian'
quest['Middle'] = f'The batle was crazy and they fought till the princess was saved. He was great at magic'
quest['End'] = 'They then lived happily ever after after they bought a castle in the mountains. They lived together for 20 years'


print(quest)
print(type(quest))
print(quest.keys())
print(quest.values())
print(quest['Beginning'])
print(quest['Middle'])
print(quest['End'])

quest['Hero']='Chris'