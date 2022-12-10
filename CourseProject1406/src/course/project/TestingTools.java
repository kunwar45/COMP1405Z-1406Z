package course.project;

import java.io.*;
import java.util.*;

public class TestingTools {
    public static boolean checkListsEqual(List a, List b){
        if(a == null || b == null){
            return a == b;
        }

        if(a.size() != b.size()){
            return false;
        }

        Set aSet = new HashSet(a);
        Set bSet = new HashSet(b);

        if(a.size() != b.size()){
            return false;
        }

        for(Object first: aSet){
            if(!bSet.contains(first)){
                return false;
            }
        }
        return true;
    }

    public static boolean compareDoubles(double a, double b){
        return Math.abs(a-b) < 0.001;
    }

    //course.project.TestingTools.checkSearch(yourResult, phrase, true, passOut, failOut)
    public static void checkSearch(List<SearchResult> result, String phrase, boolean boost, PrintWriter passOut, PrintWriter failOut, String className, String curTestName) throws IOException {
        List<TestingToolsResult> expectedResults = new ArrayList<TestingToolsResult>();
        List<TestingToolsResult> realResults = new ArrayList<TestingToolsResult>();

        for (SearchResult r : result) {
            realResults.add(new TestingToolsResult(r.getTitle(), r.getScore()));
        }

        BufferedReader in = new BufferedReader(new FileReader(className + "-expected-search-results.txt"));
        String line = in.readLine();

        while (line != null) {
            boolean correctPhrase = false;
            if (line.strip().equals(phrase)) {
                correctPhrase = true;
            }
            boolean correctBoost = (Boolean.parseBoolean(in.readLine()) == boost);
            boolean processResult = correctBoost && correctPhrase;

            int size = Integer.parseInt(in.readLine());
            for (int i = 0; i < size; i++) {
                String title = in.readLine().strip();
                double score = Double.parseDouble(in.readLine());

                if (processResult) {
                    expectedResults.add(new TestingToolsResult(title, score));
                }
            }

            if (processResult) {
                break;
            }
            line = in.readLine();
        }
        in.close();


        boolean passedTest = true;
        if(expectedResults.size() != realResults.size()){
            passedTest = false;
        }

        for(int i = 0; i < expectedResults.size(); i++){
            if(!expectedResults.get(i).getTitle().equals(realResults.get(i).getTitle())){
                passedTest = false;
            }
            if(Math.abs(expectedResults.get(i).getScore() - realResults.get(i).getScore()) > 0.001){
                passedTest = false;
            }
        }


        if (passedTest){
            passOut.println("Passed " + curTestName);
            passOut.println("Expected Result:");
            for(int i = 0; i < expectedResults.size(); i++){
                passOut.println((i+1) + ". " + expectedResults.get(i).getTitle() + " = " + expectedResults.get(i).getScore());
            }
            passOut.println("Your Result:");
            for(int i = 0; i < expectedResults.size(); i++){
                passOut.println((i+1) + ". " + realResults.get(i).getTitle() + " = " + realResults.get(i).getScore());
            }
            passOut.println();
            passOut.println();
        }else{
            failOut.println("Failed " + curTestName);
            failOut.println("Expected Result:");
            for(int i = 0; i < expectedResults.size(); i++){
                failOut.println((i+1) + ". " + expectedResults.get(i).getTitle() + " = " + expectedResults.get(i).getScore());
            }
            failOut.println("Your Result:");
            for(int i = 0; i < expectedResults.size(); i++){
                failOut.println((i+1) + ". " + realResults.get(i).getTitle() + " = " + realResults.get(i).getScore());
            }
            failOut.println();
            failOut.println();
        }
    }

    private static class TestingToolsResult implements Comparable<TestingToolsResult>{
        private String title;
        private double score;
        public TestingToolsResult(String iTitle, double iScore){
            title = iTitle;
            score = iScore;
        }

        public String getTitle() {
            return title;
        }

        public double getScore() {
            return score;
        }

        public int compareTo(TestingToolsResult o) {
            if(Math.abs(this.getScore() - o.getScore()) > 0.001){
                if(this.getScore() > o.getScore()){
                    return -1;
                }else{
                    return 1;
                }
            }

            return this.getTitle().compareTo(o.getTitle());
        }
    }
}
