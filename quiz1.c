#include <stdio.h>
#include <stdint.h>

//
// https://www.wikitechy.com/technology/c-program-reverse-bits-number/

//uint8_t reverse_bits(uint8_t x)
//{
//  return ~x;
//}

uint8_t reverse_bits(uint8_t x)
{
  uint8_t reversed = 0;

  for (int i = 0; i < 8; i++) {
    if (x & (1 << i)) {
      reversed |= 1 << (8 - 1) - i;
    }
  }

  return reversed;
}

int main(void)
{
  uint8_t value = 200;
  uint8_t rev_value = 0;

  rev_value = reverse_bits(value);

  printf("value:     0x%0x\n", value);
  printf("rev_value: 0x%0x\n", rev_value);
}

