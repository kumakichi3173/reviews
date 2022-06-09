#include <stdio.h>
#include <stdint.h>

//
// geotechlab-workshopブログ
// https://ameblo.jp/geotechlab-workshop/entry-12566193857.html
//

uint16_t convert_adc(uint16_t adc_val)
{
    return (3300 * adc_val) >> 16;
}

int main(void)
{
  uint16_t millivolt = convert_adc(1000)*1000;
  // 50000 mV 
  printf("Vin is %d mV\n", millivolt);
}

