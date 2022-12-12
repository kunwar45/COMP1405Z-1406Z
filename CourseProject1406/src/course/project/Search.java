package course.project;

import javax.print.attribute.standard.JobKOctets;
import java.io.File;
import java.util.*;
import java.text.DecimalFormat;

public class Search {
	private final DecimalFormat df = new DecimalFormat("0.000");

	private ArrayList<SearchResult> searchResults;

	public List<SearchResult> search(String phrase, boolean boost, int X) {
		SearchData tester = new SearchData();
		ArrayList<String> phraseWords = new ArrayList<String>(List.of(phrase.split(" ")));
		File files = new File("pages");
		TreeSet<Link> result = new TreeSet<>();
		ArrayList<Object> phraseDetails = getPhraseVector(phraseWords);
		HashMap<String, Integer> phraseUniques = (HashMap<String, Integer>) phraseDetails.get(0);
		ArrayList<Double> phraseVector = (ArrayList<Double>) phraseDetails.get(1);

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
			link.setScore(df.format(sim));
			if (result.size() == X + 1) {
				result.remove(result.last());
			}
			result.add(link);
			System.out.println(result);
		}
		if (result.size() == X + 1) {
			result.remove(result.last());
		}
		ArrayList<SearchResult> searchResults = new ArrayList<>();
		for (Link link : result) {
			searchResults.add((SearchResult) link);
		}
		for (SearchResult searchResult : searchResults) {
			System.out.println(searchResult.getTitle() + ": " + searchResult.getScore());
		}

		return searchResults;

	}

	public double cosineSim(ArrayList<Double> a, ArrayList<Double> b) {
		double eNormA = euclideanNorm(a);
		double eNormB = euclideanNorm(b);
		if (eNormA == 0 || eNormB == 0) {
			return 0;
		}
		return Crawler.dotProduct(a, b) / (eNormA * eNormB);
	}

	public double euclideanNorm(ArrayList<Double> a) {
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
		ArrayList<Object> result = new ArrayList<>();
		SearchData tester = new SearchData();

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
			phraseVector.add(Crawler.log2(1 + tf) * phraseIDFs.get(word));
		}
		ArrayList<Object> details = new ArrayList<Object>();
		details.add(phraseUniques);
		details.add(phraseVector);
		return details;

	}

	public ArrayList<SearchResult> getSearchResults() {
		return this.searchResults;
	}

	// public static void main(String[] args) {
	// search("gang gang", true, 3);
	// }
}
