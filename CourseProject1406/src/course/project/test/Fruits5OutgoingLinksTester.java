import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.*;

public class Fruits5OutgoingLinksTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits5-OutgoingLinks-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits5-OutgoingLinks-passed.txt"));
        List<String> expectedResult;
        List<String> yourResult;
//Test #1 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-810.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-211.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-810.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #1 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-810.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #1 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-810.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #2 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-531.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #2 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #2 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #3 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-19.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-913.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-396.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-40.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-162.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-484.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #3 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #3 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #4 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-650.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-650.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #4 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-650.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #4 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-650.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #5 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-106.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #5 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #5 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #6 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-284.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-734.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-980.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-66.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-818.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-284.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #6 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-284.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #6 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-284.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #7 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-746.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-895.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-531.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-746.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #7 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-746.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #7 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-746.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #8 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-517.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-186.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-517.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #8 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-517.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #8 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-517.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #9 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-346.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-69.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-494.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-346.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #9 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-346.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #9 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-346.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #10 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-700.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #10 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #10 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #11 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-825.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-825.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #11 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-825.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #11 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-825.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #12 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-181.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-65.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #12 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #12 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #13 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-560.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-18.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-560.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #13 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-560.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #13 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-560.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #14 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-297.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-905.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-183.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-112.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-896.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-297.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #14 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-297.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #14 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-297.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #15 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-770.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-62.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-770.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #15 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-770.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #15 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-770.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #16 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-506.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-238.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-506.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #16 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-506.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #16 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-506.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #17 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-778.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-626.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-778.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #17 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-778.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #17 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-778.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #18 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-732.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-657.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-732.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #18 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-732.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #18 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-732.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #19 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-69.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #19 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #19 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #20 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #20 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #20 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #21 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-991.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-556.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-991.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #21 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-991.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #21 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-991.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #22 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-859.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-694.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-889.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-493.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-859.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #22 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-859.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #22 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-859.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #23 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-25.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-653.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #23 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #23 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #24 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-580.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-250.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-580.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #24 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-580.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #24 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-580.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #25 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-170.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-857.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #25 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #25 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #26 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-326.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-22.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-326.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #26 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-326.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #26 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-326.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #27 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-849.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-115.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-198.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-849.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #27 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-849.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #27 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-849.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #28 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-532.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-705.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-369.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-532.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #28 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-532.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #28 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-532.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #29 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-464.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-984.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-464.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #29 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-464.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #29 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-464.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #30 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-152.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-873.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-235.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-51.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-523.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-187.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-147.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-152.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #30 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-152.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #30 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-152.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #31 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-918.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-284.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-630.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #31 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #31 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #32 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-67.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-184.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-67.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #32 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-67.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #32 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-67.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #33 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-521.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-521.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #33 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-521.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #33 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-521.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #34 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-380.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-380.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #34 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-380.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #34 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-380.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #35 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-84.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-84.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #35 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-84.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #35 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-84.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #36 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-438.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-265.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-438.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #36 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-438.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #36 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-438.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #37 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-889.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-236.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-859.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-889.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #37 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-889.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #37 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-889.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #38 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-471.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-471.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #38 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-471.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #38 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-471.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #39 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-949.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-50.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-949.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #39 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-949.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #39 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-949.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #40 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #40 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #40 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #41 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-829.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-383.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-191.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-829.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #41 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-829.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #41 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-829.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #42 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-217.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-101.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-562.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-712.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-572.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-522.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-942.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-168.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-903.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-583.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #42 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #42 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #43 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-235.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #43 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #43 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #44 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-899.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-46.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-975.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-899.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #44 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-899.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #44 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-899.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #45 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-417.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-790.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-509.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-383.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-417.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #45 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-417.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #45 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-417.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #46 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-887.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-122.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-790.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-887.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #46 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-887.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #46 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-887.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #47 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-513.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-513.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #47 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-513.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #47 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-513.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #48 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-451.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-451.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #48 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-451.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #48 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-451.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #49 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-41.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #49 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #49 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #50 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-976.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-187.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-983.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-773.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-735.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-976.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #50 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-976.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #50 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-976.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #51 checking outgoing links for http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = new ArrayList<String>();
        yourResult = tester.getOutgoingLinks("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
        if (yourResult == null) {
            passOut.println("Passed Test #51 checking outgoing links for http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + null);
            passOut.println("result = null\n\n");
        } else {
            failOut.println("Failed Test #51 checking outgoing links for http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + null);
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

        failOut.close();
        passOut.close();
    }
}
