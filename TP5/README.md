# Relatório do TP5
## Data: 2024-10-09
## Autora: Letícia Rodrigues a108960

## Resumo

O TP5 consistiu na criação de uma aplicação em Python para a gestão de um conjunto de salas de cinema de um centro comercial. Esta ferramenta foi desenvolvida com o propósito de incluir as seguintes funcionalidades: 
* Listar filmes em exibição
* Verificar disponibilidade de lugar
* Vender bilhete 
* Listar disponibilidades nas salas
* Inserir nova sala,  verificando previamente se já existe uma sala com igual nome.

A estrutura do modelo de dados foi a seguinte:
* cinema - lista de salas
* sala - tuplo contendo:
    * nome -  nome da sala
    * nlugares - número total de lugares na sala;
    * Vendidos - lista de inteiros representando os lugares já ocupados;
    * filme: string com o nome do filme exibido na sala.

Decidi alterei o modelo de dados, adicionando o nome da sala ao tuplo que representa cada sala. Desta forma, é possível listar, não apenas o filme em exibição, mas também em que sala ele está a ser exibido, tornando a aplicação mais próxima da realidade, tal como acontece nos cinemas reais.

Considerei a realização desta aplicação muito desafiadora pois envolve conceitos e técnicas que ainda não tinham sido explorados em profundidade nas aulas, sendo uns dos trabalhos mais dificeis que fizemos até agora. Para mim, o mais dificil foi compreender a lógica por trás do desenvolvimento da aplicação, especialmente no que diz respeito ao funcionamento interno das funções, como a verificação de lugares disponíveis e a manipulação da lista de salas e bilhetes vendidos. Além disso, também foi desafiante fazer com que todas as funcionalidades fossem intergradas de forma coerente e sem erros.

No entanto, este trabalho prático contribuiu significativamente para o meu crescimento em Python apesar de considerar que o projeto foi mais exigente do que os exemplos práticos vistos nas aulas teórico-práticas, o que exigiu uma maior autonomia e tempo para realizar este projeto.
