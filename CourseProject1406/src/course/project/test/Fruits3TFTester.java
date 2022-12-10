import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;

public class Fruits3TFTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits3-TF-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits3-TF-passed.txt"));
        double expectedResult;
        double yourResult;
//Test #168 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html
        expectedResult = 0.11320754716981132;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #168 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #168 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #169 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html
        expectedResult = 0.07547169811320754;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #169 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #169 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #170 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html
        expectedResult = 0.018867924528301886;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #170 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #170 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #171 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html
        expectedResult = 0.09433962264150944;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #171 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #171 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #172 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html
        expectedResult = 0.09433962264150944;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #172 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #172 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #173 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html
        expectedResult = 0.1509433962264151;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #173 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #173 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #174 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html
        expectedResult = 0.09433962264150944;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #174 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #174 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #175 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html
        expectedResult = 0.09433962264150944;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #175 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #175 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #176 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html
        expectedResult = 0.05660377358490566;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #176 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #176 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #177 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html
        expectedResult = 0.05660377358490566;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #177 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #177 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #178 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #178 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #178 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #179 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html
        expectedResult = 0.10638297872340426;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #179 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #179 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #180 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html
        expectedResult = 0.05319148936170213;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #180 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #180 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #181 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html
        expectedResult = 0.07446808510638298;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #181 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #181 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #182 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html
        expectedResult = 0.09574468085106383;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #182 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #182 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #183 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html
        expectedResult = 0.07446808510638298;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #183 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #183 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #184 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html
        expectedResult = 0.06382978723404255;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #184 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #184 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #185 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html
        expectedResult = 0.11702127659574468;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #185 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #185 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #186 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html
        expectedResult = 0.0851063829787234;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #186 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #186 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #187 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html
        expectedResult = 0.07446808510638298;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #187 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #187 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #188 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html
        expectedResult = 0.0425531914893617;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #188 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #188 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #189 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #189 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #189 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #190 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #190 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #190 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #191 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #191 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #191 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #192 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html
        expectedResult = 0.2222222222222222;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #192 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #192 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #193 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html
        expectedResult = 0.1111111111111111;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #193 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #193 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #194 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html
        expectedResult = 0.1111111111111111;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #194 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #194 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #195 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #195 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #195 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #196 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html
        expectedResult = 0.2222222222222222;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #196 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #196 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #197 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #197 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #197 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #198 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html
        expectedResult = 0.2222222222222222;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #198 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #198 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #199 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #199 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #199 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #200 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #200 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #200 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #201 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html
        expectedResult = 0.1;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #201 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #201 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #202 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html
        expectedResult = 0.2;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #202 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #202 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #203 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #203 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #203 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #204 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html
        expectedResult = 0.1;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #204 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #204 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #205 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html
        expectedResult = 0.15;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #205 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #205 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #206 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #206 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #206 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #207 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html
        expectedResult = 0.1;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #207 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #207 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #208 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html
        expectedResult = 0.15;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #208 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #208 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #209 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html
        expectedResult = 0.1;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #209 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #209 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #210 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html
        expectedResult = 0.05;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #210 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #210 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #211 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #211 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #211 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-397.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #212 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #212 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #212 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #213 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html
        expectedResult = 0.08333333333333333;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #213 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #213 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #214 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html
        expectedResult = 0.041666666666666664;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #214 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #214 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #215 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html
        expectedResult = 0.08333333333333333;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #215 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #215 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #216 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html
        expectedResult = 0.08333333333333333;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #216 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #216 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #217 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html
        expectedResult = 0.08333333333333333;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #217 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #217 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #218 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #218 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #218 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #219 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html
        expectedResult = 0.08333333333333333;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #219 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #219 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #220 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html
        expectedResult = 0.10416666666666667;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #220 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #220 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #221 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #221 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #221 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #222 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #222 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #222 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #223 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html
        expectedResult = 0.1111111111111111;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #223 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #223 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #224 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html
        expectedResult = 0.13333333333333333;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #224 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #224 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #225 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html
        expectedResult = 0.05555555555555555;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #225 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #225 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #226 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html
        expectedResult = 0.13333333333333333;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #226 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #226 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #227 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #227 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #227 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #228 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html
        expectedResult = 0.1111111111111111;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #228 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #228 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #229 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html
        expectedResult = 0.07777777777777778;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #229 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #229 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #230 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html
        expectedResult = 0.03333333333333333;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #230 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #230 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #231 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html
        expectedResult = 0.08888888888888889;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #231 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #231 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #232 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html
        expectedResult = 0.06666666666666667;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #232 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #232 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #233 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #233 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #233 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #234 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html
        expectedResult = 0.07777777777777778;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #234 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #234 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #235 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html
        expectedResult = 0.07777777777777778;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #235 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #235 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #236 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html
        expectedResult = 0.05555555555555555;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #236 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #236 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #237 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html
        expectedResult = 0.05555555555555555;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #237 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #237 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #238 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html
        expectedResult = 0.07777777777777778;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #238 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #238 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #239 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html
        expectedResult = 0.06666666666666667;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #239 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #239 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #240 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html
        expectedResult = 0.044444444444444446;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #240 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #240 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #241 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html
        expectedResult = 0.1;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #241 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #241 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #242 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html
        expectedResult = 0.06666666666666667;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #242 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #242 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #243 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html
        expectedResult = 0.08888888888888889;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #243 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #243 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #244 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #244 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #244 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #245 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html
        expectedResult = 0.05;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #245 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #245 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #246 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html
        expectedResult = 0.05;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #246 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #246 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #247 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html
        expectedResult = 0.11666666666666667;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #247 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #247 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #248 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html
        expectedResult = 0.03333333333333333;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #248 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #248 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #249 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html
        expectedResult = 0.05;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #249 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #249 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #250 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html
        expectedResult = 0.03333333333333333;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #250 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #250 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #251 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html
        expectedResult = 0.03333333333333333;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #251 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #251 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #252 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html
        expectedResult = 0.08333333333333333;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #252 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #252 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #253 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html
        expectedResult = 0.2;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #253 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #253 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #254 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html
        expectedResult = 0.03333333333333333;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #254 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #254 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #255 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #255 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #255 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #256 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html
        expectedResult = 0.05;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #256 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #256 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #257 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html
        expectedResult = 0.05;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #257 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #257 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #258 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html
        expectedResult = 0.1;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #258 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #258 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #259 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #259 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #259 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #260 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #260 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #260 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #261 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #261 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #261 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #262 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #262 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #262 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #263 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html
        expectedResult = 0.1125;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #263 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #263 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #264 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html
        expectedResult = 0.0875;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #264 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #264 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #265 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html
        expectedResult = 0.0875;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #265 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #265 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #266 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #266 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #266 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #267 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html
        expectedResult = 0.12727272727272726;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #267 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #267 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #268 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html
        expectedResult = 0.05454545454545454;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #268 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #268 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #269 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html
        expectedResult = 0.05454545454545454;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #269 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #269 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #270 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html
        expectedResult = 0.07272727272727272;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #270 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #270 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #271 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html
        expectedResult = 0.03636363636363636;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #271 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #271 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #272 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html
        expectedResult = 0.05454545454545454;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #272 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #272 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #273 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html
        expectedResult = 0.05454545454545454;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #273 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #273 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #274 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html
        expectedResult = 0.01818181818181818;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #274 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #274 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #275 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html
        expectedResult = 0.10909090909090909;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #275 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #275 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #276 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html
        expectedResult = 0.07272727272727272;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #276 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #276 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #277 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #277 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #277 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #278 checking TF for orange in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #278 checking TF for orange in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #278 checking TF for orange in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #279 checking TF for cherry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #279 checking TF for cherry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #279 checking TF for cherry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #280 checking TF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #280 checking TF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #280 checking TF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #281 checking TF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #281 checking TF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #281 checking TF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #282 checking TF for lime in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #282 checking TF for lime in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #282 checking TF for lime in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #283 checking TF for papaya in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #283 checking TF for papaya in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #283 checking TF for papaya in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #284 checking TF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #284 checking TF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #284 checking TF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #285 checking TF for apricot in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #285 checking TF for apricot in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #285 checking TF for apricot in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #286 checking TF for fig in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #286 checking TF for fig in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #286 checking TF for fig in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #287 checking TF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #287 checking TF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #287 checking TF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #288 checking TF for tomato in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #288 checking TF for tomato in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #288 checking TF for tomato in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

        failOut.close();
        passOut.close();
    }
}
