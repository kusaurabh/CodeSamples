#include <iostream>
#include <typeinfo>

using namespace std;

template <typename T> std::string type_name();

int main() 
{
  int v1=1, v2=3;

  std::cout << "The sum of " << v1
          << " and " << v2
          << " is " << v1 + v2 << std::endl;

  //std::cin >> int input_val;
  //int i = {3.14};
  double wage = 0, salary = 999.999;
  int x = 3.141;

  //int &rval1 = 1.01;
  int &rval2 = x;
  //int &rval3;
  
  int  i= 42;
  int *pi = &i;
  *pi = *pi * *pi;
  std::cout << *pi;

  double dval = 3.14;
  //int &ri = dval;
  const int &ri = dval;
  constexpr int val = 20;

  string s = "K";
  for (auto &c : s) 
  {
      c = 'L';  
  }

  cout << s << endl;

  unsigned buf_size = 1024;
  int ia[buf_size];
  int ib[10-4 + 7];

  const char ca[] = {'h', 'e', 'l', 'l', 'o'};
  const char * const cp = ca;
  while (*cp) {
    cout << *cp << endl;
    ++cp;
  }

}
