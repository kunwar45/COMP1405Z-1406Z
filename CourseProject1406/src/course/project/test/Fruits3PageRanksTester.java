import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;

public class Fruits3PageRanksTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits3-PageRanks-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits3-PageRanks-passed.txt"));
        double expectedResult;
        double yourResult;
//Test #103 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-485.html
        expectedResult = 3.8416598390267576E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-485.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #103 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-485.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #103 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-485.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #104 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-943.html
        expectedResult = 3.6376573706536154E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-943.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #104 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-943.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #104 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-943.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #105 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-297.html
        expectedResult = 3.669669885790986E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-297.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #105 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-297.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #105 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-297.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #106 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-508.html
        expectedResult = 3.6628019645288203E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-508.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #106 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-508.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #106 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-508.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #107 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-842.html
        expectedResult = 0.00116133609987969;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-842.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #107 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-842.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #107 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-842.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #108 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-736.html
        expectedResult = 0.0010123929637381;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-736.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #108 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-736.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #108 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-736.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #109 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html
        expectedResult = 6.321502738672183E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #109 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #109 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #110 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-931.html
        expectedResult = 3.727248062673383E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-931.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #110 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-931.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #110 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-931.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #111 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-356.html
        expectedResult = 6.20090346076261E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-356.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #111 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-356.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #111 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-356.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #112 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-176.html
        expectedResult = 9.638036335109475E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-176.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #112 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-176.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #112 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-176.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #113 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-133.html
        expectedResult = 6.236538277696886E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-133.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #113 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-133.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #113 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-133.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #114 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html
        expectedResult = 6.778006958758042E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #114 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #114 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #115 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-154.html
        expectedResult = 9.238653352298381E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-154.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #115 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-154.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #115 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-154.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #116 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-880.html
        expectedResult = 4.166854369025119E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-880.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #116 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-880.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #116 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-880.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #117 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-703.html
        expectedResult = 3.6376573706536154E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-703.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #117 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-703.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #117 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-703.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #118 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-221.html
        expectedResult = 6.396552076258293E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-221.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #118 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-221.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #118 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-221.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #119 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-184.html
        expectedResult = 6.571451259871909E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-184.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #119 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-184.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #119 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-184.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #120 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-313.html
        expectedResult = 6.208833636217845E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-313.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #120 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-313.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #120 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-313.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #121 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-490.html
        expectedResult = 6.510066477734025E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-490.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #121 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-490.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #121 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-490.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #122 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-920.html
        expectedResult = 8.897689252943193E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-920.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #122 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-920.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #122 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-920.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #123 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-518.html
        expectedResult = 6.203184664184463E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-518.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #123 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-518.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #123 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-518.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #124 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-922.html
        expectedResult = 3.5926247942838653E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-922.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #124 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-922.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #124 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-922.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #125 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-78.html
        expectedResult = 6.701629039974602E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-78.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #125 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-78.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #125 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-78.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #126 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-810.html
        expectedResult = 3.992865637266918E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-810.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #126 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-810.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #126 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-810.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #127 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html
        expectedResult = 3.486335788348886E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #127 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #127 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #128 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html
        expectedResult = 0.0014002792028213243;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #128 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #128 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #129 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html
        expectedResult = 3.826546108248949E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #129 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #129 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #130 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-757.html
        expectedResult = 3.7218690341268623E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-757.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #130 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-757.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #130 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-757.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #131 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-167.html
        expectedResult = 6.270090581649436E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-167.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #131 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-167.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #131 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-167.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #132 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-494.html
        expectedResult = 0.0012187102323489543;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-494.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #132 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-494.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #132 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-494.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #133 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-429.html
        expectedResult = 6.732459329709324E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-429.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #133 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-429.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #133 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-429.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #134 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html
        expectedResult = 6.500801647674794E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #134 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #134 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #135 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-315.html
        expectedResult = 3.541481817934256E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-315.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #135 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-315.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #135 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-315.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #136 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-814.html
        expectedResult = 6.093103369370912E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-814.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #136 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-814.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #136 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-814.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #137 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-954.html
        expectedResult = 3.5990159844169435E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-954.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #137 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-954.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #137 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-954.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #138 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html
        expectedResult = 6.431826909517809E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #138 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #138 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #139 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-528.html
        expectedResult = 3.549110965297863E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-528.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #139 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-528.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #139 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-528.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #140 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-487.html
        expectedResult = 0.0011843726283658651;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-487.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #140 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-487.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #140 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-487.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #141 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-191.html
        expectedResult = 6.199071838497574E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-191.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #141 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-191.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #141 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-191.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #142 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-114.html
        expectedResult = 0.0031736191013866286;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-114.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #142 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-114.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #142 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-114.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #143 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-269.html
        expectedResult = 8.711384470116741E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-269.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #143 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-269.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #143 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-269.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #144 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html
        expectedResult = 3.992865637266918E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #144 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #144 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #145 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-124.html
        expectedResult = 0.0016035395452103152;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-124.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #145 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-124.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #145 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-124.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #146 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-165.html
        expectedResult = 3.7964941444779745E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-165.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #146 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-165.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #146 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-165.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #147 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html
        expectedResult = 6.235120140145672E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #147 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #147 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #148 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-667.html
        expectedResult = 3.9377988396368304E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-667.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #148 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-667.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #148 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-667.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #149 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-942.html
        expectedResult = 4.0450558725190616E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-942.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #149 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-942.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #149 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-942.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #150 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-775.html
        expectedResult = 4.5336429507172995E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-775.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #150 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-775.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #150 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-775.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #151 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-924.html
        expectedResult = 3.870948759829557E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-924.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #151 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-924.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #151 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-924.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #152 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-330.html
        expectedResult = 6.258781994905742E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-330.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #152 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-330.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #152 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits3/N-330.html");
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
