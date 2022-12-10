package course.project.test;

import course.project.ProjectTester;
import course.project.SearchData;
import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;

public class FruitsTinyIDFTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new SearchData(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("FruitsTiny-IDF-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("FruitsTiny-IDF-passed.txt"));
        double expectedResult;
        double yourResult;
//Test #34 checking IDF for apricot
        expectedResult = 0.0;
        yourResult = tester.getIDF("apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #34 checking IDF for apricot");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #34 checking IDF for apricot");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #35 checking IDF for kiwi
        expectedResult = 0.32192809488736235;
        yourResult = tester.getIDF("kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #35 checking IDF for kiwi");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #35 checking IDF for kiwi");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #36 checking IDF for papaya
        expectedResult = 0.5145731728297582;
        yourResult = tester.getIDF("papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #36 checking IDF for papaya");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #36 checking IDF for papaya");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #37 checking IDF for fig
        expectedResult = 0.7369655941662062;
        yourResult = tester.getIDF("fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #37 checking IDF for fig");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #37 checking IDF for fig");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #38 checking IDF for coconut
        expectedResult = 0.32192809488736235;
        yourResult = tester.getIDF("coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #38 checking IDF for coconut");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #38 checking IDF for coconut");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #39 checking IDF for pear
        expectedResult = 0.7369655941662062;
        yourResult = tester.getIDF("pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #39 checking IDF for pear");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #39 checking IDF for pear");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #40 checking IDF for apple
        expectedResult = 0.32192809488736235;
        yourResult = tester.getIDF("apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #40 checking IDF for apple");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #40 checking IDF for apple");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #41 checking IDF for lime
        expectedResult = 0.32192809488736235;
        yourResult = tester.getIDF("lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #41 checking IDF for lime");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #41 checking IDF for lime");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #42 checking IDF for blueberry
        expectedResult = 0.32192809488736235;
        yourResult = tester.getIDF("blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #42 checking IDF for blueberry");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #42 checking IDF for blueberry");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #43 checking IDF for cherry
        expectedResult = 0.5145731728297582;
        yourResult = tester.getIDF("cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #43 checking IDF for cherry");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #43 checking IDF for cherry");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #44 checking IDF for peach
        expectedResult = 0.5145731728297582;
        yourResult = tester.getIDF("peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #44 checking IDF for peach");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #44 checking IDF for peach");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #45 checking IDF for banana
        expectedResult = 0.0;
        yourResult = tester.getIDF("banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #45 checking IDF for banana");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #45 checking IDF for banana");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #46 checking IDF for orange
        expectedResult = 0.32192809488736235;
        yourResult = tester.getIDF("orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #46 checking IDF for orange");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #46 checking IDF for orange");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #47 checking IDF for tomato
        expectedResult = 0.0;
        yourResult = tester.getIDF("tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #47 checking IDF for tomato");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #47 checking IDF for tomato");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

        failOut.close();
        passOut.close();
    }
}
