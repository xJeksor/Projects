//Projekt:Odkurzacz
//Na poczatku uruchamiamy program Odkurzacz.go, ile razy chcemy. 
//Potem uruchamiamy program Odkurzacz_Graph.go. 
//Pierwszy program zapisuje do plikow, a drugi z nich odczytuje. 
//Zeby zobaczyc graf, bez zmiany programu Odkurzacz_Graph.go, program Odkurzacz.go trzeba uruchomic 7 razy
//Po uruchomieniu Odkurzacz.go stworza sie 2 pliki tekstowe: DistanceTraveled.txt oraz Average.txt
//Po uruchomieniu Odkurzacz_Graph.go dodatkowo stworzy sie plik output.png, w ktorym narysowany jest graf
//Zeby moc korzystac z paczki "github.com/wcharczuk/go-chart/v2", ktora wyswietla graf trzeba dodac 2 rzeczy: go.mod i go.sum
package main

import (
	"flag"
	"fmt"
	"math"
	"math/rand"
	"time"
	"os"
)


var DistanceTraveled = 0 

func flags() (int,int){ //Flagi po to zeby mozna bylo od razu wpisywac w terminalu dlugosc i szerokosc dywanu
	x,y := 0,0
	flag.IntVar(&x, "width", 10, "Width of the carpet")
	flag.IntVar(&y, "height", 10, "Height of the carpet")
	flag.Parse()
	return x,y
}


func Distance(width int,height int,board [][]int,file *os.File){ //funkcja do liczenia odlegosci odkurzacza od srodka 
	o,p := 0,0 
	for i := 0; i<width; i++{ //Przeszukuje slice'a 2D i zapisuje wspolrzedne odkurzacza czyli "8"
		for j:= 0; j<height; j++{
			if board[i][j] == 8{
				o = i
				p = j
			}
		}
	}
	Distance := math.Pow(float64(o-width/2-1),2) + math.Pow(float64(p-height/2-1),2) //Wzor na dlugosc odcinka
	fmt.Printf("Odległość odkurzacza od srodka wynosi: %.2f", math.Sqrt(Distance))
	fmt.Fprintf(file,"%.2f ",math.Sqrt(Distance)) 
	
}




func main(){
	rand.Seed(time.Now().UnixNano()) //Generowanie losowych liczb

	f,err := os.OpenFile("...\\Average.txt", os.O_RDWR|os.O_APPEND|os.O_CREATE, 0660) 
	if err != nil { 
		fmt.Println(err)
		return
	}
	defer f.Close()

	t,err := os.OpenFile("C:\\Users\\filip\\go\\src\\Programowanie\\DistanceTraveled.txt", os.O_RDWR|os.O_APPEND|os.O_CREATE, 0660) 
	if err != nil { 
		fmt.Println(err)
		return
	}
	defer t.Close()

	width,height := flags() 

	board := make([][]int,width) //Tworzenie 2D slice'a 
	for i := range board{
		board[i] = make([]int,height)
	}

	a := width/2-1 //Ustawienie srodka dywanu
	b := height/2-1
	
	for i := 0; i<width; i++{ //Wypelnienie calego dywanu brudem czyli "1" , i ustawienie odkurzacza czyli "8"
		for j := 0; j<height; j++{
			board[i][j]=1
		}

		board[a][b] = 8
		fmt.Println(board[i])
	}
	

	for i:= rand.Intn(10) + 240; i>0; i--{ //Losowo generowana ilosc ruchow odkurzacza z danego zakresu
		x := rand.Intn(4) //Losowo wybierany kierunek, w ktorym odkurzacz ma sie poruszyc
		switch x {

		case 0: 
			
			up := rand.Intn(height) + 1 //Zakres od przynajmniej 1 ruchu do wysokosci dywanu jest najbardziej losowy
			if a-up < 0 { //Jezeli odkurzacz bedzie chcial wyjechac poza dywan to sie zatrzymuje
				break
			}
			board[a-up][b] = 8 //Ustawiamy odkurzacz na ostatnim miejscu jakie odwiedzi
			for i := a; i>a-up; i--{
				board[i][b] = 0 // Tutaj wszystkie miejsca po ktorych przejezdzal uznajemy za czyste czyli ustawiamy na "0"
			} 
			fmt.Println()
			fmt.Println("Kierunek : ↑")
			for i := 0; i<width; i++{  //Printujemy kolorami dywan zeby byl bardziej czytelny
				fmt.Print("[ ")
				for j := 0; j<height; j++{
					if board[i][j] == 8 { //Jezeli natrafimy na odkurzacz to pole na ktorym stoi staje sie czerwone
						fmt.Printf("\033[31;1;88m%d\033[0m ",board[i][j])
					} else if board[i][j] == 0 { //Jezeli natrafimy na pola po ktorych odkurzacz pojechal to te pola staja sie niebieskie
						fmt.Printf("\033[31;1;34m%d\033[0m ",board[i][j])
					} else {
						fmt.Printf("%d ",board[i][j]) // W innym przypadku piszemy "1"
					}
				}
				fmt.Println("]")
			}
			a = a-up //Zapamietujemy nowa pozycje odkurzacza
			DistanceTraveled += up

		case 1:

			left := rand.Intn(width) + 1
			if b-left < 0 {
				break
			}
			board[a][b-left] = 8
			for i := b; i>b-left; i--{
				board[a][i] = 0
			} 
			
			fmt.Println()
			fmt.Println("Kierunek : ←")
			for i := 0; i<width; i++{ 
				fmt.Print("[ ")
				for j := 0; j<height; j++{
					if board[i][j] == 8 {
						fmt.Printf("\033[31;1;88m%d\033[0m ",board[i][j])
					} else if board[i][j] == 0 {
						fmt.Printf("\033[31;1;34m%d\033[0m ",board[i][j])
					} else {
						fmt.Printf("%d ",board[i][j])
					}
				}
				fmt.Println("]")
			}
			b = b-left
			DistanceTraveled += left

		case 2:

			down := rand.Intn(height) + 1
			if a+down > 9 {
				break
			}
			board[a+down][b] = 8
			for i := a; i<a+down; i++{
				board[i][b] = 0
			} 
				
			fmt.Println()
			fmt.Println("Kierunek : ↓")
			for i := 0; i<width; i++{ 
				fmt.Print("[ ")
				for j := 0; j<height; j++{
					if board[i][j] == 8 {
						fmt.Printf("\033[31;1;88m%d\033[0m ",board[i][j])
					} else if board[i][j] == 0 {
						fmt.Printf("\033[31;1;34m%d\033[0m ",board[i][j])
					} else {
						fmt.Printf("%d ",board[i][j])
					}
				}
				fmt.Println("]")
			}
			a = a+down
			DistanceTraveled += down
		case 3:

			right := rand.Intn(width) + 1
			if b+right > 9 {
				break
			}
			board[a][b+right] = 8
			for i := b; i<b+right; i++{
				board[a][i] = 0
			} 
			
			fmt.Println()
			fmt.Println("Kierunek : →")
			for i := 0; i<width; i++{ 
				fmt.Print("[ ")
				for j := 0; j<height; j++{
					if board[i][j] == 8 {
						fmt.Printf("\033[31;1;88m%d\033[0m ",board[i][j])
					} else if board[i][j] == 0 {
						fmt.Printf("\033[31;1;34m%d\033[0m ",board[i][j])
					} else {
						fmt.Printf("%d ",board[i][j])
					}
				}
				fmt.Println("]")
			}
			b = b+right
			DistanceTraveled += right
		}	
	}

	fmt.Println()
	Distance(width,height,board,f) //Wywolujemy funkcje, ktora oblicza odleglosc odkurzacza od srodka i wpisuje ja do pliku
	fmt.Fprintf(t,"%d ",DistanceTraveled) //Wywolujemy funkcje, ktora oblicza przebyta odleglosc i wpisuje ja do pliku
}