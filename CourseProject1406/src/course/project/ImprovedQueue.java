package course.project;

import course.project.Link;

import java.util.ArrayList;
import java.util.HashMap;

public class ImprovedQueue {
    ArrayList<Link> queueList = new ArrayList<Link>();
    HashMap<String, Link> queueDict = new HashMap<String, Link>();
    //

    ImprovedQueue(Link initialLink) {
        this.addend(initialLink);
    }

    public void addend(Link l) {
        queueList.add(l);
        queueDict.put(l.getUrl(), l);
    }

    public Link removestart() {
        Link l = queueList.remove(0);
        queueDict.remove(l.getUrl());
        return l;
    }

    public boolean contains(Link l) {
        return queueDict.containsKey(l.getUrl());
    }

    public int size() {
        return queueList.size();
    }

    @Override
    public String toString() {
        return "ImprovedQueue{" +
                "queueList=" + queueList +
                '}';
    }
}
