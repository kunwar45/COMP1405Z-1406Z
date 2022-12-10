public class Fruits2AllTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html");

        Fruits2OutgoingLinksTester.runTest(tester);
        Fruits2IncomingLinksTester.runTest(tester);
        Fruits2PageRanksTester.runTest(tester);
        Fruits2IDFTester.runTest(tester);
        Fruits2TFTester.runTest(tester);
        Fruits2TFIDFTester.runTest(tester);
        Fruits2SearchTester.runTest(tester);
        System.out.println("Finished running all tests.");
    }
}
