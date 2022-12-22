import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;

public class Fruits1TFTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits1-TF-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits1-TF-passed.txt"));
        double expectedResult;
        double yourResult;
//Test #160 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html
        expectedResult = 0.2857142857142857;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #160 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #160 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #161 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html
        expectedResult = 0.25;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #161 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #161 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #162 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html
        expectedResult = 0.10714285714285714;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #162 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #162 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #163 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html
        expectedResult = 0.17857142857142858;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #163 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #163 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #164 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html
        expectedResult = 0.17857142857142858;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #164 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #164 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #165 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #165 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #165 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #166 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html
        expectedResult = 0.24242424242424243;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #166 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #166 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #167 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html
        expectedResult = 0.16666666666666666;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #167 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #167 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #168 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html
        expectedResult = 0.25757575757575757;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #168 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #168 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #169 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html
        expectedResult = 0.16666666666666666;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #169 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #169 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #170 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html
        expectedResult = 0.16666666666666666;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #170 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #170 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #171 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #171 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #171 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-280.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #172 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html
        expectedResult = 0.14864864864864866;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #172 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #172 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #173 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html
        expectedResult = 0.2702702702702703;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #173 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #173 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #174 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html
        expectedResult = 0.2972972972972973;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #174 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #174 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #175 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html
        expectedResult = 0.12162162162162163;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #175 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #175 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #176 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html
        expectedResult = 0.16216216216216217;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #176 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #176 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #177 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #177 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #177 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #178 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html
        expectedResult = 0.23809523809523808;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #178 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #178 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #179 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html
        expectedResult = 0.19047619047619047;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #179 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #179 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #180 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html
        expectedResult = 0.20238095238095238;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #180 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #180 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #181 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html
        expectedResult = 0.23809523809523808;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #181 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #181 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #182 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html
        expectedResult = 0.13095238095238096;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #182 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #182 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #183 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #183 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #183 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #184 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html
        expectedResult = 0.23809523809523808;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #184 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #184 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #185 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html
        expectedResult = 0.2619047619047619;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #185 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #185 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #186 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html
        expectedResult = 0.14285714285714285;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #186 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #186 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #187 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html
        expectedResult = 0.2261904761904762;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #187 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #187 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #188 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html
        expectedResult = 0.13095238095238096;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #188 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #188 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #189 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #189 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #189 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #190 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html
        expectedResult = 0.17647058823529413;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #190 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #190 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #191 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html
        expectedResult = 0.29411764705882354;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #191 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #191 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #192 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html
        expectedResult = 0.11764705882352941;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #192 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #192 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #193 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html
        expectedResult = 0.2647058823529412;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #193 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #193 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #194 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html
        expectedResult = 0.14705882352941177;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #194 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #194 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #195 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #195 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #195 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #196 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html
        expectedResult = 0.2972972972972973;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #196 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #196 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #197 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html
        expectedResult = 0.10810810810810811;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #197 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #197 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #198 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html
        expectedResult = 0.1891891891891892;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #198 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #198 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #199 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html
        expectedResult = 0.24324324324324326;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #199 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #199 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #200 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html
        expectedResult = 0.16216216216216217;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #200 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #200 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #201 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #201 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #201 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #202 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html
        expectedResult = 0.07142857142857142;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #202 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #202 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #203 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html
        expectedResult = 0.07142857142857142;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #203 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #203 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #204 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html
        expectedResult = 0.14285714285714285;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #204 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #204 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #205 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html
        expectedResult = 0.35714285714285715;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #205 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #205 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #206 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html
        expectedResult = 0.35714285714285715;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #206 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #206 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #207 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #207 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #207 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #208 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html
        expectedResult = 0.21348314606741572;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #208 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #208 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #209 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html
        expectedResult = 0.15730337078651685;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #209 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #209 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #210 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html
        expectedResult = 0.25842696629213485;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #210 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #210 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #211 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html
        expectedResult = 0.2247191011235955;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #211 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #211 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #212 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html
        expectedResult = 0.14606741573033707;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #212 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #212 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #213 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #213 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #213 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #214 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html
        expectedResult = 0.17567567567567569;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #214 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #214 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #215 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html
        expectedResult = 0.21621621621621623;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #215 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #215 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #216 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html
        expectedResult = 0.14864864864864866;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #216 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #216 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #217 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html
        expectedResult = 0.24324324324324326;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #217 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #217 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #218 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html
        expectedResult = 0.21621621621621623;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #218 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #218 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #219 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #219 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #219 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #220 checking TF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #220 checking TF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #220 checking TF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #221 checking TF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #221 checking TF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #221 checking TF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #222 checking TF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #222 checking TF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #222 checking TF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #223 checking TF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #223 checking TF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #223 checking TF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #224 checking TF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #224 checking TF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #224 checking TF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
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
