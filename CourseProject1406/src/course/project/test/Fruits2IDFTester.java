import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;

public class Fruits2IDFTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits2-IDF-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits2-IDF-passed.txt"));
        double expectedResult;
        double yourResult;
//Test #154 checking IDF for coconut
        expectedResult = 0.05739166388833648;
        yourResult = tester.getIDF("coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #154 checking IDF for coconut");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #154 checking IDF for coconut");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #155 checking IDF for pear
        expectedResult = 0.052894948432125555;
        yourResult = tester.getIDF("pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #155 checking IDF for pear");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #155 checking IDF for pear");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #156 checking IDF for peach
        expectedResult = 0.05139915250664415;
        yourResult = tester.getIDF("peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #156 checking IDF for peach");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #156 checking IDF for peach");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #157 checking IDF for apple
        expectedResult = 0.05439229681862769;
        yourResult = tester.getIDF("apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #157 checking IDF for apple");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #157 checking IDF for apple");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #158 checking IDF for banana
        expectedResult = 0.052894948432125555;
        yourResult = tester.getIDF("banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #158 checking IDF for banana");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #158 checking IDF for banana");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #159 checking IDF for tomato
        expectedResult = 0.0;
        yourResult = tester.getIDF("tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #159 checking IDF for tomato");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #159 checking IDF for tomato");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

        failOut.close();
        passOut.close();
    }
}
