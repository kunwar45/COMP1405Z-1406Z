import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;

public class Fruits1TFIDFTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits1-TFIDF-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits1-TFIDF-passed.txt"));
        double expectedResult;
        double yourResult;
//Test #226 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html
        expectedResult = 0.017531505668940222;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #226 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #226 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #227 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html
        expectedResult = 0.017510408491368753;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #227 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #227 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #228 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html
        expectedResult = 0.014974147360882971;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #228 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #228 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #229 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html
        expectedResult = 0.014772941820122995;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #229 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #229 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #230 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html
        expectedResult = 0.013431897262154007;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #230 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #230 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #231 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #231 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #231 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #232 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html
        expectedResult = 0.024443089428098932;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #232 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #232 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #233 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html
        expectedResult = 0.01209643459154539;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #233 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #233 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #234 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html
        expectedResult = 0.02286107235814336;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #234 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #234 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #235 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html
        expectedResult = 0.0031423938279027314;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #235 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #235 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #236 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html
        expectedResult = 0.013431897262154007;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #236 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #236 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #237 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #237 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #237 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #238 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html
        expectedResult = 0.013751095126240882;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #238 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #238 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #239 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html
        expectedResult = 0.012700064467134224;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #239 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #239 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #240 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html
        expectedResult = 0.01991331199073529;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #240 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #240 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #241 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html
        expectedResult = 0.017688282224048817;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #241 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #241 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #242 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html
        expectedResult = 0.015098006451852832;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #242 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #242 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #243 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #243 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #243 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-373.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #244 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html
        expectedResult = 0.025683485663960757;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #244 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #244 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #245 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html
        expectedResult = 0.004485306293467019;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #245 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #245 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #246 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html
        expectedResult = 0.009691629679431265;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #246 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #246 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #247 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html
        expectedResult = 0.020250685564972566;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #247 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #247 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #248 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html
        expectedResult = 0.018412387411313316;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #248 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #248 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #249 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #249 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #249 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #250 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html
        expectedResult = 0.010249233356530914;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #250 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #250 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #251 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html
        expectedResult = 0.02553638288129748;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #251 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #251 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #252 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html
        expectedResult = 0.0064573874691361815;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #252 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #252 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #253 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html
        expectedResult = 0.015820323014296082;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #253 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #253 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #254 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html
        expectedResult = 0.018092626113654836;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #254 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #254 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #255 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #255 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #255 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #256 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html
        expectedResult = 0.01512245146893712;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #256 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #256 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #257 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html
        expectedResult = 0.015654228724059967;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #257 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #257 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #258 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html
        expectedResult = 0.01550853656731848;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #258 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #258 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #259 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html
        expectedResult = 0.021135589593309995;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #259 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #259 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #260 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html
        expectedResult = 0.01163523864451864;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #260 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #260 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #261 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #261 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #261 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #262 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html
        expectedResult = 0.017531505668940222;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #262 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #262 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #263 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html
        expectedResult = 0.02133904570690138;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #263 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #263 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #264 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html
        expectedResult = 0.0069745097930178105;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #264 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #264 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #265 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html
        expectedResult = 0.014772941820122995;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #265 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #265 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #266 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html
        expectedResult = 0.01648957435463622;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #266 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #266 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #267 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #267 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #267 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #268 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html
        expectedResult = 0.020699504499228808;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #268 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #268 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #269 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html
        expectedResult = 0.010139437984053819;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #269 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #269 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #270 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html
        expectedResult = 0.013860079233488138;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #270 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #270 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #271 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html
        expectedResult = 0.01802187754377961;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #271 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #271 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #272 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html
        expectedResult = 0.0163859040796759;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #272 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #272 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #273 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #273 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #273 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #274 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html
        expectedResult = 0.014992732919867082;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #274 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #274 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #275 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html
        expectedResult = 0.014992390416066542;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #275 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #275 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #276 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html
        expectedResult = 0.01790133107342916;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #276 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #276 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #277 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html
        expectedResult = 0.014049659704981128;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #277 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #277 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #278 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html
        expectedResult = 0.0166475705100292;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #278 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #278 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #279 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #279 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #279 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #280 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html
        expectedResult = 0.018238462596626374;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #280 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #280 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #281 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html
        expectedResult = 0.01130298499144897;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #281 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #281 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #282 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html
        expectedResult = 0.015681780201008605;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #282 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #282 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #283 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html
        expectedResult = 0.01380393027455428;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #283 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #283 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #284 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html
        expectedResult = 0.01968868641345509;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #284 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #284 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #285 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #285 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #285 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #286 checking TFIDF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #286 checking TFIDF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #286 checking TFIDF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #287 checking TFIDF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #287 checking TFIDF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #287 checking TFIDF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
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

//Test #289 checking TFIDF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #289 checking TFIDF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #289 checking TFIDF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #290 checking TFIDF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #290 checking TFIDF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #290 checking TFIDF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
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
