package course.project;

import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;

public class FruitsTinyTFTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new SearchData(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("FruitsTiny-TF-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("FruitsTiny-TF-passed.txt"));
        double expectedResult;
        double yourResult;
//Test #48 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #48 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #48 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #49 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.05;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #49 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #49 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #50 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.1;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #50 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #50 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #51 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.15;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #51 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #51 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #52 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.1;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #52 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #52 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #53 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.1;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #53 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #53 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #54 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.15;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #54 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #54 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #55 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.05;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #55 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #55 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #56 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #56 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #56 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #57 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #57 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #57 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #58 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #58 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #58 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #59 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #59 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #59 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #60 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #60 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #60 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #61 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.125;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #61 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #61 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #62 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #62 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #62 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #63 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.25;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #63 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #63 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #64 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #64 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #64 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #65 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #65 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #65 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #66 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #66 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #66 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #67 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #67 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #67 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #68 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #68 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #68 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #69 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #69 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #69 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #70 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #70 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #70 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #71 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #71 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #71 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #72 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #72 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #72 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #73 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.1875;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #73 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #73 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #74 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.125;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #74 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #74 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #75 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #75 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #75 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #76 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #76 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #76 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #77 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #77 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #77 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #78 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.1875;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #78 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #78 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #79 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #79 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #79 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #80 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #80 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #80 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #81 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.2;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #81 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #81 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #82 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.06666666666666667;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #82 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #82 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #83 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.2;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #83 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #83 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #84 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #84 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #84 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #85 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #85 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #85 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #86 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.26666666666666666;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #86 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #86 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #87 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #87 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #87 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #88 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #88 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #88 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #89 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #89 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #89 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #90 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.06666666666666667;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #90 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #90 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #91 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #91 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #91 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #92 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #92 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #92 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #93 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #93 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #93 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #94 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.03125;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #94 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #94 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #95 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #95 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #95 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #96 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.09375;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #96 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #96 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #97 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.03125;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #97 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #97 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #98 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.25;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #98 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #98 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #99 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.03125;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #99 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #99 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #100 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #100 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #100 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #101 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.125;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #101 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #101 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #102 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #102 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #102 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #103 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.043478260869565216;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #103 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #103 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #104 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.08695652173913043;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #104 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #104 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #105 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.043478260869565216;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #105 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #105 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #106 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.043478260869565216;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #106 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #106 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #107 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #107 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #107 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #108 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.08695652173913043;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #108 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #108 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #109 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.043478260869565216;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #109 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #109 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #110 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.13043478260869565;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #110 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #110 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #111 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.043478260869565216;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #111 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #111 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #112 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.17391304347826086;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #112 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #112 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #113 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #113 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #113 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #114 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.18181818181818182;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #114 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #114 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #115 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #115 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #115 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #116 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.18181818181818182;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #116 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #116 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #117 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #117 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #117 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #118 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.09090909090909091;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #118 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #118 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #119 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #119 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #119 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #120 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.09090909090909091;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #120 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #120 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #121 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.09090909090909091;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #121 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #121 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #122 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #122 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #122 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #123 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.18181818181818182;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #123 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #123 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #124 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #124 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #124 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #125 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.05405405405405406;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #125 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #125 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #126 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.02702702702702703;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #126 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #126 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #127 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.16216216216216217;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #127 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #127 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #128 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #128 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #128 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #129 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.05405405405405406;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #129 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #129 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #130 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.05405405405405406;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #130 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #130 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #131 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.08108108108108109;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #131 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #131 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #132 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.05405405405405406;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #132 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #132 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #133 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.13513513513513514;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #133 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #133 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #134 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.16216216216216217;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #134 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #134 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #135 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #135 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #135 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #136 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #136 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #136 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #137 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.25;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #137 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #137 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #138 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.25;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #138 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #138 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #139 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #139 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #139 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #140 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #140 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #140 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #141 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #141 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #141 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #142 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #142 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #142 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #143 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #143 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #143 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #144 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #144 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #144 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #145 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #145 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #145 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #146 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #146 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #146 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #147 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.14285714285714285;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #147 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #147 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #148 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #148 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #148 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #149 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #149 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #149 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #150 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #150 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #150 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #151 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.2857142857142857;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #151 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #151 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #152 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #152 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #152 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #153 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.14285714285714285;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #153 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #153 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #154 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.2857142857142857;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #154 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #154 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #155 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #155 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #155 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #156 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.14285714285714285;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #156 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #156 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #157 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #157 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #157 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #158 checking TF for papaya in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #158 checking TF for papaya in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #158 checking TF for papaya in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #159 checking TF for kiwi in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #159 checking TF for kiwi in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #159 checking TF for kiwi in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #160 checking TF for apricot in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #160 checking TF for apricot in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #160 checking TF for apricot in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #161 checking TF for fig in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #161 checking TF for fig in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #161 checking TF for fig in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #162 checking TF for orange in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #162 checking TF for orange in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #162 checking TF for orange in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #163 checking TF for lime in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #163 checking TF for lime in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #163 checking TF for lime in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #164 checking TF for cherry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #164 checking TF for cherry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #164 checking TF for cherry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #165 checking TF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #165 checking TF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #165 checking TF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #166 checking TF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #166 checking TF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #166 checking TF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #167 checking TF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #167 checking TF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #167 checking TF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #168 checking TF for tomato in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #168 checking TF for tomato in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #168 checking TF for tomato in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

        failOut.close();
        passOut.close();
    }
}
