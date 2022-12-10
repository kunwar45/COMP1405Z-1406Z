import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;

public class Fruits3TFIDFTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits3-TFIDF-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits3-TFIDF-passed.txt"));
        double expectedResult;
        double yourResult;
//Test #289 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html
        expectedResult = 0.013165627148711207;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #289 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #289 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #290 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html
        expectedResult = 0.017304357236917495;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #290 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #290 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #291 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html
        expectedResult = 0.010037978816500861;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #291 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #291 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #292 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html
        expectedResult = 0.032228142227852065;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #292 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #292 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #293 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html
        expectedResult = 0.013165627148711207;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #293 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #293 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #294 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html
        expectedResult = 0.015554657231997495;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #294 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #294 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #295 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html
        expectedResult = 0.0328866563750325;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #295 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #295 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #296 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html
        expectedResult = 0.012654646839282212;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #296 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #296 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #297 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html
        expectedResult = 0.006868007395745492;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #297 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #297 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #298 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html
        expectedResult = 0.030066482304400493;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #298 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #298 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #299 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #299 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #299 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #300 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html
        expectedResult = 0.02289470289552112;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #300 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #300 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #301 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html
        expectedResult = 0.024235084020792663;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #301 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #301 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #302 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html
        expectedResult = 0.01754136709289925;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #302 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #302 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #303 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html
        expectedResult = 0.02876958206099301;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #303 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #303 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #304 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html
        expectedResult = 0.01172001055056407;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #304 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #304 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #305 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html
        expectedResult = 0.005643873312117802;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #305 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #305 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #306 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html
        expectedResult = 0.023787283262202967;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #306 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #306 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #307 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #307 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #307 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #308 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html
        expectedResult = 0.04507579008936898;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #308 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #308 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #309 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html
        expectedResult = 0.029672540985352273;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #309 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #309 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #310 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #310 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #310 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #311 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #311 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #311 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #312 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html
        expectedResult = 0.012406164068329641;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #312 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #312 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #313 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html
        expectedResult = 0.023117471758705398;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #313 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #313 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #314 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html
        expectedResult = 0.02876958206099301;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #314 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #314 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #315 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html
        expectedResult = 0.03357257486398112;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #315 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #315 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #316 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html
        expectedResult = 0.021784595623572593;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #316 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #316 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #317 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #317 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #317 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #318 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #318 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #318 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #319 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html
        expectedResult = 0.023563761377350296;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #319 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #319 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #320 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html
        expectedResult = 0.045931435170890406;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #320 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #320 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #321 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #321 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #321 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #322 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html
        expectedResult = 0.032075918518253574;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #322 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #322 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #323 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html
        expectedResult = 0.03395381822080993;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #323 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #323 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #324 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #324 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #324 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #325 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #325 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #325 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #326 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #326 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #326 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #327 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html
        expectedResult = 0.030520636907304714;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #327 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #327 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #328 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html
        expectedResult = 0.03332644075666537;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #328 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #328 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #329 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html
        expectedResult = 0.05802586506868189;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #329 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #329 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #330 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #330 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #330 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #331 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #331 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #331 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #332 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #332 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #332 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #333 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #333 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #333 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #334 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html
        expectedResult = 0.03395381822080993;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #334 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #334 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #335 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html
        expectedResult = 0.03238802197452078;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #335 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #335 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #336 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html
        expectedResult = 0.04030673707380368;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #336 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #336 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #337 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #337 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #337 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #338 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html
        expectedResult = 0.05744174657637611;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #338 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #338 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #339 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #339 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #339 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #340 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html
        expectedResult = 0.030830997742012325;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #340 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #340 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #341 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #341 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #341 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #342 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #342 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #342 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #343 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #343 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #343 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #344 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html
        expectedResult = 0.020029310274404445;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #344 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #344 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #345 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html
        expectedResult = 0.0054685102007835445;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #345 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #345 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #346 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html
        expectedResult = 0.015324034399896384;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #346 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #346 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #347 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html
        expectedResult = 0.01907068687159879;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #347 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #347 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #348 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html
        expectedResult = 0.02478615019882352;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #348 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #348 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #349 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html
        expectedResult = 0.02358433134557668;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #349 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #349 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #350 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html
        expectedResult = 0.010621925231790369;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #350 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #350 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #351 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html
        expectedResult = 0.019251938786813257;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #351 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #351 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #352 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html
        expectedResult = 0.02061463256425605;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #352 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #352 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #353 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html
        expectedResult = 0.02599473227761235;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #353 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #353 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #354 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #354 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #354 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #355 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html
        expectedResult = 0.00857993228898702;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #355 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #355 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #356 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html
        expectedResult = 0.013504549896513287;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #356 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #356 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #357 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html
        expectedResult = 0.008663416305833102;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #357 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #357 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #358 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html
        expectedResult = 0.03125397586653452;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #358 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #358 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #359 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html
        expectedResult = 0.032621236723860615;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #359 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #359 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #360 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html
        expectedResult = 0.023665801763748353;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #360 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #360 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #361 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html
        expectedResult = 0.025841431253021522;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #361 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #361 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #362 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html
        expectedResult = 0.016209426847818845;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #362 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #362 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #363 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html
        expectedResult = 0.017356765063779023;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #363 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #363 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #364 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html
        expectedResult = 0.008998293039588118;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #364 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #364 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #365 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #365 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #365 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #366 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html
        expectedResult = 0.025608998062327522;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #366 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #366 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #367 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html
        expectedResult = 0.024235084020792663;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #367 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #367 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #368 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html
        expectedResult = 0.01470449416422181;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #368 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #368 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #369 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html
        expectedResult = 0.011112376693859937;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #369 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #369 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #370 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html
        expectedResult = 0.02289470289552112;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #370 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #370 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #371 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html
        expectedResult = 0.01917239283963513;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #371 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #371 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #372 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html
        expectedResult = 0.018049615122291703;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #372 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #372 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #373 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html
        expectedResult = 0.019367354689976697;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #373 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #373 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #374 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html
        expectedResult = 0.012062507786792295;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #374 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #374 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #375 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html
        expectedResult = 0.018219413201997423;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #375 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #375 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #376 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #376 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #376 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #377 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html
        expectedResult = 0.005522371173218192;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #377 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #377 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #378 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html
        expectedResult = 0.027970579253494283;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #378 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #378 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #379 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html
        expectedResult = 0.016357873916117573;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #379 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #379 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #380 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html
        expectedResult = 0.013722915058748876;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #380 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #380 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #381 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html
        expectedResult = 0.005522371173218192;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #381 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #381 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #382 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html
        expectedResult = 0.005254605112843252;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #382 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #382 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #383 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html
        expectedResult = 0.02219929759527345;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #383 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #383 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #384 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html
        expectedResult = 0.020537041414998645;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #384 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #384 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #385 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html
        expectedResult = 0.021990697530011462;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #385 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #385 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #386 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html
        expectedResult = 0.011453127783354855;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #386 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #386 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #387 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #387 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #387 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #388 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html
        expectedResult = 0.016572954723677334;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #388 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #388 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #389 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html
        expectedResult = 0.037112565969823694;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #389 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #389 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #390 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html
        expectedResult = 0.010178411052630777;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #390 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #390 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #391 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html
        expectedResult = 0.012666983443762972;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #391 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #391 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #392 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html
        expectedResult = 0.01975462463394404;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #392 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #392 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #393 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html
        expectedResult = 0.012701337241782634;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #393 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #393 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #394 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html
        expectedResult = 0.030187058834792613;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #394 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #394 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #395 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html
        expectedResult = 0.00968909334530535;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #395 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #395 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #396 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html
        expectedResult = 0.02675390070069342;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #396 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #396 checking TFIDF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #397 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html
        expectedResult = 0.020717867619009078;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #397 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #397 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #398 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #398 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #398 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html");
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

//Test #401 checking TFIDF for orange in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #401 checking TFIDF for orange in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #401 checking TFIDF for orange in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #402 checking TFIDF for lime in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #402 checking TFIDF for lime in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #402 checking TFIDF for lime in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
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

//Test #404 checking TFIDF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #404 checking TFIDF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #404 checking TFIDF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #405 checking TFIDF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #405 checking TFIDF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #405 checking TFIDF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #406 checking TFIDF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #406 checking TFIDF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #406 checking TFIDF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #407 checking TFIDF for blueberry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #407 checking TFIDF for blueberry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #407 checking TFIDF for blueberry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
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
