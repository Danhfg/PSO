RM = rm -rf
#Compilador
CC=g++

#Variaveis para os subdiretorios
#LIB_DIR=./lib Não haverá pois nenhuma biblioteca será usada
INC_DIR=./include
SRC_DIR=./src
OBJ_DIR=./build
BIN_DIR=./bin
DOC_DIR=./doc

#Opcoes de compilacao 
CFLAGS=	-Wall -pedantic -ansi -std=c++11 -pthread

#Garante que os alvos desta lista não sejam confundidos com arquivos de mesmo nome 
.PHONY:	all	clean	doxy	debug	doc

#Ao final da compilacão, remove os arquivos objetos
all: init parte1 parte2

debug:	CFLAGS += -g -O0
debug:	parte1 parte2

# Cria a pasta/diretório bin e a obj
init:
	@mkdir -p $(OBJ_DIR)/parte1
	@mkdir -p $(OBJ_DIR)/parte2	
	@mkdir -p $(BIN_DIR)

# Alvo (target) para a construcao do executavel parte1
# Define o arquivo forkBomba.o como dependência
parte1: CFLAGS+= -I$(INC_DIR)/parte1
parte1: $(OBJ_DIR)/parte1/forkBomba.o
	@echo "============="
	@echo "Ligando o alvo $@"
	@echo "============="
	$(CC) $(CFLAGS) -o $(BIN_DIR)/$@ $^
	@echo "+++ [Executavel parte1 criado em $(BIN_DIR)] +++"
	@echo "============="

# Alvo (target) para a construcao do objeto forkBomba.o
# Define os arquivos forkBomba.cpp e forkBomba.h como dependencias.
$(OBJ_DIR)/parte1/forkBomba.o: $(SRC_DIR)/parte1/forkBomba.cpp
	$(CC) -c $(CFLAGS) -o $@ $<

parte2: CFLAGS+= -I$(INC_DIR)/parte2
parte2: $(OBJ_DIR)/parte2/part.o
	@echo "============="
	@echo "Ligando o alvo $@"
	@echo "============="
	$(CC) $(CFLAGS) -o $(BIN_DIR)/$@ $^
	@echo "+++ [Executavel parte2 criado em $(BIN_DIR)] +++"
	@echo "============="

# Alvo (target) para a construcao do objeto part2.o
# Define o arquivo part2.cpp como dependência.
$(OBJ_DIR)/parte2/part2.o:	$(SRC_DIR)/parte2/part2.cpp
	$(CC) -c $(CFLAGS) -o $@ $<

# Alvo (target) para a construcao do objeto arvore.o
# Define o arquivo arvore.cpp como dependência.
$(OBJ_DIR)/parte2/arvore.o:	$(SRC_DIR)/parte2/part.cpp
	$(CC) -c $(CFLAGS) -o $@ $<

# Gera a documentação e remove a documentações anterior existentes
doxy:
	doxygen -g

doc:
	$(RM) $(DOC_DIR)/*
	doxygen Doxyfile

#removendo os .o e os binários
clean:
	$(RM) $(BIN_DIR)/*
	$(RM) $(OBJ_DIR)/parte1/*
	$(RM) $(OBJ_DIR)/parte2/*
	$(RM) html
	
#FIM DO MAKEFILE