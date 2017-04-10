# Calculates how many loops/iterations are are needed at the specified
# frequency to create a ~1 second long delay. Modify the value i, j and k to
# achieve different timings.
#
# Don't forget to change freq_mhz!

freq_mhz = 16
freq_hz = freq_mhz * 10**6
period_secs = 1 / freq_hz

i = 10
j = 255
k = 255

loop3 = k * 24                      # k * DJNZ
loop2 = j * (12 + loop3 + 24)       # j * (MOV + loop3 + DJNZ)
loop1 = i * (12 + loop2 + 24)       # i * (MOV + loop2 + DJNZ)
clock_cycles = 24 + 12 + loop1 + 24 # LCALL + MOV + loop1 + DJNZ

instruction_cycles = clock_cycles // 12
secs = clock_cycles * period_secs
millis = secs * 10**3
micros = secs * 10**6
nanos = secs * 10**9

print("frequency = ", freq_mhz, "MHz = ", freq_hz, "Hz", sep="")
print("period = ", period_secs, "s = ", period_secs * 10**9, "ns", sep="")
print("i =", i)
print("j =", j)
print("k =", k)
print("instruction cycles = ", instruction_cycles, sep="")
print("clock cycles = ", clock_cycles, sep="")
print("time = ", secs, "s = ", millis, "ms = ", micros, "μs = ", nanos, "ns", sep="")
