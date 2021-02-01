package core;

import model.*;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class DataHandler {
    static ArrayList<Video> allVideos = new ArrayList<Video>();
    static int requestDesc;
    static DataCenter dataCenter;

    public static DataCenter readData() {
        try {
            Scanner reader = new Scanner("./src/me_at_the_zoo.in");

            String[] firstLine = reader.nextLine().split(" ");
            requestDesc = Integer.parseInt(firstLine[2]);
            int cacheCount = Integer.parseInt(firstLine[3]);
            int cacheSize = Integer.parseInt(firstLine[4]);

            for (int i = 0; i <cacheCount; i ++) {
                dataCenter.addCache(new Cache(cacheSize));
            }

            String secondLine = reader.nextLine();
            String[] videoSizesStr = secondLine.split(" ");

            for (int i = 0; i < videoSizesStr.length; i++) {
                dataCenter.addVideo(new Video(Integer.parseInt(videoSizesStr[i])));
            }

            while (reader.hasNext()) {
                String[] currentLine = reader.nextLine().split(" ");
                if (currentLine.length < 3) {
                    int dcLatency = Integer.parseInt(currentLine[0]);
                    int epCount = Integer.parseInt(currentLine[1]);

                    Endpoint temporaryEP = new Endpoint(dcLatency);

                    for (int i = 0; i < epCount; i ++) {
                        String[] latencyToCache = reader.nextLine().split(" ");
                        temporaryEP.addCache(dataCenter.getCaches().get(Integer.parseInt(latencyToCache[0])), Integer.parseInt(latencyToCache[1]));
                    }

                    dataCenter.addEndpoint(temporaryEP);

                } else {
                    String[] requestsLine = reader.nextLine().split(" ");
                    int videoNumber = Integer.parseInt(requestsLine[0]);
                    Video video = dataCenter.getVideos().get(videoNumber);
                    int epPos = Integer.parseInt(requestsLine[1]);
                    int amount = Integer.parseInt(requestsLine[2]);
                    Endpoint requestingEP = dataCenter.getEndpoints().get(epPos);

                    dataCenter.getEndpoints().get(epPos).addRequest(new Request(video, requestingEP, amount));
                }

            }

        } catch (Exception e) {
            e.printStackTrace();
        }
        return dataCenter;
    }

    public static void writeData() {
        int totalCaches = 0;
        String outputString = "";

        for (int i = 0; i < dataCenter.getCaches().size(); i ++) {
            if (!(dataCenter.getCaches().get(i).getVideos().size() == 0)) {
                totalCaches ++;
                outputString = outputString + '\n' + i;


                for (int j = 0; j < dataCenter.getCaches().get(i).getVideos().size(); j ++) {
                    //outputString = outputString + " " + dataCenter.
                }
            }
        }
    }
}
