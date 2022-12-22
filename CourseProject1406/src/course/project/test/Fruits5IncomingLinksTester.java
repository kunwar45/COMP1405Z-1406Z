import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.*;

public class Fruits5IncomingLinksTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits5-IncomingLinks-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits5-IncomingLinks-passed.txt"));
        List<String> expectedResult;
        List<String> yourResult;
//Test #52 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-421.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #52 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #52 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #53 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-523.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-101.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-152.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-523.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #53 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-523.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #53 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-523.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #54 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-66.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-299.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #54 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #54 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #55 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-509.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-417.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-440.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-509.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #55 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-509.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #55 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-509.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #56 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-559.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-559.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #56 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-559.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #56 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-559.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #57 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #57 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #57 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #58 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-650.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-650.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #58 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-650.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #58 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-650.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #59 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-650.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #59 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #59 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #60 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-217.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-48.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-117.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-217.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #60 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-217.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #60 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-217.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #61 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-804.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-939.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-525.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-216.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-690.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-864.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-968.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #61 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #61 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #62 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-828.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-46.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-357.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-277.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-109.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-978.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-828.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #62 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-828.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #62 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-828.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #63 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-992.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-16.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-992.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #63 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-992.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #63 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-992.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #64 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-948.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-314.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-948.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #64 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-948.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #64 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-948.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #65 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-858.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-858.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #65 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-858.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #65 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-858.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #66 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-477.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-79.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-922.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-477.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #66 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-477.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #66 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-477.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #67 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-275.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-233.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-275.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #67 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-275.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #67 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-275.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #68 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-669.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-204.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-669.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #68 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-669.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #68 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-669.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #69 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-185.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-323.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-767.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-96.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-185.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #69 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-185.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #69 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-185.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #70 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-133.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-133.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #70 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-133.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #70 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-133.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #71 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-279.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-279.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #71 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-279.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #71 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-279.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #72 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-674.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #72 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #72 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #73 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-910.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-910.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #73 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-910.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #73 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-910.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #74 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-868.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-93.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-868.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #74 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-868.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #74 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-868.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #75 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-86.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-51.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-86.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #75 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-86.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #75 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-86.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #76 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-815.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-664.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-815.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #76 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-815.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #76 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-815.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #77 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-658.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-658.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #77 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-658.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #77 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-658.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #78 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-616.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-196.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-616.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #78 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-616.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #78 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-616.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #79 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-238.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-834.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-853.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-506.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-238.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #79 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-238.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #79 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-238.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #80 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-437.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-275.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #80 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #80 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #81 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-186.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-29.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #81 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #81 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #82 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-916.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-9.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-916.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #82 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-916.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #82 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-916.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #83 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-634.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-563.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-634.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #83 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-634.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #83 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-634.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #84 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-333.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-896.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-333.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #84 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-333.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #84 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-333.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #85 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-336.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-162.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-336.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #85 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-336.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #85 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-336.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #86 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-628.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-628.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #86 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-628.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #86 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-628.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #87 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-426.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-862.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-38.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #87 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #87 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #88 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-384.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-519.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-51.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-934.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #88 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #88 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #89 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-101.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-105.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-166.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-523.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-149.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-576.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-624.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-101.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #89 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-101.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #89 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-101.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #90 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-498.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-433.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-498.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #90 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-498.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #90 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-498.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #91 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-453.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-127.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #91 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #91 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #92 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #92 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #92 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #93 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-64.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-64.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #93 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-64.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #93 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-64.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #94 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-930.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-176.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-930.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #94 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-930.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #94 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-930.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #95 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-41.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-450.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-410.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-943.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-51.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-611.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-41.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #95 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-41.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #95 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-41.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #96 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-727.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-51.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-697.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-727.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #96 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-727.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #96 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-727.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #97 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-112.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-143.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-297.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-123.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-667.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-29.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-744.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-112.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #97 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-112.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #97 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-112.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #98 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-262.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-41.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-96.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-36.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-379.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-708.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-220.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-879.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-236.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-703.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-75.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-122.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #98 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #98 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #99 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-609.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-330.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-609.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #99 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-609.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #99 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-609.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #100 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-409.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-727.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-383.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-122.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-376.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #100 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #100 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #101 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-827.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html");
        yourResult = tester.getIncomingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-827.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #101 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-827.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #101 checking incoming links for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-827.html");
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
