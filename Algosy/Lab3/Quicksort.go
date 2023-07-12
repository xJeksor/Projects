//https://qvault.io/golang/quick-sort-golang/

package main

import ("fmt" 
 		"math/rand" 
  		"time")

const c = 10000000


func BubbleSort(array[] int,low,high int)[]int {
	for i:=low; i< high; i++ {
	   for j:=0; j < high; j++ {
		  if (array[j] > array[j+1]) {
			 array[j], array[j+1] = array[j+1], array[j]
		  }
	   }
	}
	return array
 }


func partition(arr []int, low, high int) ([]int, int) {
	pivot := arr[high]
	i := low
	for j := low; j < high; j++ {
		if arr[j] < pivot {
			arr[i], arr[j] = arr[j], arr[i]
			i++
		}
	}
	arr[i], arr[high] = arr[high], arr[i]
	return arr, i
}

func quickSort(arr []int, low, high int) []int {
	if low + c >= high {
		BubbleSort(arr,low,high)
	}
	
	if low + c < high {
		var p int
		arr, p = partition(arr, low, high)
		arr = quickSort(arr, low, p-1)
		arr = quickSort(arr, p+1, high)
	}
	return arr
}

func main(){
	rand.Seed(time.Now().UnixNano()) 
	x,y,z := make([]int,100001),make([]int,100001),make([]int,100001)


	for i := 0; i<100000;i++{
		x[i] = i
		y[i] = rand.Intn(10000)
	}
	for i := 100000;i>0;i--{
		z[i] = i
	}
	//x := []int{5,4,6,3,1,2,10,2,7,10}
	// y := []int{rand.Intn(100),rand.Intn(100),rand.Intn(100),rand.Intn(100),rand.Intn(100),rand.Intn(100),rand.Intn(100),rand.Intn(100),rand.Intn(100),rand.Intn(100)}
	// z := []int{10,9,8,7,6,5,4,3,2,1}

	start := time.Now()
	fmt.Println(quickSort(x,0,len(x)-1))
	stop := time.Since(start)
	fmt.Println("Normalna tablica: ",stop)
	fmt.Printf("\n")

	start1 := time.Now()
	fmt.Println(quickSort(y,0,len(y)-1))
	stop1 := time.Since(start1)

	fmt.Println("Losowa tablica: ",stop1)
	fmt.Printf("\n")

	start2 := time.Now()
	fmt.Println(quickSort(z,0,len(z)-1))
	stop2 := time.Since(start2)
	fmt.Println("Malejąca tablica: ",stop2)
	fmt.Printf("\n")

	// Czasy dla Quicksorta:
	// [1 2 2 3 4 5 6 7 10 10]
	// Normalna tablica:  39.58µs

	// [0 3 11 17 29 53 57 63 68 87]
	// Losowa tablica:  8.254µs

	// [1 2 3 4 5 6 7 8 9 10]
	// Malejąca tablica:  8.583µs

	// Czasy dla Bubblesorta:

	// [1 2 2 3 4 5 6 7 10 10]
	// Normalna tablica:  112.615µs

	// [4 13 37 56 70 71 73 78 83 92]
	// Losowa tablica:  13.064µs

	// [1 2 3 4 5 6 7 8 9 10]
	// Malejąca tablica:  8.851µs

	// Czasy dla Quicksorta dla tablic o rozmiarze 100000:
	// Normalna tablica : 1.94s
	// Losowa tablica : 28.999ms
	// Malejąca tablica : 3.73s

	// Czasy dla Bubblesorta dla tablic o rozmiarze 100000:
	// Normalna tablica : 5s
	// Losowa tablica : 15.5s
	// Malejąca tablica : 5s

}