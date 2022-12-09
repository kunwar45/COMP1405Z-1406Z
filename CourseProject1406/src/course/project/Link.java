package course.project;

import java.util.ArrayList;
import java.util.HashMap;

public class Link implements Comparable<Link> {
    private String url;
    // private ArrayList<Link> outgoingLinks = new ArrayList<Link>();
    private ArrayList<Link> outgoingLinks;
    private ArrayList<Link> incomingLinks;
    private HashMap<String, Integer> countAll;
    private String title;
    private double pageRank;
    private int wordCount;
    private double cosineSim;

    Link(String url) {
        this.setUrl(url);
        outgoingLinks = null;
        incomingLinks = new ArrayList<Link>();
        countAll = new HashMap<String, Integer>();
        title = "";
        wordCount = 0;
        cosineSim = 0;
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

    public int getWordCount() {
        return wordCount;
    }

    public double getCosineSim() {
        return cosineSim;
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

    public void setWordCount(int wordCount) { this.wordCount = wordCount; }

    public void setCosineSim(double cosineSim) {
        this.cosineSim = cosineSim;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    @Override
    public int compareTo(Link l) {
        if (this.getCosineSim() == l.getCosineSim()){
            return this.getUrl().compareTo(l.getUrl());
        }else if (this.getCosineSim() > l.getCosineSim()){
            return 1;
        }else{
            return -1;
        }
    }
}
