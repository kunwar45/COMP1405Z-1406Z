package course.project;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class Link implements Comparable<Link>, SearchResult{
    private String url;
    // private ArrayList<Link> outgoingLinks = new ArrayList<Link>();
    private ArrayList<Link> outgoingLinks;
    private ArrayList<Link> incomingLinks;
    private HashMap<String, Integer> countAll;
    private String title;
    private double pageRank;
    private int wordCount;
    private double score;

    Link(String url) {
        this.setUrl(url);
        outgoingLinks = null;
        incomingLinks = new ArrayList<Link>();
        countAll = new HashMap<String, Integer>();
        title = "";
        wordCount = 0;
        score = 0;
    }

    @Override
    public String toString() {
        return "Link{" +
                "url='" + url + '\'' +
                ", title='" + title + '\'' +
                ", pageRank=" + pageRank +
                '}';
    }

    public String getRelativeLink() {
        return this.url.substring(0, this.url.lastIndexOf('/'));
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

    public double getScore() {
        return score;
    }

    public void setCountAll(HashMap<String, Integer> countAll) {
        this.countAll = countAll;
    }

    public void addCountAll(String s, Integer i) {
        this.countAll.putIfAbsent(s, i);
        this.countAll.replace(s, i);
    }

    public Integer getSpecificCountAll ( String s){
        if (this.countAll.containsKey(s)){
            return this.countAll.get(s);
        }

        return 0;
    }
    public void setIncomingLinks(ArrayList<Link> incomingLinks) {
        this.incomingLinks = incomingLinks;
    }

    public void addIncomingLink(Link newLink){
        if (!Arrays.asList(this.incomingLinks).contains(newLink)){
            this.incomingLinks.add(newLink);
        }
    }

    public void addOutgoingLink(Link newLink){
        this.outgoingLinks.add(newLink);
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

    public void setScore(double score) {
        this.score = score;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    @Override
    public int compareTo(Link l) {
        if (this.url.equals(l.getUrl())){
            return 0;
        }
        if (this.getScore() == l.getScore()){
            return this.getUrl().compareTo(l.getUrl());
        }else if (this.getScore() > l.getScore()){
            return 1;
        }else{
            return -1;
        }
    }
}
