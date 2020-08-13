package main

import (
	"fmt"
)

// Nested loop solution for: https://leetcode.com/problems/single-number-ii/

func singleNumber(nums []int) int {
	m := make(map[int]int)
	for _, val := range nums {
		m[val]++
	}
	for i, count := range m {
		if count == 1 {
			return i
		}
	}
	fmt.Println(m)
	return 0
}

func main() {
	slice1 := []int{11, 11, 3, 11}
	fmt.Println(singleNumber(slice1))
}

