package main

import (
	"bufio"
	"fmt"
	"math"
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

	distance := 0.0
	for k, _ := range tab1 {
		distance += math.Abs(tab1[k] - tab2[k])
	}

	fmt.Printf("%f", distance)
}
