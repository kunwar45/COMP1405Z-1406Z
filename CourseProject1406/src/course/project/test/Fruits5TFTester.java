import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;

public class Fruits5TFTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits5-TF-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits5-TF-passed.txt"));
        double expectedResult;
        double yourResult;
//Test #168 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html
        expectedResult = 0.11290322580645161;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #168 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #168 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #169 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html
        expectedResult = 0.08064516129032258;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #169 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #169 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #170 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html
        expectedResult = 0.04838709677419355;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #170 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #170 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #171 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html
        expectedResult = 0.08064516129032258;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #171 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #171 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #172 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html
        expectedResult = 0.0967741935483871;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #172 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #172 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #173 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html
        expectedResult = 0.08064516129032258;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #173 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #173 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #174 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html
        expectedResult = 0.03225806451612903;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #174 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #174 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #175 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html
        expectedResult = 0.06451612903225806;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #175 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #175 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #176 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html
        expectedResult = 0.04838709677419355;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #176 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #176 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #177 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html
        expectedResult = 0.0967741935483871;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #177 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #177 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #178 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #178 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #178 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #179 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html
        expectedResult = 0.045454545454545456;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #179 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #179 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #180 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html
        expectedResult = 0.045454545454545456;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #180 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #180 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #181 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html
        expectedResult = 0.09090909090909091;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #181 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #181 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #182 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html
        expectedResult = 0.045454545454545456;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #182 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #182 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #183 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html
        expectedResult = 0.09090909090909091;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #183 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #183 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #184 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html
        expectedResult = 0.09090909090909091;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #184 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #184 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #185 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html
        expectedResult = 0.09090909090909091;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #185 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #185 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #186 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html
        expectedResult = 0.045454545454545456;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #186 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #186 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #187 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #187 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #187 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #188 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html
        expectedResult = 0.09090909090909091;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #188 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #188 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #189 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #189 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #189 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #190 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html
        expectedResult = 0.020202020202020204;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #190 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #190 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #191 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html
        expectedResult = 0.06060606060606061;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #191 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #191 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #192 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html
        expectedResult = 0.050505050505050504;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #192 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #192 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #193 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html
        expectedResult = 0.08080808080808081;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #193 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #193 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #194 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html
        expectedResult = 0.10101010101010101;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #194 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #194 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #195 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html
        expectedResult = 0.06060606060606061;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #195 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #195 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #196 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html
        expectedResult = 0.050505050505050504;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #196 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #196 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #197 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html
        expectedResult = 0.1111111111111111;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #197 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #197 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #198 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html
        expectedResult = 0.10101010101010101;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #198 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #198 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #199 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html
        expectedResult = 0.06060606060606061;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #199 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #199 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #200 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #200 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #200 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #201 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = 0.08333333333333333;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #201 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #201 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #202 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = 0.05555555555555555;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #202 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #202 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #203 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = 0.05555555555555555;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #203 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #203 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #204 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = 0.027777777777777776;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #204 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #204 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #205 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = 0.1111111111111111;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #205 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #205 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #206 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = 0.027777777777777776;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #206 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #206 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #207 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = 0.08333333333333333;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #207 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #207 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #208 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = 0.05555555555555555;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #208 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #208 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #209 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = 0.1111111111111111;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #209 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #209 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #210 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = 0.08333333333333333;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #210 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #210 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #211 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #211 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #211 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #212 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #212 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #212 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #213 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html
        expectedResult = 0.1875;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #213 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #213 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #214 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #214 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #214 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #215 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #215 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #215 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #216 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #216 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #216 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #217 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #217 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #217 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #218 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #218 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #218 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #219 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html
        expectedResult = 0.1875;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #219 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #219 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #220 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #220 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #220 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #221 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #221 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #221 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #222 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #222 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #222 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #223 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html
        expectedResult = 0.0379746835443038;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #223 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #223 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #224 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html
        expectedResult = 0.08860759493670886;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #224 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #224 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #225 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html
        expectedResult = 0.06329113924050633;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #225 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #225 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #226 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html
        expectedResult = 0.05063291139240506;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #226 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #226 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #227 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html
        expectedResult = 0.02531645569620253;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #227 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #227 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #228 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html
        expectedResult = 0.0759493670886076;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #228 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #228 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #229 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html
        expectedResult = 0.08860759493670886;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #229 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #229 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #230 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html
        expectedResult = 0.10126582278481013;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #230 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #230 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #231 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html
        expectedResult = 0.16455696202531644;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #231 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #231 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #232 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html
        expectedResult = 0.06329113924050633;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #232 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #232 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #233 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #233 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #233 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #234 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html
        expectedResult = 0.05;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #234 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #234 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #235 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html
        expectedResult = 0.11666666666666667;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #235 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #235 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #236 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html
        expectedResult = 0.05;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #236 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #236 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #237 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html
        expectedResult = 0.08333333333333333;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #237 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #237 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #238 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html
        expectedResult = 0.1;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #238 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #238 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #239 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html
        expectedResult = 0.05;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #239 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #239 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #240 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html
        expectedResult = 0.11666666666666667;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #240 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #240 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #241 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html
        expectedResult = 0.06666666666666667;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #241 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #241 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #242 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html
        expectedResult = 0.08333333333333333;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #242 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #242 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #243 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html
        expectedResult = 0.06666666666666667;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #243 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #243 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #244 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #244 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #244 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #245 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html
        expectedResult = 0.13636363636363635;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #245 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #245 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #246 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #246 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #246 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #247 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html
        expectedResult = 0.045454545454545456;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #247 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #247 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #248 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html
        expectedResult = 0.13636363636363635;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #248 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #248 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #249 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html
        expectedResult = 0.09090909090909091;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #249 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #249 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #250 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html
        expectedResult = 0.09090909090909091;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #250 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #250 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #251 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html
        expectedResult = 0.09090909090909091;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #251 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #251 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #252 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html
        expectedResult = 0.09090909090909091;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #252 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #252 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #253 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html
        expectedResult = 0.045454545454545456;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #253 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #253 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #254 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html
        expectedResult = 0.09090909090909091;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #254 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #254 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #255 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #255 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #255 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #256 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #256 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #256 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #257 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html
        expectedResult = 0.13333333333333333;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #257 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #257 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #258 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html
        expectedResult = 0.044444444444444446;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #258 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #258 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #259 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html
        expectedResult = 0.1111111111111111;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #259 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #259 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #260 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html
        expectedResult = 0.044444444444444446;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #260 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #260 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #261 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html
        expectedResult = 0.022222222222222223;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #261 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #261 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #262 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html
        expectedResult = 0.08888888888888889;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #262 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #262 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #263 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html
        expectedResult = 0.044444444444444446;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #263 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #263 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #264 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html
        expectedResult = 0.06666666666666667;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #264 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #264 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #265 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html
        expectedResult = 0.2;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #265 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #265 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #266 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #266 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #266 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #267 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html
        expectedResult = 0.15;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #267 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #267 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #268 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #268 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #268 checking TF for apple in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #269 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #269 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #269 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #270 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html
        expectedResult = 0.1;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #270 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #270 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #271 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html
        expectedResult = 0.1;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #271 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #271 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #272 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html
        expectedResult = 0.05;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #272 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #272 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #273 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #273 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #273 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #274 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html
        expectedResult = 0.15;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #274 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #274 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #275 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #275 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #275 checking TF for kiwi in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #276 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html
        expectedResult = 0.2;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #276 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #276 checking TF for cherry in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #277 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #277 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #277 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits5/N-287.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #278 checking TF for fig in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #278 checking TF for fig in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #278 checking TF for fig in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #279 checking TF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "apple");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #279 checking TF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #279 checking TF for apple in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #280 checking TF for papaya in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #280 checking TF for papaya in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #280 checking TF for papaya in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #281 checking TF for lime in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #281 checking TF for lime in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #281 checking TF for lime in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #282 checking TF for orange in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #282 checking TF for orange in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #282 checking TF for orange in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #283 checking TF for apricot in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #283 checking TF for apricot in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #283 checking TF for apricot in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #284 checking TF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #284 checking TF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #284 checking TF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #285 checking TF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #285 checking TF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #285 checking TF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #286 checking TF for kiwi in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "kiwi");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #286 checking TF for kiwi in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #286 checking TF for kiwi in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #287 checking TF for cherry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "cherry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #287 checking TF for cherry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #287 checking TF for cherry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
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
