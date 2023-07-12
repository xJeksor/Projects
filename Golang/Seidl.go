package main

import (
	"fmt"
	"math"
	"math/rand"
	"time"
)

func GaussianElimination(A [][]float64, b []float64) (x,y float64){
	n := len(b)
	max := 0
	for k := 0; k < n; k++ {
		max = k
		for i := k + 1; i < n; i++{
			if math.Abs(A[i][k]) > math.Abs(A[max][k]){
				max = i
			}
		}
		temp := A[k]
		A[k] = A[max]
		A[max] = temp

		t := b[k]
		b[k] = b[max]
		b[max] = t

		for i := k + 1; i < n; i++{
			factor := A[i][k] / A[k][k]
			b[i] -= factor * b[k]
			for j := k; j < n; j++ {
				A[i][j] -= factor * A[k][j]
			}
		}
	}

	solution := make([]float64,n)
	for i := n - 1; i >= 0; i-- {
		sum :=0.
		for j := i + 1; j < n; j++ {
			sum += A[i][j] * solution[j]
		}
		solution[i] = (b[i] - sum) / A[i][i]
	}
	return solution[0],solution[1]
}

func Seidel(A [][]float64, b []float64, d, constraints int) (x ,y float64){
	rand.Seed(time.Now().UnixNano()) //Generowanie losowych liczb
	if constraints == 1 {
		if(A[0][0] >= 0){
			x := 0.
			y := (b[0]/A[0][1])
			return x ,y
		} else {
			return math.Inf(1),math.Inf(1)
		}
	}
	if d == 1 {
		y := 0.
		for i := 0; i < constraints; i++ {
			temp := b[i] / A[i][d-1]
			if temp >= y {
				y = temp
			}
		}
		return x ,y
	}
	if d == constraints {
		// fmt.Printf("Odpowiedzi GausElim: ")
		// fmt.Println(GaussianElimination(A,b))
		return GaussianElimination(A,b)
	}

	random := rand.Intn(constraints)
	fmt.Printf("Random: %d\n",random)

	tempA := make([][]float64, constraints - 1)
	for i := range tempA {
		tempA[i] = make([]float64,d)
	}
	tempB := make([]float64,constraints - 1) 

	// Usuwanie losowo wybranego ograniczenia
	k := 0
	for i := 0; i < constraints; i++ {
		if i != random {
			for j := 0; j < d; j++ {
				tempA[k][j] = A[i][j]
			}
			tempB[k] = b[i]
			k++
		}
		fmt.Println(A[i])
	} 
	
	recursion_x,recursion_y:= Seidel(tempA,tempB,d,constraints - 1)

	if recursion_x >= 0 && recursion_y >= 0 {
		return recursion_x,recursion_y
	} else { //Zerowanie "x"
		factor := []float64{(A[random][1] * (-1)) / A[random][0], b[random] / A[random][0]}
		for i := 0; i < constraints - 1; i++ {
			tempA[i][1] += factor[0] * tempA[i][0]
			tempB[i] += factor[1] * tempA[i][0]
			tempA[i][0] = 0 
		}
		return Seidel(tempA,tempB,d,constraints - 1)
	}
}
	
func main(){
	var d,constraints int
	var x,y float64

	fmt.Print("Podaj ilość zmiennych: ")
	fmt.Scanln(&d)
	fmt.Print("Podaj liczbę ograniczeń: ")
	fmt.Scanln(&constraints)

	A := [][]float64{
		{-3,1},
		{2,1},
		{6,2},
		{-2,-2},
		{-2,1},
	}

	b := []float64{4,4,24,-3,0}

	fmt.Print("Współczynnik przy x dla funkcji celu: ")
	fmt.Scanln(&x)
	fmt.Print("Współczynnik przy y dla funkcji celu: ")
	fmt.Scanln(&y)

	if d != 1 {

	min_angle := 360*math.Pi/180
	
	// Szukanie najmniejszego kąta
	for i := 0; i < constraints; i++{
		var temp = math.Acos((x * A[i][0] + y * A[i][1]) / (math.Sqrt(math.Pow(x,2) + (math.Pow(y,2))) * (math.Sqrt(math.Pow(A[i][0], 2) + math.Pow(A[i][1], 2)))))
		if temp <= min_angle {
			min_angle = temp 
		}
	}
	// Szukanie czy któryś z kątow ma 180 - min_angle
	err := false
	for i := 0; i < constraints; i++ {
		var temp = math.Acos((x * A[i][0] + y * A[i][1]) / (math.Sqrt(math.Pow(x,2) + (math.Pow(y,2))) * (math.Sqrt(math.Pow(A[i][0], 2) + math.Pow(A[i][1], 2)))))
		if temp == math.Pi - min_angle {
			err = true
			break
		}
	}
	
	if err {
		fmt.Println("Obszar nieograniczony")
	} else {
		answer_x,answer_y := Seidel(A,b,d,constraints)
		fmt.Printf("Odpowiedzi: ")
		fmt.Println(answer_x,answer_y)
	}
	} else{
		answer_x,answer_y := Seidel(A,b,d,constraints)
		fmt.Printf("Odpowiedzi: ")
		fmt.Println(answer_x,answer_y)
	}

}

//https://www.sanfoundry.com/java-program-gaussian-elimination-algorithm/
//http://adam.chlipala.net/berkeley/classes/scribe270.pdf