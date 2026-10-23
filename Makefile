CC ?= gcc
CFLAGS ?= -std=c17 -Wall -Wextra -O2 -Iinclude
LDFLAGS ?=

BIN_DIR = bin
SRC_DIR = src
CORE_DIR = $(SRC_DIR)/core
TEST_DIR = tests

CORE_SRCS = $(CORE_DIR)/metrics.c \
            $(CORE_DIR)/data_generator.c \
            $(SRC_DIR)/unit2_divide_conquer.c \
            $(SRC_DIR)/unit3_greedy.c \
            $(SRC_DIR)/unit4_dp.c \
            $(SRC_DIR)/unit5_backtracking_bb.c \
            $(SRC_DIR)/unit6_flow_string_crt.c

MAIN_SRC = $(SRC_DIR)/main.c
TEST_SRC = $(TEST_DIR)/test_all.c

TARGET = $(BIN_DIR)/soc_engine
TEST_TARGET = $(BIN_DIR)/test_all

.PHONY: all test clean run

all: $(TARGET) $(TEST_TARGET)

$(BIN_DIR):
	mkdir -p $(BIN_DIR)

$(TARGET): $(CORE_SRCS) $(MAIN_SRC) | $(BIN_DIR)
	$(CC) $(CFLAGS) $(CORE_SRCS) $(MAIN_SRC) -o $(TARGET) $(LDFLAGS)

$(TEST_TARGET): $(CORE_SRCS) $(TEST_SRC) | $(BIN_DIR)
	$(CC) $(CFLAGS) $(CORE_SRCS) $(TEST_SRC) -o $(TEST_TARGET) $(LDFLAGS)

test: $(TEST_TARGET)
	./$(TEST_TARGET)

run: $(TARGET)
	./$(TARGET) --run-all-demos

clean:
	rm -rf $(BIN_DIR) data/*.csv data/*.json
