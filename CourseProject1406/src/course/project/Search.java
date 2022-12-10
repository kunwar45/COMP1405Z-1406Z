package course.project;

import java.io.File;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.text.DecimalFormat;
import java.util.TreeSet;

public class Search {
	private static HashMap<String, Integer> phraseUniques = new HashMap<>();
	private static HashMap<String, Double> phraseIDFs = new HashMap<>();
	private static ArrayList<Double> phraseVector = new ArrayList<>();
	private static SearchData tester = new SearchData();
	private static final DecimalFormat df = new DecimalFormat("0.000");
	public static List<SearchResult> search(String phrase, boolean boost, int X){

		ArrayList<String> phraseWords = new ArrayList<String>(List.of(phrase.split(" ")));
		File files = new File("pages");
		TreeSet<Link> result = new TreeSet<>();

		for (File f:files.listFiles()){
			String url = f.getAbsolutePath();
			ArrayList<Double> documentVector = new ArrayList<>();
			for (String word: phraseUniques.keySet()){
				documentVector.add(tester.getTFIDF(url,word));
			}
			double sim= cosineSim(phraseVector,documentVector);
			if (boost){
				sim = sim*tester.getPageRank(url);
			}
			Link link = new Link(url);
			link.setScore(Math.round(Double.parseDouble(df.format(sim))));
			if (result.size() == X+1){
				result.remove(result.last());
			}
			result.add(link);
			System.out.println(result);
		}
		ArrayList<SearchResult> searchResults = new ArrayList<>();
		for (Link link : result){
			searchResults.add((SearchResult)link);
		}

		return searchResults;

	}

	public static double cosineSim(ArrayList<Double> a, ArrayList<Double> b ){
		double eNormA = euclideanNorm(a);
		double eNormB = euclideanNorm(b);
		if(eNormA == 0 || eNormB == 0){
			return 0;
		}
		return Crawler.dotProduct(a, b)/(eNormA*eNormB);
	}

	public static double euclideanNorm(ArrayList<Double> a){
		double sum = 0;
		for (int i = 0; i < a.size(); i++){
			sum+= Math.pow(a.get(i),2);
		}
		return Math.sqrt(sum);
	}

	public void getPhraseVector(ArrayList<String> phraseWords){
		ArrayList<Object> result = new ArrayList<>();


		for (String word : phraseWords){
			double idf = tester.getIDF(word);
			if (idf == 0){
				while(phraseWords.remove(word)){

				}
			}else{
				phraseUniques.putIfAbsent(word,0);
				phraseUniques.replace(word, phraseUniques.get(word)+1);
				phraseIDFs.put(word, idf);
				
			}
		}

		for (String word: phraseUniques.keySet()){
			double tf = (double)phraseUniques.get(word)/phraseUniques.size();
			phraseVector.add(Crawler.log2(1+tf)*phraseIDFs.get(word));
		}

	}

	public static void main(String[] args) {
		search("gang gang", true, 3);
	}
}
