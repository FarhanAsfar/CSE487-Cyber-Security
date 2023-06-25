def cipher_decrypt_lower(ciphertext, key):

    decrypted = ""

    for c in ciphertext:

        if c.islower():

            c_index = ord(c) - ord('a')

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decrypted += c_og

        else:
            decrypted += c

    return decrypted


cryptic_text = "xli ehzirxyvi vmhi mr Gerfivve aew ws qygl jyr, Ai aivi ws hvyro ai irhih yt geppmrk"

for i in range(0,26):

    plain_text = cipher_decrypt_lower(cryptic_text, i)

    print("For key {}, decrypted text: {}".format(i, plain_text))