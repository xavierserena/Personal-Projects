import java.io.*;
import java.util.LinkedList;

public class Reader {
    String line = null;
    FileReader fileReader;
    BufferedReader bufferedReader;
    public LinkedList<String> lines;

    Reader(String fileName) {
        try {
            // FileReader reads text files in the default encoding.
            fileReader = new FileReader(fileName);

            // Always wrap FileReader in BufferedReader.
            bufferedReader = new BufferedReader(fileReader);

            lines = new LinkedList<>();

            while((line = bufferedReader.readLine()) != null) {
                lines.add(line);
            }

            // Always close files.
            bufferedReader.close();
        }
        catch(FileNotFoundException ex) {
            System.out.println( "Unable to open file '" + fileName + "'");
        }
        catch(IOException ex) {
            System.out.println("Error reading file '" + fileName + "'");
        }
    }
}
