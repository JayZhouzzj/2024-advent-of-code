package main

import (
	"fmt"
)

func solve(l1, l2 []int) int {
	res := 0
	counter := make(map[int]int)
	for _, val := range l2 {
		counter[val]++
	}

	for _, val := range l1 {
		res += val * counter[val]
	}

	return res
}

func main() {
	var a, b int
	var list1, list2 []int
	for {
		_, err := fmt.Scan(&a, &b)
		if err != nil {
			// If the error is EOF, break the loop
			break
		}
		list1 = append(list1, a)
		list2 = append(list2, b)
	}
	fmt.Println(list1)
	fmt.Println(list2)
	fmt.Println(solve(list1, list2))
}
