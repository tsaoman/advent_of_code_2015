//Advent of Code - Part 1A
//by Brandon Tsao

#include <stdio.h>
#include <stdlib.h>

#define MAX 7001

int main (int argc, char * argv[])
{
  char buffer[MAX] = {0};
  int n = 0;

  if(fgets(buffer, MAX, stdin) == NULL)
  {
    printf("Error: Could not read from stdin.\n");
    return 1;
  }

  for(int i = 0; i < MAX; i++)
  {
    if (buffer[i] == '(')
    {
      n++;
    }

    else if (buffer[i] == ')')
    {
      n--;
    }
  }
    printf("Floor: %d\n",n);
}
