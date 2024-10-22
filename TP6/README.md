# Relatório do TP6
## Data: 2024-10-16
## Autora: Letícia Rodrigues a108960

## Resumo

O TP6 consistiu na criação de uma aplicação em Python para a gestão de alunos de uma turma que coloca no menu o seguinte menu de operações:
* 1: Criar uma turma;
* 2: Inserir um aluno na turma;
* 3: Listar a turma;
* 4: Consultar um aluno por id;
* 5: Guardar a turma em ficheiro;
* 6: Carregar uma turma dum ficheiro;
* 0: Sair da aplicação
No fim de executar cada operação, a aplicação coloca novamente o menu e pede ao utilizador a opção para continuar. Além disso, foi considerado o seguinte modelo de dados:
* aluno = (nome, id, [notaTPC, notaProj, notaTeste]) - um tuplo em que as notas do aluno são uma lista
* turma = [aluno] - uma lista de tuplos

Com este programa,criei um ficheiro "TURMA" que consiste numa turma com 5 alunos:
* Joana|a102444|19.0|20.0|17.0
* Marta|a109555|20.0|12.0|16.0
* Mariana|a102333|16.0|13.0|12.0
* Diogo|a109654|20.0|12.0|13.0
* Maria|a178333|12.0|14.0|15.0
Este ficheiro está anexado na pasta TP6, junto com o programa criado e este README.


Considerei a realização desta aplicação muito desafiadora e dinâmica, pois a sensação de ver os dados guardados e carregados corretamente num ficheiro dá realmente a impressão de que a aplicação "funciona de verdade". Esta foi uma função nova para mim, que gostei muito de implementar, embora inicialmente tenha demorado algum tempo a entender como funcionava, especialmente a parte de carregar a turma a partir de um ficheiro. Além disso, achei que a parte mais difícil, por mais incrível que pareça, foi garantir que, na opção 2, o programa não inserisse o aluno na turma se o ID já existisse ou se as notas fossem inválidas (ou seja, inferiores a 0 ou superiores a 20, conforme o intervalo definido). Para resolver esse problema, tive de usar condições e estruturas condicionais de forma cuidadosa. 

Ao concluir a aplicação, fiquei satisfeito com o resultado final, pois a funcionalidade de gerir os dados de alunos de forma automatizada mostrou-se muito útil e prática. A conclusão do projeto foi gratificante e permitiu-me consolidar várias aprendizagens importantes, que usei em futuros projetos/trabalhos.

