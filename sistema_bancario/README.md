# 🏦 Banco Money – Simulador de Operações Bancárias em Python

Este projeto é um **programa simples em Python** que simula operações bancárias básicas, permitindo ao usuário realizar depósitos, saques e visualizar um extrato detalhado.  
O sistema possui regras de limite de saque e quantidade de saques diários, simulando um cenário real de uso.

---

## 📋 Funcionalidades

- **Depósito**:
  - Adiciona saldo à conta.
  - Bloqueia valores negativos.
  - Registra cada depósito no extrato.

- **Saque**:
  - Limite de **R$ 500,00 por saque**.
  - Limite diário de **3 saques**.
  - Impede saque se não houver saldo suficiente.
  - Registra cada saque no extrato.

- **Extrato**:
  - Lista todas as movimentações realizadas.
  - Exibe saldo final.
  - Mostra mensagem caso não existam transações.

- **Encerramento**:
  - O programa pode ser encerrado a qualquer momento selecionando a opção "Sair".

## 📚 Aprendizados Durante o Desenvolvimento

Durante o desenvolvimento deste projeto, foram reforçados e aplicados conceitos importantes de Python e de lógica de programação, tais como:

1. **Entrada e saída de dados**
   - Uso de `input()` para receber informações do usuário.
   - Utilização de `print()` para exibir mensagens formatadas.
   - Aplicação de *f-strings* para formatação de valores monetários e mensagens.

2. **Controle de fluxo**
   - Estruturas condicionais (`if`, `elif`, `else`) para tomada de decisão.
   - Estrutura de repetição (`while True`) para manter o programa em execução até que o usuário opte por sair.

3. **Tratamento de erros**
   - Implementação de `try/except` para capturar exceções, como `ValueError`, evitando que o programa seja encerrado inesperadamente.

4. **Validação de dados**
   - Impedir depósitos de valores negativos.
   - Bloquear saques acima do saldo disponível ou do limite diário.
   - Respeitar o valor máximo permitido por saque.

5. **Definição de regras de negócio**
   - Controle de limite de **R$ 500,00** por saque.
   - Limitação de **3 saques diários**.
   - Registro detalhado das movimentações no extrato.

6. **Manipulação de strings**
   - Armazenamento de registros de transações na variável `extrato`.
   - Exibição formatada das operações realizadas.

7. **Boas práticas**
   - Uso de constantes (`VALOR_MAXIMO_SAQUE`, `SAQUES_DISPONIVEIS`) para facilitar manutenção.
   - Código organizado e legível para fácil compreensão e futuras melhorias.

