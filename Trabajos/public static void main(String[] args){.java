import java.util.Scanner;
public class cho{

public static void main(String[] args){
    Scanner scan= new Scanner(System.in);
    String s= scan.next();
    int q= 0;

    for (char c:s.toCharArray()){
        switch (q) {
            case 0: q=(c=='c')? 1: 0; break;
            case 1: q=(c=='h')? 2: ((c=='c')? 1: 0); break;
            case 2: q=(c=='o')? 3: ((c=='c')? 1: 0); break;
            case 3: q=(c=='c')? 1: 0;
        }
        if(q==3){
            System.out.println("Aceptar");
        }else {
            System.out.println("Rechazar");
        }
    }
    }
}