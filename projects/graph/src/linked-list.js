class LinkedList {
  /* Do not modify the constructor */
  constructor() {
    this.head = null;
    this.tail = null;
  }

  /* Add the given value to the tail
  of the list. The `tail` pointer
  should be updated accordingly */
  addToTail(value) {
    const node = {
      value: value,
      next: null
    };
    if (this.head === null) {
      this.head = node;
      this.tail = node;
      return;
    }
    this.tail.next = node;
    this.tail = node;
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    if (!this.head) return null;
    if (!this.head.next) {
      const value = this.head.value;
      this.head = null;
      return value;
    }
    const removedHead = this.head;
    this.head = this.head.next;
    return removedHead.value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    if (!this.head) return false;

    // iterative solution
    // let current = this.head;
    // while(current){
    //   if(current.value === value){
    //     return true;
    //   }
    //   current = current.next
    // }
    // return false;

    //recursive solution
    // const recurse = (node) => {
    //   if(node.value ===value ) return true;
    //   if(!node.next) return false;
    //   return recurse(node.next);
    // }
    // return recurse(this.head);

    function checkObject(node) {
      if (node.value === value) {
        return true;
      } else if (node.next === null) {
        return false;
      } else {
        return checkObject(node.next);
      }
    }
    return checkObject(this.head);
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    let biggest = null;
    let node = this.head;
    while (node) {
      if (biggest < node.value) {
        biggest = node.value;
      }
      node = node.next;
    }
    return biggest;
  }
}

module.exports = LinkedList;
