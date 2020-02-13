package model;

import java.util.ArrayList;

public class Cache {
    private ArrayList<Video> videos;
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
}
