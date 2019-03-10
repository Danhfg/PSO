# Trabalho 1.1 - Manipulação de Processos

## Introdução  

Nesta pasta contém a implementação dos programas relativos ao trabalho 1.1, o qual era divido em 2 partes.

## Parte 1: Fork Bomb

### Objetivo
Implementar na BeagleBone um programa que evite o fork bomb.

#### Requisitos
* Evitar o travamento ao executar while(1) fork();
* Capturar mensagens de exceção geradas.
* Configurar parâmetro correspondente ao nº de processos suportados pelo programa.

### Imagens de Testes

![](/image/print_antibomb_BBB.png)

![](/image/print_antibomb_notebook.png)

## Parte 2: Hierarquia de Processos

### Objetivo
Implementar um programa que através de um processamento na pasta /proc imprima periodicamente informações sobre os processos.

#### Requisitos
* Dado o ID de um processo (PID) imprimir a árvore de hierarquia (filhos, netos, bisnetos, tataranetos, etc.).
* A saída deve estar estruturada em algum formato conhecido (JSON, csv, etc) e de fácil manipulação.
* Imprimir a cada x instantes de tempo:
  * Número total de processos no sistema operacional
  * Número total de processos no sistema operacional organizados por usuário

  
## Autores  
Samuel Lucas de Moura Ferino ( _samuellucas97@ufrn.edu.br_ ) e Daniel Henrique Ferreira Gomes ( _danhfg@ufrn.edu.br_ )     
:copyright: IMD/UFRN 2019. 


