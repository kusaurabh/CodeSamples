#include <vector>
#include <iostream>

using namespace std;
int binary_search(vector<int> list, int searchNum);

int main() 
{
  vector<int> numList{1,2,3,4,5,6,7,8,9,10};
  
  cout << "List is : ";  
  for(auto i : numList) {
     cout << i << " ";  
  }
  cout << endl;
  int num;
  while (true) {
    cout << "Search For :";
    cin >> num;
    binary_search(numList, num);
  }
}

int binary_search(vector<int> list, int searchNum)
{ 
 
  auto begin = list.begin();
  auto end = list.end();
  auto mid = begin + (end-begin)/2;

  while((mid != end) && (*mid != searchNum))
  {
      if(*mid > searchNum) {
          end = mid;   //Value might lie in the first half
      }
      else if(*mid < searchNum) {
          begin = mid+1; //Value might lie in second half
      }
      //Change the mid point
      mid = begin + (end-begin)/2;
  }
 
  if(mid == end) 
     cout << "Value not found !!" << endl;

  if(*mid == searchNum)
    cout << "Value found " << endl;
  return 0;
}
