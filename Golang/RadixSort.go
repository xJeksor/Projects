package main

import (
	"fmt"
)

func radixSort(arr [7]string) [7]string {

	counter := 0 
	semiSorted := [7]string{}  
	z := 0
	a := 6
	
	for i := 0; i < len(arr) ; i++{

		arrcounter := [26]int{}
		sum := 0

		for j := 0; j < len(arr) ; j++{   //zliczenia wystapien liter
		counter = int(arr[j][6-z]) - 97
		arrcounter[counter]++
		}
		z++

		for  x := 0; x < 26 ; x++{ //sumowanie 
			if arrcounter[x]!=0{
				sum = sum + arrcounter[x] 
				arrcounter[x] = sum - 1
			}
		}

		fmt.Println(arrcounter)


		for y := 6; y >= 0; y--{
			semiSorted[arrcounter[int(arr[y][a]) - 97]] = arr[y]  //wkladanie do pomocniczej tablicy
			arrcounter[int(arr[y][a]) - 97]--
		}
		
		a--	
			fmt.Println(i+1, "digit:" ,semiSorted, "\n")
	}
	return semiSorted

}


func main(){
	
	arr := [7]string{"filipek","yasuoyo","polakak","abcdefg","gfedcba","poiuytr","bwelrtj"}  
	fmt.Println("Sorted Array :",radixSort(arr))

}