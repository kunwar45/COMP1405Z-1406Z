package course.project;

import javax.print.attribute.standard.JobKOctets;
import java.io.File;
import java.util.*;
import java.text.DecimalFormat;

public class Search {
	private static final DecimalFormat df = new DecimalFormat("0.000");

	private ArrayList<SearchResult> searchResults;
	private SearchData tester;


	public Search(String seedURL){
		tester = new SearchData();
	}

	public Search(){
		tester = new SearchData();

	}

	public ArrayList<SearchResult> search(String phrase, boolean boost, int X) {

		ArrayList<String> phraseWords = new ArrayList<String>(List.of(phrase.split(" ")));
		File files = new File("pages");
		TreeSet<Link> result = new TreeSet<>();
		ArrayList<Object> phraseDetails = getPhraseVector(phraseWords);
		HashMap<String, Integer> phraseUniques = (HashMap<String, Integer>) phraseDetails.get(0);
		ArrayList<Double> phraseVector = (ArrayList<Double>) phraseDetails.get(1);


		//Finds the score of each link and puts it into the TreeSet. The TreeSet only ever has 11 elements, so it will
		//always compare 10 times maximum regardless of the amount of urls, therefore the TreeSet sorting is O(1)
		for (File f : files.listFiles()) {
			String url = f.getName();
			ArrayList<Double> documentVector = new ArrayList<>();
			for (String word : phraseUniques.keySet()) {
				documentVector.add(tester.getTFIDF(url, word));
			}
			double sim = cosineSim(phraseVector, documentVector);
			if (boost) {
				sim = sim * tester.getPageRank(url);
			}
			Link link = new Link(url);
			link.setTitle(tester.getTitle(url));
			link.setScore(Double.parseDouble(df.format(sim)));
			if (result.size() == X + 1) {
				result.remove(result.last());
			}
			result.add(link);
		}
		if (result.size() == X + 1) {
			result.remove(result.last());
		}
		searchResults = new ArrayList<>();
		for (Link link : result) {
			searchResults.add((SearchResult) link);
		}
		return searchResults;
	}

	public static double cosineSim(ArrayList<Double> a, ArrayList<Double> b) {
		double eNormA = euclideanNorm(a);
		double eNormB = euclideanNorm(b);
		if (eNormA == 0 || eNormB == 0) {
			return 0;
		}
		Crawler crawler = new Crawler();
		return crawler.dotProduct(a, b) / (eNormA * eNormB);
	}

	public static double euclideanNorm(ArrayList<Double> a) {
		double sum = 0;
		for (int i = 0; i < a.size(); i++) {
			sum += Math.pow(a.get(i), 2);
		}
		return Math.sqrt(sum);
	}

	public ArrayList<Object> getPhraseVector(ArrayList<String> phraseWords) {
		HashMap<String, Integer> phraseUniques = new HashMap<>();
		HashMap<String, Double> phraseIDFs = new HashMap<>();
		ArrayList<Double> phraseVector = new ArrayList<>();
//		ArrayList<Object> result = new ArrayList<>();
		Crawler crawler = new Crawler();
		tester = new SearchData();

		for (int wordIndex = 0; wordIndex < phraseWords.size(); wordIndex++) {
			String word = phraseWords.get(wordIndex);
			double idf = tester.getIDF(word);
			if (idf == 0) {
				while (phraseWords.remove(word)) {
				}
			} else {
				phraseUniques.putIfAbsent(word, 0);
				phraseUniques.replace(word, phraseUniques.get(word) + 1);
				phraseIDFs.put(word, idf);

			}
		}
		for (String word : phraseUniques.keySet()) {
			double tf = (double) phraseUniques.get(word) / phraseUniques.size();
			phraseVector.add(crawler.log2(1 + tf) * phraseIDFs.get(word));
		}
		ArrayList<Object> details = new ArrayList<Object>();
		details.add(phraseUniques);
		details.add(phraseVector);
		return details;

	}

	public ArrayList<SearchResult> getSearchResults() {
		return this.searchResults;
	}

	 public static void main(String[] args) {
		SearchData tester = new SearchData();
		tester.initialize();
	 	tester.crawl("http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html");
	 }
}
