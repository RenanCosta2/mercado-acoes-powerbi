
# 📊 Projeto Power BI - Mercado de Ações

## 1. Informações Gerais do Projeto

**Nome do Projeto:** Análise de dados da bolsa de valores eletrônica americana NASDAQ

**Responsável:** Renan Costa  

**Data de Início:** 25/04/2025

**Data de Conclusão:** 29/04/2025

**Versão Atual:** 1.0  

**Setor/Departamento:** Mercado de Ações  

---

## 2. Requisitos do Projeto

- Obter o **total de volume negociado de ações ao longo do tempo** para as 5 empresas analisadas.
- Calcular o **valor médio de abertura (_Open_), mais alto (_High_), mais baixo (_Low_), de fechamento (_Close_) e do Volume das ações de todas as empresas, para todos os meses do período analisado (5 anos)**.
- Calcular a **variação da média do valor de fechamento (_Close_)** das ações de todas as empresas ao longo do tempo, mês a mês.
- Explicar as **principais características e tendências nos dados**.
- Deve ser possível realizar a análise para **uma única empresa ou uma combinação de empresas**.

---

## 3. Objetivo do Projeto

**Resumo:** O projeto desenvolvido no Power BI tem como objetivo oferecer uma visão estratégica do comportamento do mercado de ações de cinco empresas selecionadas (IBM, Microsoft, Oracle, Tesla e Walmart), permitindo análises detalhadas ao longo do tempo. Os dados analisados abrangem o período de 25 de abril de 2020 até 25 de abril de 2025, garantindo uma visão histórica consistente dos últimos cinco anos. O dashboard possibilita responder perguntas-chave como o total de volume negociado, médias mensais dos valores de abertura, máximos, mínimos e fechamento das ações, além da variação da média de fechamento mês a mês. Também conta com recursos de filtragem por empresa ou combinação de empresas, e utiliza Narrativa Inteligente para destacar padrões e tendências nos dados, com uma apresentação visual formatada e acessível.

---

## 4. Fontes de Dados

**Origem dos Dados:** site da [NASDAQ](https://www.nasdaq.com/market-activity/stocks)

- **Tabela Utilizada: stock_data**

- **Campos Considerados:**  
  - _Company_
  - _Date_
  - _Close/Last_
  - _Volume_
  - _Open_
  - _High_
  - _Low_

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
- **Formatação dos nomes das empresas**: Os valores na coluna _Company_ foram padronizados para que apenas a primeira letra de cada nome fique em maiúscula. A empresa IBM, originalmente em letras minúsculas, foi convertida para letras maiúsculas.
- **Correção de formatação numérica**: As colunas com valores monetários estavam em formato de texto devido à presença do caractere "$" e ao uso do ponto como separador decimal, conforme o padrão dos EUA. O caractere "$" foi removido e o ponto decimal substituído por vírgula, adequando os dados ao padrão numérico brasileiro.
- **Ajuste no formato de data**: As datas da coluna _Date_ estavam no formato americano (MM/DD/AAAA), com o mês e o dia invertidos em relação ao padrão brasileiro. A coluna foi convertida para o formato nacional (DD/MM/AAAA).

---

## 6. Validação e Verificação dos Dados

**Métodos de Validação:** Verificação Manual.
**Erros Encontrados e Correções:** Nenhum erro encontrado.

---

## 7. Modelagem de Dados

**Relacionamentos Criados:** Tabela única.

---

## 8. Funções DAX Utilizadas

### Medidas Criadas (DAX):
- **MediaClose**
  ``` DAX
  MediaClose = AVERAGE(stock_data[Close/Last]) 
  ```

- **MediaClose MoM%**
  ``` DAX
  MediaClose MoM% = 
  IF(
  	ISFILTERED('stock_data'[Date]),
  	ERROR("Medidas rápidas de inteligência de tempo somente podem ser agrupadas ou filtradas pela hierarquia de data fornecida pelo Power BI ou pela coluna de data primária."),
  	VAR __PREV_MONTH = CALCULATE([MediaClose], DATEADD('stock_data'[Date].[Date], -1, MONTH))
  	RETURN
  		DIVIDE([MediaClose] - __PREV_MONTH, __PREV_MONTH)
  )
  ```

- **MediaHigh**
  ``` DAX
  MediaHigh = AVERAGE(stock_data[High]) 
  ```

- **MediaLow**
  ``` DAX
  MediaLow = AVERAGE(stock_data[Low]) 
  ```

- **MediaOpen**
  ``` DAX
  MediaOpen = AVERAGE(stock_data[Open])
  ```

- **MediaVolume**
  ``` DAX
  MediaVolume = AVERAGE(stock_data[Volume])
  ```

- **TotalVolume**
  ``` DAX
  TotalVolume = SUM(stock_data[Volume])
  ```

---

## 9. Dashboards e Relatórios

![image](https://github.com/user-attachments/assets/9fcabbcf-70f0-4031-8268-932e2095ba23)

### Visão Geral do Volume Negociado
- Forte **queda de 59,28%** no volume total entre **abril/2020 e abril/2025**.
- Picos anormais:
  - **2021:** Volume atinge **0,81 Bi** — possivelmente por IPOs ou eventos macroeconômicos.
  - Redução consistente até **2025**, com volumes estabilizando próximos de **0,15 Bi**.

### 📊 Variação da Média de Fechamento MoM

- **Tesla**: Maior volatilidade. Destaque para **queda acentuada em maio (~-70%)**, seguida de forte recuperação.
- **Microsoft, Oracle, Walmart**: Curvas mais estáveis. Menores riscos.
- **IBM**: Comportamento intermediário entre defensivo e volátil.

### 📅 Tabela de Valores Médios (2020–2025)

- Houve uma tendência clara de crescimento no valor médio de abertura e fechamento ao longo dos anos, indicando uma valorização progressiva dos ativos.
- O pico no volume negociado ocorreu em 2020, sugerindo um evento atípico (ex.: pandemia ou forte movimentação de mercado); após isso, o volume caiu consideravelmente e não retornou aos mesmos níveis.
- Mesmo com menor volume, os preços continuaram subindo, o que pode indicar baixa oferta ou alta demanda institucional mais concentrada.
- A média geral (linha "Total") está consistentemente puxada para cima pelos dois últimos anos (2024 e 2025), o que reforça a importância de avaliar as tendências recentes com atenção.

### 🤖 Narrativa Inteligente (Resumo Automático)

Análise geral para todos os anos e empresas:
- **Queda estrutural** desde 2020.
- **Ponto de inflexão identificado** em dez/2022.
- **Tesla em maio** representa **8,84%** da variação MoM — comportamento que pode impactar o índice geral.

Ao interagir com o dashboard a análise feita pela narrativa inteligente atualizará em conjunto.

---

## 10. Acesso e Compartilhamento

**Modo de Compartilhamento:** Publicado no Power BI Service  
[🔗 Acessar Dashboard](https://app.powerbi.com/view?r=eyJrIjoiNGUwYTA0MDctMmE4NS00Y2MxLTkzODktYjVjMzZhOTViOTRjIiwidCI6ImJhZTkwYjYxLTg4OTItNDQyMC1hMTEyLTE0NTQ4MzBkYmJiOSJ9)

---

## 11. Observações Gerais

- Os dados utilizados na análise são do período entre o dia 24/04/2020 até o dia 24/04/2025 (5 anos).
- Os arquivos .csv de cada empresa foram extraídos individualmente do site da NASDAQ. Utilizou-se um script em Python para inserir uma coluna identificadora da empresa em cada dataset, possibilitando a unificação dos dados em um único arquivo .csv, que serviu como base para o projeto.

---

## 12. Anexo: LOG de Desenvolvimento

Para acompanhar todo o histórico de desenvolvimento, ajustes e decisões tomadas ao longo do projeto, acesse o LOG de Desenvolvimento disponível no link abaixo:
[🔗 Acessar LOG de Desenvolvimento](./log-desenvolvimento.md)

Última Atualização: 29/04/2025

Autor: Renan Costa
