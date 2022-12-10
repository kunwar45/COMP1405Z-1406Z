import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.*;

public class Fruits1OutgoingLinksTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits1-OutgoingLinks-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits1-OutgoingLinks-passed.txt"));
        List<String> expectedResult;
        List<String> yourResult;
//Test #1 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-539.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-400.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-83.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-539.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #1 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-539.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #1 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-539.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #2 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-944.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-276.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-944.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #2 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-944.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #2 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-944.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #3 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-218.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-118.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-16.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-218.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #3 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-218.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #3 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-218.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #4 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-582.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-821.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-582.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #4 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-582.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #4 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-582.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #5 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-778.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-208.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-778.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #5 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-778.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #5 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-778.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #6 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-596.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-369.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-596.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #6 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-596.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #6 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-596.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #7 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-661.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-10.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #7 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #7 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #8 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-978.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-733.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #8 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #8 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-870.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #9 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-920.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-454.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-11.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-941.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-920.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #9 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-920.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #9 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-920.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #10 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-671.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-645.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-671.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #10 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-671.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #10 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-671.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #11 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-359.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-270.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-359.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #11 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-359.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #11 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-359.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #12 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-207.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-22.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-207.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #12 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-207.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #12 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-207.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #13 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-332.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-300.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-332.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #13 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-332.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #13 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-332.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #14 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-462.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-462.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #14 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-462.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #14 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-462.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #15 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-287.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-10.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-52.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-541.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-287.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #15 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-287.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #15 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-287.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #16 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-136.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-24.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-28.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-136.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #16 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-136.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #16 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-136.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #17 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-291.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-844.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-291.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #17 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-291.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #17 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-291.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #18 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-463.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-188.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-463.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #18 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-463.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #18 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-463.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #19 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-357.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-394.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-385.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-202.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-245.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-357.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #19 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-357.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #19 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-357.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #20 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-40.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #20 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #20 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #21 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-438.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-154.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-438.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #21 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-438.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #21 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-438.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #22 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-446.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-866.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-223.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-601.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-636.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-446.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #22 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-446.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #22 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-446.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #23 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-902.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-62.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-902.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #23 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-902.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #23 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-902.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #24 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-337.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-21.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-337.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #24 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-337.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #24 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-337.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #25 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-31.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-97.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-49.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-31.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #25 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-31.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #25 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-31.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #26 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-64.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-62.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-959.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-119.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-149.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-210.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-74.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-64.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #26 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-64.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #26 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-64.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #27 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-294.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-909.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-21.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-294.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #27 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-294.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #27 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-294.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #28 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-607.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-607.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #28 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-607.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #28 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-607.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #29 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-731.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-623.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-731.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #29 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-731.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #29 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-731.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #30 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-129.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-694.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-5.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-129.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #30 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-129.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #30 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-129.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #31 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-279.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-279.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #31 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-279.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #31 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-279.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #32 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-931.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-943.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-564.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-931.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #32 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-931.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #32 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-931.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #33 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-387.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-183.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-10.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-513.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-423.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #33 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #33 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #34 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-115.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-518.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-645.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-863.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-43.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-115.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #34 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-115.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #34 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-115.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #35 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-97.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-99.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-31.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-745.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-97.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #35 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-97.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #35 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-97.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #36 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-90.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-424.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-874.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-256.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-516.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-90.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #36 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-90.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #36 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-90.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #37 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-600.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-276.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-683.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-600.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #37 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-600.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #37 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-600.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #38 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-130.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #38 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #38 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #39 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-559.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-382.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-637.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-559.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #39 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-559.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #39 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-559.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #40 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-762.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-89.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-749.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-53.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-78.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #40 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #40 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #41 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-442.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-53.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-442.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #41 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-442.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #41 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-442.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #42 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-418.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-109.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-418.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #42 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-418.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #42 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-418.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #43 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-751.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-284.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-328.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-700.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-435.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #43 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #43 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #44 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-424.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #44 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #44 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #45 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-810.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-810.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #45 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-810.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #45 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-810.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #46 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-956.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-821.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-465.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-956.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #46 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-956.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #46 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-956.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #47 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-939.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-47.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-451.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-939.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #47 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-939.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #47 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-939.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #48 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-754.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-95.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-270.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-754.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #48 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-754.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #48 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-754.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #49 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-521.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-74.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-521.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #49 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-521.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #49 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-521.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #50 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-440.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-469.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-378.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-348.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-858.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-440.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #50 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-440.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #50 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-440.html");
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
