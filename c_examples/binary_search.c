#include <stdio.h>

int binarySearch(int * list, int numItems, int valToFind)
{
    int start =0;
    int finish = numItems-1;

    while(start <= finish)
    {
        int mid = (finish + start)/2;
        if(list[mid] < valToFind)
            start = mid+1;
        else if(list[mid] > valToFind)
            finish = mid-1;
        else
            return mid;
    }

    return -1;

}

void printArray(int * list, int numItems) 
{
    printf("List :");
    for(int i=0; i<numItems;i++)
    {
        printf(" %d", list[i]);
    }
    printf("\n");
}

int main()
{
    int numList[] = { 1,2,3,4,5,6,7,8,9,10 };
    int len = sizeof(numList)/sizeof(numList[0]);
    printArray(numList, len);
    int valToFind =11;
    int index = binarySearch(numList, len, valToFind);
   
    if (index >=0)
        printf("\n %d found at pos %d\n", valToFind, index);
    else
        printf("\n %d not found\n", valToFind);


}
