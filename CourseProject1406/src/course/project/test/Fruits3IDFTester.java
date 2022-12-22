import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;

public class Fruits3IDFTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits3-IDF-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits3-IDF-passed.txt"));
        double expectedResult;
        double yourResult;
//Test #154 checking IDF for cherry
        expectedResult = 0.1600404125104682;
        yourResult = tester.getIDF("cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #154 checking IDF for cherry");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #154 checking IDF for cherry");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #155 checking IDF for orange
        expectedResult = 0.16812275880832706;
        yourResult = tester.getIDF("orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #155 checking IDF for orange");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #155 checking IDF for orange");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #156 checking IDF for fig
        expectedResult = 0.16650266314016507;
        yourResult = tester.getIDF("fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #156 checking IDF for fig");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #156 checking IDF for fig");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #157 checking IDF for banana
        expectedResult = 0.15842936260448298;
        yourResult = tester.getIDF("banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #157 checking IDF for banana");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #157 checking IDF for banana");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #158 checking IDF for kiwi
        expectedResult = 0.15842936260448298;
        yourResult = tester.getIDF("kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #158 checking IDF for kiwi");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #158 checking IDF for kiwi");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #159 checking IDF for peach
        expectedResult = 0.1600404125104682;
        yourResult = tester.getIDF("peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #159 checking IDF for peach");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #159 checking IDF for peach");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #160 checking IDF for papaya
        expectedResult = 0.1762506396917273;
        yourResult = tester.getIDF("papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #160 checking IDF for papaya");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #160 checking IDF for papaya");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #161 checking IDF for coconut
        expectedResult = 0.18114943910456646;
        yourResult = tester.getIDF("coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #161 checking IDF for coconut");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #161 checking IDF for coconut");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #162 checking IDF for apricot
        expectedResult = 0.16650266314016507;
        yourResult = tester.getIDF("apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #162 checking IDF for apricot");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #162 checking IDF for apricot");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #163 checking IDF for lime
        expectedResult = 0.20922796213800016;
        yourResult = tester.getIDF("lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #163 checking IDF for lime");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #163 checking IDF for lime");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #164 checking IDF for blueberry
        expectedResult = 0.17136841831198113;
        yourResult = tester.getIDF("blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #164 checking IDF for blueberry");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #164 checking IDF for blueberry");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #165 checking IDF for pear
        expectedResult = 0.17462139610706884;
        yourResult = tester.getIDF("pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #165 checking IDF for pear");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #165 checking IDF for pear");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #166 checking IDF for apple
        expectedResult = 0.1729939903610231;
        yourResult = tester.getIDF("apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #166 checking IDF for apple");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #166 checking IDF for apple");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #167 checking IDF for tomato
        expectedResult = 0.0;
        yourResult = tester.getIDF("tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #167 checking IDF for tomato");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #167 checking IDF for tomato");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

        failOut.close();
        passOut.close();
    }
}
