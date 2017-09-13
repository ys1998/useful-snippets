#include "SkipList.h">
using namespace std;

template<class T>
SkipList<T>::SkipList(){
	max_level=4;
	p=0.0;
	head=NULL;
}
template<class T>
SkipList<T>::SkipList(int l){
	max_level=l;
	head=NULL;
}
template<class T>
SkipList<T>::~SkipList(){
	if(head!=NULL) delete head;	 
}
template<class T>
SkipList<T>::Node(){
	
}