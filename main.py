import encoder
import decoder

option = input('[1] Encoding\n[2] Decoding\n')
if option == '2':
    image = input('image: ')
    binary = decoder.image_to_binary_text(image)
    base64 = decoder.binary_to_string(binary)
    text = decoder.base64_to_string(base64)
    with open('output.txt', 'w') as f:
        f.write(text)
elif option == '1':
    string = input('string or file: ')
    try:
        with open(string, 'r') as file:
            string = file.read()
        base64 = encoder.string_to_base64(string)
        print(f'base64: {base64}')
        binary = encoder.string_to_binary(base64)
        print(f'Binary: {binary}')
        image = encoder.create_binary_image(binary)
    except:
        base64 = encoder.string_to_base64(string)
        print(f'base64: {base64}')
        binary = encoder.string_to_binary(base64)
        print(f'Binary: {binary}')
        image = encoder.create_binary_image(binary)