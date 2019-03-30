## Trabalho 1.3 - _Threads_ + ADC + GPIO

## Introdução  

Nesta pasta contém a implementação dos programas relativos ao trabalho 1.3 .


- [Objetivo](#objetivo) - Objetivo do trabalho 1.3 .
- [Requisitos](#requisitos) - Requisitos do trabalho 1.3 .
- [Sobre o jogo](#sobre-o-jogo) - Sobre o jogo e sua interface.
- [Compilação e execução](#compilação-e-execução) - Como compilar e executar o projeto
- [Autores](#autores) - Autores do projeto.
## Objetivo
Implementar um controle de video game (joystick) usando a BeagleBone Black e as ferramentas do sistema operacional.


## Requisitos:
* Funcionalidades:
    1. Utilizar para teste qualquer jogo disponibilizado de forma open source;
    2. É possível achar códigos de jogos de terminal no GitHub (Ex.: Tetris, Ping-Pong, Naves, etc);
    3. Também é possível implementar protótipo de jogos simples.
* Controle:
	1. 3 tipos de movimentos e usar potenciômetro (ADC), LDR (ADC) e botão (GPIO IN).
* Threads:  
    1. Coleta de informações do controle será feita por 3 threads c/ prioridades diferentes;
    2. Maior prioridade: thread do potenciômetro;
    3. Menor prioridade: thread do botão terá a menor prioridade.

* Casos omissos:
    1. Projetistas ficam livres para implementar de acordo com suas decisões.

## Sobre o jogo  

Trata-se de uma implementação em terminal do famoso jogo eletrônico chamado [Tetris](https://pt.wikipedia.org/wiki/Tetris)


![](https://github.com/fanux/tetris/blob/master/img/tetris.png?raw=true)  


## Compilação e execução  

Execute na linha de terminal para a compilação e execução os seguintes comandos:

```
$ cd src && make
$ ./game
$ g++ --version
g++ (GCC) 4.8.5 20150623 (Red Hat 4.8.5-4)
$ uname -a
Linux docker-86-106 3.10.0-327.22.2.el7.x86_64 #1 SMP Thu Jun 23 17:05:11 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux
```

## Ship on docker
```
$ docker build -t tetris:latest .
$ docker run -it tetris:latest /bin/bash
```
Then you will enter the tetris container.

run game:
```
$ game
```
Thats all

Alternative:
```
$ docker run -it fanux/tetris:latest /bin/bash
# game
```

Play well in iTerm


## Autores  
Samuel Lucas de Moura Ferino ( _samuellucas97@ufrn.edu.br_ ) e Daniel Henrique Ferreira Gomes ( _danhfg@ufrn.edu.br_ )     
:copyright: IMD/UFRN 2019. 
