import argparse

parser = argparse.ArgumentParser(
    description="Calculates delay timings for `blink.asm'.")

parser.add_argument(
    '-f',
    '--frequency',
    dest='frequency_mhz',
    type=float,
    default=16.0,
    help='clock frequency to use in MHz',
)

parser.add_argument(
    '-d',
    '--delay',
    dest='delay_seconds',
    type=float,
    default=1.0,
    help='target delay to achieve in seconds',
)

args = parser.parse_args()


def calc(frequency, secs):
    """Calculates such i, j and k values that define instructions taking
    approximately (frequency * secs) number of clock cycles.
    """
    target_clock_cycles = frequency * secs
    results = []
    for k in range(1, 256):
        for j in range(1, 256):
            for i in range(1, 256):
                loop3 = k * (12 + 24)                # k * (NOP + DJNZ)
                loop2 = j * (12 + loop3 + 24)        # j * (MOV + loop3 + DJNZ)
                loop1 = i * (12 + loop2 + 24)        # i * (MOV + loop2 + DJNZ)
                clock_cycles = 24 + 12 + loop1 + 24  # LCALL + MOV + loop1 + DJNZ
                if abs(target_clock_cycles - clock_cycles) <= (frequency * 0.1):
                    results.append((clock_cycles, i, j, k))
    return min(results, key=lambda r: (abs(target_clock_cycles - r[0]), r[1], r[2], r[3]))


FREQUENCY = args.frequency_mhz * 10**6
PERIOD = 1 / FREQUENCY

clock_cycles, i, j, k = calc(FREQUENCY, args.delay_seconds)
instruction_cycles = clock_cycles // 12
secs = clock_cycles * PERIOD
millis = secs * 10**3
micros = secs * 10**6
nanos = secs * 10**9

print("frequency = ", FREQUENCY / 10**6, "MHz = ", FREQUENCY, "Hz", sep="")
print("period = ", PERIOD * 10**9, "ns", sep="")
print("i =", i)
print("j =", j)
print("k =", k)
print("instruction cycles = ", instruction_cycles, sep="")
print("clock cycles = ", clock_cycles, sep="")
print("time = ", secs, "s = ", millis, "ms = ",
      micros, "μs = ", nanos, "ns", sep="")
