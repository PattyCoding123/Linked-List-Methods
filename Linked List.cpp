#include <iostream>
#include <string>
using namespace std;

// Short exception class for the Linked List
class LinkedListException {
private:
	string message;

public:
	string what(){
		return message;
	}

	LinkedListException(string m) {
		message = m;
	}
};

// The student class will contain the information we want the nodes to represent
class Student {
private:
	string firstName;
	string lastName;

public:
	// Set method for first name
	void setFirstName(string f) {
		firstName = f;
	}

	// Set method for last name
	void setLastName(string l) {
		lastName = l;
	}

	// Get method for first name
	string getFirstName() const {
		return firstName;
	}

	// Get method for last name
	string getLastName() const {
		return lastName;
	}


	// Constructor which initializes the student's first and last name based on
	// the input parameters
	Student(string f, string l) {
		firstName = f;
		lastName = l;
	}

	// Constructor which initializes the student's first and last name as an empty string
	Student() {
		firstName = "";
		lastName = "";
	}
};

// The NodeType class will represent the nodes in the linked list
// Each node will have a Student member as the data as well as a 
// pointer to the next node in the list.
// We create the NodeType objects dynamically.
class NodeType {
public:
	// Empty constructor declaration of Student member "data"
	Student data;
	NodeType* next;
	NodeType() {
		next = nullptr;
	}
};

// The LinkedList class will contain the members and methods for making a Linked List
class LinkedListType {
private:
	int size;
	NodeType* first;
	NodeType* last;

public:

	// Checks if the list is empty by seeing
	// if the first and last nodes are null
	bool isEmpty() const {
		return (first == nullptr && last == nullptr);
	}

	// Get method for the list size
	int getSize() const {
		return size;
	}

	// Allows us to traverse the linked list and print out the data
	void display() const {
		NodeType* current = first;
		while (current != nullptr) {
			cout << current->data.getFirstName() << " " << current->data.getLastName() << endl;
			current = current->next;
		}
	}

	// The addLast function will create a new node dynamically, and then will
	// assign the new node's data to be the student object that we declare. Then, it 
	// will insert the node into the list at the last position.
	void addLast(const Student studentData) {
		NodeType* newNode = new NodeType();
		newNode->data = studentData;

		// If the list is empty, have the first and last pointers point to
		// newNode.
		if (isEmpty()) {
			first = newNode;
			last = newNode;
		}

		// If list is NOT empty, have the node pointed to by "last" change its next link
		// so that it points to newNode. Then, change "last" to point to the current final 
		// node in the list which we just added.
		else {
			last->next = newNode;
			last = newNode;
		}

		// Increase size by 1.
		size++;

	}

	// The addFirst function will create a new node dynamically, and then we will assign
	// the new node's data to be the student object that we declare. Then, it will
	// insert the node into the first position of the linked list.
	void addFirst(const Student studentData) {
		NodeType* newNode = new NodeType();
		newNode->data = studentData;

		// If the list is empty, have the first and last pointers point to
		// newNode.
		if (isEmpty()) {
			first = newNode;
			last = newNode;
		}

		// If the list is not empty, have new node's link point to first and then
		// update first pointer to point to newNode which we just added.
		else {
			newNode->next = first;
			first = newNode;
		}

		// Increase size by 1.
		size++;
	}
	
	// This function returns a copy of the first element in the list. If the list is empty,
	// it will throw an exception.
	Student getFirst() const {

		// If the function is empty, throw an exception
		if (isEmpty())
			throw LinkedListException("The list is empty.");

		// Return data of first node if list is not empty.
		else
			return first->data;

	}

	// This function returns a copy of the last element in the list. If the list is empty,
	// it will throw an exception.
	Student getLast() const {

		// If the function is empty, throw an exception
		if (isEmpty())
			throw LinkedListException("The list is empty.");

		// Return data of last node if list is not empty.
		else
			return last->data;

	}

	// DeleteFirst function
	void DeleteFirst() {
		// Throw an exception if list is empty
		// Since we cannot remove non-existing nodes
		if (isEmpty())
			throw LinkedListException("The list is empty.");

		// If size is only 1 node, delete it and set first and last
		// to null pointers since there is nothing to point to in the list
		// and decrease size by 1
		else if (size == 1) {
			delete first;
			first = nullptr;
			last = nullptr;
			size--;
		}

		// If size > 1, We must use a temp variable to point to "first" node and delete
		// the temp once we have first point to first->next
		// Reason: If we simply delete first, then we will have no method to access
		// The next node in the list since the firts node's data, including its link
		// Will also be deleted, and we won't be able to set "first" to first->next
		// And simply having first = first->next will not delete first node.
		else {
			NodeType* temp = first;
			first = first->next;
			delete temp;
			size--;
		}
	}

	// DeleteLast function
	void DeleteLast() {
		// Throw an exception if list is empty
		// Since we cannot remove non-existing nodes
		if (isEmpty()) 
			throw LinkedListException("The list is empty.");

		// If size is only 1 node, delete it and set first and last
		// to null pointers since there is nothing to point to in the list
		// and decrease size by 1
		else if (size == 1) {
			delete first;
			first = nullptr;
			last = nullptr;
			size--;
		}

		// If size > 1, keep track of previous pointer pointed to by last
		// Since we don't want the previous node to be pointing to a dangling 
		// pointer after we delete node pointed to by "last"
		else {
			NodeType* previous = first;

			// Keep traversing through linked list until the next link
			// Points to "last"
			while (previous->next != last)
				previous = previous->next;

			// Delete node pointed to by "last" once previous->next points
			// to last, then have "last" point to previous since last is
			// now a dangling pointer.
			delete last;
			last = previous;

			// We must then set previous->next to nullptr to
			// avoid it pointing to a dangling pointer
			previous->next = nullptr;
			size--;
		}

	}

	// Constructor for Linked List class
	LinkedListType() {
		size = 0;
		first = nullptr;
		last = nullptr;
	}

};

int main()
{
	cout << "Linked List Application!\n";
	cout << "===========================\n";

	// Create three student objects
	Student student_1("Patrick", "Ducusin");
	Student student_2("Bruce", "Banner");
	Student student_3("Tony", "Stark");

	// Declare a Queue, represented by a linked list 
	LinkedListType queue;

	// Add the three student objects into linked list using addFirst() function
	// Since we want to represent the data in a Queue
	queue.addFirst(student_1);
	queue.addFirst(student_2);
	queue.addFirst(student_3);

	// Display contents of front element in queue using getLast() function
	// Since the first element becomes the "final" one in the queue, and should
	// be the first one to get retrieved again
	cout << queue.getLast().getFirstName() << " " << queue.getLast().getLastName() << endl;

	// Delete front element using the deleteLast() function
	queue.DeleteLast();

	// Repeat process with second element
	cout << queue.getLast().getFirstName() << " " << queue.getLast().getLastName() << endl;
	queue.DeleteLast();

	// Repeat process with third element
	cout << queue.getLast().getFirstName() << " " << queue.getLast().getLastName() << endl;
	queue.DeleteLast();

	// Show that queue is empty by trying to retrieve information
	try {
		cout << queue.getLast().getFirstName() << " " << queue.getLast().getLastName() << endl;
	}
	catch (LinkedListException obj) {
		cout << obj.what();
	}
}