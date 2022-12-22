import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.*;

public class Fruits4IncomingLinksTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits4-IncomingLinks-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits4-IncomingLinks-passed.txt"));
        List<String> expectedResult;
        List<String> yourResult;
//Test #52 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-936.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-61.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-936.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #52 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-936.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #52 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-936.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #53 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-113.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-315.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-561.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-813.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-568.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #53 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #53 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #54 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-357.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-677.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-833.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-73.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-152.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-357.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #54 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-357.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #54 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-357.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #55 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-270.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-270.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #55 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-270.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #55 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-270.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #56 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-542.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-342.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-542.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #56 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-542.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #56 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-542.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #57 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-447.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-253.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-820.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-447.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #57 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-447.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #57 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-447.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #58 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-234.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-707.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-11.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-234.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #58 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-234.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #58 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-234.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #59 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-116.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-326.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-886.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-116.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #59 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-116.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #59 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-116.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #60 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-445.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #60 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #60 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #61 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-972.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-433.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-972.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #61 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-972.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #61 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-972.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #62 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-440.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-218.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-586.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-440.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #62 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-440.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #62 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-440.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #63 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-370.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-853.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-360.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-412.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-370.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #63 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-370.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #63 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-370.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #64 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-730.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-389.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-775.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-730.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #64 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-730.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #64 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-730.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #65 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-105.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-631.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-913.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-932.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-141.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-911.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-105.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #65 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-105.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #65 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-105.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #66 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-74.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-74.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #66 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-74.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #66 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-74.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #67 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-351.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-51.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-351.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #67 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-351.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #67 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-351.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #68 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-16.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-293.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-56.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-369.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-124.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-28.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-58.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-298.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-16.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #68 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-16.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #68 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-16.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #69 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-252.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-726.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-930.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-175.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-173.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-478.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #69 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #69 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #70 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-652.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-218.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-477.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-239.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-899.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-674.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-709.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-447.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-608.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-219.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-509.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-145.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-446.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-502.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-427.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-649.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-627.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-402.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-861.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-495.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-768.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-524.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-556.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-867.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-317.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-158.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-441.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-351.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-303.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-757.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-527.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-195.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-45.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-531.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-541.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-585.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-77.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-242.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #70 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #70 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #71 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-838.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-290.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-838.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #71 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-838.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #71 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-838.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #72 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-572.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-966.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-572.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #72 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-572.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #72 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-572.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #73 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-302.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-728.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-124.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #73 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #73 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #74 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-722.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-379.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-129.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-256.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-195.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-216.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-722.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #74 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-722.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #74 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-722.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #75 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-555.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-95.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-555.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #75 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-555.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #75 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-555.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #76 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-203.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-80.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-403.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-171.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-233.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-625.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-203.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #76 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-203.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #76 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-203.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #77 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-67.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-67.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #77 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-67.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #77 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-67.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #78 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-37.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-823.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-765.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-57.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-265.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-252.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-37.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #78 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-37.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #78 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-37.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #79 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-806.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-64.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-806.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #79 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-806.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #79 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-806.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #80 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-688.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #80 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #80 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #81 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-943.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-788.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-943.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #81 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-943.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #81 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-943.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #82 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-855.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-244.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-855.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #82 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-855.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #82 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-855.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #83 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-573.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-229.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-573.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #83 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-573.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #83 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-573.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #84 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-606.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-452.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-733.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-826.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-606.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #84 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-606.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #84 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-606.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #85 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-42.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-472.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-42.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #85 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-42.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #85 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-42.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #86 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-969.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-190.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-120.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-969.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #86 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-969.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #86 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-969.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #87 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-568.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-568.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #87 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-568.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #87 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-568.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #88 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-579.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-389.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-579.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #88 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-579.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #88 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-579.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #89 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-413.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-95.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-413.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #89 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-413.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #89 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-413.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #90 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-805.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-243.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-205.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-805.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #90 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-805.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #90 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-805.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #91 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-970.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-101.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-436.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-970.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #91 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-970.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #91 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-970.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #92 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-728.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-380.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-728.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #92 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-728.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #92 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-728.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #93 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-531.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-276.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-531.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #93 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-531.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #93 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-531.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #94 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-909.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-909.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #94 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-909.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #94 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-909.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #95 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-566.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-86.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-566.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #95 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-566.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #95 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-566.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #96 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-538.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-538.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #96 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-538.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #96 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-538.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #97 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-925.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-765.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-925.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #97 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-925.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #97 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-925.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #98 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-419.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-419.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #98 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-419.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #98 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-419.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #99 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-851.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-41.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-851.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #99 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-851.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #99 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-851.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #100 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-160.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-118.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-944.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-170.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-102.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-232.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-243.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-160.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #100 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-160.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #100 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-160.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #101 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-356.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-394.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-396.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-50.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-632.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-111.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-188.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-438.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-356.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #101 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-356.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #101 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-356.html");
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
