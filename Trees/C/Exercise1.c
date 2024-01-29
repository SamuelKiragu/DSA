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

// call newNode() three times
struct node* build123a() {
  struct node* root = newNode(2);
  struct node* lChild = newNode(1);
  struct node* rChild = newNode(3);

  root->left = lChild;
  root->right = rChild;

  return(root);
}
