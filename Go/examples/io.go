package main 

import (
 "os"
 "fmt"
 "io"
)

func main(){
  // You are already familiar with the methods of working with stdout in Go, but you should know that stdout in Go is an io type that can be written to and read from.
  // Write directly
  os.Stdout.Write([]byte("Hello World!"))
  // Write string using ready-made methods in io 
  io.WriteString(os.Stdout, "Hello World!")
  // Write using fmt
  fmt.Fprint(os.Stdout,"Hello World!")
  // You can also use the format feature 
  fmt.Fprintf(os.Stdout, "%s", "Hello World")
}
