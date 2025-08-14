"""
Vocẽ trabalha em um sistema que precisa verificar se todas as senhas digitadas são válidas.
Para uma senhar ser válida deve conter pelo menos 8 caracteres.
"""

"""
Aplicando método dos 5Q's:

1. Quais são os dados de entrada necessários?
Senhas

2. O que devo fazer com esses dados?
Verificar se a senha contém pelo menos 8 caracteres.

3. Quais são os dados de saída esperados?
Uma mensagem indicando se a senha é válida ou não.

4. Quais são as regras de negócio que devem ser aplicadas?
A senha deve conter pelo menos 6 caracteres.

5. Quais são os possíveis erros que podem ocorrer?
Nenhum erro esperado, apenas uma verificação de comprimento da senha.

6. Qual a sequência lógica para resolver o problema?
- Receber a senha como entrada.
- Verificar o comprimento da senha.
- Exibir uma mensagem indicando se a senha é válida ou não.

"""

senhas = ["12345678", "senha123", "abc", "senha_valida_2023", "senha"]

for senha in senhas:
    if len(str(senha)) >= 8:
        print(f"Senha {senha} é válida")
    else:
        print(f"Senha {senha} inválida, deve conter pelo menos 8 caracteres")