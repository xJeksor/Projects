package main

import (
	"fmt"
	"io"
	"os"
)

const m = 20000
const x = 0.8

type nazwiska struct {
	value int
	name  string
}

func hash(word string, j int) int {

	len := len(word)
	var result byte
	var i int

	for i = 0; i < len-1; i = i + 2 {
		result ^= ((word[i] << 4) + word[i+1])
	}

	if word[i-1] != 0 {
				result ^= (word[i-1] << 4)
	}

	return (int(result)%m + j*(int(result)%(m-2))) % m
}

func main() {

	

	Hash := [m]nazwiska{}

	file, err := os.Open("...\\nazwiska.txt")
	defer file.Close()
	if err != nil {
		fmt.Println(err)
		return
	}

	var (
		count   int
		name    string
		index   int
		deleted int
	)

	for i := 0; i < m*x; i++ {
		_, err := fmt.Fscanf(file, "%d %s", &count, &name)
		j := 0

		if err != nil {
			if err == io.EOF {
				break
			}
		}

		for {

			if j == m {
				break
			}

			index = hash(name, j)

			if Hash[index].name == "" {
				Hash[index].value = count
				Hash[index].name = name
				break
			} else {
				j++
			}
		}
	}
	for i, _ := range Hash {
		fmt.Println(i, " ", Hash[i], "\n")
	}

	for i := 0; i < m; i++ {
		if Hash[i].name != "" {
			Hash[i].name = "DEL"
			Hash[i].value = 0
			deleted++
		}

		if deleted == m*x*0.5 {
			break
		}

	}

	for i, _ := range Hash {
		fmt.Println(i, " ", Hash[i], "\n")
	}

	fmt.Println("Usunieto :", deleted, "elementow")
}
