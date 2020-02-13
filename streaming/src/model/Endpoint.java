package model;

import java.util.HashMap;
import java.util.Map;

public class Endpoint {
    private int dcLatency;
    private Map<Cache, Integer> caches;

    public int getDcLatency() {
        return dcLatency;
    }

    public Endpoint(int dcLatency) {
        this.dcLatency = dcLatency;
        caches = new HashMap<>();
    }

    public void addCache(Cache cache, int latency) {
        caches.put(cache, latency);
    }

    public int getCacheLatency(Cache cache) {
        return caches.get(cache);
    }
}
