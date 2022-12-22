import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.*;

public class Fruits1IncomingLinksTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits1-IncomingLinks-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits1-IncomingLinks-passed.txt"));
        List<String> expectedResult;
        List<String> yourResult;
//Test #52 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-483.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-467.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-67.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-752.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-340.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-483.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #52 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-483.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #52 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-483.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #53 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-746.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-562.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-746.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #53 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-746.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #53 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-746.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #54 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-557.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-38.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-96.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-557.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #54 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-557.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #54 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-557.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #55 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-43.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-155.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-115.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-10.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-490.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-693.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-598.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-498.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-120.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-833.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-43.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #55 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-43.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #55 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-43.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #56 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-985.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-503.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-985.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #56 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-985.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #56 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-985.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #57 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-626.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-331.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-605.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-717.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-626.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #57 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-626.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #57 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-626.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #58 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-365.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-661.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-445.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-734.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-767.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-103.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-782.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #58 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #58 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #59 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-225.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-17.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-116.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-225.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #59 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-225.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #59 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-225.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #60 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-301.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-187.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-27.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-814.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-301.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #60 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-301.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #60 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-301.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #61 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-118.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-218.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-828.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-930.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-819.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-263.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-118.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #61 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-118.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #61 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-118.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #62 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-245.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-183.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-357.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-171.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-25.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-245.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #62 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-245.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #62 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-245.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #63 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-914.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-914.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #63 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-914.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #63 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-914.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #64 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-309.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-309.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #64 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-309.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #64 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-309.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #65 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-619.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-445.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-619.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #65 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-619.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #65 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-619.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #66 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-848.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-51.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-848.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #66 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-848.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #66 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-848.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #67 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-487.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-970.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-487.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #67 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-487.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #67 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-487.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #68 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-417.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-164.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-417.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #68 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-417.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #68 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-417.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #69 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-46.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-988.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-878.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-386.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-114.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-156.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-669.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-56.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-404.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-46.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #69 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-46.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #69 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-46.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #70 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-360.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-360.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #70 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-360.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #70 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-360.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #71 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-603.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-91.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-980.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-774.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-581.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-74.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-603.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #71 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-603.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #71 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-603.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #72 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-587.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-474.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-326.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-587.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #72 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-587.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #72 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-587.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #73 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-899.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-918.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-899.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #73 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-899.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #73 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-899.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #74 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-211.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-5.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-209.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-250.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-355.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-47.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-324.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-453.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-758.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-846.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-211.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #74 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-211.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #74 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-211.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #75 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-501.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-93.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-501.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #75 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-501.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #75 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-501.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #76 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-144.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-493.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-144.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #76 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-144.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #76 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-144.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #77 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-326.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-839.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-672.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-374.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-587.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-436.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-326.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #77 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-326.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #77 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-326.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #78 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-451.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-939.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-451.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #78 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-451.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #78 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-451.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #79 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-496.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-861.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-786.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-47.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-511.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-496.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #79 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-496.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #79 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-496.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #80 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-263.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-118.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-102.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-263.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #80 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-263.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #80 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-263.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #81 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-438.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-19.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-865.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-465.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #81 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #81 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #82 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-525.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-95.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-525.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #82 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-525.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #82 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-525.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #83 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-51.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-848.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-51.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #83 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-51.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #83 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-51.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #84 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-220.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-687.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-836.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-220.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #84 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-220.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #84 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-220.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #85 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-593.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-159.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-593.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #85 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-593.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #85 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-593.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #86 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-352.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-352.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #86 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-352.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #86 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-352.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #87 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-347.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-24.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-322.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-118.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-687.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-318.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-180.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-21.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-146.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-14.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-282.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-173.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-171.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-441.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-243.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-201.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-58.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-274.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-152.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-476.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #87 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #87 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #88 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-31.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-97.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-49.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-31.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #88 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-31.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #88 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-31.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #89 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-505.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-21.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-646.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-505.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #89 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-505.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #89 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-505.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #90 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-944.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-276.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-944.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #90 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-944.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #90 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-944.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #91 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-526.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-864.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-526.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #91 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-526.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #91 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-526.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #92 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-976.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-209.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-551.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-976.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #92 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-976.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #92 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-976.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #93 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-930.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-118.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-930.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #93 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-930.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #93 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-930.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #94 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-602.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-602.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #94 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-602.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #94 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-602.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #95 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-908.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-71.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-908.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #95 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-908.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #95 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-908.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #96 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-975.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-938.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-975.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #96 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-975.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #96 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-975.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #97 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-818.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-713.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-818.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #97 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-818.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #97 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-818.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #98 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-537.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-100.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-537.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #98 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-537.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #98 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-537.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #99 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-274.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-364.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-41.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-274.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #99 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-274.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #99 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-274.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #100 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-963.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-258.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-62.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-963.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #100 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-963.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #100 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-963.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #101 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-601.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-142.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-241.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits/N-446.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits/N-601.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #101 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-601.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #101 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits/N-601.html");
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
