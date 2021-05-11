import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Main {

    public static void main(String[] args) {

        readPizza("test.txt");
    }

    public static void readPizza(String filePath){
        try {
            FileReader fileReader = new FileReader(filePath);
            BufferedReader bufferedReader = new BufferedReader(fileReader);

            String[] pizzaParameters = bufferedReader.readLine().split(" ");
            String[][] pizzaArray = new String[Integer.parseInt(pizzaParameters[0])][Integer.parseInt(pizzaParameters[1])];

            for (int i = 0; i < Integer.parseInt(pizzaParameters[0]); i++){
                String[] currentRow = bufferedReader.readLine().split("");

                for (int j = 0; j < Integer.parseInt(pizzaParameters[1]); j++){
                    pizzaArray[i][j] = currentRow[j];
                }
            }

            Pizza pizza = new Pizza(Integer.parseInt(pizzaParameters[0]),Integer.parseInt(pizzaParameters[1]),
                    Integer.parseInt(pizzaParameters[2]),Integer.parseInt(pizzaParameters[3]));

            bufferedReader.close();
        }
        catch(FileNotFoundException ex) {
            System.out.println("Unable to open file '" + filePath + "'");
        }
        catch(IOException ex) {
            System.out.println("Error reading file '" + filePath + "'");
        }
    }
}
