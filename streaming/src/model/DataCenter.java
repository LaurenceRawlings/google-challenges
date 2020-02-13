package model;

import java.util.ArrayList;

public class DataCenter {
    private ArrayList<Video> videos;
    private ArrayList<Endpoint> endpoints;
    private ArrayList<Cache> caches;

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

    public void addCache(Cache cache) {
        caches.add(cache);
    }

    public ArrayList<Video> getVideos() {
        return videos;
    }

    public ArrayList<Endpoint> getEndpoints() {
        return endpoints;
    }

    public ArrayList<Cache> getCaches() {
        return caches;
    }
}
