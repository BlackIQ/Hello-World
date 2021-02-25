// Learn here about "File in Go" -> https://vrgl.ir/Csdnc
// I wrote it :)
// GitHub account -> Mr-SinaYeganeh 
package main

import (
    "fmt"
    "io/ioutil"
    "log"
)

func main() {
    CreatFile()
    ReadFile()
}

func ReadFile() {
    output, err := ioutil.ReadFile("file-to-read.txt")
    
    if err != nil {
        log.Println("you have an error:", err)
    }
    result := string(output)
    fmt.Println("file text:\n", result)
}

func CreatFile() {
    info := []byte("Hello! you can learn about Go lang!!!")
    err := ioutil.WriteFile("file-to-read.txt", info, 0777)
    
    if err != nil {
        log.Println("you have an error:", err)
    }
}
