package course.project;

import course.project.Crawler;
import course.project.Link;

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
	private static final DecimalFormat df = new DecimalFormat("0.000");
	public static void search(String phrase, boolean boost){

		ArrayList<String> phraseWords = new ArrayList<String>(List.of(phrase.split(" ")));
		ArrayList<Link> cosineSimilarities = new ArrayList<>();
		File files = new File("pages");

		for (File f:files.listFiles()){
			String url = f.getAbsolutePath();
			ArrayList<Double> documentVector = new ArrayList<>();
			for (String word: phraseUniques.keySet()){
				documentVector.add(SearchData.get_tf_idf(url,word));
			}
			double sim= cosineSim(phraseVector,documentVector);
			if (boost){
				sim = sim*SearchData.get_page_rank(url);
			}
			Link link = new Link(url);
			link.setCosineSim(Math.round(Double.parseDouble(df.format(sim))));

			int insert = 0;
			if (cosineSimilarities.get(0) != null){
				for (int i=0;i<11;i++){
					if (cosineSimilarities.get(i) == null){
						cosineSimilarities.set(i, link);
						break;
					}else if (link.compareTo(cosineSimilarities.get(i))<0){
						insert++;
					}else if (insert == 10){
						break;
					}else{
						cosineSimilarities.add(insert, link);
						break;
					}

				}
			}else{
				cosineSimilarities.add(link);
			}if (cosineSimilarities.size()>10){
				cosineSimilarities.remove(10);
			}
			System.out.println(cosineSimilarities);
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

	public void getPhraseVector(ArrayList<String> phraseWords){
		ArrayList<Object> result = new ArrayList<>();

		for (String word : phraseWords){
			double idf = SearchData.get_idf(word);
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
		search("gang gang", true);
	}
}
