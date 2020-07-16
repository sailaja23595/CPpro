// # Write the function vowelCount(s), that takes a string s, 
// # and returns the number of vowels in s, ignoring case, 
// # so "A" and "a" are both vowels. The vowels are "a", "e", "i", "o", and "u". 
// # So, for example, ("Abc def!!! a? yzyzyz!") returns 3 (two a's and one e).

class vowelscount {
	public int fun_vowelscount(String s){
		int c =0;
		String st = s.toLowerCase();
		for(int i = 0;i< st.length(); i++){
			char var = st.charAt(i);
			if(var == 'a' || var == 'e' || var == 'i' || var == 'o' || var == 'u'){
				c += 1;
			}
		
		}
		return c;
	}

	public static void main(String[] args) {
		
	}
	
}