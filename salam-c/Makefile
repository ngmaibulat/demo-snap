# Makefile

# Compiler
CXX := g++

# Compiler flags
CXXFLAGS := -std=c++17 -Wall

# Target binary
TARGET := salam-c

# Source file
SRC := main.cpp

# Object file
OBJ := $(SRC:.cpp=.o)

# Default target
all: $(TARGET)

# Rule to build the target binary
$(TARGET): $(OBJ)
	$(CXX) $(CXXFLAGS) -o $@ $^

# Rule to build object files
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean rule
clean:
	rm -f $(OBJ) $(TARGET)
