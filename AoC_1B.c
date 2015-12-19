//Advent of Code - Day 1 Part 2
//by Brandon Tsao

#include <stdio.h>

#define MAX 7001

int main (int argc, char * argv[])
{
  char buffer[MAX] = {0};
  int n = 0;
  int count = 1;

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

      if(n < 0)
      {
        printf("Count: %d\n", count);
        return 0;
      }
    }

    count++;
  }

    printf("Floor: %d\n",n);

}
