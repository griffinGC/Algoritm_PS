package algorithm;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class boj_1991_Tree {
	public static void main(String[] args) throws Exception {
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
		char a =' ', b = ' ', c = ' ';
		int n = Integer.parseInt(br.readLine());
		Tree tr = new Tree();
		
		for(int i = 0 ; i < n; i++) {
			String line = br.readLine();
			a = line.charAt(0);
			b = line.charAt(2);
			c = line.charAt(4);
			tr.add(a, b, c);
		}	
		tr.preOrderTra(tr.root);
		System.out.println();
		tr.inOrderTra(tr.root);
		System.out.println();
		tr.postOrderTra(tr.root);
	}
}
class treeNode {
	treeNode left;
	treeNode right;
	char item;
	public treeNode(char data) {
		this.item = data;
	}
}

class Tree{
	treeNode root;
	public Tree() {
		
	}
	
	//노드를 추가!
	public void add(char data, char left, char right) {
		//루트노드가 아예 비어 있을 경우! 
        if(root == null) {
        	if(data != '.') {
				root = new treeNode(data);
			}
			if(left != '.') {
				root.left = new treeNode(left);
			}
			if(right != '.') {
				root.right = new treeNode(right);
			}	
		}else {
			//새로운것을 어디다 넣을지 찾아야함 
			search(root, data, left, right);
		}

	}
	
	//새로운 것을 어디다 넣을지 찾아야함 
	public void search(treeNode item, char data, char left, char right) {
		if(item == null) {
			return;
		}else if(item.item == data) {//처음에는 안만나도 재귀를 계속 반복하다 보면은 만나게 됨. 
			if(left !='.') {
				item.left = new treeNode(left);//왼쪽에 추가 
			}
			if(right !='.') {
				item.right = new treeNode(right);//오른쪽에 추가 
			}
		}else {
			search(item.left, data, left, right);//왼쪽으로 재귀로 계속 들어감 
			search(item.right, data, left, right);//오른쪽으로 재귀로 계속 들어감 
		}
	}
	
	public void preOrderTra(treeNode data) {
		System.out.print(data.item);
		//비어있을때는 작동하면 안되기 때문에 넣어줌 아래도 다 마찬가지!
		if(data.left != null) preOrderTra(data.left);
		if(data.right != null) preOrderTra(data.right);
	}
	public void inOrderTra(treeNode data) {
		if(data.left != null) inOrderTra(data.left);
		System.out.print(data.item);
		if(data.right != null) inOrderTra(data.right);
	}
	public void postOrderTra(treeNode data) {
		if(data.left != null) postOrderTra(data.left);
		if(data.right != null) postOrderTra(data.right);
		System.out.print(data.item);
	}
	
}
