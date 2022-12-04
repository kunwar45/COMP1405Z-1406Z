package course.project;

import java.util.ArrayList;
import java.util.HashMap;

public class ImprovedQueue {
    ArrayList<Link> queueList = new ArrayList<Link>();
    HashMap<Link, Integer> queueDict = new HashMap<Link, Integer>();

    ImprovedQueue(Link initialLink) {
        this.addend(initialLink);
    }

    public void addend(Link l) {
        queueList.add(l);
        queueDict.put(l, 1);
    }

    public Link removestart() {
        Link l = queueList.remove(0);
        queueDict.remove(l);
        return l;
    }

    public boolean contains(Link l) {
        return queueDict.containsKey(l);
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
