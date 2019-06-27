# Gerenciamento de Processos Zumbi

## Introdução  

Nesta pasta contém a implementação de um daemon de arquitetura cliente-servidor responsavel por fazer o gerenciamento de processos zumbi dos clientes conectados.  

- [Requisitos](#requisitos) - Requisitos de software utilizado no projeto
- [Execução](#compilação-e-execução) - Executar o projeto
- [Vídeo](#vídeo) - Vídeo com demonstração de execução do projeto

## Requisitos    

Faz-se necessario que haja um compilador C++ e um interpretador do Python instalado na maquina a ser utilizada. Porem, caso nao haja previamente instalada, acesse esse [link] para download. Em seguida, dentro dessa pagina web, faca o download e instale o instalador de acordo com o seu sistema operacional.

[link]:https://www.python.org/downloads/

### Bibliotecas Python necesárias
Para correta execução do projeto, faz-se necessário que a máquina (host) tenha instalado as seguintes biliotecas:  
- pandas

Assim, caso não possui previamente essa bibliotecas, use esse comandos...

```
$ pip install pandas
```    

## Execução    


Execute na linha de terminal, depois de adentrar a essa pasta, a execução do servidor, `serverSocket.py`

```
$ python3 serverSocket.py
```    

Em seguida, no lado cliente execute-os substituindo as parte que estao entre `<>`.

```
$ sudo python3 clienteSocket.py <nome do usuario> <IP do servidor> <tempo do log>
```  

Por fim, compile e execute o arquivo `zumbi.c` responsavel por gerar processos zumbi.
```
$ ./zumbi
```  
Feito isso, o cliente pode aperta os seguintes botões para controlar sua cobra


## Vídeo  
  
Esse é o link do [vídeo] onde se demonstra a execução de três clientes se conectando a um servidor.

[vídeo]:https://youtu.be/LUjfCrN4dGY
