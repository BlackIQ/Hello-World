package main

import "fmt"

func fibonacci() func() int {
	a, b, c := 0, 1, 0
	return func() int {
		c = a
		a, b = b, a+b
		return c
	}
}

func main() {
	fib := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Printf("fib(%d) = %d\n", i, fib())
	}
}
