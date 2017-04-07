#include <8051.h>

void delay() {
  // Oscillator frequency = 16Mhz
  // Oscillator cycle period = 0.0000000625s = 62.5ns
  // Instruction cycle = 12 * 1 (Oscillator cycle period)
  // Instruction cycle period = 12 * 62.5ns = 750ns
  // 1s =~ 1s / 750ns
  // This statement =~ 16 * (Instruction cycle period) =~ 85196 * 16 * 750ns =~ 1.022352s
  unsigned long i;
  for (i = 85196; i > 0; i--) {}
}

void main() {
  P1_2 = 0x00;
  while (1) {
    P1_2 = 1;
    delay();
    P1_2 = 0;
    delay();
  }
}
