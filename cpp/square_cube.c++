#include <iostream>
using namespace std;

int main()
{
    int integer, square, cube;
    
    cout << "Enter integers: ";
    cin >> integer ;
    
    square = integer * integer;
    cout << "Square of input number = " << square << "\n";
    
    cube = integer * integer * integer;
    cout << "Cube of input number = " << cube;
    
    return 0;
}