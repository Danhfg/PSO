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
.PHONY:	all	clean doc debug

#Ao final da compilacão, remove os arquivos objetos
all: init game 

debug:	CFLAGS += -g -O0
debug:	game  

# Cria a pasta/diretório bin e a obj
init:
	@mkdir -p $(OBJ_DIR)/Jogo
	@mkdir -p $(OBJ_DIR)/LeituraEntradas_BBB	
	@mkdir -p $(BIN_DIR)
	@mkdir -p $(DOC_DIR)

# Alvo (target) para a construcao do executavel Jogo
# Define o arquivo game.o como dependência
game: CFLAGS+= -I$(INC_DIR)/Jogo
game: $(OBJ_DIR)/Jogo/Game.o $(OBJ_DIR)/Jogo/Cur.o $(OBJ_DIR)/Jogo/CubePoint.o $(OBJ_DIR)/Jogo/Rand.o $(OBJ_DIR)/Jogo/Score.o $(OBJ_DIR)/Jogo/graph.o
	@echo "============="
	@echo "Ligando o alvo $@"
	@echo "============="
	$(CC) $(CFLAGS) -o $(BIN_DIR)/$@ $^
	@echo "+++ [Executavel game criado em $(BIN_DIR)] +++"
	@echo "============="

# Alvo (target) para a construcao do objeto Game.o
# Define os arquivos Game.cpp e Game.h como dependencias.
$(OBJ_DIR)/Jogo/Game.o: $(SRC_DIR)/Jogo/Game.cpp  $(INC_DIR)/Jogo/Game.h
	$(CC) -c $(CFLAGS) -o $@ $<

# Alvo (target) para a construcao do objeto Cur.o
# Define os arquivos Cur.cpp e Cur.h como dependencias.
$(OBJ_DIR)/Jogo/Cur.o: $(SRC_DIR)/Jogo/Cur.cpp  $(INC_DIR)/Jogo/Cur.h
	$(CC) -c $(CFLAGS) -o $@ $<

# Alvo (target) para a construcao do objeto CubePoint.o
# Define os arquivos CubePoint.cpp e CubePoint.h como dependencias.
$(OBJ_DIR)/Jogo/CubePoint.o: $(SRC_DIR)/Jogo/CubePoint.cpp  $(INC_DIR)/Jogo/CubePoint.h
	$(CC) -c $(CFLAGS) -o $@ $<

# Alvo (target) para a construcao do objeto Rand.o
# Define os arquivos Rand.cpp e Rand.h como dependencias.
$(OBJ_DIR)/Jogo/Rand.o: $(SRC_DIR)/Jogo/Rand.cpp  $(INC_DIR)/Jogo/Rand.h
	$(CC) -c $(CFLAGS) -o $@ $<

# Alvo (target) para a construcao do objeto Score.o
# Define os arquivos Score.cpp e Score.h como dependencias.
$(OBJ_DIR)/Jogo/Score.o: $(SRC_DIR)/Jogo/Score.cpp  $(INC_DIR)/Jogo/Score.h
	$(CC) -c $(CFLAGS) -o $@ $<

# Alvo (target) para a construcao do objeto graph.o
# Define os arquivos graph.cpp e graph.h como dependencias.
$(OBJ_DIR)/Jogo/graph.o: $(SRC_DIR)/Jogo/graph.cpp  $(INC_DIR)/Jogo/graph.h
	$(CC) -c $(CFLAGS) -o $@ $<

doc:
	$(RM) $(DOC_DIR)/*
	doxygen Doxyfile

#removendo os .o e os binários
clean:
	$(RM) $(BIN_DIR)/*
	$(RM) $(OBJ_DIR)/Jogo/*
	$(RM) $(OBJ_DIR)/LeituraEntradas_BBB/*
	$(RM) $(DOC_DIR)/*
	
#FIM DO MAKEFILE
