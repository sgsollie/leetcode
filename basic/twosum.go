package main

import (
	"fmt"
)

/*
1. i = 0, num = 2, target = 9, table[7], false, table[2]=0
2. i = 1, num = 7, target = 9, table[2], true, return 0,1

*/

// Solution for: https://leetcode.com/problems/two-sum/

func twoSum(nums []int, target int) []int {
	table := make(map[int]int)
	for i, num := range nums {
		value, ok := table[target-num]
		if ok {
			return []int{value, i}
		}
		table[num] = i
	}
	return []int{}
}

func main() {

	a := []int{2, 7, 11, 15}
	fmt.Println(twoSum(a, 9))
}
