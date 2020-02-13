package model;

import java.util.ArrayList;

public class Cache {
    private ArrayList<Video> videos;
    private int maxCapacity;
    private int capacity;

    public Cache(ArrayList<Video> videos, int capacity) {
        this.videos = videos;
        this.capacity = capacity;
    }

    public ArrayList<Video> getVideos() {
        return videos;
    }

    public int getCapacity() {
        return capacity;
    }

    public int getMaxCapacity() {
        return maxCapacity;
    }

    public boolean addVideo(Video video) {
        if (capacity + video.getSize() > maxCapacity) {
            return false;
        } else {
            videos.add(video);
            return true;
        }
    }
}
