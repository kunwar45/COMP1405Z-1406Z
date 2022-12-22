import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;

public class Fruits4PageRanksTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits4-PageRanks-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits4-PageRanks-passed.txt"));
        double expectedResult;
        double yourResult;
//Test #103 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-502.html
        expectedResult = 3.5356662791376627E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-502.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #103 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-502.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #103 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-502.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #104 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-590.html
        expectedResult = 3.549755303334436E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-590.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #104 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-590.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #104 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-590.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #105 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-380.html
        expectedResult = 7.025434327756503E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-380.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #105 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-380.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #105 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-380.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #106 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-56.html
        expectedResult = 0.004129506779916748;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-56.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #106 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-56.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #106 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-56.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #107 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-140.html
        expectedResult = 0.0011608097818288986;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-140.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #107 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-140.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #107 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-140.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #108 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-546.html
        expectedResult = 4.2080421200661256E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-546.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #108 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-546.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #108 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-546.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #109 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html
        expectedResult = 0.0018077391810959046;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #109 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #109 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #110 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-890.html
        expectedResult = 3.5914886005699773E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-890.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #110 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-890.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #110 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-890.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #111 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-111.html
        expectedResult = 0.00140083098007733;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-111.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #111 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-111.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #111 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-111.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #112 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-465.html
        expectedResult = 3.865694872169223E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-465.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #112 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-465.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #112 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-465.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #113 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html
        expectedResult = 6.045558558302194E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #113 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #113 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #114 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-240.html
        expectedResult = 3.557466228936837E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-240.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #114 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-240.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #114 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-240.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #115 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-45.html
        expectedResult = 8.763828700531529E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-45.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #115 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-45.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #115 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-45.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #116 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html
        expectedResult = 3.6883050894148206E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #116 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #116 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #117 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-237.html
        expectedResult = 3.56281609053414E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-237.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #117 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-237.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #117 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-237.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #118 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-762.html
        expectedResult = 3.6450820750152035E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-762.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #118 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-762.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #118 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-762.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #119 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html
        expectedResult = 0.016873232508716116;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #119 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #119 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #120 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html
        expectedResult = 9.619865182963681E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #120 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #120 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #121 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-807.html
        expectedResult = 8.674167948568336E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-807.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #121 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-807.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #121 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-807.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #122 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-644.html
        expectedResult = 6.599907618328992E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-644.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #122 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-644.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #122 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-644.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #123 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-949.html
        expectedResult = 6.809924034226131E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-949.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #123 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-949.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #123 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-949.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #124 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html
        expectedResult = 6.566860081145487E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #124 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #124 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #125 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html
        expectedResult = 4.43618761493719E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #125 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #125 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #126 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-671.html
        expectedResult = 4.0470840334746186E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-671.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #126 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-671.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #126 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-671.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #127 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-668.html
        expectedResult = 3.883079054867013E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-668.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #127 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-668.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #127 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-668.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #128 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-846.html
        expectedResult = 6.293064955678464E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-846.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #128 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-846.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #128 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-846.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #129 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-116.html
        expectedResult = 0.0010273047029126527;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-116.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #129 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-116.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #129 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-116.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #130 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-394.html
        expectedResult = 0.0022691721157267687;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-394.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #130 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-394.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #130 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-394.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #131 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html
        expectedResult = 0.0011124804911806557;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #131 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #131 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #132 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-619.html
        expectedResult = 8.726307733553746E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-619.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #132 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-619.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #132 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-619.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #133 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-719.html
        expectedResult = 3.6885428529847295E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-719.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #133 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-719.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #133 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-719.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #134 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-952.html
        expectedResult = 9.296297903162818E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-952.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #134 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-952.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #134 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-952.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #135 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-329.html
        expectedResult = 3.543720970628618E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-329.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #135 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-329.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #135 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-329.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #136 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-390.html
        expectedResult = 3.5397078127791053E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-390.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #136 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-390.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #136 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-390.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #137 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-374.html
        expectedResult = 3.6576388986525707E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-374.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #137 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-374.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #137 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-374.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #138 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-664.html
        expectedResult = 0.001326611235254265;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-664.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #138 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-664.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #138 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-664.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #139 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-328.html
        expectedResult = 3.5482096605485747E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-328.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #139 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-328.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #139 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-328.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #140 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-978.html
        expectedResult = 3.7061788098279947E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-978.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #140 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-978.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #140 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-978.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #141 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-935.html
        expectedResult = 3.581819567216839E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-935.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #141 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-935.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #141 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-935.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #142 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-842.html
        expectedResult = 6.475996832238897E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-842.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #142 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-842.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #142 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-842.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #143 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html
        expectedResult = 0.0018382600261050192;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #143 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #143 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #144 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-454.html
        expectedResult = 6.453197178411358E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-454.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #144 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-454.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #144 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-454.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #145 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html
        expectedResult = 0.00661719382593155;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #145 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #145 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #146 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-367.html
        expectedResult = 3.8537783541767786E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-367.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #146 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-367.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #146 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-367.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #147 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-173.html
        expectedResult = 0.0011745290188745416;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-173.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #147 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-173.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #147 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-173.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #148 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-577.html
        expectedResult = 0.0014041926412019393;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-577.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #148 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-577.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #148 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-577.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #149 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-684.html
        expectedResult = 0.001535825682816165;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-684.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #149 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-684.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #149 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-684.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #150 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-124.html
        expectedResult = 0.0022042338543449397;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-124.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #150 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-124.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #150 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-124.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #151 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-148.html
        expectedResult = 8.757895984529496E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-148.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #151 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-148.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #151 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-148.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #152 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-593.html
        expectedResult = 3.6241466089304106E-4;
        yourResult = tester.getPageRank("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-593.html");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #152 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-593.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #152 checking page rank for https://people.scs.carleton.ca/~davidmckenney/fruits4/N-593.html");
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
