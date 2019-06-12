# Snake Game

## Introdução  

Nesta pasta contém a implementação  parcial em _Python_ do jogo Snake com suporte multithread e que faz uso da arquitetura cliente-servidor.  

- [Requisitos](#requisitos) - Requisitos de software utilizado no projeto
- [Execução](#compilação-e-execução) - Executar o projeto
- [Vídeo](#vídeo) - Vídeo com demonstração de execução do projeto

## Requisitos    

Faz-se necessario que haja o interpretador do Python instalado na maquina a ser utilizada. Porem, caso nao haja previamente instalada, acesse esse [link] para download. Em seguida, dentro dessa pagina web, faca o download e instale o instalador de acordo com o seu sistema operacional.

[link]:https://www.python.org/downloads/

### Bibliotecas Python necesárias
Para correta execução do projeto, faz-se necessário que a máquina (host) tenha instalado as seguintes biliotecas:  
- turtle  
- keyboard

Assim, caso não possui previamente essa bibliotecas, use esse comandos...

```
$ pip install turtle
$ pip install keyboard
```    

## Execução    


Execute na linha de terminal, depois de adentrar a essa pasta, a execução do servidor, `serverSocket.py`

```
$ python3 serverSocket.py
```    

Em seguida, por meio de outros quatros terminais execute os clientes seguidos dos nomes, usuario1, para o primeiro, usuario2, para o segundo e assim por diante. Diante disso, tome o primeiro usuário como exemplo abaixo.

```
$ sudo python3 clientSocket.py usuario1
```  

Por fim, execute `test.py` em outro terminal.
```
$ python3 ´test.py
```  
Feito isso, o cliente pode aperta os seguintes botões para controlar sua cobra


| Botão apertado: | Descrição: | 
| ---------- | ------------- |
|`w` 	|Move a respectiva cobra para **cima**.  
|`s` 	|Move a respectiva cobra para **baixo**.  
|`a` 	|Move a respectiva cobra para à **esquerda**.  
|`d` 	|Move a respectiva cobra para à **direita**.  


## Vídeo  
  
Esse é o [link] do vídeo o qual demonstra a execução de três clientes se conectando a um servidor.

[link]:
