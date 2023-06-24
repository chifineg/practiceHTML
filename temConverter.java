import java.util.*;
/**
 *
 * @author Chidinma
 */
public class temConverter {

    public static void main(String[] args) {
        // scanner object to get input from user
        Scanner sc = new Scanner(System.in);
		
		//formular: F = 9/5 * C + 32
		System.out.println("What temperature are you converting from? F or C?");
		char user_option = sc.next().charAt(0);
		
		if (user_option == 'F'){
			System.out.println("Enter temperature in ^F: ");
			double user_inputF = sc.nextInt();
			double C = (user_inputF - 32)/ 1.8;
			System.out.println("Temperature in ^C = " + C);
		}
		else if (user_option == 'C'){
			System.out.println("Enter temperature in ^C: ");
			double user_inputC = sc.nextInt();
			double F = 1.8 * user_inputC + 32 ;
			System.out.println("Temperature in ^F = " + F);
		}
                else {
                    System.out.println("Invalid selection");
                }
		
		
		
		}
}
