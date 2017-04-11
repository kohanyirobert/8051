; Using i=10, j=255 and k=255 results in a loop
; that takes approximately ~1 seconds to execute
; when a 16MHz quartz crystal resonator is used.
; See calc.py for calculating the timing.
i	equ	12d
j	equ	188d
k	equ	196d
setup:	mov	p1, #11111111b
	lcall	main
delay:	mov	r0, #i
loop_i:	mov	r1, #j
loop_j:	mov	r2, #k
loop_k:	nop
	djnz	r2, loop_k
	djnz	r1, loop_j
	djnz	r0, loop_i
	ret
main:	mov	p1, #11111011b
	lcall	delay
	mov	p1, #11111111b
	lcall	delay
	ljmp	main
	end
