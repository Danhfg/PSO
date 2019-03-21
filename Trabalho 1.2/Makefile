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
all: init gpioMonitor memfill

debug:	CFLAGS += -g -O0
debug:	gpioMonitor memfill 

# Cria a pasta/diretório bin e a obj
init:
	@mkdir -p $(OBJ_DIR)/gpioMonitor
	@mkdir -p $(OBJ_DIR)/memfill	
	@mkdir -p $(BIN_DIR)
	@mkdir -p $(DOC_DIR)

# Alvo (target) para a construcao do executavel gpioMonitor
# Define o arquivo gpioMonitor.o como dependência
gpioMonitor: $(OBJ_DIR)/gpioMonitor/gpioMonitor.o
	@echo "============="
	@echo "Ligando o alvo $@"
	@echo "============="
	$(CC) $(CFLAGS) -o $(BIN_DIR)/$@ $^
	@echo "+++ [Executavel gpioMonitor criado em $(BIN_DIR)] +++"
	@echo "============="

# Alvo (target) para a construcao do objeto gpioMonitor.o
# Define os arquivos gpioMonitor.cpp e gpioMonitor.h como dependencias.
$(OBJ_DIR)/gpioMonitor/gpioMonitor.o: $(SRC_DIR)/gpioMonitor.cpp
	$(CC) -c $(CFLAGS) -o $@ $<

# Alvo (target) para a construcao do executavel memfill
# Define o arquivo memfill.o como dependência
memfill: $(OBJ_DIR)/memfill/memfill.o
	@echo "============="
	@echo "Ligando o alvo $@"
	@echo "============="
	$(CC) $(CFLAGS) -o $(BIN_DIR)/$@ $^
	@echo "+++ [Executavel memfill criado em $(BIN_DIR)] +++"
	@echo "============="

# Alvo (target) para a construcao do objeto memfill.o
# Define os arquivos memfill.cpp e memfill.h como dependencias.
$(OBJ_DIR)/memfill/memfill.o: $(SRC_DIR)/memfill.cpp
	$(CC) -c $(CFLAGS) -o $@ $<

doc:
	$(RM) $(DOC_DIR)/*
	doxygen Doxyfile

#removendo os .o e os binários
clean:
	$(RM) $(BIN_DIR)/*
	$(RM) $(OBJ_DIR)/gpioMonitor/*
	$(RM) $(OBJ_DIR)/memfill/*
	$(RM) $(DOC_DIR)/*
	
#FIM DO MAKEFILE
