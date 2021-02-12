import csv
import sys
import pandas        

k=[]
listA=[]
listB=[]
listC=[]
listD=[]
listfA=[]
listfB=[]
listfC=[]
listfD=[]
flag=0

# data structure that represents a node in the tree
class Node():
    def __init__(self, id,gen,age_,annual_income,score,dist):
        self.key = id # holds the key
        self.gender = gen
        self.age = age_
        self.income = annual_income
        self.spendscore = score
        self.distance = dist
        self.parent = None #pointer to the parent
        self.left = None # pointer to left child
        self.right = None #pointer to right child
        self.color = 1 # 1 . Red, 0 . Black
     
def heap_values_scoreage(m,cent):
    list=[]
    for i in range(4):
        ltemp=[]
        ltemp.append(abs(m-cent[i][0]))
        ltemp.append(cent[i][1])
        list.append(ltemp)
    heapify(list)
    return list

def heap_values_gen(k):
    list=[]
    if k=='Male':
        list.append('M')
    else:
        list.append('F')
    return list

# class RedBlackTree implements the operations in Red Black Tree
class RedBlackTree():
   
    def __init__(self):
        self.TNULL = Node(0,None,0,0,0,None)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
    #def__copy__(self,)

    def __pre_order_helper_score(self, node,k):
        if node != self.TNULL:
            self.distance=heap_values_scoreage(node.spendscore,[[k[0],'A'],[k[1],'B'],[k[2],'C'],[k[3],'D']])
            self.__pre_order_helper_score(node.left,k)
            self.__pre_order_helper_score(node.right,k)
   
    def __pre_order_helper_age(self, node,k):
        if node != self.TNULL:
            self.distance=heap_values_scoreage(node.age,[[k[0],'A'],[k[1],'B'],[k[2],'C'],[k[3],'D']])
            print(self.distance)
            self.__pre_order_helper_age(node.left,k)
            self.__pre_order_helper_age(node.right,k)
           
    def __in_order_score(self, node):
        if node != self.TNULL:
            self.__in_order_score(node.left)
            if node.distance[0][1]=='A':
                listA.append(node.spendscore)
            if node.distance[0][1]=='B':
                listB.append(node.spendscore)
            if node.distance[0][1]=='C':
                listC.append(node.spendscore)
            if node.distance[0][1]=='D':
                listD.append(node.spendscore)
            self.__in_order_score(node.right)
           
    def __in_order_age(self, node):
        if node != self.TNULL:
            self.__in_order_age(node.left)
            if node.distance[0][1]=='A':
                listA.append(node.age)
            if node.distance[0][1]=='B':
                listB.append(node.age)
            if node.distance[0][1]=='C':
                listC.append(node.age)
            if node.distance[0][1]=='D':
                listD.append(node.age)
            self.__in_order_age(node.right)

    # fix the red-black tree
    def __fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left # uncle
                if u.color == 1:
                    # case 3.1
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        # case 3.2.2
                        k = k.parent
                        self.right_rotate(k)
                    # case 3.2.1
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right # uncle

                if u.color == 1:
                    # mirror case 3.1
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        # mirror case 3.2.2
                        k = k.parent
                        self.left_rotate(k)
                    # mirror case 3.2.1
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def __print_helper(self, node, indent, last):
        # print the tree structure on the screen
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.spendscore) + "(" + s_color + ")" + "(" + str(node.key) + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)
       

    # rotate left at node x
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # rotate right at node x
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # insert the key to the tree in its appropriate position
    # and fix the tree
    def insert(self, id,gen,age_,annual_income,score,dist):
        # Ordinary Binary Search Insertion
        node = Node(id,gen,age_,annual_income,score,dist)
        node.parent = None
        node.key = id # holds the key
        node.gender = gen
        node.age = age_
        node.income = annual_income
        node.spendscore = score
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1 # new node must be red

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.spendscore < x.spendscore:
                x = x.left
            else:
                x = x.right
        # y is parent of x
        node.parent = y
        if y == None:
            self.root = node
        elif node.spendscore <= y.spendscore:
            y.left = node
        else:
            y.right = node
        # if new node is a root node, simply return
        if node.parent == None:
            node.color = 0
            return
        # if the grandparent is None, simply return
        if node.parent.parent == None:
            return
        # Fix the tree
        self.__fix_insert(node)

    def get_root(self):
        return self.root

    # print the tree structure on the screen
    def pretty_print(self):
        self.__print_helper(self.root, "", True)
       
    def pretty_traverse(self,opt):
        if opt==1:
            self.__in_order_score(self.root)
        elif opt==2:
            self.__in_order_age(self.root)
           
    def update(self,k,opt):
        if opt==1:
            self.__pre_order_helper_score(self.root,k)
        elif opt==2:
            self.__pre_order_helper_age(self.root,k)
           
    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node
           
    def __fix_delete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    # case 3.1
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right
                if s.left.color == 0 and s.right.color == 0:
                    # case 3.2
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        # case 3.3
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right
                    # case 3.4
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    # case 3.1
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left
                if s.right.color == 0 and s.right.color == 0:
                    # case 3.2
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        # case 3.3
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left
                    # case 3.4
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0
           
    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
           
    def __delete_node_helper(self, node, dataID, dataSS):
        # find the node containing key
        z = self.TNULL
        while node != self.TNULL:
            if node.spendscore == dataSS and node.key == dataID:
                z = node
            if node.spendscore < dataSS:
                node = node.right
            else:
                node = node.left
        if z == self.TNULL:
            print("Couldn't find key in the tree")
            return
        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.__fix_delete(x)
           
    def delete_node(self, dataID, dataSS):
        self.__delete_node_helper(self.root, dataID, dataSS)
       
    def __pre_order_helper(self, node, data, s):
        if node != self.TNULL:
            if(node.key==data):
                s=node.spendscore
                return s
            s=self.__pre_order_helper(node.left,data,s)
            s=self.__pre_order_helper(node.right,data,s)
            return s
        else:
            return s
             
    def find(self,data):
        return self.__pre_order_helper(self.root, data, -1)
   
    def filescore(self, node):
        l=[]
        if node != self.TNULL:
            self.filescore(node.left)
            if(node.distance[0][1]=='A'):
                l=[node.key,node.gender,node.age,node.income,node.spendscore]
                listfA.append(l)
            if(node.distance[0][1]=='B'):
                l=[node.key,node.gender,node.age,node.income,node.spendscore]
                listfB.append(l)
            if(node.distance[0][1]=='C'):
                l=[node.key,node.gender,node.age,node.income,node.spendscore]
                listfC.append(l)
            if(node.distance[0][1]=='D'):
                l=[node.key,node.gender,node.age,node.income,node.spendscore]
                listfD.append(l)
            self.filescore(node.right)
    def filegender(self, node):
        l=[]
        if node != self.TNULL:
            self.filegender(node.left)
            if(node.gender=='Male'):
                l=[node.key,node.gender,node.age,node.income,node.spendscore]
                listfA.append(l)
            if(node.gender=='Female'):
                l=[node.key,node.gender,node.age,node.income,node.spendscore]
                listfB.append(l)
            self.filegender(node.right)

    def create_file(self,opt):
        if opt==1 or opt==2:
            l=["Customer ID","Gender","Age","Income","Spendscore"]
            self.filescore(self.root)
            index = [i[0] for i in listfA]
            not_index_list = [i[1:] for i in listfA]
            pd = pandas.DataFrame(listfA,columns=l)
            pd.to_csv('E:\AmrithaNagarajan\Programs\SpendScoreClassA.csv')
            index = [i[0] for i in listfB]
            not_index_list = [i[1:] for i in listfB]
            pd = pandas.DataFrame(listfB,columns=l)
            pd.to_csv('E:\AmrithaNagarajan\Programs\SpendScoreClassB.csv')
            index = [i[0] for i in listfC]
            not_index_list = [i[1:] for i in listfC]
            pd = pandas.DataFrame(listfC,columns=l)
            pd.to_csv('E:\AmrithaNagarajan\Programs\SpendScoreClassC.csv')
            index = [i[0] for i in listfD]
            not_index_list = [i[1:] for i in listfD]
            pd = pandas.DataFrame(listfD,columns=l)
            pd.to_csv('E:\AmrithaNagarajan\Programs\SpendScoreClassD.csv')
        elif opt==3:
            l=["Customer ID","Gender","Age","Income","Spendscore"]
            self.filegender(self.root)
            index = [i[0] for i in listfA]
            not_index_list = [i[1:] for i in listfA]
            pd = pandas.DataFrame(listfA,columns=l)
            pd.to_csv('E:\AmrithaNagarajan\Programs\GenderM.csv')
            index = [i[0] for i in listfB]
            not_index_list = [i[1:] for i in listfB]
            pd = pandas.DataFrame(listfB,columns=l)
            pd.to_csv('E:\AmrithaNagarajan\Programs\GenderF.csv')
           
           
def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem[0] < parent[0]:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem

def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    childpos = 2*pos + 1    
    while childpos < endpos:
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos][0] < heap[rightpos][0]:
            childpos = rightpos
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)

def heapify(x):
    """Transform list into a heap, in-place, in O(len(x)) time."""
    n = len(x)
    for i in reversed(range(n//2)):
        _siftup(x, i)

def cluster(k):
    flag=0
    avg=sum(listA)
    if k[0]!=avg/len(listA):
        k[0]=avg/len(listA)
        flag=1
    avg=sum(listB)
    if k[1]!=avg/len(listB):
        k[1]=avg/len(listB)
        flag=1
    avg=sum(listC)
    if k[2]!=avg/len(listC):
        k[2]=avg/len(listC)
        flag=1
    avg=sum(listD)
    if k[3]!=avg/len(listD):
        k[3]=avg/len(listD)
        flag=1
    return flag

       
           
if __name__ == "__main__":
    data = RedBlackTree()
    with open('E:\Sangeetha\Programs\Semester_3\ADS\Mall_Customers.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        print("On what basis you wanna segment the cusomers?")
        print("1. Spend Score")
        print("2. Age")
        print("3. Gender")
        print("Your choice?")
        opt=int(input())
        f=-1
        for row in readCSV:
            if f==-1:
                f=1
                continue
            id = int(row[0])
            gen = row[1]
            age_=int(row[2])
            annual_income = row[3]
            score = int(row[4])
            if opt==1:
                k=[12.5,37.5,62.5,87.5]
                dist=heap_values_scoreage(score,[[k[0],'A'],[k[1],'B'],[k[2],'C'],[k[3],'D']])  # 4 clusters 0-25;25-50;50-75;75-100
            elif opt==2:
                k=[15,35,45,65]
                dist=heap_values_scoreage(age_,[[k[0],'A'],[k[1],'B'],[k[2],'C'],[k[3],'D']])  # 4 clusters 1-10;11-20;21-40;41 and above
            elif opt==3:
                dist=heap_values_gen(gen)
            data.insert(id,gen,age_,annual_income,score,dist)
        print("The Red-Black Tree is:")
        data.pretty_print()
        while(opt==1 or opt==2):
            data.pretty_traverse(opt)
            flag=cluster(k)
            if flag==0:
                break
            data.update(k,opt)
        data.pretty_print()
        data.create_file(opt)
        ch=input("Wanna remove a customer from data set?(Y/N)")
        if(ch=='Y' or ch=='y'):
            ID=int(input("Enter the customer ID:"))
            s=data.find(ID)
            data.delete_node(ID,s)
            data.pretty_print()

