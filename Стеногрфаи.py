from steganocryptopy.steganography import Steganography
Key_text = input("/key.key/" + "Key file:")

Img_text = input("Введите имя файла:")



result = Steganography.decrypt(f'{Key_text}', "img/" + f'{Img_text}' + ".PNG_cecret.png")


with open("secret_message.txt", 'r', encoding='utf-8') as file:
    record = file.read()
    print(record)

input()