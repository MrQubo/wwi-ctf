from Crypto.PublicKey import RSA 

keys = [RSA.generate(1024, e=3) for _ in range(3)]

flag = "wwi{NeverImplementYourOwnCrypto}"*3
flag_int = sum([(ord(flag[i]) << (i*8)) for i in range(len(flag))])

print ("flag len bits:", len(flag)*8)
print ("flag_int:", flag_int)

for key in keys:
    print("n=", key.n)
    print("e=", key.e)
    print("flag_enc=", pow(flag_int, 3, key.n))
    print()
