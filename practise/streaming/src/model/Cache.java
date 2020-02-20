package model;

import java.util.ArrayList;

public class Cache implements Comparable<Cache> {
    private ArrayList<Video> videos;
    private int maxCapacity;
    private int capacity;

    public Cache(int maxCapacity) {
        videos = new ArrayList<>();
        this.maxCapacity = maxCapacity;
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

    @Override
    public int compareTo(Cache o) {
        return 0;
    }
}
