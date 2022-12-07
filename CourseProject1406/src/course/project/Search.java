package course.project;

import course.project.Crawler;
import course.project.Link;

import java.io.File;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.TreeSet;

public class Search {
	public static void search(String phrase, boolean boost){
		ArrayList<String> phraseWords = new ArrayList<String>(List.of(phrase.split(" ")));
		Link[] cosineSimilarities = new Link[11];
		File files = new File("pages");
		for (File f:files.listFiles()){
			String url = f.getAbsolutePath();
			ArrayList<Double> documentVector = new ArrayList<>();
//			for ()
			System.out.println(f);
		}


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

	public ArrayList<Object> getPhraseVector(ArrayList<String> phraseWords){
		HashMap<String, Integer> phraseUniques = new HashMap<>();
		HashMap<String, Double> phraseIDFs = new HashMap<>();
		ArrayList<Double> phraseVectors = new ArrayList<>();
		for (String word : phraseWords){
			double idf = SearchData.get_idf(word);
			if (idf == 0){
				while(phraseWords.remove(word)){

				}
			}else{
				phraseUniques.putIfAbsent(word,0);
				phraseUniques.replace(word, phraseUniques.get(word)+1);
				
			}
		}
	}

	public static void main(String[] args) {
		search("gang gang", true);
	}
}
