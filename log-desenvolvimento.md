# 📈 Log de Desenvolvimento

## 📅 25/04/2025

### ✅ Tarefas Realizadas

- Criei o repositório do projeto no GitHub.
- Adicionei um README com a estrutura inicial da documentação.
- Baixei os dados (arquivos CSV) dos últimos 5 anos do mercado de ações de 5 empresas: **IBM**, **Microsoft**, **Oracle**, **Tesla** e **Walmart**, via [Nasdaq](https://www.nasdaq.com/market-activity/stocks).
- Escrevi um código em Python para:
  - Adicionar uma coluna com o nome da empresa em cada dataset.
  - Unificar os dados em um único arquivo CSV.

- Iniciei o projeto no Power BI:
  - Padronizei os nomes das empresas com letra inicial maiúscula; exceto "IBM", que ficou toda maiúscula.
  - Colunas monetárias estavam como Texto (devido ao caractere `$` e uso de `.` como separador decimal).
    - Removi o caractere `$` e substituí o `.` por `,`.
  - Modifiquei o formato da coluna de datas de `MM/DD/YYYY` para `DD/MM`.

- Criei a medida `TotalVolume`:
```DAX
  TotalVolume = SUM(stock_data[Volume])
```

- Visualizações:
  - Gráfico de linhas representando o total de volume por mês.
    - Filtro de seleção de ano adicionado.
  - Filtro para selecionar as empresas.
  - Medidas de média:
```DAX
  MediaOpen = AVERAGE(stock_data[Open])
  MediaClose = AVERAGE(stock_data[Close/Last])
  MediaHigh = AVERAGE(stock_data[High])
  MediaLow = AVERAGE(stock_data[Low])
  MediaVolume = AVERAGE(stock_data[Volume])
```
  - Matriz para exibir médias por ano e mês.
  - Medida rápida para variação mês a mês da média de fechamento.
  - Gráfico de área representando a variação nas empresas.


---

## 📅 29/04/2025

### ✅ Tarefas Realizadas

- Adicionei uma narrativa inteligente para análise no dashboard.
- Organizei o layout dos visuais.
- Escolhi e apliquei a paleta de cores:
  - `#4b7d93` → Azul Petróleo
  - `#339ba8` → Azul Piscina
  - `#33b8ab` → Verde Água
  - `#65d39c` → Verde Menta
  - `#aae984` → Verde Limão
  - `#f9f871` → Amarelo Canário
  - `#1e3f2e` → Verde Musgo Escuro

- Construí o background do dashboard no PowerPoint (base: Azul Petróleo).
- Formatei os gráficos com base na paleta definida.
