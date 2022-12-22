import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.*;

public class Fruits4OutgoingLinksTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits4-OutgoingLinks-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits4-OutgoingLinks-passed.txt"));
        List<String> expectedResult;
        List<String> yourResult;
//Test #1 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-263.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-263.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #1 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-263.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #1 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-263.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #2 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-412.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-591.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-73.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #2 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #2 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #3 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-941.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-223.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-941.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #3 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-941.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #3 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-941.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #4 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-485.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-154.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-485.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #4 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-485.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #4 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-485.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #5 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-76.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-718.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-719.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-318.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-155.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-69.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-436.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-76.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #5 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-76.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #5 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-76.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #6 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-953.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-369.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-953.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #6 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-953.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #6 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-953.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #7 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-200.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-200.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #7 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-200.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #7 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-200.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #8 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-714.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-625.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-143.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-699.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-714.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #8 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-714.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #8 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-714.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #9 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-10.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-177.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-576.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-75.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-173.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-10.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #9 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-10.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #9 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-10.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #10 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-23.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-906.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-997.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-705.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-23.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #10 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-23.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #10 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-23.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #11 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-212.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-813.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-940.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-953.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-182.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-970.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-420.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-206.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-37.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-33.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-221.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-120.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-52.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-393.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-410.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-957.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-956.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-271.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-148.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-413.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-22.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-388.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-134.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-282.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #11 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #11 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #12 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-470.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-64.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-470.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #12 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-470.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #12 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-470.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #13 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-382.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-565.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-140.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-485.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #13 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #13 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #14 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-424.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-894.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-865.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-394.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-802.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-396.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-424.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #14 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-424.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #14 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-424.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #15 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-414.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-323.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-448.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-216.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-414.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #15 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-414.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #15 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-414.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #16 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-244.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-259.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-291.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-216.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-855.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-655.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-244.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #16 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-244.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #16 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-244.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #17 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-660.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-412.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-660.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #17 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-660.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #17 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-660.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #18 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-886.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-116.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-886.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #18 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-886.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #18 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-886.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #19 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #19 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #19 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #20 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-430.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-411.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-488.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-343.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-430.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #20 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-430.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #20 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-430.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #21 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-856.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-856.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #21 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-856.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #21 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-856.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #22 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-506.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-253.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-213.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-506.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #22 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-506.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #22 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-506.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #23 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-910.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-219.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-910.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #23 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-910.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #23 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-910.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #24 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-517.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-517.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #24 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-517.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #24 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-517.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #25 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-454.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-64.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-454.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #25 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-454.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #25 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-454.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #26 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-560.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-253.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-560.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #26 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-560.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #26 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-560.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #27 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-945.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-810.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-326.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-945.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #27 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-945.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #27 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-945.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #28 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-536.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-366.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-536.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #28 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-536.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #28 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-536.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #29 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-864.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-171.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-864.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #29 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-864.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #29 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-864.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #30 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-217.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-86.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-217.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #30 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-217.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #30 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-217.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #31 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-60.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-86.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-858.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-844.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-682.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-61.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-376.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-87.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-60.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #31 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-60.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #31 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-60.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #32 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-181.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-154.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-181.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #32 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-181.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #32 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-181.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #33 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-436.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-752.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-76.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-970.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-684.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-142.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-148.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-436.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #33 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-436.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #33 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-436.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #34 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-380.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-253.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-728.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-380.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #34 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-380.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #34 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-380.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #35 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-830.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-669.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-741.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-830.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #35 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-830.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #35 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-830.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #36 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-524.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-345.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-366.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-524.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #36 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-524.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #36 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-524.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #37 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-943.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-788.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-943.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #37 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-943.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #37 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-943.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #38 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-213.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-904.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-630.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-989.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-506.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-401.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-389.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-45.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-586.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-213.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #38 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-213.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #38 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-213.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #39 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-228.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-195.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-510.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-228.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #39 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-228.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #39 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-228.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #40 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-393.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-393.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #40 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-393.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #40 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-393.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #41 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-238.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-146.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-952.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-283.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-666.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-902.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-238.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #41 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-238.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #41 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-238.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #42 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-594.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-594.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #42 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-594.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #42 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-594.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #43 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-247.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-152.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-337.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-247.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #43 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-247.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #43 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-247.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #44 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-558.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-100.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-558.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #44 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-558.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #44 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-558.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #45 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-459.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-49.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-162.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-261.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-459.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #45 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-459.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #45 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-459.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #46 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-74.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-74.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #46 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-74.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #46 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-74.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #47 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-532.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-131.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-532.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #47 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-532.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #47 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-532.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #48 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-880.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-880.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #48 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-880.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #48 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-880.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #49 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-927.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-103.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-219.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-927.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #49 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-927.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #49 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-927.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #50 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-610.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-206.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-610.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #50 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-610.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #50 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-610.html");
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
