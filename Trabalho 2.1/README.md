## Trabalho 2.1 - Sockets

## Introdução  

Nesta pasta contém a implementação dos programas relativos ao trabalho 2.1 .


- [Objetivo](#objetivo) - Objetivo do trabalho 2.1 .
- [Requisitos](#requisitos) - Requisitos do trabalho 2.1 .
- [Sobre o jogo](#sobre-o-jogo) - Sobre o jogo e sua interface.
- [Compilação e execução](#compilação-e-execução) - Como compilar e executar o projeto
- [Autores](#autores) - Autores do projeto.
## Objetivo  

Explorar aspectos teóricos e práticos sobre sockets.

## Requisitos:
* Funcionalidades:
    1. o trabalho terá 2 programas, um cliente e outro servidor;
    2. Um será o jogo (executado em desktop - não precisa ser o mesmo jogo usado no trabalho anterior) e o outro, o joystick (obrigatoriamente implementado na BBB);
    3. A escolha de quem será o cliente e servidor fica a critério de cada grupo.
* Sockets:
	1.  A comunicação entre o cliente e o servidor será realizada via socket.
* Programas:
    1. Cliente e servidor deverão ser implementados em linguagens diferentes.
* Threads:  
    1. Threads separadas devem ficar responsáveis pelo gerenciamento da
comunicação socket em ambos os lados (cliente e servidor).

* Casos omissos:
    1. Projetistas tomam a decisão de que forma implementar.

## Sobre o jogo  

Trata-se de uma implementação em terminal do famoso jogo eletrônico chamado [Tetris](https://pt.wikipedia.org/wiki/Tetris).


![](https://github.com/fanux/tetris/blob/master/img/tetris.png?raw=true)  


## Compilação e execução  

Execute na linha de terminal para a compilação e criação do objetos

```
$ make
```  
Ou, caso deseje apagar os objetos e os executáveis, digite  

```
$ make clean
```  
Em seguida, serão criados os seguintes arquivos binários (executáveis):

| Nome do executável: | Descrição: | 
| ---------- | ------------- |
|`game` 	|Jogo de tetris implementado com interface gráfica.  
|`leitorEntradas_BBB` 	|Programa que lê as entradas da BeagleBone.  
  
Diante disso, execute como super usuário o arquivo binário `game`  

```
$ ./bin/game
```
E, em outra janela do bash, execute o arquivo binário `leitorEntradas_BBB`  

```
$ ./bin/leitorEntradas_BBB
```
  
Além disso, caso deseje ver a documentação, execute  

```
$ make doc
```  
Em seguida, vá até a pasta **doc** e abra o arquivo `index.html` em um navegador qualquer.

## Autores  
Samuel Lucas de Moura Ferino ( _samuellucas97@ufrn.edu.br_ ) e Daniel Henrique Ferreira Gomes ( _danhfg@ufrn.edu.br_ )     
:copyright: IMD/UFRN 2019. 
