
# 📊 Projeto Power BI - Mercado de Ações

## 1. Informações Gerais do Projeto

**Nome do Projeto:** Análise de dados da bolsa de valores eletrônica americana NASDAQ

**Responsável:** Renan Costa  

**Data de Início:** 25/04/2025

**Data de Conclusão:** -

**Versão Atual:** 1.0  

**Setor/Departamento:** Mercado de Ações  

---

## 2. Requisitos do Projeto

- Obter o **total de volume negociado de ações ao longo do tempo** para as 5 empresas analisadas.
- Calcular o **valor médio de abertura (_Open_), mais alto (_High_), mais baixo (_Low_) e de fechamento (_Close_) das ações de todas as empresas, para todos os meses do período analisado (5 anos)**.
- Calcular a **variação da média do valor de fechamento (_Close_)** das ações de todas as empresas ao longo do tempo, mês a mês.
- Explicar as **principais características e tendências nos dados**.
- Deve ser possível realizar a análise para **uma única empresa ou uma combinação de empresas**.

---

## 3. Objetivo do Projeto

**Resumo:** O projeto desenvolvido no Power BI tem como objetivo oferecer uma visão estratégica do comportamento do mercado de ações de cinco empresas selecionadas (IBM, Microsoft, Oracle, Tesla e Walmart), permitindo análises detalhadas ao longo do tempo. Os dados analisados abrangem o período de 25 de abril de 2020 até 25 de abril de 2025, garantindo uma visão histórica consistente dos últimos cinco anos. O dashboard possibilita responder perguntas-chave como o total de volume negociado, médias mensais dos valores de abertura, máximos, mínimos e fechamento das ações, além da variação da média de fechamento mês a mês. Também conta com recursos de filtragem por empresa ou combinação de empresas, e utiliza Narrativa Inteligente para destacar padrões e tendências nos dados, com uma apresentação visual formatada e acessível.

---

## 4. Fontes de Dados

**Origem dos Dados:** site da [NASDAQ](https://www.nasdaq.com/market-activity/stocks)

- **Tabela Utilizada: **

- **Campos Considerados:**  


### Dicionário de Dados

| Nome do Campo                          | Tipo de Dado | Descrição                                                                                 | Tipo de Coluna | Exemplo                  | Valores Possíveis                                         |
|---------------------------------------|--------------|-------------------------------------------------------------------------------------------|----------------|---------------------------|-----------------------------------------------------------|
| `Company`                      |   Texto    | Nome da empresa                                                        | Original        | `IBM`                   | -                                                     |
| `Date`                      |   Data    |  Data em que a ação foi negociada na NASDAQ                                                       | Original       | `24/04/2025`                   | -                                                       |
| `Close/Last`                      | Número Decimal | Fornece o preço de fechamento da ação na NASDAQ no final do dia de negociação. O preço de fechamento é o último preço pelo qual a ação foi negociada naquele dia | Original | `229,33` | - |
| `Volume`                      |    Número Inteiro   | Indica o número total de ações negociadas durante o dia. Isso pode incluir várias transações feitas por um ou mais investidores | Original | `7.948.259` | - |
| `Open`                      |    Número Decimal   | Indica o preço de abertura da ação na NASDAQ no início do dia de negociação. O preço de abertura é o primeiro preço pelo qual a ação foi negociada naquele dia | Original | `231,175` | - |
| `High`                      |    Número Decimal   | Indica o preço máximo que a ação foi negociada naquele dia. O preço máximo é o preço mais alto pelo qual a ação foi negociada durante o dia | Original | `232,78` | - |
| `Low`                      |   Número Decimal    |Indica o preço mínimo que a ação foi negociada naquele dia. O preço mínimo é o preço mais baixo pelo qual a ação foi negociada durante o dia | Original | `243,66` | - |




---

## 5. Tratamento de Dados

**Transformações Realizadas no Power Query:**  
- 

---

## 6. Validação e Verificação dos Dados

**Métodos de Validação:** 
**Erros Encontrados e Correções:** 

---

## 7. Modelagem de Dados

**Relacionamentos Criados:** 

---

## 8. Funções DAX Utilizadas

### Medidas Criadas (DAX):
  
---

## 9. Dashboards e Relatórios



---

## 10. Acesso e Compartilhamento

**Modo de Compartilhamento:** 

---

## 11. Considerações Finais



## 12. Anexo: LOG de Desenvolvimento



Última Atualização: 25/04/2025

Autor: Renan Costa
