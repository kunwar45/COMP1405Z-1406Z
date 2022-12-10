import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.*;

public class Fruits2OutgoingLinksTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits2-OutgoingLinks-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits2-OutgoingLinks-passed.txt"));
        List<String> expectedResult;
        List<String> yourResult;
//Test #1 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-610.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-445.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-610.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #1 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-610.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #1 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-610.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #2 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-657.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-549.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-657.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #2 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-657.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #2 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-657.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #3 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-296.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-53.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-341.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-296.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #3 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-296.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #3 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-296.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #4 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-861.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-848.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-861.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #4 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-861.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #4 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-861.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #5 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-746.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-268.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-291.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-746.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #5 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-746.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #5 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-746.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #6 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-893.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-893.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #6 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-893.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #6 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-893.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #7 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-426.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-84.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-827.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-426.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #7 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-426.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #7 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-426.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #8 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-270.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-53.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-837.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-995.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-885.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-485.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-270.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #8 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-270.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #8 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-270.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #9 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-931.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-931.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #9 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-931.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #9 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-931.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #10 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-991.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-991.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #10 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-991.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #10 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-991.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #11 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-661.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-623.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-661.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #11 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-661.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #11 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-661.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #12 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-822.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-64.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-822.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #12 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-822.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #12 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-822.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #13 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #13 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #13 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #14 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-639.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-277.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-639.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #14 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-639.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #14 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-639.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #15 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-631.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-763.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-573.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-631.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #15 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-631.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #15 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-631.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #16 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-580.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-83.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-313.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-580.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #16 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-580.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #16 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-580.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #17 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-922.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-922.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #17 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-922.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #17 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-922.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #18 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-938.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-824.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-938.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #18 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-938.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #18 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-938.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #19 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-303.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-261.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-440.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-303.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #19 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-303.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #19 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-303.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #20 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-944.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-928.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-944.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #20 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-944.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #20 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-944.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #21 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-148.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-148.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #21 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-148.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #21 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-148.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #22 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-106.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-401.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-418.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-2.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-65.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-233.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-17.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-315.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-441.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-47.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-106.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #22 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-106.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #22 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-106.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #23 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-952.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-413.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-952.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #23 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-952.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #23 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-952.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #24 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-762.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-762.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #24 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-762.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #24 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-762.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #25 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-684.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-216.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #25 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #25 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #26 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-562.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-41.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-62.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-320.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-562.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #26 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-562.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #26 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-562.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #27 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-976.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-443.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-487.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-976.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #27 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-976.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #27 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-976.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #28 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-987.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-17.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-188.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-726.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-987.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #28 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-987.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #28 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-987.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #29 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-584.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-329.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-584.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #29 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-584.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #29 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-584.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #30 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-145.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-133.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-145.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #30 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-145.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #30 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-145.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #31 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-592.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-169.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-458.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-61.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-592.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #31 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-592.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #31 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-592.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #32 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-593.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-288.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-593.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #32 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-593.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #32 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-593.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #33 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-566.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-60.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-566.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #33 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-566.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #33 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-566.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #34 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-999.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-941.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-999.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #34 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-999.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #34 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-999.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #35 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-431.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-461.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-248.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-158.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-503.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #35 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #35 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #36 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-367.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-501.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-248.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-168.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-298.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-919.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-622.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-601.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #36 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #36 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #37 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-444.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-791.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-649.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-444.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #37 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-444.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #37 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-444.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #38 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-877.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-147.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-877.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #38 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-877.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #38 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-877.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #39 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-324.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-48.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-324.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #39 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-324.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #39 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-324.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #40 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-432.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-449.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-601.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-109.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-41.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-622.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-432.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #40 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-432.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #40 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-432.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #41 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-529.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-569.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-39.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-183.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-88.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-529.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #41 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-529.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #41 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-529.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #42 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-47.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-528.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-80.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-117.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-336.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-714.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-632.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-106.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-47.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #42 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-47.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #42 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-47.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #43 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-149.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-115.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-149.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #43 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-149.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #43 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-149.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #44 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-670.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-526.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-823.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-670.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #44 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-670.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #44 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-670.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #45 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-319.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #45 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #45 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #46 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-953.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-776.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-953.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #46 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-953.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #46 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-953.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #47 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-851.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-263.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-293.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-851.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #47 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-851.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #47 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-851.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #48 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-682.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-74.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-2.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-791.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-682.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #48 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-682.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #48 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-682.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #49 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-232.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-172.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-232.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #49 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-232.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #49 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-232.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #50 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-379.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-671.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-69.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-575.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-379.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #50 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-379.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #50 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-379.html");
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
