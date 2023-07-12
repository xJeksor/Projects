package main

import (
	"encoding/json"
	"fmt"
	"sort"
)

type WordTime struct {
	Word      string  `json:"w"`
	StartTime float64 `json:"t"`
	EndTime   float64 `json:"e"`
	Speaker   int64   `json:"s,omitempty"`
}

func main() {
	transcript := `[
		{
			"w": "dobry",
			"t": 0.5,
			"e": 0.75,
            "s": 3
		},
		{
			"w": "Dzień",
			"t": 0,
			"e": 0.25,
			"s": 3
		},
		{
			"w": "z",
			"t": 1,
			"e": 1.25,
			"s": 1
		},
		{
			"w": "Głogowski",
			"t": 5.5,
			"e": 5.75,
			"s": 1
		},
		{
			"w": "strony",
			"t": 2,
			"e": 2.25,
			"s": 1
		},
		{
			"w": "Kołodziej",
			"t": 3,
			"e": 3.25,
			"s": 2
		},
		{
			"w": "Witam",
			"t": 3.5,
			"e": 3.75,
			"s": 2
		},
		{
			"w": "serdecznie",
			"t": 4,
			"e": 4.25,
			"s": 1
		},
		{
			"w": "tutaj",
			"t": 4.5,
			"e": 4.75,
			"s": 1
		},
		{
			"w": "Łukasz",
			"t": 5,
			"e": 5.5,
			"s": 1
		},
		{
			"w": "firma",
			"t": 6,
			"e": 6.25,
			"s": 1
		},
		{
			"w": "tej",
			"t": 1.5,
			"e": 1.75,
			"s": 1
		},
		{
			"w": "voicelab",
			"t": 6.5,
			"e": 6.75,
			"s": 2
		},
		{
			"w": "Tomasz",
			"t": 2.5,
			"e": 2.75,
			"s": 2
		}]`
	// 1. unmarshal to slice of WordTime
	// 2. sort the slice by "t"
	// 3. print sorted array

	fmt.Println(transcript)
	var wordtimes []WordTime
	err := json.Unmarshal([]byte(transcript), &wordtimes)
	
	if err != nil{
		panic(err)
	}

	sort.Slice(wordtimes, func(i ,j int) bool {
		return wordtimes[i].StartTime < wordtimes[j].StartTime
	})

	for i, val := range wordtimes{
		fmt.Printf("Indeks: %d\n %+v\n",i,val)
	}
}
