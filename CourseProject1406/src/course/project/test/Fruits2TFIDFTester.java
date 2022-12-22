import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;

public class Fruits2TFIDFTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits2-TFIDF-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits2-TFIDF-passed.txt"));
        double expectedResult;
        double yourResult;
//Test #226 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html
        expectedResult = 0.014814953377474498;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #226 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #226 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #227 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html
        expectedResult = 0.0182606477551756;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #227 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #227 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #228 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html
        expectedResult = 0.01522328839807838;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #228 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #228 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #229 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html
        expectedResult = 0.010739693078853689;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #229 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #229 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #230 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html
        expectedResult = 0.01190488385409745;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #230 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #230 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #231 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #231 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #231 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #232 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html
        expectedResult = 0.013748527125785285;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #232 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #232 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #233 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html
        expectedResult = 0.020219183274955924;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #233 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #233 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #234 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html
        expectedResult = 0.017352409869448283;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #234 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #234 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #235 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html
        expectedResult = 0.008909097490936069;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #235 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #235 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #236 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html
        expectedResult = 0.010594786788472388;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #236 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #236 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #237 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #237 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #237 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #238 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html
        expectedResult = 0.0018464733541746505;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #238 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #238 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #239 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html
        expectedResult = 0.01926081640007922;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #239 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #239 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #240 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html
        expectedResult = 0.010189951463465836;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #240 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #240 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #241 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html
        expectedResult = 0.022645057814895477;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #241 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #241 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #242 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html
        expectedResult = 0.01481629394112972;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #242 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #242 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #243 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #243 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #243 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #244 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html
        expectedResult = 0.008977951515803797;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #244 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #244 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #245 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html
        expectedResult = 0.017972652094802942;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #245 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #245 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #246 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html
        expectedResult = 0.014680145323764436;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #246 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #246 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #247 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html
        expectedResult = 0.021332575721409498;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #247 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #247 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #248 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html
        expectedResult = 0.006639949534464946;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #248 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #248 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #249 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #249 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #249 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #250 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html
        expectedResult = 0.01084086385545448;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #250 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #250 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #251 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html
        expectedResult = 0.020295813237741787;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #251 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #251 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #252 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html
        expectedResult = 0.015313437587287848;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #252 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #252 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #253 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html
        expectedResult = 0.011430781980593952;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #253 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #253 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #254 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html
        expectedResult = 0.012965212933132814;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #254 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #254 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #255 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #255 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #255 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #256 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html
        expectedResult = 0.00938088691656765;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #256 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #256 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #257 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html
        expectedResult = 0.015532915514235366;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #257 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #257 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #258 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html
        expectedResult = 0.015313437587287848;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #258 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #258 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #259 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html
        expectedResult = 0.013911056751070329;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #259 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #259 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #260 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html
        expectedResult = 0.016298112923978706;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #260 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #260 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #261 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #261 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #261 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #262 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html
        expectedResult = 0.012954055115744;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #262 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #262 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #263 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html
        expectedResult = 0.013668383588816477;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #263 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #263 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #264 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html
        expectedResult = 0.012597447017525647;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #264 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #264 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #265 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html
        expectedResult = 0.013835964792828196;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #265 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #265 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #266 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html
        expectedResult = 0.01741870985606104;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #266 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #266 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #267 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #267 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #267 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #268 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html
        expectedResult = 0.016825063550925296;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #268 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #268 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #269 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html
        expectedResult = 0.014795442247750068;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #269 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #269 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #270 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html
        expectedResult = 0.009355940104227141;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #270 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #270 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #271 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html
        expectedResult = 0.01458671793977727;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #271 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #271 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #272 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html
        expectedResult = 0.01501121430200124;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #272 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #272 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #273 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #273 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #273 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #274 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html
        expectedResult = 0.010478408260090461;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #274 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #274 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #275 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html
        expectedResult = 0.011056221563012366;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #275 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #275 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #276 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html
        expectedResult = 0.010189951463465836;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #276 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #276 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #277 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html
        expectedResult = 0.018635794804640688;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #277 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #277 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #278 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html
        expectedResult = 0.019178125652085806;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #278 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #278 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #279 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #279 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #279 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #280 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html
        expectedResult = 0.020232236146893463;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #280 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #280 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #281 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html
        expectedResult = 0.009209334532466874;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #281 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #281 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #282 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html
        expectedResult = 0.008487770560839684;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #282 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #282 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #283 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html
        expectedResult = 0.012051315329198346;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #283 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #283 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #284 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html
        expectedResult = 0.01967526929824393;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #284 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #284 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #285 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #285 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #285 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #286 checking TFIDF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #286 checking TFIDF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #286 checking TFIDF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #287 checking TFIDF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #287 checking TFIDF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #287 checking TFIDF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #288 checking TFIDF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #288 checking TFIDF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #288 checking TFIDF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #289 checking TFIDF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #289 checking TFIDF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #289 checking TFIDF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #290 checking TFIDF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #290 checking TFIDF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #290 checking TFIDF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #291 checking TFIDF for tomato in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #291 checking TFIDF for tomato in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #291 checking TFIDF for tomato in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

        failOut.close();
        passOut.close();
    }
}
