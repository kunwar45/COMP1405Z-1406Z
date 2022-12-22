import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.*;

public class Fruits2IncomingLinksTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits2-IncomingLinks-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits2-IncomingLinks-passed.txt"));
        List<String> expectedResult;
        List<String> yourResult;
//Test #52 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-160.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-160.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #52 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-160.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #52 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-160.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #53 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-525.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-32.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-525.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #53 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-525.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #53 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-525.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #54 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-313.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-634.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-84.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-943.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-580.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-313.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #54 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-313.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #54 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-313.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #55 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-861.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-848.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-861.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #55 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-861.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #55 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-861.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #56 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-77.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-98.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-919.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-409.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-366.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-77.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #56 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-77.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #56 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-77.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #57 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-989.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-104.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-520.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-989.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #57 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-989.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #57 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-989.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #58 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-185.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-98.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-93.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-730.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-483.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #58 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #58 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #59 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-695.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-512.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-984.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-695.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #59 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-695.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #59 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-695.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #60 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-172.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-232.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-876.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-664.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-927.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-600.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-143.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-84.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-172.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #60 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-172.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #60 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-172.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #61 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-994.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-637.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-994.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #61 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-994.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #61 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-994.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #62 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-82.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-120.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-228.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-230.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-113.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-684.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-388.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #62 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #62 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #63 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-225.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-325.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-298.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-84.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #63 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #63 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #64 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-438.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-128.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-165.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-463.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-438.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #64 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-438.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #64 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-438.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #65 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-999.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-941.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-999.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #65 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-999.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #65 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-999.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #66 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-813.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-624.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-813.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #66 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-813.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #66 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-813.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #67 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-455.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-407.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-122.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-258.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-618.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-780.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-455.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #67 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-455.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #67 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-455.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #68 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-296.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-53.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-341.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-296.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #68 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-296.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #68 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-296.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #69 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-270.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-885.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-485.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-53.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-837.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-270.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #69 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-270.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #69 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-270.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #70 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-983.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-983.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #70 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-983.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #70 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-983.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #71 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-889.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-889.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #71 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-889.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #71 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-889.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #72 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-426.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-84.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-827.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-426.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #72 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-426.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #72 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-426.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #73 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-265.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-685.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-265.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #73 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-265.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #73 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-265.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #74 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-304.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-513.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-492.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-304.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #74 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-304.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #74 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-304.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #75 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-159.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-360.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-48.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-159.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #75 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-159.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #75 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-159.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #76 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-149.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-115.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-149.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #76 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-149.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #76 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-149.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #77 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-187.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-253.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-107.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-305.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-41.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-690.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-761.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-918.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-187.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #77 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-187.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #77 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-187.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #78 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-407.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-88.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-455.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-407.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #78 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-407.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #78 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-407.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #79 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-800.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-490.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-800.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #79 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-800.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #79 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-800.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #80 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-330.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-21.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-675.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-597.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-330.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #80 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-330.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #80 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-330.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #81 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-858.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-147.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-858.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #81 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-858.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #81 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-858.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #82 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-228.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-228.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #82 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-228.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #82 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-228.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #83 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-816.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-624.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-816.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #83 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-816.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #83 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-816.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #84 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-643.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-243.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-643.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #84 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-643.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #84 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-643.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #85 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-658.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-658.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #85 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-658.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #85 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-658.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #86 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-92.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-743.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-770.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-92.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #86 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-92.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #86 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-92.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #87 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-631.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-763.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-573.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-631.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #87 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-631.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #87 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-631.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #88 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-121.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-62.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-121.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #88 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-121.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #88 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-121.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #89 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-35.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-83.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-80.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-628.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-920.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-855.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-35.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #89 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-35.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #89 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-35.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #90 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-838.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-298.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-838.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #90 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-838.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #90 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-838.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #91 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-851.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-293.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-263.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-851.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #91 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-851.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #91 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-851.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #92 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-672.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-109.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-672.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #92 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-672.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #92 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-672.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #93 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-225.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-225.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #93 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-225.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #93 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-225.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #94 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-290.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-114.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-290.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #94 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-290.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #94 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-290.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #95 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-716.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-539.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-716.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #95 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-716.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #95 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-716.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #96 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-921.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-456.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-921.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #96 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-921.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #96 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-921.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #97 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-871.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-526.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-871.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #97 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-871.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #97 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-871.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #98 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-47.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-117.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-528.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-632.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-336.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-106.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-80.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-714.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-47.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #98 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-47.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #98 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-47.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #99 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-644.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-644.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #99 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-644.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #99 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-644.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #100 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-242.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-242.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #100 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-242.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #100 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-242.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #101 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-568.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-156.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-543.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-364.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-568.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #101 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-568.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #101 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-568.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #102 checking incoming links for http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = new ArrayList<String>();
        yourResult = tester.getIncomingLinks("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
        if (yourResult == null) {
            passOut.println("Passed Test #102 checking incoming links for http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + null);
            passOut.println("result = null\n\n");
        } else {
            failOut.println("Failed Test #102 checking incoming links for http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + null);
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

        failOut.close();
        passOut.close();
    }
}
