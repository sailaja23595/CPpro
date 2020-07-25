// # Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
// # and returns the nth Additive Prime, which is a prime number such that 
// # the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
// # is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

import java.util.*;
class nthtenlyprime {
	public boolean Tenly(int n){
		int s = 0;
		while(n!=0){
			s = s + n % 10;
			n = n / 10;
		}
		if(s == 10){
			return true;
		}
		else{
			return false;
		}
	}
	public boolean Prime(int n){
		int count = 0;
		for(int i = 1; i<=n ; i++){
			if (n % i == 0){
				count = count + 1;
			}
		}
		return count == 2;
	}
	public int fun_nthtenlyprime(int n){
		List<Integer> arli = new ArrayList<Integer>();
		for(int i = 0; i<3000; i++){
			if(Prime(i) && Tenly(i)){
				arli.add(i);
			}
		}
		return arli.get(n);

	}
	public static void main(String[] args) {
		
	}
}