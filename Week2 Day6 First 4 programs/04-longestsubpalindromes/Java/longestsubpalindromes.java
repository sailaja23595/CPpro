// # Write the function longestSubpalindrome(s), that takes a string s and returns 
// the longest palindrome that occurs as consecutive characters (not just letters, but 
// 	any characters) in s. So:
// #    	longestSubpalindrome("ab-4-be!!!") 
// # returns "b-4-b". If there is a tie, return the lexicographically larger value -- 
// in java, a string s1 is lexicographically greater than a string s2 if (s1 > s2). So:
// #    	longestSubpalindrome("abcbce") 
// # returns "cbc", since ("cbc" > "bcb"). Note that unlike the previous functions, 
// this function is case-sensitive (so "A" is not treated the same as "a" here). Also, 
// from the explanation above, we see that longestSubpalindrome("aba") is "aba", 
// and longestSubpalindrome("a") is "a".

class longestsubpalindromes {
	public boolean palindrome(String s){
		String str = "";
		for(int i = s.length()-1; i>=0; i--){
			str = str + s.charAt(i);
		}
		return str.equals(s);
	}
	public String fun_longestsubpalindromes(String s){
		String spalin = "";
		for(int i = 0; i < s.length(); i++){
			String t = "";
			for(int j = i; j < s.length(); j++){
				t = t + s.charAt(j);
				if(palindrome(t)){
					if(t.length() > spalin.length() || (t.length() == spalin.length() && t.compareTo(spalin) > 0)){
						spalin = t;
					}
				}
			}
		}
		return spalin;
		// if(s.isEmpty()){
		// 	return "";
		// }
		// int n = s.length();
		// int l = 0, begin = 0; 
		// int end = 0;
		// boolean[][] palin = new boolean[n][n];
		// for (int j = 0;j < n; j++){
		// 	palin[j][j] = true;
		// 	for(int i = 0;i < j;i++){
		// 		if(s.charAt(i) == s.charAt(j) && (j-i <= 2 || palin[i+1][j-1])){
		// 			palin[i][j] = true;
		// 			if(j-i+1 > l){
		// 				l = j - i + 1;
		// 				begin = i;
		// 				end = j;
		// 			}
		// 		}
		// 	}
		// }
		// return s.substring(begin,end + 1);
		

	}
	public static void main(String[] args) {
		
	}
}
