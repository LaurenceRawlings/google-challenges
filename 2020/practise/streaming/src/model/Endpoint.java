package model;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Endpoint implements Comparable<Endpoint> {
    private int dcLatency;
    private Map<Cache, Integer> caches;
    private ArrayList<Request> requests;

    public ArrayList<Request> getRequests() {
        return requests;
    }

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

    public void addRequest(Request request) {
        requests.add(request);
    }

    public int getCacheAmount() {
        return caches.size();
    }

    @Override
    public int compareTo(Endpoint o) {
        return Integer.compare(getCacheAmount(), o.getCacheAmount());
    }
}
