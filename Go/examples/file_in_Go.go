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

// ReadFile used to readfiles from disk
func ReadFile() {
    output, err := ioutil.ReadFile("myfile.txt")
    
    if err != nil {
        log.Println("error in reading file:", err)
    }
    result := string(output)
    fmt.Println(result)
}

// CreateFile used to create file and store in disk
func CreatFile() {
    info := []byte("Hello! you can learn about Go lang!!!")
    err := ioutil.WriteFile("myfile.txt", info, 0777)
    
    if err != nil {
        log.Println("error in writing file:", err)
    }
}
