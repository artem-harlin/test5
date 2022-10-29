from functools import reduce 
s = ['nau4itsya plesti ribolovnie seti', 'obu4at neironnie seti', 'pauk lovit v seti muh']
print(sum(map(lambda x: 'seti' in x.lower(), s)))

