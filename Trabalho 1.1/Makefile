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
CFLAGS=	-Wall -pedantic -ansi -std=c++11

#Garante que os alvos desta lista não sejam confundidos com arquivos de mesmo nome 
.PHONY:	all	clean doc debug

#Ao final da compilacão, remove os arquivos objetos
all: init forkBomb antiBomb part2

debug:	CFLAGS += -g -O0
debug:	forkBomb antiBomb part2 

# Cria a pasta/diretório bin e a obj
init:
	@mkdir -p $(OBJ_DIR)/parte1
	@mkdir -p $(OBJ_DIR)/parte2	
	@mkdir -p $(BIN_DIR)
	@mkdir -p $(DOC_DIR)

# Alvo (target) para a construcao do executavel parte1
# Define o arquivo forkBomb.o como dependência
forkBomb: CFLAGS+= -I$(INC_DIR)/parte1
forkBomb: $(OBJ_DIR)/parte1/forkBomb.o
	@echo "============="
	@echo "Ligando o alvo $@"
	@echo "============="
	$(CC) $(CFLAGS) -o $(BIN_DIR)/$@ $^
	@echo "+++ [Executavel parte1 criado em $(BIN_DIR)] +++"
	@echo "============="

# Alvo (target) para a construcao do objeto forkBomb.o
# Define os arquivos forkBomb.cpp e forkBomb.h como dependencias.
$(OBJ_DIR)/parte1/forkBomb.o: $(SRC_DIR)/parte1/forkBomb.cpp
	$(CC) -c $(CFLAGS) -o $@ $<

# Alvo (target) para a construcao do executavel parte1
# Define o arquivo forkBomb.o como dependência
antiBomb: CFLAGS+= -I$(INC_DIR)/parte1
antiBomb: $(OBJ_DIR)/parte1/antiBomb.o
	@echo "============="
	@echo "Ligando o alvo $@"
	@echo "============="
	$(CC) $(CFLAGS) -o $(BIN_DIR)/$@ $^
	@echo "+++ [Executavel parte1 criado em $(BIN_DIR)] +++"
	@echo "============="

# Alvo (target) para a construcao do objeto antiBomb.o
# Define os arquivos antiBomb.cpp e antiBomb.h como dependencias.
$(OBJ_DIR)/parte1/antiBomb.o: $(SRC_DIR)/parte1/antiBomb.cpp
	$(CC) -c $(CFLAGS) -o $@ $<

main: CFLAGS+= -I$(INC_DIR)/parte2
main: $(OBJ_DIR)/parte2/main.o
	@echo "============="
	@echo "Ligando o alvo $@"
	@echo "============="
	$(CC) $(CFLAGS) -o $(BIN_DIR)/$@ $^
	@echo "+++ [Executavel parte2 criado em $(BIN_DIR)] +++"
	@echo "============="

# Alvo (target) para a construcao do objeto main.o
# Define o arquivo main.cpp como dependência.
$(OBJ_DIR)/parte2/main.o:	$(SRC_DIR)/parte2/main.cpp
	$(CC) -c $(CFLAGS) -o $@ $<

doc:
	$(RM) $(DOC_DIR)/*
	doxygen Doxyfile

#removendo os .o e os binários
clean:
	$(RM) $(BIN_DIR)/*
	$(RM) $(OBJ_DIR)/parte1/*
	$(RM) $(OBJ_DIR)/parte2/*
	$(RM) $(DOC_DIR)/*
	
#FIM DO MAKEFILE
