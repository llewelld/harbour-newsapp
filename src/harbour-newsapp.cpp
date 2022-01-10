#include <iostream>

#include <newslib.h>

int main(int, char *[])
{
  std::cout << "News application" << std::endl;
  news_print();
  news_footer();
 
  return 0;
}
