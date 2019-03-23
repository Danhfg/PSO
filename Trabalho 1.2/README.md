# Trabalho 1.2 - Tratamento de Sinais e GPIO

## Introdução  

Nesta pasta contém a implementação dos programas relativos ao trabalho 1.2.

## Objetivo
Monitoramento (e finalização) de processos fazendo uso de GPIO na BeagleBoneBoard.

## Requisitos:
* Executar programa que em execução (processo) consuma de forma crescente um determinado recurso (CPU, memória, etc.);
* Usar GPIOs da BeagleBoneBoard para sinalizar, através de LEDs, o 
percentual de uso desse(s) recurso(s):
	1. LED verde acende se até 25% do recurso estiver sendo usado;
	2. LED amarelo acende se o uso do recurso estiver entre 25% e 50%;
	3. LED vermelho acende se o uso do recurso estiver entre 50% e 75%;
	4. Acima de 75% todos os LEDs ficarão piscando.
* Quando o recurso tiver ultrapassado os 75% um "botão do pânico" deve ser acionado e o processo que estiver causando o aumento do uso do recurso deverá ser terminado.
* Ao ser acionado o botão do pânico todos os LEDs ficarão apagados por "X" segundos e depois segue a lógica citada.

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
|`gpioMonitor` 	|Programa que monitora o uso da memória.  
|`memfill` 	|Programa provoca um estresse de uso de memória.  
  
Diante disso, execute como super usuário o arquivo binário `gpioMonitor`  

```
$ ./bin/gpioMonitor
```
E, em outra janela do bash, execute o arquivo binário `memfill`  

```
$ ./bin/memfill
```
  
Além disso, caso deseje ver a documentação, execute  

```
$ make doc
```  
Em seguida, vá até a pasta **doc** e abra o arquivo `index.html` em um navegador qualquer.   
## Autores  
Samuel Lucas de Moura Ferino ( _samuellucas97@ufrn.edu.br_ ) e Daniel Henrique Ferreira Gomes ( _danhfg@ufrn.edu.br_ )     
:copyright: IMD/UFRN 2019. 


