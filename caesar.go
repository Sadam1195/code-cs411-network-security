package main 

import "fmt"

func main() {
	var plain_text string 


	plain_text = "syedowaisalichishti"
	fmt.Println(len(plain_text))

	for i := 0 ; i < len(plain_text) ; i++ {
		ch := (plain_text[i] + 3) % 26
		if (ch >= 'a' && ch <= 'z') || ch >= 'A' && ch <= 'Z' {
			fmt.Printf("%c", ch)
		}
	}

	fmt.Println(plain_text)
}