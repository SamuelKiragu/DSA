#include <stdlib.h>

void Heap1() {
  int* intPtr;
  // Allocates local pointer local varaible (but not its pointee)
  // Allocates heap block and stores its pointer in local variable
  // Dereference the pointer to set the pointeee to 42
  intPtr = malloc(sizeof(int));
  *intPtr = 42;
  // Deallocates heap block making the pointer bad
  // The programmer must remember not to use the pointer
  // after the pointee has been deallocated (this is free(intPtr);
  free(intPtr);
}

void HeapArray() {
  struct fraction* fracts;
  int i;

  // allocate the array
  fracts = malloc(sizeof(struct fraction) * 100);

  // use it like an array -- in this case set them all to 22/7
  for (i=0; i<99; i++) {
    fracts[i].numerator = 22;
    fracts[i].denominator = 7;
  }

  // Deallocate the whole array
  free(fracts);
}

/*
 * Given a C string, return a heap allocated copy of the string.
 * Allocate a block in the heap of the appropriate size,
 * copies the string into the block, and returns a pointer to the block.
 * The caller takes over ownership of the block and is responsible
 * for freeing it.
 * */
char* StringCopy(const char* string) {
  char* newString;
  int len;

  len = strlen(string) + 1; // +1 to account for the \0
  new String = malloc(sizeof(char)*len); //elem-size * number-of-elements
  assert(newString != NULL); // simplistic error check (a good habit)
  strcpy(newString, string); // copy the passed in string to the block

  return (newString); // return a ptr to the block
}
