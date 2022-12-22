import course.project.TestingTools;

import java.io.FileWriter;
import java.io.PrintWriter;

public class Fruits4TFTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html");
        runTest(tester);
    }

    public static void runTest(ProjectTester tester) throws Exception {
        PrintWriter failOut = new PrintWriter(new FileWriter("Fruits4-TF-failed.txt"));
        PrintWriter passOut = new PrintWriter(new FileWriter("Fruits4-TF-passed.txt"));
        double expectedResult;
        double yourResult;
//Test #168 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #168 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #168 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #169 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #169 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #169 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #170 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #170 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #170 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #171 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #171 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #171 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #172 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #172 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #172 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #173 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #173 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #173 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #174 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #174 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #174 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #175 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html
        expectedResult = 0.5;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #175 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #175 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #176 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html
        expectedResult = 0.5;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #176 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #176 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #177 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #177 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #177 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #178 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #178 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #178 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-908.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #179 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html
        expectedResult = 0.07692307692307693;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #179 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #179 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #180 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html
        expectedResult = 0.08791208791208792;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #180 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #180 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #181 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html
        expectedResult = 0.06593406593406594;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #181 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #181 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #182 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html
        expectedResult = 0.08791208791208792;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #182 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #182 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #183 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html
        expectedResult = 0.07692307692307693;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #183 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #183 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #184 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html
        expectedResult = 0.08791208791208792;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #184 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #184 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #185 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html
        expectedResult = 0.0989010989010989;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #185 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #185 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #186 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html
        expectedResult = 0.07692307692307693;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #186 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #186 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #187 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html
        expectedResult = 0.07692307692307693;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #187 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #187 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #188 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html
        expectedResult = 0.08791208791208792;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #188 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #188 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #189 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #189 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #189 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #190 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html
        expectedResult = 0.11940298507462686;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #190 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #190 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #191 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html
        expectedResult = 0.014925373134328358;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #191 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #191 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #192 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html
        expectedResult = 0.11940298507462686;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #192 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #192 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #193 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html
        expectedResult = 0.029850746268656716;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #193 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #193 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #194 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html
        expectedResult = 0.1044776119402985;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #194 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #194 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #195 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html
        expectedResult = 0.08955223880597014;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #195 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #195 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #196 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html
        expectedResult = 0.05970149253731343;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #196 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #196 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #197 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html
        expectedResult = 0.04477611940298507;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #197 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #197 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #198 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html
        expectedResult = 0.08955223880597014;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #198 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #198 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #199 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html
        expectedResult = 0.11940298507462686;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #199 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #199 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #200 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #200 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #200 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #201 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html
        expectedResult = 0.09523809523809523;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #201 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #201 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #202 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #202 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #202 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #203 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html
        expectedResult = 0.14285714285714285;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #203 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #203 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #204 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html
        expectedResult = 0.047619047619047616;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #204 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #204 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #205 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html
        expectedResult = 0.11904761904761904;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #205 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #205 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #206 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html
        expectedResult = 0.11904761904761904;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #206 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #206 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #207 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html
        expectedResult = 0.047619047619047616;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #207 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #207 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #208 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html
        expectedResult = 0.07142857142857142;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #208 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #208 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #209 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html
        expectedResult = 0.07142857142857142;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #209 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #209 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #210 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html
        expectedResult = 0.09523809523809523;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #210 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #210 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #211 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #211 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #211 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #212 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #212 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #212 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #213 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html
        expectedResult = 0.078125;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #213 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #213 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #214 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html
        expectedResult = 0.078125;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #214 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #214 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #215 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html
        expectedResult = 0.09375;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #215 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #215 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #216 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html
        expectedResult = 0.09375;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #216 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #216 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #217 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html
        expectedResult = 0.046875;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #217 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #217 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #218 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html
        expectedResult = 0.09375;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #218 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #218 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #219 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html
        expectedResult = 0.078125;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #219 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #219 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #220 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html
        expectedResult = 0.15625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #220 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #220 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #221 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html
        expectedResult = 0.0625;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #221 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #221 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #222 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #222 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #222 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #223 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html
        expectedResult = 0.0707070707070707;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #223 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #223 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #224 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html
        expectedResult = 0.09090909090909091;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #224 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #224 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #225 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html
        expectedResult = 0.08080808080808081;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #225 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #225 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #226 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html
        expectedResult = 0.10101010101010101;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #226 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #226 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #227 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html
        expectedResult = 0.08080808080808081;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #227 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #227 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #228 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html
        expectedResult = 0.050505050505050504;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #228 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #228 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #229 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html
        expectedResult = 0.0707070707070707;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #229 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #229 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #230 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html
        expectedResult = 0.050505050505050504;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #230 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #230 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #231 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html
        expectedResult = 0.10101010101010101;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #231 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #231 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #232 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html
        expectedResult = 0.04040404040404041;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #232 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #232 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #233 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #233 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #233 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #234 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html
        expectedResult = 0.1276595744680851;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #234 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #234 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #235 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html
        expectedResult = 0.02127659574468085;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #235 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #235 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #236 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html
        expectedResult = 0.14893617021276595;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #236 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #236 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #237 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html
        expectedResult = 0.0425531914893617;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #237 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #237 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #238 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html
        expectedResult = 0.14893617021276595;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #238 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #238 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #239 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html
        expectedResult = 0.06382978723404255;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #239 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #239 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #240 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html
        expectedResult = 0.02127659574468085;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #240 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #240 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #241 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html
        expectedResult = 0.0851063829787234;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #241 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #241 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #242 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html
        expectedResult = 0.10638297872340426;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #242 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #242 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #243 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html
        expectedResult = 0.10638297872340426;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #243 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #243 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #244 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #244 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #244 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #245 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html
        expectedResult = 0.1935483870967742;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #245 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #245 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #246 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html
        expectedResult = 0.03225806451612903;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #246 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #246 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #247 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html
        expectedResult = 0.03225806451612903;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #247 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #247 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #248 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html
        expectedResult = 0.0967741935483871;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #248 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #248 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #249 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html
        expectedResult = 0.16129032258064516;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #249 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #249 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #250 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html
        expectedResult = 0.03225806451612903;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #250 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #250 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #251 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html
        expectedResult = 0.06451612903225806;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #251 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #251 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #252 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html
        expectedResult = 0.03225806451612903;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #252 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #252 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #253 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html
        expectedResult = 0.03225806451612903;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #253 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #253 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #254 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html
        expectedResult = 0.16129032258064516;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #254 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #254 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #255 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #255 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #255 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #256 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html
        expectedResult = 0.1111111111111111;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #256 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #256 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #257 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html
        expectedResult = 0.1111111111111111;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #257 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #257 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #258 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html
        expectedResult = 0.05555555555555555;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #258 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #258 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #259 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html
        expectedResult = 0.2777777777777778;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #259 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #259 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #260 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html
        expectedResult = 0.05555555555555555;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #260 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #260 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #261 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #261 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #261 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #262 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html
        expectedResult = 0.05555555555555555;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #262 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #262 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #263 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html
        expectedResult = 0.1111111111111111;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #263 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #263 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #264 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html
        expectedResult = 0.1111111111111111;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #264 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #264 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #265 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #265 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #265 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #266 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #266 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #266 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #267 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html
        expectedResult = 0.09302325581395349;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html", "fig");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #267 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #267 checking TF for fig in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #268 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html
        expectedResult = 0.13953488372093023;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #268 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #268 checking TF for papaya in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #269 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html
        expectedResult = 0.06976744186046512;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #269 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #269 checking TF for lime in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #270 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html
        expectedResult = 0.046511627906976744;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #270 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #270 checking TF for pear in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #271 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html
        expectedResult = 0.09302325581395349;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #271 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #271 checking TF for blueberry in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #272 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #272 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #272 checking TF for coconut in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #273 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html
        expectedResult = 0.13953488372093023;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #273 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #273 checking TF for orange in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #274 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html
        expectedResult = 0.18604651162790697;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #274 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #274 checking TF for banana in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #275 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html
        expectedResult = 0.046511627906976744;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #275 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #275 checking TF for apricot in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #276 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html
        expectedResult = 0.046511627906976744;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #276 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #276 checking TF for peach in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #277 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html
        expectedResult = 0.0;
        yourResult = tester.getTF("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html", "tomato");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #277 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #277 checking TF for tomato in https://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html");
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

//Test #279 checking TF for papaya in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "papaya");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #279 checking TF for papaya in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #279 checking TF for papaya in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #280 checking TF for lime in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "lime");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #280 checking TF for lime in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #280 checking TF for lime in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #281 checking TF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "pear");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #281 checking TF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #281 checking TF for pear in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #282 checking TF for blueberry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "blueberry");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #282 checking TF for blueberry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #282 checking TF for blueberry in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #283 checking TF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "coconut");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #283 checking TF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #283 checking TF for coconut in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #284 checking TF for orange in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "orange");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #284 checking TF for orange in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #284 checking TF for orange in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #285 checking TF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "banana");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #285 checking TF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #285 checking TF for banana in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #286 checking TF for apricot in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "apricot");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #286 checking TF for apricot in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #286 checking TF for apricot in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            failOut.println("expected = " + expectedResult);
            failOut.println("result = " + yourResult + "\n\n");
        }

//Test #287 checking TF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
        expectedResult = 0.0;
        yourResult = tester.getTF("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html", "peach");
        if (TestingTools.compareDoubles(yourResult, expectedResult)) {
            passOut.println("Passed Test #287 checking TF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
            passOut.println("expected = " + expectedResult);
            passOut.println("result = " + yourResult + "\n\n");
        } else {
            failOut.println("Passed Test #287 checking TF for peach in http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html");
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
