# Trabalho 1.1 - Manipulação de Processos

## Introdução  

Nesta pasta contém a implementação dos programas relativos ao trabalho 1.1, o qual era divido em 2 partes.

### Fork Bomb :bomb: (Parte 1)

#### Objetivo
Implementar na BeagleBone um programa que evite o fork bomb.

#### Requisitos
* Evitar o travamento ao executar while(1) fork();
* Capturar mensagens de exceção geradas.
* Configurar parâmetro correspondente ao nº de processos suportados pelo programa.

### Imagens de Testes

![](/image/print_antibomb_BBB.png)

### Hierarquia de Processos (Parte 2)

#### Objetivo
Implementar um programa que através de um processamento na pasta /proc imprima periodicamente informações sobre os processos.

#### Requisitos
* Dado o ID de um processo (PID) imprimir a árvore de hierarquia (filhos, netos, bisnetos, tataranetos, etc.).
* A saída deve estar estruturada em algum formato conhecido (JSON, csv, etc) e de fácil manipulação.
* Imprimir a cada x instantes de tempo:
  * Número total de processos no sistema operacional
  * Número total de processos no sistema operacional organizados por usuário

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
|`antiBomb` 	|Programa que impede que um fork bomb cause danos.  
|`forkBomb` 	|Programa fork bomb que implementa o ataque de negação de serviço (DDos).  
|`main` 	|Programa que implementa o objetivo da parte 2 deste trabalho.  
  
Diante disso, basta executa o respectivo código de acordo como o nome do executável. Logo, caso seja o `forkBomb`  

```
$ ./bin/forkBomb
```
Caso contrário, se for o executável `antiBomb`  

```
$ ./bin/antiBomb
```
Ou, por fim, se for executável `main`  

```
$ ./bin/main
```  
  
Além disso, caso deseje ver a documentação, execute  

```
$ make doc
```  
Em seguida, vá até a pasta **doc** e abra o arquivo `index.html` em um navegador qualquer.   
## Autores  
Samuel Lucas de Moura Ferino ( _samuellucas97@ufrn.edu.br_ ) e Daniel Henrique Ferreira Gomes ( _danhfg@ufrn.edu.br_ )     
:copyright: IMD/UFRN 2019. 


