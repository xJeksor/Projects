package main

import (
	"fmt"
)


type Node struct {
	value string
	prev *Node
	next *Node
}

func addNode(s string,pointer *Node){ 
	node := Node{value: s}

	if pointer.next == pointer{
		node.next = pointer
		node.prev = pointer
		pointer.next = &node
		pointer.prev = &node
	}else {
		node.next = pointer.next
		pointer.next = &node

		node.next.prev = &node
		node.prev = pointer
	
	}

}

func show(pointer *Node){
	cart := pointer
	cart = cart.prev
	for ;cart.value != "";cart = cart.prev {
		fmt.Println(cart.value)
	}
}

func find(s string,pointer *Node) *Node{
	cart := pointer
	cart = cart.next
	for ;cart.value != "";cart = cart.next {
		if cart.value == s{
			return cart
		}
	}
	return nil
}

// func deleteNode(s string,pointer *Node){  Another way for deleting
// 	if find(s,pointer) != nil {
// 		NodeToDelete := find(s,pointer)
// 		tmp := Node{}
// 		tmp.next = NodeToDelete.next
// 		tmp.prev = NodeToDelete.prev
// 		NodeToDelete.prev.next = tmp.next
// 		NodeToDelete.next.prev = tmp.prev
// 	}
// }

func deleteNode(s string,pointer *Node){
	cart := pointer
	cart = cart.next
	for ;cart.value != "";cart = cart.next{
		if cart.value == s{
			tmp := Node{}
			tmp.next = cart.next
			tmp.prev = cart.prev
			cart.prev.next = tmp.next
			cart.next.prev = tmp.prev
			break
		}
	}
}

func deleteAll(pointer *Node){
	pointer.next = pointer
	pointer.prev = pointer
}

func noRepeatance(pointer *Node) *Node{
	counter := 1
	cart1,cart2 := pointer,pointer
	cart1,cart2 = cart1.next,cart2.next
	cart2 = cart2.next

	for ;cart1.value != "";cart1 = cart1.next {
		counter++
	}
	
	for i := 0; i < counter; i++{
		for j := 0; j < counter; j++{
			if cart1.value == cart2.value{
				deleteNode(cart2.value,cart2)
			}
			cart2 = cart1.next
		}
		cart1 = cart1.next
	}
	return cart1
}

func merge(pointer1 *Node,pointer2 *Node) Node{

	cart1:= pointer1
	pointer1 = pointer1.prev
	pointer1.next = pointer2.next
	pointer2.next.prev = pointer1
	pointer2 = pointer2.prev
	pointer2.next = cart1
	cart1.prev = pointer2
	return *cart1

}

func main(){ 

	Sentinel := Node{}
	Sentinel.value = ""
	Sentinel.prev = &Sentinel
	Sentinel.next = &Sentinel

	List3 := Node{}
	List3.value = ""
	List3.prev = &List3
	List3.next = &List3

	List2 := Node{}
	List2.value = ""
	List2.prev = &List2
	List2.next = &List2

	addNode("lorem",&Sentinel)
	addNode("ipsum",&Sentinel)
	addNode("Filip",&Sentinel)
	addNode("Darek",&Sentinel)
	addNode("Tomek",&Sentinel)
	addNode("nice",&Sentinel)

	addNode("123",&List2)
	addNode("567",&List2)
	addNode("890",&List2)
	addNode("123",&List2)
	addNode("312",&List2)
	
	List3 = merge(&Sentinel,&List2)
	show(&List3)
	

	//show(&Sentinel)
	//fmt.Println("--------------")

	// noRepeatance(&Sentinel)

	// show (&Sentinel)
	// fmt.Println("--------------")

	// fmt.Println("Szukamy \"ez\" w LinkedList: ")
	// find("ez",&Sentinel)
	// fmt.Println("--------------")

	// fmt.Println("Usuwamy \"ez\" w LinkedList: ")
	// deleteNode("ez",&Sentinel)
	// fmt.Println("--------------")
	// show(&Sentinel)
	// fmt.Println("--------------")

	// fmt.Println("Usuwamy wszystko.")
	// deleteAll(&Sentinel)
	// show(&Sentinel)
	// fmt.Println("--------------")

	// addNode("qwerty",&Sentinel)
	// addNode("Tomek",&Sentinel)
	// addNode("Filip",&Sentinel)
	// addNode("Darek",&Sentinel)
	// addNode("qwe123",&Sentinel)
	// addNode("ez",&Sentinel)
	// fmt.Println("Na nowo tworzymy: ")
	// show(&Sentinel)
	
}