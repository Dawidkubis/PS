import shelve

databasa = shelve.open('number_names.txt')
AND = 3


def pasta(num, databasa):
    assert(num < 100), 'LOL REKT 420'
    if str(num) in databasa.keys():
        return databasa[str(num)]
    else:
        return databasa[str(num - num % 10)] + databasa[str(num % 10)]

syme = 0
for i in range(1, 1_001):
    if i == 1_000:
        syme += len(databasa[str(i)])
        continue
    hunderts = i - i % 100
    if hunderts == 0:
        syme += len(pasta(i, databasa))
        continue
    hunderts = str(hunderts)[0]
    syme += len(databasa[hunderts]) + len(databasa['100'])
    if i % 100 != 0:
        syme += len(pasta(i % 100, databasa))
        syme += AND


#databasa.close()
