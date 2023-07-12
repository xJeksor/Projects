//Projekt:Odkurzacz
//Na poczatku uruchamiamy program Odkurzacz.go, ile razy chcemy. 
//Potem uruchamiamy program Odkurzacz_Graph.go. 
//Pierwszy program zapisuje do plikow, a drugi z nich odczytuje. 
//Zeby zobaczyc graf, bez zmiany programu Odkurzacz_Graph.go, program Odkurzacz.go trzeba uruchomic 7 razy
//Po uruchomieniu Odkurzacz.go stworza sie 2 pliki tekstowe: DistanceTraveled.txt oraz Average.txt
//Po uruchomieniu Odkurzacz_Graph.go dodatkowo stworzy sie plik output.png, w ktorym narysowany jest graf
//Zeby moc korzystac z paczki "github.com/wcharczuk/go-chart/v2",ktora wyswietla graf trzeba dodac 2 rzeczy: go.mod i go.sum
package main

import (
    "fmt"
	"os"
	"io"
    "github.com/wcharczuk/go-chart/v2"  
	
)


func readFile(filePath string) (numbers []float64) { 
    f, err := os.Open(filePath)
    if err != nil {
        panic(fmt.Sprintf("open %s: %v", filePath, err))
    }
    var val float64 //Zmienna do przechowywania liczb z pliku 
	
    for {
        _, err := fmt.Fscanf(f, "%f", &val) 

		

        if err != nil {
            if err == io.EOF { 
                break
            }
        }
        numbers = append(numbers, val) 
    }
    return
}



func main() {
    
	Graph := make(map[float64]float64)
	var sum,count float64 
	max := 0.0
    numbers := readFile("...\\Average.txt") // Utworzenia slice'a z danych z pliku
	numbers2 := readFile("...\\DistanceTraveled.txt")
    for i := range numbers { // Petla do liczenia sredniej i maksymalnej odleglosci odkurzacza od srodka
		sum += numbers[i]
		count++
		if numbers[i] > max {
			max = numbers[i]
		}
	}
	fmt.Printf("Srednia odleglosc odkurzacza od srodka wynosi: %.2f, a maksymalna: %.2f",sum/count,max)
    fmt.Println()

	for i := 0; i<len(numbers); i++{
		Graph[numbers[i]]=numbers2[i]
	}

	fmt.Println(Graph)

	keys := make([]float64, 0, len(Graph))
	values := make([]float64, 0,len(Graph))

	fmt.Println("Klucze:")
	
    for k := range Graph {
        keys = append(keys, k)
		values = append(values, Graph[k])
		fmt.Println(k)
    }
	fmt.Println()
	fmt.Println("Wartosci:")

	for _, i := range values {
		fmt.Println(i)
	}
	fmt.Println()
	fmt.Println("Tak wyglada mapa:",Graph)

	
	graph := chart.BarChart{
		Title: "OX:Srednia odleglosc od srodka OY:Przebyta odleglosc",
		Background: chart.Style{
			Padding: chart.Box{
				Top: 40,
			},
		},
		Height:   512,
		BarWidth: 60,
		Bars: []chart.Value{
			 {Value: values[0], Label: fmt.Sprint(keys[0])},
			 {Value: values[1], Label: fmt.Sprint(keys[1])},
			 {Value: values[2], Label: fmt.Sprint(keys[2])},
			 {Value: values[3], Label: fmt.Sprint(keys[3])},
			 {Value: values[4], Label: fmt.Sprint(keys[4])},
			 {Value: values[5], Label: fmt.Sprint(keys[5])},
			 {Value: values[6], Label: fmt.Sprint(keys[6])},
			
		},
	}


	f, _ := os.Create("output.png")
	defer f.Close()
	graph.Render(chart.PNG, f)



}




