package core;

import model.Video;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class DataHandler {
    static ArrayList<Video> allVideos = new ArrayList<Video>();

    public static void readData() {
<<<<<<< HEAD

=======
        try {
            BufferedReader reader = new BufferedReader(new FileReader("./src/me_at_the_zoo.in"));

            reader.readLine();
            String secondLine = reader.readLine();
            String[] videoSizesStr = secondLine.split(" ");

            for (int i = 0; i < videoSizesStr.length; i ++) {
                allVideos.add(new Video(Integer.parseInt(videoSizesStr[i])));
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
>>>>>>> 4cf33adaf07b36a28204626d27c51c138ec41ceb
    }
}
