import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.*;

public class Fruits3OutgoingLinksTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits3-OutgoingLinks-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits3-OutgoingLinks-passed.txt"));
        List<String> expectedResult;
        List<String> yourResult;
//Test #1 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-575.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-231.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-575.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #1 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-575.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #1 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-575.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #2 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-401.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-364.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-634.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-401.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #2 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-401.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #2 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-401.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #3 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-811.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-73.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-811.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #3 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-811.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #3 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-811.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #4 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-167.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-989.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-33.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-167.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #4 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-167.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #4 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-167.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #5 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-628.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-521.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-309.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-976.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-611.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-628.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #5 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-628.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #5 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-628.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #6 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-934.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-137.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-934.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #6 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-934.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #6 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-934.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #7 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-935.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-268.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-15.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-935.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #7 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-935.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #7 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-935.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #8 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-650.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-277.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-650.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #8 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-650.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #8 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-650.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #9 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-381.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-487.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-579.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-737.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-12.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-180.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-45.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-440.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-104.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-477.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-996.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-695.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-368.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-125.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-372.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-131.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-357.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-987.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-172.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-128.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-8.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-73.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-273.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-448.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-486.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-32.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-458.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-496.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-291.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-450.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-110.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-419.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-986.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #9 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #9 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #10 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-229.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-229.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #10 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-229.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #10 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-229.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #11 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-87.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-304.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-62.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-580.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-557.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-30.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-856.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-390.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-92.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-435.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-112.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-87.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #11 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-87.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #11 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-87.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #12 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-228.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-564.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-68.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-228.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #12 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-228.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #12 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-228.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #13 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-484.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-372.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-460.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-484.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #13 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-484.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #13 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-484.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #14 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-98.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-101.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-377.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-816.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-39.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-695.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-759.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-776.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-300.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-641.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-22.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-332.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-545.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-542.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-805.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #14 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #14 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #15 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-273.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-813.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #15 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #15 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #16 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-699.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-509.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-699.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #16 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-699.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #16 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-699.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #17 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-101.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-736.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-593.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-786.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-873.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #17 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #17 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #18 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-785.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-410.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-288.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-785.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #18 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-785.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #18 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-785.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #19 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-672.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-795.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-140.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-672.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #19 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-672.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #19 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-672.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #20 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-339.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-273.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-339.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #20 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-339.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #20 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-339.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #21 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-600.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-90.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-600.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #21 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-600.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #21 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-600.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #22 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-717.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-198.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-717.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #22 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-717.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #22 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-717.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #23 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-501.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-501.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #23 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-501.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #23 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-501.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #24 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-330.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-829.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-330.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #24 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-330.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #24 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-330.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #25 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-331.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-278.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-581.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-331.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #25 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-331.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #25 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-331.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #26 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-856.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-87.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-412.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-856.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #26 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-856.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #26 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-856.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #27 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-648.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-648.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #27 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-648.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #27 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-648.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #28 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-51.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-980.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #28 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #28 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #29 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-942.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-235.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-942.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #29 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-942.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #29 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-942.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #30 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-635.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-635.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #30 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-635.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #30 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-635.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #31 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-158.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-176.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-474.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-71.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-158.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #31 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-158.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #31 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-158.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #32 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-630.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-452.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-630.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #32 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-630.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #32 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-630.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #33 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-794.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-542.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-794.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #33 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-794.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #33 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-794.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #34 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-565.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-477.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-565.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #34 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-565.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #34 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-565.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #35 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-213.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-196.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-213.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #35 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-213.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #35 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-213.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #36 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-109.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-234.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-109.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #36 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-109.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #36 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-109.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #37 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-497.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-896.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-613.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-419.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-38.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-11.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-617.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-497.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #37 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-497.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #37 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-497.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #38 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-296.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-354.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #38 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #38 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #39 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-577.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-86.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-577.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #39 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-577.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #39 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-577.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #40 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-516.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-516.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #40 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-516.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #40 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-516.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #41 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-489.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-337.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-489.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #41 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-489.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #41 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-489.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #42 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-141.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-173.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-50.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-100.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-141.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #42 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-141.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #42 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-141.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #43 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-133.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-57.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-464.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-133.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #43 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-133.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #43 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-133.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #44 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-658.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-658.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #44 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-658.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #44 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-658.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #45 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-449.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-597.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-171.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-827.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #45 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #45 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #46 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-50.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-649.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-521.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-373.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-579.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-530.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-382.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-192.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-15.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-886.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-943.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-141.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-728.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-761.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-703.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-203.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-533.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-700.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-50.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #46 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-50.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #46 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-50.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #47 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-117.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-117.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #47 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-117.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #47 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-117.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #48 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-265.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-108.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-265.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #48 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-265.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #48 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-265.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #49 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-138.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-645.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-688.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-124.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-138.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #49 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-138.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #49 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-138.html");
            failOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            failOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        }

//Test #50 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-385.html
        expectedResult = new ArrayList<String>();
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html");
        expectedResult.add("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-446.html");
        yourResult = tester.getOutgoingLinks("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-385.html");
        if (TestingTools.checkListsEqual(yourResult, expectedResult)) {
            passOut.println("Passed Test #50 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-385.html");
            passOut.println("expected = " + Arrays.toString(expectedResult.toArray(new String[expectedResult.size()])));
            passOut.println("result = " + Arrays.toString(yourResult.toArray(new String[yourResult.size()])) + "\n\n");
        } else {
            failOut.println("Failed Test #50 checking outgoing links for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-385.html");
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
