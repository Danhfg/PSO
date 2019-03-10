# Projetos de Sistemas Operacionais  

## Introdução  

Neste respositório contém as implementações das atividades feitas na disciplina de ***Projeto de Sistemas Operacionais*** do bacharelado de _Tecnologia da Informação_ ( **UFRN** ).   
  
## :page_facing_up: Requisitos mínimos

Compilador C++ 11 (**g++**), GNU debugger (**GDB**) e Doxygen.
	
	Obs.: Para usuários Linux, tanto o g++ quanto o gdb são ambos nativo, faltando apenas instalar o Doxygen.  
	Porém, caso deseje usar o gdb no Windows será necessário instalar o MinGW. 

### :package: Download Doxygen 
  
Visite a página de [Download] ou instale diretamente no terminal usando o seguinte código caso seja usuário ***Ubuntu***:  

```$ sudo apt-get install doxygen``` 	

[Download]:http://www.stack.nl/~dimitri/doxygen/download.html

## Etapa de compilação e execução

	Obs.: Todos os códigos digitados no terminal deverão ser na respectiva pasta raiz do programa.  
	Exceto na vizualização da documentação do projeto, não será necessário alterar a pasta.

Depois de clonar o repositório na respectiva pasta local, **digite** ```make``` **para** 
**realizar a compilação**, resultando na criação dos respectivos arquivos binários(executáveis)
. Em seguida, digite ```.bin/antiBomb``` para executar o programa, seguido de seu respectivo argumento.



###  Documentação e exclusão dos objetos e do executável

Caso deseje verificar a documentação, digite na pasta doc ```make doc ```. Diante disso, abra a pasta **html**, depois abra o arquivo chamado **index.html** o qual possui a documentação.  
  
  
Além disso, caso deseje fazer o debugger do programa, primeiro digite no terminal ```make debug```, depois digite ```gdb .bin/questao2``` ou ```gdb .bin/questao1```, de acordo com o programa que desejar.  **Ou, se quiser apagar os objetos e o executável, digite** ```make clean```.

<p align="right">
<img src="https://www.star.bnl.gov/public/comp/sofi/doxygen/doxygen_logo.gif" width="14%"  />
</p>

## Autores  

Programas desenvolvidos por Samuel Lucas de Moura Ferino ( _samuellucas97@ufrn.edu.br_ ) e Daniel Henrique Ferreira Gomes ( _danhfg@ufrn.edu.br_ )     
:copyright: IMD/UFRN 2019. 
