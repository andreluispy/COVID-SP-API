# Docs

- Fonte: [https://brasil.io/dataset/covid19/files/](https://brasil.io/dataset/covid19/files/)
- Dataset: caso.csv.gz

## Como usar o JSON
---
 Formato do JSON:
 ```json
{
    "citys":[
        {"date":"2021-10-10", "city":"City Name",
        "confirmed": "1000", "deaths": "100"}
    ]
}
 ```

 O JSON retornado é formado pelo campo `"citys` que contem um array com todas as cidades, cada array é formado por 4 campos: `"date"` que contem a data de coleta dos dados, `"city"` que tem o nome da cidade, `"confirmed"` que contem o numero de casos confirmados e `"deaths"` que contem o numero de mortes na cidade.

## O que o Código do Back faz?
---
O Código baixa o arquivo caso.csv.gz do **brasil.io** e depois extrai o arquivo principal caso.csv.

Depois o código filtra o arquivo para pegar somente dados do estado de São Paulo e filtra novamente para pegar os dados mais recentes. Feito isso o arquivo JSON é gerado.

# Contribuidores

Back por: [Andé Luís](https://github.com/andreluispy) - Estudante de IA, Compiladores e Arquitetura de Sistema Operacionais
