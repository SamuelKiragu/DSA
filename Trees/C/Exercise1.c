#include <stddef.h>
#include <stdio.h>

struct node {
  int data;
  struct node* left;
  struct node* right;
};

/*
 * Helper function that allocates a new node
 * with the given data and Null left and right
 * */
struct node* NewNode(int data) {
 struct node* node = new(sizeof(struct node));
 node->data = data;
 node->left = NULL;
 node->right = NULL;

 return (node);
}

/*
 * Give a binary search tree and a number, inserts a new node
 * with the given numer in the correct place in the tree.
 * then use (the standard trick to avoid using reference parameters).
 * */
struct node* insert(struct node* node, int data) {
  // 1. If the tree is empty, return a new, single node
  if (node == NULL) {
    return (newNode(data));
  }
  else {
    // 2. Otherwise, recur down the tree
    if (data <= node->data) node->left = insert(node->left, data);
    else node->right = insert(node->right,data);

    return (node); // return the (unchanged) node pointer 
  }
}

// call newNode() three times
struct node* build123a() {
  struct node* root = NULL;
  root = insert(root, 2);
  root = insert(root, 1);
  root = insert(root, 3);
  return(root);
}

int size(struct node* node) {
  if(node == NULL) {
    return 0;
  } else {
    return (size(node->left) + 1 + size(node->right));
  }
}

int maxDepth(struct node* node) {
  if(node == NULL) {
   return 0;
  } else {
    int lDepth = maxDepth(node->left);
    int rDepth = maxDepth(node->right);

    // use the larger one
    if (lDepth > rDepth) return (lDepth + 1);
    else return (rDepth + 1); 
  }
}

int minValue(struct node* node) {
  if (node->left == NULL) return node->data;
  else return minValue(node->left);
}

void printTree(struct node* node) {
  if (node == NULL) return;

  printTree(node->left);
  printf("%d", node->data);
  printTree(node->right);
}

void printPostorder(struct node* node) {
  if (node == NULL) return;

  // first recur on both subtrees
  printPostorder(node->left);
  printPostorder(node->right);

  // then deal with the node
  printf("%d", node->data);
}

int hasPathSum(struct node* node, int sum) {
  if(node == NULL) {
    return 0;
  } else {
    // otherwise check both subtrees
    int subSum = sum - node-> data;
    return(hasPathSum(node->left, subSum) || 
	   hasPathSum(node->right, subSum));
  }
}
