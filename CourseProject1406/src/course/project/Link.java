package course.project;

import java.util.ArrayList;
import java.util.HashMap;

public class Link {
    private String url;
    // private ArrayList<Link> outgoingLinks = new ArrayList<Link>();
    private ArrayList<Link> outgoingLinks = null;
    private ArrayList<Link> incomingLinks = new ArrayList<Link>();
    private HashMap<String, Integer> countAll = new HashMap<String, Integer>();
    private String title = "";
    private double pageRank;

    Link(String url) {
        this.url = url;
    }

    @Override
    public String toString() {
        return "Link{" +
                "url='" + url + '\'' +
                ", title='" + title + '\'' +
                ", pageRank=" + pageRank +
                '}';
    }

    public ArrayList<Link> getIncomingLinks() {
        return incomingLinks;
    }

    public ArrayList<Link> getOutgoingLinks() {
        return outgoingLinks;
    }

    public double getPageRank() {
        return pageRank;
    }

    public HashMap<String, Integer> getCountAll() {
        return countAll;
    }

    public String getTitle() {
        return title;
    }

    public String getUrl() {
        return url;
    }

    public void setCountAll(HashMap<String, Integer> countAll) {
        this.countAll = countAll;
    }

    public void setIncomingLinks(ArrayList<Link> incomingLinks) {
        this.incomingLinks = incomingLinks;
    }

    public void setOutgoingLinks(ArrayList<Link> outgoingLinks) {
        this.outgoingLinks = outgoingLinks;
    }

    public void setPageRank(double pageRank) {
        this.pageRank = pageRank;
    }

    public void setTitle(String title) {
        this.title = title;
    }
}
