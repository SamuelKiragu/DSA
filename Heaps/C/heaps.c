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
