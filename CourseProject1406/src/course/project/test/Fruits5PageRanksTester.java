import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;

public class Fruits5PageRanksTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits5-PageRanks-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits5-PageRanks-passed.txt"));
        double expectedResult;
        double yourResult;
//Test #103 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-766.html
        expectedResult = 6.975065993869461E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-766.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #103 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-766.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #103 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-766.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #104 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-166.html
        expectedResult = 6.441723470208682E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-166.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #104 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-166.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #104 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-166.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #105 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html
        expectedResult = 6.51156893063885E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #105 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #105 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #106 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-334.html
        expectedResult = 8.927574200784144E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-334.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #106 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-334.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #106 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-334.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #107 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-61.html
        expectedResult = 3.583350173815755E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-61.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #107 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-61.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #107 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-61.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #108 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-248.html
        expectedResult = 3.58785824341776E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-248.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #108 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-248.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #108 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-248.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #109 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-847.html
        expectedResult = 3.972206853161858E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-847.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #109 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-847.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #109 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-847.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #110 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-309.html
        expectedResult = 7.757479420195431E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-309.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #110 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-309.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #110 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-309.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #111 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-866.html
        expectedResult = 6.373800995467483E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-866.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #111 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-866.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #111 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-866.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #112 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-772.html
        expectedResult = 7.301141469841886E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-772.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #112 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-772.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #112 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-772.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #113 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-707.html
        expectedResult = 6.510425441225172E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-707.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #113 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-707.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #113 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-707.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #114 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-159.html
        expectedResult = 0.0012750930901969566;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-159.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #114 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-159.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #114 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-159.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #115 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html
        expectedResult = 4.364947617880432E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #115 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #115 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #116 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-266.html
        expectedResult = 0.0013111664365640788;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-266.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #116 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-266.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #116 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-266.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #117 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-136.html
        expectedResult = 3.768184276601744E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-136.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #117 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-136.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #117 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-136.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #118 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-930.html
        expectedResult = 3.844855543258839E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-930.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #118 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-930.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #118 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-930.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #119 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-955.html
        expectedResult = 4.020142437156067E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-955.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #119 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-955.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #119 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-955.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #120 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-98.html
        expectedResult = 0.001990365164628709;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-98.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #120 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-98.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #120 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-98.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #121 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-726.html
        expectedResult = 3.890462467190846E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-726.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #121 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-726.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #121 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-726.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #122 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-680.html
        expectedResult = 6.38546788962126E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-680.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #122 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-680.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #122 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-680.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #123 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-574.html
        expectedResult = 0.0010309088028426301;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-574.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #123 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-574.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #123 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-574.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #124 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html
        expectedResult = 9.199732528214855E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #124 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #124 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #125 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-380.html
        expectedResult = 3.5916035563303026E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-380.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #125 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-380.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #125 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-380.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #126 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-247.html
        expectedResult = 8.990466321543318E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-247.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #126 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-247.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #126 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-247.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #127 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-382.html
        expectedResult = 0.0012326111200158321;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-382.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #127 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-382.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #127 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-382.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #128 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html
        expectedResult = 0.007498844836947286;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #128 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #128 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #129 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html
        expectedResult = 3.6762762826672644E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #129 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #129 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #130 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-51.html
        expectedResult = 0.003792782216784374;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-51.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #130 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-51.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #130 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-51.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #131 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-822.html
        expectedResult = 3.8825620346561444E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-822.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #131 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-822.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #131 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-822.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #132 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-228.html
        expectedResult = 6.533940198141097E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-228.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #132 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-228.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #132 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-228.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #133 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html
        expectedResult = 6.915604818190293E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #133 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #133 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #134 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-375.html
        expectedResult = 3.853567557857959E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-375.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #134 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-375.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #134 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-375.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #135 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-77.html
        expectedResult = 0.0014207132529543555;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-77.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #135 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-77.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #135 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-77.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #136 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-122.html
        expectedResult = 0.0038166570473998863;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-122.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #136 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-122.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #136 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-122.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #137 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-768.html
        expectedResult = 4.0922354812105257E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-768.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #137 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-768.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #137 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-768.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #138 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-699.html
        expectedResult = 6.211174704624728E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-699.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #138 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-699.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #138 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-699.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #139 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-553.html
        expectedResult = 3.664020898118488E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-553.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #139 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-553.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #139 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-553.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #140 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html
        expectedResult = 7.978364804543305E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #140 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #140 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #141 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html
        expectedResult = 0.007732993581600556;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #141 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #141 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #142 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-604.html
        expectedResult = 4.373312269559997E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-604.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #142 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-604.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #142 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-604.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #143 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-662.html
        expectedResult = 3.5916035563303026E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-662.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #143 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-662.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #143 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-662.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #144 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-197.html
        expectedResult = 0.0010783756576944806;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-197.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #144 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-197.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #144 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-197.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #145 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-917.html
        expectedResult = 0.0011744026429453506;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-917.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #145 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-917.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #145 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-917.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #146 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-525.html
        expectedResult = 3.687991708465412E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-525.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #146 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-525.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #146 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-525.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #147 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-434.html
        expectedResult = 0.0011720051301324893;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-434.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #147 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-434.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #147 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-434.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #148 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-356.html
        expectedResult = 3.824842328843707E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-356.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #148 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-356.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #148 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-356.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #149 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-66.html
        expectedResult = 0.003344886326114618;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-66.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #149 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-66.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #149 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-66.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #150 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-644.html
        expectedResult = 3.9190303260238664E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-644.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #150 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-644.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #150 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-644.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #151 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-152.html
        expectedResult = 0.001979629362168631;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-152.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #151 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-152.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #151 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-152.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #152 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-221.html
        expectedResult = 3.662003734750768E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-221.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #152 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-221.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #152 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits5/N-221.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #153 checking page rank for http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = -1.0;
        yourResult = tester.getPageRank("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #153 checking page rank for http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #153 checking page rank for http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

        failOut.close();
        passOut.close();
    }
}
