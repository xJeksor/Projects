package main

import (
	"bufio"
	"fmt"
	"os"
)

const m = 983

func hash(word string) int {

    len := len(word)
    var result byte
	var i int 

    for i = 0; i < len-1; i = i + 2{
        result ^= ((word[i] << 4) + word[i+1])

    }

	if word[i-1] != 0{
		result ^= (word[i-1] << 4)
	}
	fmt.Println(int(result)%m)
    return int(result)%m
}

func main(){

	Arr := [m]int{}
	var line string

	
	file, err := os.Open("C:\\Users\\filip\\Desktop\\VSC\\Algosy\\Lab6\\liczenie.txt") 
	defer file.Close()
	if err != nil {
		fmt.Println(err)
		return
	}

	scanner := bufio.NewScanner(file)
	for i:=0;scanner.Scan();i++{
		line = scanner.Text()
		fmt.Println(line)
		if i == m {
			break
		}
		index := hash(line)
		Arr[index]++
		
	}
	counter,counterZero,max,srednia := 0.,0,0,0.

	for i, _ := range Arr{
		fmt.Println(Arr[i])
		if Arr[i] == 0 {
			counterZero++
		}
		if Arr[i] >= max{
			max = Arr[i]
		}
		if Arr[i] != 0 {
			srednia += float64(Arr[i])
			counter++
		}
	}
	fmt.Println("Max: ",max)
	fmt.Println("Srednia: ",srednia/counter)
	fmt.Println("Ilosc zer: ",counterZero)


		
}