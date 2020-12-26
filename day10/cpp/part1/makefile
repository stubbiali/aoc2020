CXX = clang++
CXXFLAGS =

SRC = $(wildcard *.cpp)
INC = $(wildcard *.hpp)

OBJ = $(SRC:.cpp=.o)

all: main clean

main: $(OBJ)
	$(CXX) $(CXXFLAGS) -o $@ $(OBJ)

$(OBJ): %.o: %.cpp $(INC)
	$(CXX) $(CXXFLAGS) -c -o $@ $<

.PHONY: clean distclean

clean:
	$(RM) $(OBJ)

distclean: clean
	$(RM) main