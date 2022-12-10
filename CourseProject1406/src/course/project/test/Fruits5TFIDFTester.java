import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;

public class Fruits5TFIDFTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits5-TFIDF-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits5-TFIDF-passed.txt"));
        double expectedResult;
        double yourResult;
//Test #289 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #289 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #289 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #290 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #290 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #290 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #291 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #291 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #291 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #292 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html
        expectedResult = 0.05008290494448164;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #292 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #292 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #293 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html
        expectedResult = 0.013493965809283838;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #293 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #293 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #294 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #294 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #294 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #295 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html
        expectedResult = 0.04820362275966532;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #295 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #295 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #296 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html
        expectedResult = 0.012735307853409157;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #296 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #296 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #297 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html
        expectedResult = 0.024817228830548887;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #297 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #297 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #298 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html
        expectedResult = 0.04867265117608714;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #298 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #298 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #299 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #299 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #299 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #300 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = 0.019227264232435187;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #300 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #300 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #301 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = 0.01298762597983467;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #301 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #301 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #302 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = 0.01210697658820754;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #302 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #302 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #303 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = 0.019976864637262157;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #303 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #303 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #304 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = 0.00683816945309014;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #304 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #304 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #305 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = 0.018109149908590503;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #305 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #305 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #306 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = 0.025308919864144203;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #306 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #306 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #307 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = 0.024817228830548887;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #307 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #307 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #308 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = 0.006453713783605871;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #308 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #308 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #309 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = 0.02555517941738175;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #309 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #309 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #310 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #310 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #310 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #311 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html
        expectedResult = 0.018849868135314314;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #311 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #311 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #312 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html
        expectedResult = 0.027747647068634366;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #312 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #312 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #313 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html
        expectedResult = 0.021757345765381856;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #313 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #313 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #314 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html
        expectedResult = 0.01958475525260531;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #314 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #314 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #315 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html
        expectedResult = 0.009984434279832238;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #315 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #315 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #316 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html
        expectedResult = 0.0045707331249277144;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #316 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #316 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #317 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html
        expectedResult = 0.009609784097532346;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #317 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #317 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #318 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html
        expectedResult = 0.013996938174706455;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #318 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #318 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #319 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html
        expectedResult = 0.01848366083779472;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #319 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #319 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #320 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html
        expectedResult = 0.01903328015489108;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #320 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #320 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #321 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #321 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #321 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #322 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html
        expectedResult = 0.014562795993986995;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #322 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #322 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #323 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html
        expectedResult = 0.014562795993986995;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #323 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #323 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #324 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #324 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #324 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #325 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #325 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #325 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #326 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html
        expectedResult = 0.029396004061608222;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #326 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #326 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #327 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html
        expectedResult = 0.013715932363297578;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #327 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #327 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #328 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html
        expectedResult = 0.0282929652742414;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #328 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #328 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #329 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html
        expectedResult = 0.02774330146346468;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #329 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #329 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #330 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html
        expectedResult = 0.014279876128075786;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #330 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #330 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #331 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #331 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #331 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #332 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #332 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #332 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #333 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #333 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #333 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #334 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #334 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #334 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #335 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #335 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #335 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #336 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #336 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #336 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #337 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #337 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #337 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #338 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #338 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #338 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #339 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html
        expectedResult = 0.16650266314016507;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #339 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #339 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #340 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #340 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #340 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #341 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #341 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #341 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #342 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #342 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #342 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #343 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #343 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #343 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #344 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html
        expectedResult = 0.005652321171738842;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #344 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #344 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #345 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html
        expectedResult = 0.011174692344957056;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #345 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #345 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #346 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html
        expectedResult = 0.02518657848585213;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #346 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #346 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #347 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html
        expectedResult = 0.03847255239304207;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #347 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #347 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #348 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html
        expectedResult = 0.011610352551439574;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #348 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #348 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #349 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html
        expectedResult = 0.005323624317693927;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #349 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #349 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #350 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html
        expectedResult = 0.016572954723677334;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #350 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #350 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #351 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html
        expectedResult = 0.010957595129481424;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #351 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #351 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #352 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html
        expectedResult = 0.016250982340756406;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #352 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #352 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #353 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html
        expectedResult = 0.022065193013251137;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #353 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #353 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #354 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #354 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #354 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-17.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #355 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html
        expectedResult = 0.02404130443487356;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #355 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #355 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #356 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html
        expectedResult = 0.018252769725939477;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #356 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #356 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #357 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html
        expectedResult = 0.01148582634157894;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #357 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #357 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #358 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html
        expectedResult = 0.012801655872994823;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #358 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #358 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #359 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html
        expectedResult = 0.00648289882797836;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #359 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #359 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #360 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html
        expectedResult = 0.011604779303045994;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #360 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #360 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #361 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html
        expectedResult = 0.02404130443487356;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #361 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #361 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #362 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html
        expectedResult = 0.017898162604786147;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #362 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #362 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #363 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html
        expectedResult = 0.0061184171891118504;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #363 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #363 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #364 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html
        expectedResult = 0.012441181905748045;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #364 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #364 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #365 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #365 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #365 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #366 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html
        expectedResult = 0.021313608362829885;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #366 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #366 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #367 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html
        expectedResult = 0.0167379925634961;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #367 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #367 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #368 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html
        expectedResult = 0.015603042805088452;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #368 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #368 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #369 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html
        expectedResult = 0.007601935048999819;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #369 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #369 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #370 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html
        expectedResult = 0.029109955237174696;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #370 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #370 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #371 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html
        expectedResult = 0.017929662715806864;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #371 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #371 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #372 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html
        expectedResult = 0.01903669495119289;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #372 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #372 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #373 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html
        expectedResult = 0.01866685806099626;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #373 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #373 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #374 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html
        expectedResult = 0.01866685806099626;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #374 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #374 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #375 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html
        expectedResult = 0.012191001511836164;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #375 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #375 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #376 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #376 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #376 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #377 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html
        expectedResult = 0.013730169280254405;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #377 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #377 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #378 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html
        expectedResult = 0.013730169280254405;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #378 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #378 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #379 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html
        expectedResult = 0.012799170401601181;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #379 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #379 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #380 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #380 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #380 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #381 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #381 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #381 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #382 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html
        expectedResult = 0.04780732893089021;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #382 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #382 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #383 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html
        expectedResult = 0.013730169280254405;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #383 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #383 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #384 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html
        expectedResult = 0.03828065416593777;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #384 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #384 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #385 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html
        expectedResult = 0.026198733188798045;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #385 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #385 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #386 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html
        expectedResult = 0.02697776338040238;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #386 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #386 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #387 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #387 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #387 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #388 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html
        expectedResult = 0.010445670339545651;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #388 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #388 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #389 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html
        expectedResult = 0.005279609589739715;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #389 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #389 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #390 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html
        expectedResult = 0.014451757388162253;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #390 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #390 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #391 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html
        expectedResult = 0.016107367405820545;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #391 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #391 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #392 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html
        expectedResult = 0.016107367405820545;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #392 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #392 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #393 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html
        expectedResult = 0.023837141795301758;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #393 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #393 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #394 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html
        expectedResult = 0.010445670339545651;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #394 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #394 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #395 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html
        expectedResult = 0.020058565612500703;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #395 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #395 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #396 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html
        expectedResult = 0.024817228830548887;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #396 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #396 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #397 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html
        expectedResult = 0.020655015375922698;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #397 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #397 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #398 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #398 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #398 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #399 checking TFIDF for fig in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #399 checking TFIDF for fig in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #399 checking TFIDF for fig in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #400 checking TFIDF for papaya in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #400 checking TFIDF for papaya in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #400 checking TFIDF for papaya in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #401 checking TFIDF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #401 checking TFIDF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #401 checking TFIDF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #402 checking TFIDF for blueberry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #402 checking TFIDF for blueberry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #402 checking TFIDF for blueberry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #403 checking TFIDF for apricot in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #403 checking TFIDF for apricot in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #403 checking TFIDF for apricot in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #404 checking TFIDF for cherry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #404 checking TFIDF for cherry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #404 checking TFIDF for cherry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #405 checking TFIDF for orange in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #405 checking TFIDF for orange in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #405 checking TFIDF for orange in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #406 checking TFIDF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #406 checking TFIDF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #406 checking TFIDF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #407 checking TFIDF for lime in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #407 checking TFIDF for lime in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #407 checking TFIDF for lime in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #408 checking TFIDF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #408 checking TFIDF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #408 checking TFIDF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #409 checking TFIDF for tomato in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #409 checking TFIDF for tomato in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #409 checking TFIDF for tomato in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

        failOut.close();
        passOut.close();
    }
}
