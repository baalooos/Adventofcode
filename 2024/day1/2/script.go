package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func main() {

	var tab1 []float64
	var tab2 []float64

	f, err := os.Open("input.txt")

	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(f)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		line := fileScanner.Text()
		split_line := strings.Split(line, "   ")

		left, err := strconv.ParseFloat(split_line[0], 64)
		if err != nil {
			fmt.Println(err)
		}

		right, err := strconv.ParseFloat(split_line[1], 64)
		if err != nil {
			fmt.Println(err)
		}

		tab1 = append(tab1, left)
		tab2 = append(tab2, right)
	}

	slices.Sort(tab1)
	slices.Sort(tab2)

	similarity := 0.0

	length1 := len(tab1)
	length2 := len(tab2)

	start := 0

	for i := 0; i < length1; i++ {
		factor := 0.0
		for j := start; j < length2; j++ {
			if tab1[i] < tab2[j] {
				start = j
				println("break")
				break
			} else if tab1[i] == tab2[j] {
				factor += 1
			}
		}
		similarity += tab1[i] * factor
	}

	fmt.Printf("%f", similarity)
}
