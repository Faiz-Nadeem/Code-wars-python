# credit_card=cc8
# len---string\

# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.
# 
# Your task is to write a function maskify, which changes all but the last four characters into '#'.

def maskify(cc):
    return '#' * (len(cc)-4) + cc[-4:]

credit_card="12322342342342234234"
masked_card=maskify(credit_card)
print(masked_card)

