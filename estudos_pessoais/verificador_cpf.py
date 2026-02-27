"""
- abcdefghI-JK  onde  I (estado de emissao) J e K(digitos verificadores)
- oito primeiros digitos sao aleatorios
- sobre o I:
    ● 1: Distrito Federal (DF), Goiás (GO), Mato Grosso do Sul (MS), Mato Grosso (MT) e Tocantins (TO);
    ● 2: Acre (AC), Amazonas (AM), Amapá (AP), Pará (PA), Rondônia (RO) e Roraima (RR);
    ● 3: Ceará (CE), Maranhão (MA) e Piauí (PI);
    ● 4: Alagoas (AL), Paraíba (PB), Pernambuco (PE) e Rio Grande do Norte (RN);
    ● 5: Bahia (BA) e Sergipe (SE);
    ● 6: Minas Gerais (MG);
    ● 7: Espírito Santo (ES) e Rio de Janeiro (RJ);
    ● 8: São Paulo (SP);
    ● 9: Paraná (PR) e Santa Catarina (SC);
    ● 0: Rio Grande do Sul (RS).
- calculo do J:
    Os numeros dos 9 primeiros digitos são multiplicados pela sequencia (10,9,8,7...2) e o resultado de cada um é somado
    O resultado é dividido por 11
    se o resto da divisao for menor que 2 (0,1) o J será 0, senão fará 11-resto e o resultado será o J
- O calculo do K é o mesmo que o do J, mas nesse calculo o J entra junto.
"""

cpf= str (input("digite o seu cpf: "))



