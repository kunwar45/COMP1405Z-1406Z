import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.*;

public class Fruits3IncomingLinksTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits3-IncomingLinks-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits3-IncomingLinks-passed.txt"));
        List<String> expectedResult;
        List<String> yourResult;
//Test #52 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-277.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-627.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-650.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-664.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-30.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-277.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #52 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-277.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #52 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-277.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #53 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-764.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-764.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #53 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-764.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #53 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-764.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #54 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-842.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-896.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-338.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-137.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-842.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #54 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-842.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #54 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-842.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #55 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-954.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-12.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-954.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #55 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-954.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #55 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-954.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #56 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-816.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-78.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-909.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-816.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #56 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-816.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #56 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-816.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #57 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-544.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-118.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-579.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-544.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #57 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-544.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #57 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-544.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #58 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-330.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-829.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-330.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #58 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-330.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #58 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-330.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #59 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-858.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-611.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-691.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-858.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #59 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-858.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #59 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-858.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #60 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-299.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #60 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #60 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #61 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-858.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #61 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #61 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #62 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-919.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-613.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-918.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-919.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #62 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-919.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #62 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-919.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #63 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-221.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-299.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-221.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #63 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-221.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #63 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-221.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #64 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-306.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-51.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-68.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-646.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-306.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #64 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-306.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #64 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-306.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #65 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-633.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-256.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-633.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #65 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-633.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #65 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-633.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #66 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-516.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-516.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #66 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-516.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #66 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-516.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #67 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-242.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-206.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-242.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #67 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-242.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #67 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-242.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #68 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-389.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-389.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #68 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-389.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #68 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-389.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #69 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-399.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-46.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #69 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #69 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #70 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-362.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-76.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-534.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-362.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #70 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-362.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #70 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-362.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #71 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-894.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-319.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-60.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-894.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #71 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-894.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #71 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-894.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #72 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-936.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-478.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-936.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #72 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-936.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #72 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-936.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #73 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-945.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-71.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-945.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #73 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-945.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #73 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-945.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #74 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-785.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-288.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-410.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-785.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #74 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-785.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #74 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-785.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #75 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-253.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-253.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #75 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-253.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #75 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-253.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #76 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-319.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-179.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-894.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-43.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-346.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-319.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #76 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-319.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #76 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-319.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #77 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-262.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #77 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #77 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #78 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-56.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-13.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-135.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-56.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #78 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-56.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #78 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-56.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #79 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-718.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-127.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-718.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #79 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-718.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #79 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-718.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #80 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-534.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-43.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-362.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-534.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #80 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-534.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #80 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-534.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #81 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-715.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-470.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-715.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #81 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-715.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #81 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-715.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #82 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-101.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-101.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #82 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-101.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #82 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-101.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #83 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-642.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-642.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #83 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-642.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #83 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-642.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #84 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-334.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-334.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #84 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-334.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #84 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-334.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #85 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-43.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-250.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-606.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-620.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-850.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-319.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-990.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-534.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-43.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #85 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-43.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #85 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-43.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #86 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-338.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-842.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-814.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-874.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-271.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-338.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #86 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-338.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #86 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-338.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #87 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-740.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-372.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-740.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #87 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-740.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #87 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-740.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #88 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-517.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-207.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-220.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-360.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-517.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #88 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-517.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #88 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-517.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #89 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-873.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-736.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-786.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-593.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-101.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #89 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #89 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #90 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-229.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-229.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #90 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-229.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #90 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-229.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #91 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-834.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-834.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #91 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-834.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #91 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-834.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #92 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-117.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-117.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #92 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-117.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #92 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-117.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #93 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-118.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-582.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-917.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-60.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-378.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-768.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-544.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-288.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-679.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-118.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #93 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-118.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #93 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-118.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #94 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-411.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-411.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #94 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-411.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #94 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-411.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #95 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #95 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #95 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #96 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-790.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-32.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-790.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #96 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-790.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #96 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-790.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #97 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-18.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-629.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-15.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-40.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-608.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-18.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #97 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-18.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #97 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-18.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #98 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-206.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-931.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-660.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-242.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-607.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-206.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #98 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-206.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #98 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-206.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #99 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-272.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-272.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #99 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-272.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #99 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-272.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #100 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-771.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #100 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #100 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #101 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-168.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-880.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-835.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-725.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-998.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-44.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-168.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #101 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-168.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #101 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-168.html");
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
