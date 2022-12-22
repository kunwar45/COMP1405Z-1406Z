import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;

public class Fruits2PageRanksTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits2-PageRanks-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits2-PageRanks-passed.txt"));
        double expectedResult;
        double yourResult;
//Test #103 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-836.html
        expectedResult = 3.440183926048478E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-836.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #103 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-836.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #103 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-836.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #104 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-55.html
        expectedResult = 6.196276934586521E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-55.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #104 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-55.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #104 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-55.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #105 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-739.html
        expectedResult = 4.5362833804366183E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-739.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #105 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-739.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #105 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-739.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #106 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-516.html
        expectedResult = 3.5774349553997466E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-516.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #106 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-516.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #106 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-516.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #107 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-820.html
        expectedResult = 4.1283113365790273E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-820.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #107 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-820.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #107 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-820.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #108 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-965.html
        expectedResult = 0.001150377069056384;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-965.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #108 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-965.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #108 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-965.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #109 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html
        expectedResult = 9.50371867909481E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #109 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #109 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #110 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-72.html
        expectedResult = 0.002002796707909987;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-72.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #110 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-72.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #110 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-72.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #111 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-673.html
        expectedResult = 3.5384852903240515E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-673.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #111 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-673.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #111 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-673.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #112 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html
        expectedResult = 3.7735734985848467E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #112 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #112 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #113 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-859.html
        expectedResult = 8.621328490798698E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-859.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #113 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-859.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #113 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-859.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #114 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-980.html
        expectedResult = 7.147182389867217E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-980.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #114 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-980.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #114 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-980.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #115 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-640.html
        expectedResult = 3.487925519172669E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-640.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #115 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-640.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #115 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-640.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #116 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-510.html
        expectedResult = 0.0010657244687502297;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-510.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #116 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-510.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #116 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-510.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #117 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-478.html
        expectedResult = 9.077676695952732E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-478.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #117 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-478.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #117 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-478.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #118 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-47.html
        expectedResult = 0.002784802828799483;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-47.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #118 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-47.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #118 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-47.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #119 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-270.html
        expectedResult = 0.001912679759615558;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-270.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #119 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-270.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #119 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-270.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #120 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-383.html
        expectedResult = 4.1133978861969503E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-383.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #120 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-383.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #120 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-383.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #121 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-361.html
        expectedResult = 5.903414831025885E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-361.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #121 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-361.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #121 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-361.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #122 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-639.html
        expectedResult = 6.218613057557382E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-639.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #122 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-639.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #122 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-639.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #123 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-856.html
        expectedResult = 6.346721281556817E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-856.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #123 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-856.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #123 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-856.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #124 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-789.html
        expectedResult = 6.635320926911974E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-789.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #124 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-789.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #124 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-789.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #125 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-329.html
        expectedResult = 0.002040972060430078;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-329.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #125 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-329.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #125 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-329.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #126 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-765.html
        expectedResult = 3.950598673105265E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-765.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #126 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-765.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #126 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-765.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #127 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-362.html
        expectedResult = 3.5181420974675755E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-362.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #127 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-362.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #127 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-362.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #128 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-650.html
        expectedResult = 3.4752878811773676E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-650.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #128 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-650.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #128 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-650.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #129 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-880.html
        expectedResult = 6.205336983796334E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-880.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #129 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-880.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #129 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-880.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #130 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html
        expectedResult = 0.002570748097825336;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #130 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #130 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #131 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html
        expectedResult = 0.0038561023868215953;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #131 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #131 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #132 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-61.html
        expectedResult = 0.0021936841031614993;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-61.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #132 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-61.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #132 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-61.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #133 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-818.html
        expectedResult = 3.743404224100811E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-818.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #133 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-818.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #133 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-818.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #134 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-605.html
        expectedResult = 8.505558653316477E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-605.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #134 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-605.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #134 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-605.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #135 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-37.html
        expectedResult = 0.0011451721426287156;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-37.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #135 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-37.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #135 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-37.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #136 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html
        expectedResult = 6.81127726475573E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #136 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #136 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #137 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-550.html
        expectedResult = 8.721560149181919E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-550.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #137 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-550.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #137 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-550.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #138 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-290.html
        expectedResult = 3.6753030785860815E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-290.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #138 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-290.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #138 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-290.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #139 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-426.html
        expectedResult = 7.365056607011859E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-426.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #139 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-426.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #139 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-426.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #140 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-832.html
        expectedResult = 3.6749098953763515E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-832.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #140 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-832.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #140 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-832.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #141 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-372.html
        expectedResult = 3.440963021120649E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-372.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #141 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-372.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #141 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-372.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #142 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-729.html
        expectedResult = 3.8603107849933486E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-729.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #142 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-729.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #142 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-729.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #143 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-762.html
        expectedResult = 6.082040711085188E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-762.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #143 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-762.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #143 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-762.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #144 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-613.html
        expectedResult = 3.766920475728569E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-613.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #144 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-613.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #144 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-613.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #145 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-981.html
        expectedResult = 9.33870432293359E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-981.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #145 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-981.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #145 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-981.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #146 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-463.html
        expectedResult = 0.0010885026897501364;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-463.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #146 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-463.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #146 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-463.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #147 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-309.html
        expectedResult = 3.403201547189664E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-309.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #147 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-309.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #147 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-309.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #148 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-626.html
        expectedResult = 3.550945608802363E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-626.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #148 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-626.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #148 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-626.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #149 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-905.html
        expectedResult = 4.0337884554803233E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-905.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #149 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-905.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #149 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-905.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #150 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-173.html
        expectedResult = 8.655169552281298E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-173.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #150 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-173.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #150 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-173.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #151 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-44.html
        expectedResult = 0.0017761685359935938;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-44.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #151 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-44.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #151 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-44.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #152 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-342.html
        expectedResult = 3.691876655788804E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-342.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #152 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-342.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #152 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits2/N-342.html");
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
