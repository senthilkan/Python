"""
Linked List implemention using class
each node is refering to class object and each object's next_node pointing other class

"""

class node:
	def __init__(self, data=None, next_node=None):
		self.data=data
		self.next_node= next_node
	
	def get_data(self):
		return self.data
	def get_next(self):
		return self.next_node
	
	def set_next(self,node):
		self.next_node=node


class link_list():
	def __init__(self,head=None):
		self.head=None
	def insert(self,data):
		n=node(data)
		n.set_next(self.head)
		self.head=n
		#print(n.get_data())
		
	def size(self):
		curr=self.head
		c=0
		while curr:
			c+=1
			curr=curr.get_next()
		return c
	def search(self,data):
		
		curr=self.head
		c=0
		while curr:
			
			if curr.get_data()==data:
				 	
				
				return curr,c
			
			curr=curr.get_next()
			c+=1
		return None
	def insert_after(self,pos,data):
		
		curr,c=self.search(pos)	
		n=node(data)
		n.set_next(curr.get_next())
		curr.set_next(n)	
		return None
	
	def reverse(self):
		curr=self.head
		
		p_node=None
		n_node=None
		while curr:
			c= curr.get_next()
			curr.set_next(p_node)
			p_node=curr
			curr = c
			
		self.head=p_node
		
			
		return True	
	def display(self):
		curr=self.head
		c=0
		while curr:
			print(curr.get_data())
			curr=curr.get_next()
if __name__=="__main__":			
    ll=link_list()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.insert(40)

    ll.insert_after(30,60)
    print(ll.size())
    ll.display()
    print(ll.search(60))
    ll.reverse()
    ll.display()

