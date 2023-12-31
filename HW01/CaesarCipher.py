def cipher_encrypt(plain_text, key):

    encrypted = ""

    for c in plain_text:

        if c.isupper():

            c_index = ord(c) - ord('A')

            c_shifted = (c_index + key) % 26 + ord('A')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.islower():

            c_index = ord(c) - ord('a')

            c_shifted = (c_index + key) % 26 + ord('a')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.isdigit():
            c_new = (int(c) + key) % 10

            encrypted += str(c_new)

        else:
            encrypted += c

    return encrypted


def cipher_decrypt(ciphertext, key):

    decrypted = ""

    for c in ciphertext:

        if c.isupper():

            c_index = ord(c) - ord('A')


            c_og_pos = (c_index - key) % 26 + ord('A')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.islower():

            c_index = ord(c) - ord('a')

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.isdigit():
            c_og = (int(c) - key) % 10

            decrypted += str(c_og)

        else:
            decrypted += c

    return decrypted

plain_text = "Mate, the adventure ride in Canberra was so much fun, We were so drunk we ended up calling 911!"

ciphertext = cipher_encrypt(plain_text, 4)

print("Plain text message:\n", plain_text)

print("Encrypted ciphertext:\n", ciphertext)
print("\n")


ciphertext = "Qexi, xli ehzirxyvi vmhi mr Gerfivve aew ws qygl jyr, Ai aivi ws hvyro ai irhih yt geppmrk 355!"

decrypted_msg = cipher_decrypt(ciphertext, 4)

print("The cipher text:\n", ciphertext)

print("The decrypted message is:\n",decrypted_msg)