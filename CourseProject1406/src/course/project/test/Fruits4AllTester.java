public class Fruits4AllTester {
    public static void main(String[] args) throws Exception {
        ProjectTester tester = new ProjectTesterImp(); //Instantiate your own ProjectTester instance here
        tester.initialize();
        tester.crawl("https://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html");

        Fruits4OutgoingLinksTester.runTest(tester);
        Fruits4IncomingLinksTester.runTest(tester);
        Fruits4PageRanksTester.runTest(tester);
        Fruits4IDFTester.runTest(tester);
        Fruits4TFTester.runTest(tester);
        Fruits4TFIDFTester.runTest(tester);
        Fruits4SearchTester.runTest(tester);
        System.out.println("Finished running all tests.");
    }
}
