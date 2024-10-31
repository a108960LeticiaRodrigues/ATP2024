# Relatório do TP7
## Data: 2024-10-23
## Autora: Letícia Rodrigues a108960

## Resumo

Para o TP7, a tarefa era criar uma aplicação que reune todos os exercícios feitos em aula, baseando-se em uma tabela meteorológica representada como uma lista de tuplos. Cada tuplo contém dados específicos de um dia, como a data, temperatura mínima, temperatura máxima e precipitação. 

#### Estrutura da Tabela Meteorológica

A tabela meteorológica é uma lista onde cada elemento é um tuplo com os seguintes dados:

* Data: Representada como um tuplo (dia, mês, ano), onde cada valor é um inteiro.
* Temperatura Mínima: Um número do tipo float, representando a temperatura mínima registrada.
* Temperatura Máxima: Um número do tipo float, representando a temperatura máxima registrada.
* Precipitação: Um número do tipo float, representando a quantidade de precipitação em milímetros.

* Exemplo de Estrutura da Tabela: TabMeteo = [((ano,mes,dia),TempMin,TempMax,Precipitacao)]

#### Exercícios realizados

A aplicação incluiu funcionalidades para os seguintes cálculos e operações:
* Temperatura média de cada dia;
* Guardar uma tabela meteorológica num ficheiro de texto;
* Carregar uma tabela meteorológica de um ficheiro de texto;
* Temperatura mínima mais baixa registada na tabela;
* Amplitude térmica de cada dia;
* Dia em que a precipitação registada teve o seu valor máximo;
* Dias em que a precipitação foi superior ao limite escolhido (p);
* Maior número consecutivo de dias com precipitação abaixo do limite escolhido; 
* Desenho dos gráficos da temperatura mínima, máxima e de pluviosidade.

Para organizar a aplicação, foi criado um menu interativo onde cada opção corresponde a um exercício, identificado por um número. A aplicação também inclui a opção 0 para que o utilizador possa sair facilmente.

No geral, a aplicação se mostrou de fácil implementação, pois seguiu a mesma linha dos exercícios realizados nas TP e TPC anteriores. A abordagem incremental e prática das aulas facilitou a execução dos exercícios e proporcionou uma base sólida para consolidar os conhecimentos de programação e manipulação de dados meteorológicos. 