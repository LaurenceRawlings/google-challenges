package core;

import model.DataCenter;
import model.Endpoint;
import model.Request;

import java.util.ArrayList;
import java.util.Collections;

public class DataCenterHandler {
    public static void optimizeCaches(DataCenter dc) {
        ArrayList<Endpoint> endpoints = dc.getEndpoints();
        Collections.sort(endpoints);

        for (Endpoint endpoint : endpoints) {
            if (endpoint.getCacheAmount() > 0) {
                ArrayList<Request> requests = endpoint.getRequests();
                Collections.sort(requests);
                Collections.reverse(requests);

                for (Request request : requests) {

                }
            }
        }
    }
}
