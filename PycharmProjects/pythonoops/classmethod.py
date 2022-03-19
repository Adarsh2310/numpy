class Mobile:
    fp='yes'

    @classmethod
    def is_fp(cls):
        print('fringerprint',cls.fp)

sam=Mobile()
apple=Mobile()

print("Samsung:",Mobile.fp)
print("Apple:",Mobile.fp)

print()
Mobile.fp='no'
print("Samsung:",Mobile.fp)
print("Apple:",Mobile.fp)



