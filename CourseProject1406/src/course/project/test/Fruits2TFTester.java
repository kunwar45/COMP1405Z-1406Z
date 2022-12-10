import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;

public class Fruits2TFTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits2-TF-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits2-TF-passed.txt"));
        double expectedResult;
        double yourResult;
//Test #160 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html
        expectedResult = 0.14;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #160 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #160 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #161 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html
        expectedResult = 0.22;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #161 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #161 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #162 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html
        expectedResult = 0.16;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #162 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #162 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #163 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html
        expectedResult = 0.16;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #163 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #163 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #164 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html
        expectedResult = 0.32;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #164 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #164 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #165 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #165 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #165 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #166 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html
        expectedResult = 0.15384615384615385;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #166 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #166 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #167 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html
        expectedResult = 0.23076923076923078;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #167 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #167 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #168 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html
        expectedResult = 0.34615384615384615;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #168 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #168 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #169 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html
        expectedResult = 0.15384615384615385;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #169 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #169 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #170 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html
        expectedResult = 0.11538461538461539;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #170 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #170 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #171 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #171 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #171 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #172 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html
        expectedResult = 0.21176470588235294;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #172 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #172 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #173 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html
        expectedResult = 0.17647058823529413;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #173 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #173 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #174 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html
        expectedResult = 0.21176470588235294;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #174 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #174 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #175 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html
        expectedResult = 0.17647058823529413;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #175 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #175 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #176 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html
        expectedResult = 0.2235294117647059;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #176 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #176 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #177 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #177 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #177 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #178 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html
        expectedResult = 0.3333333333333333;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #178 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #178 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #179 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html
        expectedResult = 0.3333333333333333;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #179 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #179 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #180 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #180 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #180 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #181 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #181 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #181 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #182 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html
        expectedResult = 0.3333333333333333;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #182 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #182 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #183 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #183 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #183 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #184 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html
        expectedResult = 0.23076923076923078;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #184 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #184 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #185 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html
        expectedResult = 0.15384615384615385;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #185 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #185 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #186 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html
        expectedResult = 0.2;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #186 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #186 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #187 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html
        expectedResult = 0.16923076923076924;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #187 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #187 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #188 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html
        expectedResult = 0.24615384615384617;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #188 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #188 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #189 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #189 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #189 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-604.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #190 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html
        expectedResult = 0.2;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #190 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #190 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #191 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html
        expectedResult = 0.4;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #191 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #191 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #192 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html
        expectedResult = 0.2;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #192 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #192 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #193 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html
        expectedResult = 0.2;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #193 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #193 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #194 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #194 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #194 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #195 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #195 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #195 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #196 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html
        expectedResult = 0.22988505747126436;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #196 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #196 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #197 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html
        expectedResult = 0.19540229885057472;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #197 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #197 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #198 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html
        expectedResult = 0.21839080459770116;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #198 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #198 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #199 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html
        expectedResult = 0.20689655172413793;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #199 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #199 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #200 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html
        expectedResult = 0.14942528735632185;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #200 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #200 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #201 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #201 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #201 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-247.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #202 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html
        expectedResult = 0.22448979591836735;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #202 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #202 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #203 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html
        expectedResult = 0.20408163265306123;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #203 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #203 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #204 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html
        expectedResult = 0.12244897959183673;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #204 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #204 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #205 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html
        expectedResult = 0.30612244897959184;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #205 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #205 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #206 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html
        expectedResult = 0.14285714285714285;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #206 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #206 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #207 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #207 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #207 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-612.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #208 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html
        expectedResult = 0.26666666666666666;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #208 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #208 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #209 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html
        expectedResult = 0.24444444444444444;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #209 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #209 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #210 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html
        expectedResult = 0.1111111111111111;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #210 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #210 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #211 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html
        expectedResult = 0.2222222222222222;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #211 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #211 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #212 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html
        expectedResult = 0.15555555555555556;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #212 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #212 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #213 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #213 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #213 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #214 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html
        expectedResult = 0.16666666666666666;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #214 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #214 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #215 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html
        expectedResult = 0.16666666666666666;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #215 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #215 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #216 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html
        expectedResult = 0.16666666666666666;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #216 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #216 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #217 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html
        expectedResult = 0.1111111111111111;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #217 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #217 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #218 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html
        expectedResult = 0.3888888888888889;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #218 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #218 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #219 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #219 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #219 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #220 checking TF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #220 checking TF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #220 checking TF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #221 checking TF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #221 checking TF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #221 checking TF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #222 checking TF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #222 checking TF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #222 checking TF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #223 checking TF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #223 checking TF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #223 checking TF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #224 checking TF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #224 checking TF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #224 checking TF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #225 checking TF for tomato in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #225 checking TF for tomato in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #225 checking TF for tomato in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

        failOut.close();
        passOut.close();
    }
}
