package main

import (
	"errors"
	"fmt"
	"time"
)

func timetolive() (string, error) {
	var err error
	//TTL := "2006-01-02T15:04:05Z07:00"
	//TTL := "2012-11-01T22:08:41+00:00"
	TTL := "test"

	if TTL == "" {
		// Set TTL to be 24h from now by default
		TTL = time.Now().AddDate(0, 0, +1).Format(time.RFC3339)
	} else {
		fmt.Printf("TTL before parse: %v\n", TTL)
		parsedTTL, err := time.Parse(time.RFC3339, TTL)
		fmt.Printf("ParsedTTL is %v", parsedTTL)
		if err != nil {
			return TTL, errors.New("TTL not in the correct format eg: 2021-01-08T22:23:38Z")
		}
		if parsedTTL.After(time.Now().AddDate(0, 0, +1)) {
			err = errors.New("Environment TTL cannot be extended past 24h")
			return TTL, err
		} else {
			// change parsedTTL back to string and assign to TTL
			TTL = parsedTTL.Format(time.RFC3339)
		}
	}
	return TTL, err
}

func main() {
	myvar, err := timetolive()
	fmt.Println(myvar)
	fmt.Println(err)
}
