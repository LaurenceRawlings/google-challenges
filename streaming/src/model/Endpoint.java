package model;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Endpoint implements Comparable<Endpoint> {
    private int dcLatency;
    private Map<Cache, Integer> caches;
    private ArrayList<Request> requests;

    public int getDcLatency() {
        return dcLatency;
    }

    public Endpoint(int dcLatency) {
        this.dcLatency = dcLatency;
        caches = new HashMap<>();
        requests = new ArrayList<>();
    }

    public void addCache(Cache cache, int latency) {
        caches.put(cache, latency);
    }

    public int getCacheLatency(Cache cache) {
        return caches.get(cache);
    }

    @Override
    public int compareTo(Endpoint o) {
        return Integer.compare(caches.size(), o.caches.size());
    }
}
