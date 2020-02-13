package model;

import java.util.ArrayList;

public class DataCenter {
    private ArrayList<Video> videos;
    private ArrayList<Endpoint> endpoints;

    public DataCenter() {
        videos = new ArrayList<>();
        endpoints = new ArrayList<>();
    }

    public void addVideo(Video video) {
        videos.add(video);
    }

    public void addEndpoint(Endpoint endpoint) {
        endpoints.add(endpoint);
    }
}
