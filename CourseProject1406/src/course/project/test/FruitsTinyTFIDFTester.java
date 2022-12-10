import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;

public class FruitsTinyTFIDFTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("FruitsTiny-TFIDF-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("FruitsTiny-TFIDF-passed.txt"));
        double expectedResult;
        double yourResult;
//Test #169 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.02445006963027565;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #169 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #169 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #170 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.03908124238104001;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #170 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #170 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #171 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.02445006963027565;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #171 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #171 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #172 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.07620758655640758;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #172 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #172 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #173 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.13476451852905313;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #173 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #173 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #174 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.05787647829766945;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #174 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #174 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #175 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.06979767743420133;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #175 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #175 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #176 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #176 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #176 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #177 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #177 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #177 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #178 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #178 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #178 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #179 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #179 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #179 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #180 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.05694192097566775;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #180 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #180 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #181 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.031595073081303486;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #181 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #181 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #182 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.03872609348667805;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #182 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #182 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #183 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.031595073081303486;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #183 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #183 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #184 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.04525008888053903;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #184 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #184 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #185 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.031595073081303486;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #185 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #185 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #186 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.07447019235682993;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #186 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #186 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #187 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #187 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #187 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #188 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #188 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #188 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #189 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.04525008888053903;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #189 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #189 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #190 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #190 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #190 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #191 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.02266030222847964;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #191 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #191 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #192 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #192 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #192 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #193 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.044266247441115764;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #193 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #193 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #194 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.03622045978643087;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #194 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #194 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #195 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #195 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #195 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #196 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.10375537569198201;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #196 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #196 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #197 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #197 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #197 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #198 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #198 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #198 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #199 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #199 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #199 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #200 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.14859721830091777;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #200 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #200 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #201 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #201 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #201 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #202 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.11672149491947882;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #202 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #202 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #203 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.0991299889868547;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #203 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #203 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #204 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #204 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #204 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #205 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #205 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #205 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #206 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #206 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #206 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #207 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.0991299889868547;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #207 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #207 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #208 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.06201786293142292;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #208 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #208 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #209 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #209 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #209 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #210 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #210 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #210 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #211 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #211 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #211 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #212 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #212 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #212 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #213 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.0404119177187868;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #213 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #213 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #214 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.12401630243933787;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #214 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #214 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #215 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #215 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #215 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #216 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #216 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #216 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #217 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #217 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #217 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #218 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.06459482428200948;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #218 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #218 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #219 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.07758727832568058;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #219 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #219 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #220 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #220 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #220 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #221 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #221 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #221 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #222 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #222 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #222 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #223 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #223 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #223 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #224 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #224 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #224 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #225 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #225 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #225 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #226 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #226 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #226 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #227 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #227 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #227 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #228 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #228 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #228 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #229 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #229 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #229 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #230 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #230 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #230 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #231 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #231 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #231 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #232 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #232 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #232 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #233 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #233 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #233 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #234 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #234 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #234 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #235 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #235 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #235 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #236 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #236 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #236 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #237 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.02815674585715757;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #237 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #237 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #238 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.045006031726892604;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #238 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #238 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #239 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.18271404725510207;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #239 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #239 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #240 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #240 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #240 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #241 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.02815674585715757;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #241 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #241 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #242 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #242 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #242 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #243 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #243 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #243 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #244 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.18271404725510207;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #244 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #244 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #245 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #245 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #245 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #246 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.02815674585715757;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #246 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #246 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #247 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #247 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #247 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #248 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.02815674585715757;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #248 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #248 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #249 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.045006031726892604;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #249 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #249 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #250 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.06445710476952095;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #250 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #250 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #251 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #251 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #251 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #252 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #252 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #252 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #253 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #253 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #253 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #254 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #254 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #254 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #255 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.06445710476952095;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #255 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #255 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #256 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #256 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #256 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #257 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.014291714269269087;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #257 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #257 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #258 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.045006031726892604;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #258 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #258 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #259 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.014291714269269087;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #259 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #259 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #260 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #260 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #260 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #261 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.06445710476952095;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #261 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #261 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #262 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.1656555612092295;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #262 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #262 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #263 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.054703631988055924;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #263 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #263 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #264 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #264 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #264 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #265 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #265 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #265 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #266 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.06445710476952095;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #266 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #266 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #267 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #267 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #267 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #268 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #268 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #268 checking TFIDF for coconut in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #269 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.13535044877328553;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #269 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #269 checking TFIDF for papaya in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #270 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.10978936524490102;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #270 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #270 checking TFIDF for lime in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #271 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.04791160163801364;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #271 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #271 checking TFIDF for peach in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #272 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #272 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #272 checking TFIDF for pear in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #273 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #273 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #273 checking TFIDF for cherry in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #274 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.02997453317184664;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #274 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #274 checking TFIDF for apple in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #275 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #275 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #275 checking TFIDF for apricot in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #276 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #276 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #276 checking TFIDF for banana in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #277 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #277 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #277 checking TFIDF for fig in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #278 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #278 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #278 checking TFIDF for tomato in https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #279 checking TFIDF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #279 checking TFIDF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #279 checking TFIDF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #280 checking TFIDF for papaya in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #280 checking TFIDF for papaya in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #280 checking TFIDF for papaya in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #281 checking TFIDF for lime in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #281 checking TFIDF for lime in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #281 checking TFIDF for lime in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #282 checking TFIDF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #282 checking TFIDF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #282 checking TFIDF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #283 checking TFIDF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #283 checking TFIDF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #283 checking TFIDF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #284 checking TFIDF for cherry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #284 checking TFIDF for cherry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #284 checking TFIDF for cherry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #285 checking TFIDF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #285 checking TFIDF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #285 checking TFIDF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #286 checking TFIDF for apricot in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #286 checking TFIDF for apricot in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #286 checking TFIDF for apricot in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #287 checking TFIDF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #287 checking TFIDF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #287 checking TFIDF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #288 checking TFIDF for fig in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #288 checking TFIDF for fig in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #288 checking TFIDF for fig in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #289 checking TFIDF for tomato in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTFIDF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #289 checking TFIDF for tomato in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #289 checking TFIDF for tomato in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

        failOut.close();
        passOut.close();
    }
}
