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
