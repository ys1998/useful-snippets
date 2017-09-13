#include "bst.h"
#include <iostream>
using namespace std;

template<class T>
BST<T>::BST(){
	root=NULL;
}
template<class T>
BST<T>::~BST(){
	if(root!=NULL){
		delete root;
	}
}
template<class T>
void BST<T>::printInorder(BST<T>::Node *ptr){
	if(ptr==NULL){
		return;
	}else{
		printInorder(ptr->left);
		cout<<ptr->data<<" ";
		printInorder(ptr->right);
		return;
	}
}
template<class T>
void BST<T>::printPreorder(BST<T>::Node * ptr){
	if(ptr==NULL){
		return;
	}else{
		cout<<ptr->data<<" ";
		printPreorder(ptr->left);
		printPreorder(ptr->right);
		return;
	}
}
template<class T>
void BST<T>::printPostorder(BST<T>::Node * ptr){
	if(ptr==NULL){
		return;
	}else{
		printPostorder(ptr->left);
		printPostorder(ptr->right);
		cout<<ptr->data<<" ";
		return;
	}
}
template<class T>
void BST<T>::Inorder(){
	printInorder(this->root);
}
template<class T>
void BST<T>::Preorder(){
	printPreorder(this->root);
}
template<class T>
void BST<T>::Postorder(){
	printPostorder(this->root);
}
template<class T>
bool BST<T>::Search(T x){
	bool found=false;
	Node *ptr=this->root;
	while(ptr!=NULL){
		if(ptr->data==x){
			found=true;
			break;
		}else if(ptr->data<x){
			ptr=ptr->right;
		}else{
			ptr=ptr->left;
		}
	}
	return found;
}
template<class T>
void BST<T>::Insert(T x){
	Node * X=new Node();
	X->data=x;
	X->left=NULL;
	X->right=NULL;
	if(this->root==NULL){
		this->root=X;
	}else{
		Node * ptr=this->root;
		Node * parent=NULL;
		while(ptr!=NULL){
			if(ptr->data>x){
				parent=ptr;
				ptr=ptr->left;
			}else if(ptr->data<x){
				parent=ptr;
				ptr=ptr->right;
			}else{
				delete X;
				break;
			}
		}
		if(ptr==NULL){
			if(parent->data>x){
				parent->left=X;
			}else{
				parent->right=X;
			}
		}
	}
	return;

}
template<class T>
void BST<T>::Delete(T x){
	if(this->root==NULL){
		return;
	}
	Node *ptr=this->root,*parent=NULL;
	bool present=true;
	while(ptr->data!=x){
		if(ptr->data>x){
			parent=ptr; ptr=ptr->left;
		}else if(ptr->data<x){
			parent=ptr; ptr=ptr->right;
		}
		if(ptr==NULL){
			present=false;
			break;
		}
	}
	if(present){
		if(parent==NULL){
			if(ptr->left==NULL && ptr->right==NULL){
				this->root=NULL;
				delete ptr;
			}else if(ptr->left==NULL){
				this->root=ptr->right;
				delete ptr;
			}else if(ptr->right==NULL){
				this->root=ptr->left;
				delete ptr;
			}else{
				Node * join=ptr->left;
				while(join->right!=NULL){
					join=join->right;
				}
				join->right=ptr->right;
				this->root=ptr->left;
				delete ptr;
			}
		}else{
			if(ptr->left==NULL && ptr->right==NULL){
				if(parent->data>x){
					parent->left=NULL;
					delete ptr;
				}else{
					parent->right=NULL;
					delete ptr;
				}
			}else if(ptr->left==NULL){
				if(parent->data>x){
					parent->left=ptr->right;
					delete ptr;
				}else{
					parent->right=ptr->right;
					delete ptr;
				}
			}else if(ptr->right==NULL){
				if(parent->data>x){
					parent->left=ptr->left;
					delete ptr;
				}else{
					parent->right=ptr->left;
					delete ptr;
				}
			}else{
				Node * join=ptr->left;
				while(join->right!=NULL){
					join=join->right;
				}
				join->right=ptr->right;
				if(parent->data>x){
					parent->left=ptr->left;
					delete ptr;
				}else{
					parent->right=ptr->left;
					delete ptr;
				}
			}
		}
	}else{
		return;
	}
}
template<class T>
T BST<T>::findLCA(Node *ptr,T a, T b){
	// a < b always
	if(ptr->data==b){
		return b;
	}else if(ptr->data==a){
		return a;
	}else if(ptr->data>b){
		return findLCA(ptr->left,a,b);
	}else if(ptr->data<a){
		return findLCA(ptr->right,a,b);
	}else{
		return ptr->data;
	}
}

template<class T>
T BST<T>::LCA(T x, T y){
	if(!this->Search(x)||!this->Search(y)){
		return -1;
	}else{
		if(x==y){
			return x;
		}else if(x<y){
			return findLCA(this->root,x,y);
		}else{
			return findLCA(this->root,y,x);
		}
	}
}

template<class T>
int BST<T>::find_minTurns(Node *lca,T a, T x){
	int turns=0;
	bool d; // 0 is left and 1 is right
	Node *ptr=lca;
	d=!(a>x);
	while(ptr->data!=x){
		if(ptr->data>x){
			if(d){
				ptr=ptr->left; d=!d; turns++;
			}else{
				ptr=ptr->left;
			}
		}else if(ptr->data<x){
			if(!d){
				ptr=ptr->right; d=!d; turns++;
			}else{
				ptr=ptr->right;
			}
		}
	}
	return turns;
}

template<class T>
int BST<T>::minTurns(T x, T y){
	T a=this->LCA(x,y);
	if(a==-1) return -1;
	else{
		Node *ptr=this->root;
		while(ptr->data!=a){
			if(ptr->data<a){
				ptr=ptr->right;
			}else{
				ptr=ptr->left;
			}
		}
		if(a==x){
			return find_minTurns(ptr,x,y);
		}else if(a==y){
			return find_minTurns(ptr,y,x);
		}else{
			return find_minTurns(ptr,a,x)+find_minTurns(ptr,a,y)+1;
		}
	}
}
