import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;

public class FruitsTinyPageRanksTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("FruitsTiny-PageRanks-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("FruitsTiny-PageRanks-passed.txt"));
        double expectedResult;
        double yourResult;
//Test #23 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.04626765223510332;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #23 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #23 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #24 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.1193929620567529;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #24 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #24 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #25 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.04626765223510332;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #25 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #25 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #26 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.11896803724120768;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #26 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #26 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #27 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.04626765223510332;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #27 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #27 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #28 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.08195866555128291;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #28 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #28 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #29 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.32240189578896944;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #29 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #29 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #30 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.04626765223510332;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #30 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #30 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #31 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.04743429650546998;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #31 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #31 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #32 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.12477353391590358;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #32 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #32 checking page rank for https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #33 checking page rank for http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = -1.0;
        yourResult = tester.getPageRank("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #33 checking page rank for http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #33 checking page rank for http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

        failOut.close();
        passOut.close();
    }
}
