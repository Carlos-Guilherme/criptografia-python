import cryptocode

mensagem_criptografada = open('mensagem_criptografada.txt', 'a')
mensagem_descriptografada = open('mensagem_descriptografada.txt', 'a')
escolha1 = int(input('criptografar [1]\ndescriptografar [2]'))
if escolha1 == 1:
    mensagem_a_ser_cripto = str(input('digite uma mensagem para criptografar: '))
    senha_a_ser_chaveada = str(input('digite a palavra chave: '))
    str_criptografada = cryptocode.encrypt(mensagem_a_ser_cripto, senha_a_ser_chaveada)
    print(f'mensagem criptografada: {str_criptografada}')
    mensagem_criptografada.write(str_criptografada)
elif escolha1 == 2:
    mensagem_a_ser_descripto = str(input('digite a mensagem: '))
    senha_da_mensagem = str(input('digite a senha: '))
    str_descriptografada = cryptocode.decrypt(mensagem_a_ser_descripto, senha_da_mensagem)
    print(f'mensagem descriptograda: {str_descriptografada}')
    mensagem_descriptografada.write(str_descriptografada)

