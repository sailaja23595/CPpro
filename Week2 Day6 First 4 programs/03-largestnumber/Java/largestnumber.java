// # largestNumber: Write the function largestNumber(text) that takes a string of text and 
// # returns the largest int value that occurs within that text, or 0 if no such value occurs. 
// # You may assume that the only numbers in the text are non-negative integers and 
// # that numbers are always composed of consecutive digits (without commas, for example). For example:
// #     	largestNumber("I saw 3 dogs, 17 cats, and 14 cows!")
// # returns 17 (the int value 17, not the string "17"). And
// #     	largestNumber("One person ate two hot dogs!")
// # returns None (the value None, not the string "None").


class largestnumber {
	public int fun_largestnumber(String s){
		int n = 0, result = 0;
		for (int i = 0;i<s.length();i++){
			if(Character.isDigit(s.charAt(i))){
				n = n * 10 + (s.charAt(i) - '0');
			}
			else{
				result = Math.max(result,n);
				n = 0;
			}

		}

		return Math.max(result,n);	
	}
	public static void main(String[] args) {
		
	}
}
	