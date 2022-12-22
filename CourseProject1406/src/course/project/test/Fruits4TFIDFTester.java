import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;

public class Fruits4TFIDFTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits4-TFIDF-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits4-TFIDF-passed.txt"));
        double expectedResult;
        double yourResult;
//Test #289 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html
        expectedResult = 0.02025256410716449;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #289 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #289 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #290 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html
        expectedResult = 0.014217910699412391;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #290 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #290 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #291 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html
        expectedResult = 0.005062029914333525;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #291 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #291 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #292 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html
        expectedResult = 0.023233281765029874;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #292 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #292 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #293 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html
        expectedResult = 0.021408499095574744;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #293 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #293 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #294 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html
        expectedResult = 0.009390593368558851;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #294 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #294 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #295 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html
        expectedResult = 0.03811160860327052;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #295 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #295 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #296 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html
        expectedResult = 0.01779036043488439;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #296 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #296 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #297 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html
        expectedResult = 0.008799382626291262;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #297 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #297 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #298 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html
        expectedResult = 0.020637005662867348;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #298 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #298 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #299 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #299 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #299 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #300 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html
        expectedResult = 0.010673558250150036;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #300 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #300 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #301 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html
        expectedResult = 0.010370498201111137;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #301 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #301 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #302 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html
        expectedResult = 0.023364510303940655;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #302 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #302 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #303 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html
        expectedResult = 0.024453712421857454;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #303 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #303 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #304 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html
        expectedResult = 0.01854276773439614;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #304 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #304 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #305 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html
        expectedResult = 0.01854276773439614;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #305 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #305 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #306 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html
        expectedResult = 0.014803166403464307;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #306 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #306 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #307 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html
        expectedResult = 0.028020565084247783;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #307 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #307 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #308 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html
        expectedResult = 0.017375356576688834;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #308 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #308 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #309 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html
        expectedResult = 0.017874546040411894;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #309 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #309 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #310 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #310 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #310 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #311 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html
        expectedResult = 0.01705727094203789;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #311 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #311 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #312 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #312 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #312 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #313 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html
        expectedResult = 0.02805014865308157;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #313 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #313 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #314 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html
        expectedResult = 0.048456986672874264;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #314 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #314 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #315 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html
        expectedResult = 0.01803083143464337;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #315 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #315 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #316 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #316 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #316 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #317 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #317 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #317 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #318 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html
        expectedResult = 0.04891283591008144;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #318 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #318 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #319 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html
        expectedResult = 0.0168956506406513;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #319 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #319 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #320 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #320 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #320 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #321 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #321 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #321 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #322 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html
        expectedResult = 0.01246813932530466;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #322 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #322 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #323 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html
        expectedResult = 0.019863589283763146;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #323 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #323 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #324 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html
        expectedResult = 0.017370558909364963;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #324 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #324 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #325 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html
        expectedResult = 0.01258641000195803;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #325 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #325 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #326 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html
        expectedResult = 0.025726663074829;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #326 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #326 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #327 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html
        expectedResult = 0.013179770623456925;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #327 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #327 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #328 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html
        expectedResult = 0.025494492949089675;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #328 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #328 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #329 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html
        expectedResult = 0.012704814091698532;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #329 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #329 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #330 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html
        expectedResult = 0.01633203749879458;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #330 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #330 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #331 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html
        expectedResult = 0.028705455643450558;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #331 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #331 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #332 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #332 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #332 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #333 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html
        expectedResult = 0.023563761377350296;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #333 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #333 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #334 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html
        expectedResult = 0.01172001055056407;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #334 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #334 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #335 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #335 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #335 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #336 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #336 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #336 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #337 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html
        expectedResult = 0.02490868620220216;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #337 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #337 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #338 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html
        expectedResult = 0.012750987266474166;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #338 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #338 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #339 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #339 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #339 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #340 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html
        expectedResult = 0.03520958633990325;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #340 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #340 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #341 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #341 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #341 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #342 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #342 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #342 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #343 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #343 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #343 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-683.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #344 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html
        expectedResult = 0.017400410993323703;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #344 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #344 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #345 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html
        expectedResult = 0.012196150580407399;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #345 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #345 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #346 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html
        expectedResult = 0.01882429534332318;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #346 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #346 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #347 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html
        expectedResult = 0.015130545916208906;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #347 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #347 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #348 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html
        expectedResult = 0.030781818701117535;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #348 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #348 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #349 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html
        expectedResult = 0.023419546005326836;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #349 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #349 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #350 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html
        expectedResult = 0.018227563994177097;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #350 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #350 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #351 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html
        expectedResult = 0.02257558091186388;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #351 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #351 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #352 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html
        expectedResult = 0.021945103801947294;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #352 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #352 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #353 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html
        expectedResult = 0.01028409820442975;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #353 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #353 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #354 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #354 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #354 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #355 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #355 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #355 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #356 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #356 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #356 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #357 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #357 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #357 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #358 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #358 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #358 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #359 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #359 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #359 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #360 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html
        expectedResult = 0.05831709382084734;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #360 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #360 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #361 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html
        expectedResult = 0.05779081153675332;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #361 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #361 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #362 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #362 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #362 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #363 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #363 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #363 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #364 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html
        expectedResult = 0.10214696854621055;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #364 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #364 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #365 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #365 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #365 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #366 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html
        expectedResult = 0.020193452961093577;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #366 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #366 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #367 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html
        expectedResult = 0.017253444035438038;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #367 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #367 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #368 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html
        expectedResult = 0.019207042020118525;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #368 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #368 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #369 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html
        expectedResult = 0.02281992712091888;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #369 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #369 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #370 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html
        expectedResult = 0.01354413930911738;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #370 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #370 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #371 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html
        expectedResult = 0.016170728226645063;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #371 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #371 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #372 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html
        expectedResult = 0.02368007918447645;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #372 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #372 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #373 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html
        expectedResult = 0.015587987205275117;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #373 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #373 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #374 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html
        expectedResult = 0.024757408047701716;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #374 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #374 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #375 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html
        expectedResult = 0.007914538499910733;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #375 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #375 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #376 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #376 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #376 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #377 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #377 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #377 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #378 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #378 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #378 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #379 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html
        expectedResult = 0.020021244885693453;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #379 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #379 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #380 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html
        expectedResult = 0.045503371467428756;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #380 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #380 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #381 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html
        expectedResult = 0.02490868620220216;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #381 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #381 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #382 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #382 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #382 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #383 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html
        expectedResult = 0.02468389790413389;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #383 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #383 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #384 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html
        expectedResult = 0.045931435170890406;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #384 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #384 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #385 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #385 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #385 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #386 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html
        expectedResult = 0.02401105728685515;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #386 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #386 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #387 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #387 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #387 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #388 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html
        expectedResult = 0.009449520925226409;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #388 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #388 checking TFIDF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #389 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html
        expectedResult = 0.01802439458618298;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #389 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #389 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #390 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html
        expectedResult = 0.018277964537757777;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #390 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #390 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #391 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html
        expectedResult = 0.030474094601908325;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #391 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #391 checking TFIDF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #392 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html
        expectedResult = 0.009988861613318339;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #392 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #392 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #393 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html
        expectedResult = 0.016442112879750222;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #393 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #393 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #394 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html
        expectedResult = 0.016293731124852256;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #394 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #394 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #395 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html
        expectedResult = 0.009628895176601109;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #395 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #395 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #396 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html
        expectedResult = 0.024206336876701724;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #396 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #396 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #397 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html
        expectedResult = 0.021920377884035263;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #397 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #397 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #398 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #398 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #398 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #399 checking TFIDF for orange in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #399 checking TFIDF for orange in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #399 checking TFIDF for orange in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #400 checking TFIDF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #400 checking TFIDF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #400 checking TFIDF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #401 checking TFIDF for apricot in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #401 checking TFIDF for apricot in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #401 checking TFIDF for apricot in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #402 checking TFIDF for kiwi in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #402 checking TFIDF for kiwi in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #402 checking TFIDF for kiwi in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #403 checking TFIDF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #403 checking TFIDF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #403 checking TFIDF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
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

//Test #405 checking TFIDF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #405 checking TFIDF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #405 checking TFIDF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #406 checking TFIDF for fig in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #406 checking TFIDF for fig in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #406 checking TFIDF for fig in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #407 checking TFIDF for papaya in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #407 checking TFIDF for papaya in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #407 checking TFIDF for papaya in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
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
