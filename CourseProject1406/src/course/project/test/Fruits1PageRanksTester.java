import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;

public class Fruits1PageRanksTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits1-PageRanks-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits1-PageRanks-passed.txt"));
        double expectedResult;
        double yourResult;
//Test #103 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html
        expectedResult = 3.7696947136891433E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #103 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #103 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #104 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-507.html
        expectedResult = 3.6524082707211264E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-507.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #104 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-507.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #104 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-507.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #105 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-906.html
        expectedResult = 6.854706536515731E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-906.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #105 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-906.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #105 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-906.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #106 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-51.html
        expectedResult = 9.716648218941745E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-51.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #106 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-51.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #106 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-51.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #107 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-787.html
        expectedResult = 9.163228606503471E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-787.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #107 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-787.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #107 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-787.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #108 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-616.html
        expectedResult = 3.9842867205528804E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-616.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #108 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-616.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #108 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-616.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #109 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-913.html
        expectedResult = 6.281628905558996E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-913.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #109 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-913.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #109 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-913.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #110 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-282.html
        expectedResult = 0.0016210614178369727;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-282.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #110 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-282.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #110 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-282.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #111 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-204.html
        expectedResult = 6.506150163785502E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-204.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #111 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-204.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #111 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-204.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #112 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-577.html
        expectedResult = 3.7306411702595733E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-577.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #112 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-577.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #112 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-577.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #113 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-645.html
        expectedResult = 0.0021043328876023146;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-645.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #113 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-645.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #113 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-645.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #114 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-749.html
        expectedResult = 3.800285506337937E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-749.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #114 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-749.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #114 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-749.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #115 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-851.html
        expectedResult = 0.0012272735255774818;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-851.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #115 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-851.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #115 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-851.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #116 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-998.html
        expectedResult = 3.631425237550395E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-998.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #116 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-998.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #116 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-998.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #117 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-502.html
        expectedResult = 3.649906802903496E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-502.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #117 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-502.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #117 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-502.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #118 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-18.html
        expectedResult = 6.366232998383605E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-18.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #118 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-18.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #118 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-18.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #119 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-632.html
        expectedResult = 3.616784340087035E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-632.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #119 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-632.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #119 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-632.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #120 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-817.html
        expectedResult = 6.21624041882522E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-817.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #120 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-817.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #120 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-817.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #121 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-698.html
        expectedResult = 6.673546359107768E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-698.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #121 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-698.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #121 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-698.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #122 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html
        expectedResult = 0.0017318262349169723;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #122 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #122 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #123 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-407.html
        expectedResult = 0.0011663317825963571;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-407.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #123 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-407.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #123 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-407.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #124 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-126.html
        expectedResult = 3.5556580825027185E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-126.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #124 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-126.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #124 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-126.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #125 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-395.html
        expectedResult = 3.605345591405607E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-395.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #125 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-395.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #125 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-395.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #126 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html
        expectedResult = 0.007892875309786116;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #126 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #126 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #127 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-739.html
        expectedResult = 0.0012066341676299729;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-739.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #127 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-739.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #127 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-739.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #128 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-953.html
        expectedResult = 3.71588510772104E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-953.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #128 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-953.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #128 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-953.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #129 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-100.html
        expectedResult = 0.0015906325884644768;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-100.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #129 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-100.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #129 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-100.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #130 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-718.html
        expectedResult = 8.643770825738093E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-718.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #130 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-718.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #130 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-718.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #131 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-394.html
        expectedResult = 4.238961943826268E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-394.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #131 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-394.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #131 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-394.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #132 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-567.html
        expectedResult = 8.91494238155256E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-567.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #132 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-567.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #132 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-567.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #133 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-823.html
        expectedResult = 6.46639267610087E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-823.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #133 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-823.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #133 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-823.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #134 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-358.html
        expectedResult = 0.0012967534797202623;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-358.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #134 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-358.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #134 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-358.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #135 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-297.html
        expectedResult = 6.883992040042426E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-297.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #135 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-297.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #135 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-297.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #136 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-848.html
        expectedResult = 3.9155092573113845E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-848.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #136 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-848.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #136 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-848.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #137 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-389.html
        expectedResult = 0.0012296093917433875;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-389.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #137 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-389.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #137 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-389.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #138 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-320.html
        expectedResult = 0.0018463880959291347;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-320.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #138 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-320.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #138 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-320.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #139 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-737.html
        expectedResult = 9.532508844364268E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-737.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #139 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-737.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #139 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-737.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #140 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-236.html
        expectedResult = 0.0016802965302209708;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-236.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #140 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-236.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #140 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-236.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #141 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-558.html
        expectedResult = 9.701209156908553E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-558.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #141 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-558.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #141 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-558.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #142 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-16.html
        expectedResult = 9.199225749227882E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-16.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #142 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-16.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #142 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-16.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #143 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-73.html
        expectedResult = 7.414318963031327E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-73.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #143 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-73.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #143 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-73.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #144 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-882.html
        expectedResult = 3.5885478265859996E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-882.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #144 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-882.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #144 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-882.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #145 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-847.html
        expectedResult = 4.793731626936133E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-847.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #145 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-847.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #145 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-847.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #146 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-173.html
        expectedResult = 6.141643644509567E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-173.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #146 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-173.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #146 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-173.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #147 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-91.html
        expectedResult = 0.0011665632313430684;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-91.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #147 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-91.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #147 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-91.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #148 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-699.html
        expectedResult = 6.945620625598681E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-699.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #148 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-699.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #148 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-699.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #149 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-14.html
        expectedResult = 0.0037376806518641397;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-14.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #149 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-14.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #149 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-14.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #150 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-964.html
        expectedResult = 6.431820609615675E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-964.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #150 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-964.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #150 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-964.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #151 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-404.html
        expectedResult = 6.858353617300508E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-404.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #151 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-404.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #151 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-404.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #152 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-312.html
        expectedResult = 3.6457853655908786E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits/N-312.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #152 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-312.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #152 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits/N-312.html");
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
