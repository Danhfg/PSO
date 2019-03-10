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
# Define o arquivo Fork_Bomb.o como dependência
forkBomb: CFLAGS+= -I$(INC_DIR)/parte1
forkBomb: $(OBJ_DIR)/parte1/Fork_bomb.o
	@echo "============="
	@echo "Ligando o alvo $@"
	@echo "============="
	$(CC) $(CFLAGS) -o $(BIN_DIR)/$@ $^
	@echo "+++ [Executavel parte1 criado em $(BIN_DIR)] +++"
	@echo "============="

# Alvo (target) para a construcao do objeto Fork_bomb.o
# Define os arquivos Fork_bomb.cpp e Fork_bomb.h como dependencias.
$(OBJ_DIR)/parte1/Fork_bomb.o: $(SRC_DIR)/parte1/Fork_bomb.cpp
	$(CC) -c $(CFLAGS) -o $@ $<

# Alvo (target) para a construcao do executavel parte1
# Define o arquivo Fork_Bomb.o como dependência
antiBomb: CFLAGS+= -I$(INC_DIR)/parte1
antiBomb: $(OBJ_DIR)/parte1/anti_bomb.o
	@echo "============="
	@echo "Ligando o alvo $@"
	@echo "============="
	$(CC) $(CFLAGS) -o $(BIN_DIR)/$@ $^
	@echo "+++ [Executavel parte1 criado em $(BIN_DIR)] +++"
	@echo "============="

# Alvo (target) para a construcao do objeto anti_bomb.o
# Define os arquivos anti_bomb.cpp e anti_bomb.h como dependencias.
$(OBJ_DIR)/parte1/anti_bomb.o: $(SRC_DIR)/parte1/anti_bomb.cpp
	$(CC) -c $(CFLAGS) -o $@ $<

part2: CFLAGS+= -I$(INC_DIR)/parte2
part2: $(OBJ_DIR)/parte2/part2.o
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